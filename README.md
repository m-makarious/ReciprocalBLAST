# **ReciprocalBLAST**

##### Created by:
Fahed al Rafati, Mary B. Makarious, Ariane Quenum, Anthony Volchek
##### Loyola Univerisity Chicago: Department of Biology and Computer Science
##### COMP 383: Final Project
Computational Biology | Spring 2018 | Dr. Heather E. Wheeler

##### [Link to Github](https://github.com/m-makarious/ReciprocalBLAST)
#
![LUC](http://www.luc.edu/media/home/images/loyola-logo-tag.png)

---
## Table of Contents
* [Visualization](#visualization)
* [Background](#background)
* [Overview](#overview)
* [Getting Started](#gettingstarted)
* [Hardware Requirements](#hardware)
* [Software Requirements](#software)
* [Input](#input)
* [Usage](#usage)
* [Output](#output)


## Visualization
######  Here is a graphical depiction of how the program works:
[![Graphical Depiction.png](https://s14.postimg.cc/4jxqfv3a9/Screen_Shot_2018-04-25_at_9.34.32_PM.png)](https://postimg.cc/image/4jxqfv3a5/)

###### This is a link to a video walkthrough with the code and sample data found on this repository

[Video Walkthrough](https://streamable.com/1v1s2 "Video Walkthrough")

---

## Background
- Automated tool to identify homologs (orthologs and paralogs) between genomes
- Keeps homolog lists for each genome and output a FASTA file for each cluster of homologs
- Makes a local BLAST database for each genome and then BLAST everything against each other

![alt text](https://i.imgur.com/qQCafdD.png)

Reciprocal BLAST is an extension of BLAST aimed at finding orthologous sequences between two species and also a common computational method used to predict orthologues. Reciprocal BLAST is done by taking a gene and BLAST-ing it to a database of the gene sequences from the organism of interest. The gene with the highest score is BLASTed against a database of the query gene sequences. If the BLAST returns the original gene used as the best hit, the genes are considered candidate orthologs; however, only experimental evidence can prove  orthology.

---

## Overview <a id="overview"></a>
We are building a tool to identify homologs between multiple microbial genomes; identify the global similarities and differences that exist within an assortment of bacteria. In order to do that, we are taking some genes of interest and blasting them to a local database of the gene sequence from the organism of interest. The highest scoring gene is taken and blasted to a database of the gene sequence.
___

## Getting Started <a id="gettingstarted"></a>
You will need to download the `reciblast` folder found on this GitHub to get started!

Everything to run the program is in the folder.

To use, you will need to
`cd path/to/the/reciblast/folder`
and run the program by typing
`python py_blast.py`

There is sample data in the default `fasta_in` subfolder in the `reciblast`  folder
___

## Hardware Requirements <a id="hardware"></a>
This program can work on any Windows or Mac machine with average RAM and processing capabilities. 
___

## Software Requirements <a id="software"></a>
In order for the program to run you must have BLAST+ and Python 3.1 need to be installed on your device.

### BLAST+
Before you begin you must have BLAST Command Line Applications (BLAST+) downloaded on your computer. Proper installation instructions can be found here. (https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) to be installed and on your local PATH. NCBI BLAST+ tools can be found at: BLAST+: architecture and applications. C. Camancho et al. BMC Bioinformatics 2009, 10:421.DOI:http://dx.doi.org/10.1186/1471-2105-10-421


### Python 3.1 
This code was created and tested using Python 3.1. **DISCLAIMER**: The program has not been tested or used on other versions of Python. User may run into some syntactical issues using other versions of Python. The Python website has detailed information on the Python programming language. Python 3.1 installation instructions can be found here. Python was installed using the [Anaconda] (https://docs.continuum.io/anaconda/install) free distribution.

___

## Input Files <a id="input"></a>
This program only accepts .fasta files. FASTA files often start with a header line that may contain comments or other information. The rest of the file contains sequence data. Each sequence starts with a “>” symbol followed by the name of the sequence. The rest of the line describes the sequence and the remaining lines contain the sequences itself.
___

## Usage <a id="usage"></a>

The `reciblast` folder have some default folders that can be used if desired, and these are the defaults that pop up in the configurations on the menu.

However, if you would like to change the paths of the inputs/outputs accordingly, pick the menu item `[3]` and choose what needs to be changed.

Sample FASTA files can be found at:
___

## Output Files <a id="output"></a>
The program goes through each of those .fasta files and generates a local database for each of them. Three files are created with the following extensions .nhr, .nin, .nsq. Each file is necessary for the program to run therefore, they should not be removed.


| File | Description|
|:----:|:--:|
| .nhr    |  This is the header file  |
| .nin	 | This is the index file |
| .nsq | This is the sequence file|
          

A BLAST is then performed based on the designation of ‘nucl’ and ‘prot’. Each individual FASTA is BLAST-ed against each individual Database as required in reciprocal BLAST. After looping through the FASTA files and databases, a Comma-Delimited output will be produced with the comparisons. This will be in “.txt” format, and is used to make the .csv files that contain the bit scores.
