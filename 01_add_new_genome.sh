#!/bin/bash
##usage: ./compare_genomes path/to/output/directory path/to/new/genome.fasta
##input file should be fasta

dir=$1
new_genome=$2
genome_name="$(basename -s .fasta $new_genome)"

###Directories already created in output directory
###$dir/database
###$dir/LINs
###$dir/temp

#####adding genome to database
#step1: create the skf fille
ska fasta $new_genome -o $dir/temp/$genome_name

#step:2 compare new skf file with files in database
ska compare $dir/database/* -q $dir/temp/${genome_name}.skf > $dir/temp/out  

