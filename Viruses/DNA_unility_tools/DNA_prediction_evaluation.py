# NOTE: LAST RUN TOOK 118 SECONDS TO COMPLETE AND MADE COMPUTER WITH I7 PROCESSOR HEAT UP. CONSIDER IF YOU REALLY NEED TO RUN IT

import glob 
import sys
import os
import numpy as np
from Bio import Entrez
from PIL import Image
from pathlib import Path 
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

import time
start_time = time.time()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def dna_to_type_prediction(num_train, sequence):
	similarity = 100.0
	position = 0
	i = 0
	program_limiter = 0
	for filename in glob.glob('..\\..\\Training set\\DNA_collection_shapes\\*.txt'):
		program_limiter += 1
		if program_limiter > num_train:
			break
		else:
			with open(filename) as file:
				similarity_coefficient = similar(sequence, file.read())
				if abs(similarity_coefficient - 1.0) < similarity:
					position = i
					similarity = abs(similarity_coefficient - 1.0)
		i += 1

	filename = glob.glob('..\\..\\Training set\\DNA_collection_shapes\\*.txt')[position]
	with open(filename) as file:
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		return(''.join(filter(str.isalpha, fname.lower())))

for num_train in range(30):
	truth = 0
	falsehood = 0
	for filenames in glob.glob('..\\..\\Testing set\\DNA_collection_shapes\\*.txt'):
		ffname = Path(filenames).name
		ffname = ffname.replace(".txt", "")
		with open(filenames) as fnm:
			if ''.join(filter(str.isalpha, ffname.lower())) == dna_to_type_prediction(num_train, fnm.read()):
				truth += 1
			else:
				falsehood += 1
	
	plt.plot(num_train, (truth*100/(falsehood+truth)), "o")

plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
print("\n\n" + str(truth*100/(falsehood+truth)) + " % correct guesses!" ) # + str(falsehood*100/(falsehood+truth)) + " %")
