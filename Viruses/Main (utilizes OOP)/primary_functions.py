# functions for functioning of the framework

import glob 
import sys
import os
import numpy as np
from Bio import Entrez
from PIL import Image
from pathlib import Path 
from difflib import SequenceMatcher


# Clear screen
def clear():
	os.system('cls')
	return None

# Return width 
def get_width():
	hw = os.get_terminal_size()
	return(hw[0]-3)


def list_available_organisms():
	arr = []
	for filename in glob.glob('..\\..\\Training set\\DNA_collection\\*.txt'):
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		arr.append(fname)
	return arr


def extractor(organism_name):
	try:
		Entrez.email = "a@example.com" 
		handle = Entrez.esearch(db="nucleotide", term=organism_name)
		record = Entrez.read(handle)
		for i in range(20):
			select = record["IdList"][i]
			handle = Entrez.efetch(db="nucleotide", id=select, rettype="gb", retmode="xml")
			h = handle.read()
			locus = h.split("<GBSeq_locus>")[1].split("</GBSeq_locus>")
			organism_name_from_database = h.split("<GBSeq_organism>")[1].split("</GBSeq_organism>")
			hh = h.split("<GBSeq_sequence>")[1].split("</GBSeq_sequence>")
			if len(hh[0]) < 1000000:
				return(hh[0])
			if i == 19:
				return("Not found. Please try again")
			handle.close()

	except:
		return("Unexpected error. Please check input or try again later")


def artist(shape):
	chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
	f, SC, GCF, WCF = ("..\\Drawing_samples\\" + shape + ".png"), 0.08, 3, 7/4
	img = Image.open(f)
	S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
	img = np.sum( np.asarray( img.resize(S) ), axis=2)
	img -= img.min()
	img = (1.0 - img/img.max())**GCF*(chars.size-1)
	print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) )) # does not center
	return(0)


def filesize(filename, where):
	if where == 1:
		return os.stat("..\\..\\Training set\\DNA_collection\\" + filename).st_size
	elif where == 2:
		return os.stat("..\\..\\Training set\\DNA_collection_shapes\\" + filename).st_size


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

''' beta functions below '''

# artist()
# extractor()
# list_available_organisms()
