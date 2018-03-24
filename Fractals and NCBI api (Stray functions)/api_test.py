from Bio import Entrez
# import re

# delimiters = re.compile("[<GBSeq_sequence>|</GBSeq_sequence>]+")
organism_name = input("\nEnter the name: ")
try:
	Entrez.email = "a@example.com" 
	handle = Entrez.esearch(db="nucleotide", term=organism_name)
	record = Entrez.read(handle)
	for i in range(20):
		select = record["IdList"][i]
		handle = Entrez.efetch(db="nucleotide", id=select, rettype="gb", retmode="xml")

		# print(handle.read())	
		# h = re.findall(delimiters, handle.read())
		h = handle.read()
		locus = h.split("<GBSeq_locus>")[1].split("</GBSeq_locus>")
		# print(locus)
		hh = h.split("<GBSeq_sequence>")[1].split("</GBSeq_sequence>")
		# print(hh)

		if len(hh[0]) < 2000:
			print("ID: ", select, "\n")
			print("locus: ", locus[0], "\n")
			print(hh[0])
			print()
			break
		if i == 19:
			print("not found. Please try again")
		handle.close()

except:
	print("Unexpected error. Please check input or try again later")
