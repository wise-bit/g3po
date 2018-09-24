# import DictWriter
import pickle

'''

There are three main formulas being used for the prediction functions, you know what they are. Now code!
Also, refactor your old garbage code

'''

def make_dict():
	keyfile = open('keywords.txt', 'r')
	resp_file = open('out_res.txt', 'r')
	freq1 = word_freq(keyfile)
	freq2 = word_freq(resp_file)

	## The next 5 lines or so deal with the creation of a full dictionary of all words with percentages
	word_freq = sorted(word_freq)
	word_freq = sorted(word_freq.keys(), key=lambda x:x.lower())

	# Store with pickle
	with open('objs.pkl', 'w') as f:  # Python 3: open(..., 'wb')
		pickle.dump([obj0, obj1, obj2], f)

	corpus = len(words)*1.0
	for key in word_freq:
		resp_file.write("{} --> {}      ---> {}%\n".format(key, word_freq[key], (word_freq[key]*100.0/corpus)))

	'''

	This next section was useful for another project, and therefore commented out until use is appropriate

	# myList = []

	# for key in freq2:
	# 	try:
	# 		if freq1[key] < 5:
	# 			myList.append(key)
	# 	except KeyError:
	# 		myList.append(key)

	#print myList
	strr = "Some keywords are: {}".format([item for item in myList])
	print(re.sub('[^A-Za-z0-9:]+', ' ', strr))

	keyfile.close()
	resp_file.close()


	'''

def word_freq(file):
	data = file.read().lower()
	data = re.sub('[^A-Za-z0-9]+', ' ', data)
	words = data.split()
	word_freq = {}

	for word in words:
		if word in word_freq: word_freq[word] += 1
		else: word_freq[word] = 1

	return word_freq

# make_dict()

def function1(): # using a dictionary with word frequencies

	# TODO: Store dictionary as file

	return 0


def create_symptoms_database(file):
	symptoms = file.read().lower().split(", ")
	with open('Prediction_storage\\symptoms_set.pkl', 'wb') as f:
		pickle.dump(symptoms, f)

def check_symptoms_database(file):
	with open('prediction_storage\\symptoms_set.pkl', 'rb') as f:
		stored_symptoms = pickle.load(f)

	print(len(stored_symptoms))
