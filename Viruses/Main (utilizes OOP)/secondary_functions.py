# functions directly related to the UX
from primary_functions import *
from UX import *

def lookup(name_of_search, array_of_search):
	print("Match found: ".center(get_width()))
	for names in array_of_search:
		if name_of_search.lower() in names.lower():
			print(names.center(get_width()) + "\n")
			return(names) # for now it only returns one and ends. Maybe return more in the future
	print("Sorry, no matches found for your search. Please try again!")
	return("Nothing")


def find_file_same_size(size):
	for filename in glob.glob('..\\..\\Training set\\DNA_collection_shapes\\*.txt'):
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		if filesize(fname + ".txt", 2) == size:
			return(''.join(filter(str.isalpha, fname.lower())))

# beta functions below


def find_file_similar(sequence):
	similarity = 100.0
	position = 0
	i = 0
	for filename in glob.glob('..\\..\\Training set\\DNA_collection_shapes\\*.txt'):
		with open(filename) as file:
			similarity_coefficient = similar(sequence, file.read())
			if abs(similarity_coefficient - 1.0) < similarity:
				position = i
				similarity = abs(similarity_coefficient - 1.0)
			# print(i, " : ", abs(similarity_coefficient-1.0), "Saved position: ", position)
		i += 1

	filename = glob.glob('..\\..\\Training set\\DNA_collection_shapes\\*.txt')[position]
	with open(filename) as file:
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		return(''.join(filter(str.isalpha, fname.lower())))
		#print(fname, " Similarity percentage: ", similar(sequence, file.read()))


def dna_to_name(sequence):
	similarity = 100.0
	position = 0
	i = 0
	for filename in glob.glob('..\\..\\Training set\\DNA_collection\\*.txt'):
		with open(filename) as file:
			similarity_coefficient = similar(sequence, file.read())
			if abs(similarity_coefficient - 1.0) < similarity:
				position = i
				similarity = abs(similarity_coefficient - 1.0)
			# print(i, " : ", abs(similarity_coefficient-1.0), "Saved position: ", position)
		i += 1

	filename = glob.glob('..\\..\\Training set\\DNA_collection\\*.txt')[position]
	with open(filename) as file:
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		return(fname)
		#print(fname, " Similarity percentage: ", similar(sequence, file.read()))
