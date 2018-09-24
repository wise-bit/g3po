import glob 
import sys
import os
import numpy as np
from Bio import Entrez
from pathlib import Path 
from difflib import SequenceMatcher


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


def test_accuracy():
