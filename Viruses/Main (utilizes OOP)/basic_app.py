from primary_functions import *
from secondary_functions import *
from genetic_functions import *
from tertiary_functions import *
print("\n\n")

try:
	choice = introduction()
	if choice == 1:
		name = user_query_input()
		arr = list_available_organisms()
		actual_name = lookup(name, arr)

		if (actual_name == "Nothing"):
			print("Please run the program again!")
		else:
			if "pox" not in actual_name:
				shape = find_file_same_size(filesize(actual_name + ".txt", 1))
				print("The shape is: ".center(get_width()))
			else:
				shape = "pox"
				print("The shape is: COMPLEX")
			print(shape.upper().center(get_width()))
			artist(shape)
			print(definition_fetcher(actual_name))
			resp_sym = str(input("Would you like to look at the symptoms? (y/n) "))
			if resp_sym.lower() == 'y':
				print(symptoms_fetcher(name))
			print("If this isn't the result you were looking for, please repeat DNA analysis, or use more precise search terms.".center(get_width()))
			print("INPUT ANYTHING TO EXIT THIS SEARCH".center(get_width()))
			input()
			clear()

	elif choice == 2:
		dna = ""
		try:
			dna = device_input()
		except:
			print("Program not paired with sequencer".center(get_width()))
			print("Please enter DNA sequence manually: ".center(get_width()))
			dna = input()
			shape = find_file_similar(dna)
			print("The shape is: ".center(get_width()))
			print(shape.upper().center(get_width()))
			artist(shape)
			print("There is a chance this DNA is similar to: ".center(get_width()))
			name = dna_to_name(dna)
			print(name.center(get_width()))
			print(definition_fetcher(name))
			resp_sym = str(input("Would you like to look at the symptoms? (y/n) "))
			if resp_sym.lower() == 'y':
				print(symptoms_fetcher(name))
			print("If this isn't the result you were looking for, please repeat DNA analysis, or use more precise experiment measures.".center(get_width()))
			print("INPUT ANYTHING TO EXIT THIS SEARCH".center(get_width()))
			input()
			clear()

	elif choice == 3:
		dna = input()
		find_file_similar(dna)

	elif choice == 4:
		print("Unable to establish connection to database, try again.")
		exit()

	elif choice == 5:
		clear()
		exit()

	else:
		print("Sorry, that choice isn't available.")
		exit()

except:
	print("\n\n\n" + "Invalid choice. Please try again.".center(get_width()))
