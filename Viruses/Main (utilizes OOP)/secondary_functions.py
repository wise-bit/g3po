# functions directly related to the UX
from primary_functions import *

def user_query_input():
	print("Hello! What would you like to look up today?".center(get_width()))
	organism = input("".center(int(get_width()/2) - 21))
	return organism

def introduction():
	clear()
	print("Welcome to the DNA analyzer v 2.0 [AKA G3PO]\n\n\n\n".center(get_width()))
	print("Please chose one of the options below in order to begin analysis\n\n".center(get_width()))
	print("\t\t1. Analysis of name of disease from our growing database")
	print("\t\t2. Analysis from provided DNA (Can be paired with a DNA sequencer)")
	print("\t\t3. Debug (ONLY for testing purposes)")
	print("\t\t4. New addition to training database")
	print("\t\t5. Exit application (Can also be done by pressing ctrl+Z at any moment)")
	a = int(input("\n\t\tYour choice: "))
	clear()
	return a


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
