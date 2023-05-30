#!/bin/bash

##Usage ./All_steps_pipeline /input/genome/directory/ output/directory


in_dir=$1
out_dir=$2
#storing list of input genomes
ls $in_dir > list


mkdir $out_dir/database
mkdir $out_dir/LINs
mkdir $out_dir/temp

###extracting first line of the input file==first genome file.  
first_genome=$(head -1 list)
first_genome_name="$(basename -s .fasta $first_genome)" 
echo $first_genome_name
#Remove the first file from the loop --> edit the input genome file to remove first line
sed '1d' list > $out_dir/temp/input

###calculate signature of first genome file
ska fasta $in_dir/$first_genome -o $out_dir/database/$first_genome_name

###Record LINs of the first genome
echo $first_genome_name,0,0,0,0,0,0,0,0,0,0 > $out_dir/LINs/LIN-scheme.csv
echo 0,0,0,0,0,0,0,0,0,0 > $out_dir/temp/counter.csv
####start a loop for sequentially adding more genomes
while read LINE;
do
	echo $LINE
	file_name="$(basename -s .fasta $LINE)"
	./01_add_new_genome.sh $out_dir $in_dir/${file_name}.fasta	
	python 02_modiefied_LIN_assignment.py $out_dir/temp/out $out_dir/LINs/LIN-scheme.csv $file_name $out_dir/temp/counter.csv
	mv $out_dir/temp/${file_name}.skf $out_dir/database/
	
done < $out_dir/temp/input
