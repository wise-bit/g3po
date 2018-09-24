# functions for functioning of the framework

import glob 
import sys
import os
from pathlib import Path 
from difflib import SequenceMatcher
import wikipedia
from prediction_functions import get_symptoms_list


def filesize(filename, where):
	if where == 1:
		return os.stat("..\\..\\Training set\\DNA_collection\\" + filename).st_size
	elif where == 2:
		return os.stat("..\\..\\Training set\\DNA_collection_shapes\\" + filename).st_size


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def list_available_organisms():
	arr = []
	for filename in glob.glob('..\\..\\Training set\\DNA_collection\\*.txt'):
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		arr.append(fname)
	return arr


# made this to add the wikipedia function

# This fetches the definition of a disease from wikipedia 
def definition_fetcher(name):
	page = wikipedia.page(name)
	info = wikipedia.summary(name, sentences=2)
	loc1, loc2 = 0, 50
	for i in range (len(info)):
		if info[i] == "(":
			loc1 = i; break;
	for i in range(loc2, 0, -1):
		if info[i] == ")":
			loc2 = i; break;
	info = info[0:loc1-1] + info[loc2+1:]
	return("\n" + info)
	# 	print("\n" + str(loc1) + " " + str(loc2))


# This part fetches sypmtoms of a disease 
def symptoms_fetcher(name):
	page = wikipedia.page(name)
	cont = page.content
	# print(page.sections)
	symptoms = page.section("Signs and symptoms")
	# return 0
	# print(str(cont))
	if len(str(symptoms)) > 5:
		return(symptoms)
	elif (symptoms != None):
		try:
			symps = str(cont).lower().split("== signs and symptoms ==")[1]
			# symps = symps.split("== c")[0]
			# if (len(symp) > 5):
			# 	return("\nSymptoms include: " + symp)
			# else:
			# 	return("\nThere are no available symptoms")
		except:
			return("\nThere are no available symptoms")
	else:
		try:
			symps = cont.lower().split("symptoms")[1]
			# symps = symps.split(". ")[0]
			# if (len(symp) > 5):
			# 	return("\nSymptoms include: " + symp)
			# else:
			# 	return("\nThere are no available symptoms")
		except:
			return("\nThere are no available symptoms")

	valid = []
	symp_dict = get_symptoms_list()

	for x in symps.split(" "):
		print(x)
		if x.lower() in symp_dict:
			valid.append(x)

	valid = list(set(valid))
	return ("Symptoms and potential victims include: " + ', '.join([str(x) for x in valid]) )

