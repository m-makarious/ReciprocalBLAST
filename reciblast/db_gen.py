# >> Changed it all to functions so it could be called from the main script

# Import necessary packages 
import sys
import os

# Progress Bars
# These progress bars (kinda) work

# To track the progress of each DB made per fasta so the user can follow along
def progress_Generating_DB(fasta):
    sys.stdout.flush()
    out = "A database has been generated from %s" % fasta
    backspace = "\b" * 1000           

    print (backspace)
    sys.stdout.write(out)
    sys.stderr = os.devnull # Errors that don't break the code will be supressed from showing in the console
    sys.stdout.flush() # This "flushes" the terminal screen so all the output from os.system isn't clogging up the screen

# To track the progress of each FASTA being BLAST-ed to a DB so the user can follow along
def progress_BLAST(fasta, database):
    sys.stdout.flush()

    out = fasta + " has been BLAST-ed against " + database
    backspace = "\b" * 1000            

    print (backspace)
    sys.stderr = os.devnull
    sys.stdout.write(out)

# Go through the folders and subfolders

def list_files(dir_name):                                                                                                 
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir_name)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                            
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)                                                                        
    return r

# Go through folders and subfolders for all databases 
def list_databases(dir):
    s = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                            
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                s.append(subdir + "/" + file)                                                                        
    return s

def generate(fasta_in, db_out, comp_out, db_type):

     # Run the list_files function and return as list_fastas
    list_fastas = list_files(fasta_in)

    # Loop through the list of fastas and generate the databases depending on user inputs
    for i in list_fastas:
        head, tail = os.path.split(i)
        
        # If example input file is EcoliK12.fasta, then output should be /whatever/desired/path/EcoliK12_db
        command = "makeblastdb -in " + i + " -dbtype " + db_type + " -out " + db_out + "/"+tail[:-6]+"_db"
        progress_Generating_DB(tail)
        sys.stdout.flush()
        sys.stderr = os.devnull
        os.system(command)

    # Run the list_databases function and return as list_dbs
    list_dbs = list_databases(db_out)

    # This takes the database_type raw input and reduces it to "n" or "p" to run the BLAST depending on if the FASTAs and dbs are nucl or prot
    blast_variable = db_type[0]

    # Loop through the input FASTAs and all existing databases one by one and generate a .txt file that saves the output
    # .txt files will be saved as FASTA_vs_DatabaseName.txt
    for i in list_fastas:
        FASTA_head, FASTA_tail = os.path.split(i)
        for j in list_dbs:
            db_head, db_tail = os.path.split(j)
            if FASTA_tail[:-6] != db_tail[:-7]:
                blast_results = "blast" + blast_variable + " -query " + i + " -db " + j[:-4] + " -evalue 0.1" + " -outfmt 10" + " -out " + comp_out + "/" + FASTA_tail[:-6]+ "_vs_" + db_tail[:-4] + ".txt"
                progress_BLAST(FASTA_tail[:-6], db_tail[:-4])
                sys.stdout.flush()
                sys.stderr = os.devnull
                os.system(blast_results)