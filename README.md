# ReciprocalBLAST
COMP 383: Computational Biology

### Collaborators
- Fahed al Rafati
- Mary B. Makarious
- Ariane Quenum
- Anthony Volchek ....
##### [Link to Google Drive](https://drive.google.com/drive/folders/1McYLmD6kR-d7lGICvDZfpASVYIHUPB_9?usp=sharing)

### Background
- Automated tool to identify homologs (orthologs and paralogs) between genomes
- Keeps homolog lists for each genome and output a FASTA file for each cluster of homologs
- Makes a local BLAST database for each genome and then BLAST everything against each other

---

### Getting Started
You will need to make a local database for your FASTA files. Using Local Blast+ from NCBI, the following command can be run from your terminal
```makeblastdb -in /path/to/FASTA/file/name.fasta -dbtype "TYPE" -out /path/where/you/want/the/database/files/name_of_Database```

For nucleotides (a FASTA file that includes nucleotides), type in ```-dbtype nucl```
For proteins (a FASTA file that includes amino acids), type in ```-dbtype prot```


### HARDWARE REQUIREMENT
This program can work on any Windows or Mac machine with average RAM and processing capabilities. 

### SOFTWARE REQUIREMENT
In order for the program to run you must have BLAST+, Python 3.1 or above, and Bio Python.


BLAST+

Before you begin you must have BLAST Command Line Applications (BLAST+) downloaded on your computer. Proper installation instructions can be found here. (https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) to be installed and on your local PATH. NCBI BLAST+ tools can be found at: BLAST+: architecture and applications. C. Camancho et al. BMC Bioinformatics 2009, 10:421.DOI:http://dx.doi.org/10.1186/1471-2105-10-421


Python 3.1 
This code was created and tested using Python3.1. DISCLAIMER: The program has not been tested or used on other versions of Python. User may run into some syntactical issues using other versions of Python. The Python website has detailed information on the Python programming language. Python 3.1 installation instructions can be found here. Python was installed using the [Anaconda] (https://docs.continuum.io/anaconda/install) free distribution.


### OVERVIEW
We are building a tool to identify homologs between multiple microbial genomes; identify the global similarities and differences that exist within an assortment of bacteria. In order to do that, we are taking some genes of interest and blasting them to a local database of the gene sequence from the organism of interest. The highest scoring gene is taken and blasted to a database of the gene sequence.


### INPUT FILE
This program only accepts .fasta files. Fasta files often start with a header line that may contain comments or other information. The rest of the file contains sequence data. Each sequence starts with a “>” symbol followed by the name of the sequence. The rest of the line describes the sequence and the remaining lines contain the sequences itself.

### USAGE
To run the program, you will need to create a folder that contains all the .fasta files that you need. Once you have the folder, open a terminal window and try to run the python script.
The program will then prompt the user: 

“Enter the path for the folder that have all the .fasta files:” To enter the path, you can simply drag the folder to the terminal

“Enter the database type (nucl or prot): “If your database type is nucleotide type “nucl” and if your database type is protein type “prot”

“Enter the output folder:” You can simply drag the output folder to the terminal

“Where would you like the .csv BLAST results?:” You can also drag the folder of the results to the terminal

Once the database is created, the program will begin to blast each .fasta file against the database.

### OUTPUT FILE 
The program will now go through each of those .fasta files and generate a local database for each of them. Three files are created with the following extensions .nhr, .nin, .nsq. Each file is necessary for the program to run therefore, they should not be removed. 


| File | Description|
|:----:|:--:|
| .nhr    |  This is the header file  |
| .nin	 | This is the index file |
| .nsq	 | This is the sequence file|
          

BLAST is then performed based on the designation of ‘nucl’ and ‘prot’. Each individual FASTA is BLASTed against each individual Database as required in reciprocal BLAST. After looping through the FASTA files and databases, a ‘comma’ Delimited output will be produced for the purpose of parsing. This will be in “.txt” format. Comma delimited aids parsing as it’s a simpler output as well as for future output in “.csv”.
