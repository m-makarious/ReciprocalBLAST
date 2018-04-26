# Import the necessary packages 

import numpy as np
import os

# Does the parsing
# Writes the results in "blast_results.csv" in the parsing output directory

def parse(parse_in, parse_out):
    # Get all files to be processed that are the output of the blasting
    files_temp = [f for f in os.listdir(parse_in) if f.endswith(".txt")]

    # Clean out .DS_S comparison text files (this is mainly a Mac issue? But if the .DS_S files stay then the parser won't work)
    # Maybe it's just an issue with my Mac? 
    files = [f for f in files_temp if not f.endswith(".DS_S.txt")]

    # Remove duplicate files 
    files = list(set(files))

    # The files are really files^2 because you compare each one against each other
    # So, we take each file from each output .txt file's name
    # Then create a list of all of them so we know which inputs were used
    inputs = []

    for f in files:
        parts = f[:-7].split("_vs_")
        inputs += parts

    # Remove the replicated inputs 
    inputs = list(set(inputs))

    # Prep for scoring the inputs against each other
    l = len(inputs)

    # Stores top bitscore
    arr = np.zeros((l, l))

    # Stores reference file for each bitscore
    ref_files = []
    for i in range(0, l):
        ref_files.append([])
        for j in range(0, l):
            ref_files[i].append("")

    # NOW ACTUALLY GETTING THE DATA
    for f in files:

        # Determine which of the inputs we are working with
        parts = f[:-7].split("_vs_")
        i = inputs.index(parts[0])
        j = inputs.index(parts[1])

        # If they're different (you don't want to compare the exact same ones, obviously)
        if i != j:
            # Grab the first line of the file to get the top bitscore
            # They are sortest by the best at the top, so you only really need the first line
            with open("./{}/".format(parse_in) + f, "r") as fl:
                line = fl.read().split('\n')[0]
            try:
                # Grab the bitscore from the line of outputs 
                vals = line.split(",")
                bitscore = vals[11]

                # Assign that to the score array and log which file this is from
                arr[i][j] = bitscore
                ref_files[i][j] = f

            except: # This will also catch any files that just do not output a bitscore
                return "There was some error in getting the bitscore\nThe offending piece of data is:\n" + line
    

    # NOW ACTUALLY OUTPUTTING IT TO THE SPREADSHET
    with open("{}/blast_results.csv".format(parse_out), "w") as f:
        
        # Write out the bit scores
        f.write('Bit Scores,{}\n'.format("," * len(inputs)))
        
        # Input columns
        f.write(",{}\n".format(",".join(inputs)))
        
        # Input rows and corresponding scores
        for i in range(0, l):
            f.write("{},{}\n".format(inputs[i], ",".join(["%.5f" % score for score in arr[i]])))
        
        # Write out the reference files
        f.write("Reference Files,{}\n".format("," * len(inputs)))
        
        # input columns
        f.write(",{}\n".format(",".join(inputs)))
        
        # Input rows and corresponding reference files
        for i in range(0, l):
            f.write("{},{}\n".format(inputs[i], ",".join(ref_files[i])))
            
    return None