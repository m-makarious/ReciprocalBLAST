import sys, re
import csv

infl1 = sys.argv[1]
infl2 = sys.argv[2]
csvfile = sys.argv[3]

def list_output(dir):
    a = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        files = os.walk(subdir).__next__()[2]
        if (len(files) > 0):
            for file in files:
                a.append(subdir + "/" + file)
    return a

fastaoutput=list_output(outputFolder)

for i in fastaoutput:
    
    #parse first BLAST Results
    FL1 = open(infl1, 'r')
    Line=FL1.readline()
    Line.strip()
    Elements1 = re.split(',', Line)
    query1 = Elements1[0]
    subject1 = Elements1[1]
    print (query1 + " " + subject1)

    #parse second BLAST results
    FL2 = open(infl2, 'r')
    Line=FL2.readline()
    Line.strip()
    Elements2 = re.split(',', Line)
    query2 = Elements2[0]
    subject2 = Elements2[1]
    print (query2 + " " + subject2)

    if (subject1 == query2) and (query1 == subject2):
        print("match")
    elif (subject1 != query2) and (query1 != subject2):
        print("no match")


    lista= [query1,query2]
    listb= [subject1,subject2]
    res= [lista, listb]
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(res)

    print("Done.")
