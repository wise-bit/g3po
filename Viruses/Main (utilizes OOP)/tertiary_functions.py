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
	return(info)
	# 	print("\n" + str(loc1) + " " + str(loc2))

# tester

