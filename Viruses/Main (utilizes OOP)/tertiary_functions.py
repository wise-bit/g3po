# made this to add the wikipedia function

import wikipedia

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
			print(symps)
			symp = symps.split("== c")[0]
			if (len(symp) > 5):
				return("\nSymptoms include: " + symp)
			else:
				return("\nThere are no available symptoms")
		except:
			return("\nThere are no available symptoms")
	else:
		try:
			symps = cont.lower().split("symptoms")[1]
			symp = symps.split(". ")[0]
			if (len(symp) > 5):
				return("\nSymptoms include: " + symp)
			else:
				return("\nThere are no available symptoms")
		except:
			return("\nThere are no available symptoms")

