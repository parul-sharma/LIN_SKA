#!/bin/python


'''Usage: pipeline command to be used along with compare_genomes.sh
as a standalone script, it might be used as : 
python LIN-assignemnt.py /path/to/temporary/directoty/output/file /path/to/LIN-scheme.csv genome_name /count_df/
'''

import sys
import pandas as pd
import numpy

out_file=sys.argv[1] 
LIN_scheme=sys.argv[2]
name=sys.argv[3]
counter_file=sys.argv[4] ###the file that stores the counter at position

data = pd.read_csv(out_file,sep='\t')
print(data)

most_similar=data['Matches'].idxmax() #finding genome with most matches
#print(most_similar)
#print(data.iloc[most_similar])
#print(data.iloc[most_similar]['SNPs']) #printing the SNP number of most similar genome

SNP=data.iloc[most_similar]['SNPs'] ##recording the number of SNPs shared between query genome and most similar genome
Genome=data.iloc[most_similar]['Subject']
#Genome=Genome+'.skf'  ##extracting the final genome name of most similar genome
print(SNP)
print(Genome)

LIN=pd.read_csv(LIN_scheme, sep=',', header=None, index_col=False)
print(LIN)
#print(LIN.loc[LIN[0]==Genome])

Genome_LIN=LIN.loc[LIN[0]==Genome].copy() ##creating new df with LIN of most similar genome
#print(Genome_LIN)
New_LIN=Genome_LIN	##initializing new LIN to be added for the new genome
print("LIN initialization")
print(New_LIN)
New_LIN = New_LIN.reset_index(drop=True)
New_LIN.at[0,0]=name ##renaming the genome file name
#newLin = New_LIN.iloc[:,1:10]
#newLin.columns = range(newLin.shape[1])

df=(LIN.iloc[:,1:]) ###new df to created. This one will help toc heck whether a similar LIN postion exists. 
		    #It exists only then increase the counter in df_counter
df.columns = range(df.shape[1]) ##reshping to get column names starting from 0 
##read counter file as dataframe
#df_count=pd.read_csv(counter_file, header=None)
#print(New_LIN)




if SNP>=900:
	#df_count.at[0,0]=df_count.at[0,0]+1
	New_LIN.at[0,1]=New_LIN.at[0,1]+1
	i=1 ##index to keep track of the position at which change happened
elif SNP<900 and SNP>=700:
	New_LIN.at[0,2]=New_LIN.at[0,2]+1
	i=2
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).any(axis=1):
		#df_count.at[0,1]=df_count.at[0,1]+1
		#New_LIN.at[0,2]=df_count.at[0,1]
	#else: 
	#	New_LIN.at[0,2]=New_LIN.at[0,2]+1
elif SNP<700 and SNP>=500:
	New_LIN.at[0,3]=New_LIN.at[0,3]+1
	i=3
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).any(axis=1):
	#	df_count.at[0,2]=df_count.at[0,2]+1
	#	New_LIN.at[0,3]=df_count.at[0,2]
	#else:
	#	New_LIN.at[0,3]=New_LIN.at[0,3]+1
elif SNP<500 and SNP>=400:
	New_LIN.at[0,4]=New_LIN.at[0,4]+1
	i=4
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).all(1).any():
	#	df_count.at[0,3]=df_count.at[0,3]+1
	#	New_LIN.at[0,4]=df_count.at[0,3]
	#else: 
	#	New_LIN.at[0,4]=New_LIN.at[0,4]+1
elif SNP<400 and SNP>=300:
	New_LIN.at[0,5]=New_LIN.at[0,5]+1
	i=5
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).all(1).any():
	#	df_count.at[0,4]=df_count.at[0,4]+1
	#	New_LIN.at[0,5]=df_count.at[0,4]
	#else:
        #        New_LIN.at[0,5]=New_LIN.at[0,5]+1					
elif SNP<300 and SNP>=200:
	New_LIN.at[0,6]=New_LIN.at[0,6]+1
	i=6
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).all(1).any():
	#	df_count.at[0,5]=df_count.at[0,5]+1
	#	New_LIN.at[0,6]=df_count.at[0,5]	
	#else:
        #        New_LIN.at[0,6]=New_LIN.at[0,6]+1					
elif SNP<200 and SNP>=150:
	New_LIN.at[0,7]=New_LIN.at[0,7]+1
	i=7
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).all(1).any():
	#	df_count.at[0,6]=df_count.at[0,6]+1
	#	New_LIN.at[0,7]=df_count.at[0,6]							
	#else:
        #        New_LIN.at[0,7]=New_LIN.at[0,7]+1
elif SNP<150 and SNP>=100:
	New_LIN.at[0,8]=New_LIN.at[0,8]+1
	i=8
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).all(1).any():
	#	df_count.at[0,7]=df_count.at[0,7]+1
	#	New_LIN.at[0,8]=df_count.at[0,7]								
	#else:
        #        New_LIN.at[0,8]=New_LIN.at[0,8]+1
elif SNP<100 and SNP>=50:
	New_LIN.at[0,9]=New_LIN.at[0,9]+1
	i=9
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == newLin.to_numpy()).any(axis=1):
	#	df_count.at[0,8]=df_count.at[0,8]+1
	#	New_LIN.at[0,9]=df_count.at[0,8]
	#else:
        #        New_LIN.at[0,9]=New_LIN.at[0,9]+1
elif SNP<50:
	New_LIN.at[0,10]=New_LIN.at[0,10]+1		
	i=10
	#newLin = New_LIN.iloc[:,1:10]
	#newLin.columns = range(newLin.shape[1])
	#if (df == New_LIN.iloc[:,1:10].to_numpy()).any(axis=1):		
	#	df_count.at[0,9]=df_count.at[0,9]+1
	#	New_LIN.at[0,10]=df_count.at[0,9]
	#else:
        #        New_LIN.at[0,10]=New_LIN.at[0,10]+1
else:
	print('Something went wrong with LIN-assignment')							

print("LIN after comparing before while loop")					
print(New_LIN)
newLin = New_LIN.iloc[:,1:]
newLin.columns = range(newLin.shape[1])
while (df == newLin.to_numpy()).all(axis=1).any():
	New_LIN.at[0,i]= New_LIN.at[0,i]+1
	newLin.at[0,i-1]=newLin.at[0,i-1]+1

print("LIN after while loop")
print(New_LIN)

###adding the LIN-assignmnet of the new genome to the original DF
#LIN=LIN.append(New_LIN)

###writing to the output file
New_LIN.to_csv(LIN_scheme, mode='a', header=None, index=False)
#n = New_LIN.iloc[:,1:10]
#newLin.columns = range(newLin.shape[1])
#df_count.to_csv(counter_file,header=None, index=False)
