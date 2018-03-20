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
