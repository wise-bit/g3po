import glob ## for going through every file in a directory
from pathlib import Path   # for extracting simply the file name
import matplotlib.pyplot as plt
import os

wordfreq = {}
total = len(os.listdir('..\\..\\Training set\\DNA_collection_shapes'))

def list_available_organisms():
	for filename in glob.glob('..\\..\\Training set\\DNA_collection_shapes\\*.txt'):
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		word = ''.join(filter(str.isalpha, fname.lower())) # replaceAll("\\P{L}+", "");
		if word not in wordfreq:
			wordfreq[word] = 0 
		wordfreq[word] += 1
	return wordfreq

print(list_available_organisms())

for word in wordfreq:
	wordfreq[word] = wordfreq[word]*100/total

plt.bar(range(len(wordfreq)), list(wordfreq.values()), align='center')
plt.xticks(range(len(wordfreq)), list(wordfreq.keys())) # plt.xticks(range(len(wordfreq)), map(lambda x: 2*x, list(wordfreq.keys())))
plt.xlabel("Shape")
plt.ylabel("Frequency (%)")
plt.ylim(ymax=100)
plt.show()