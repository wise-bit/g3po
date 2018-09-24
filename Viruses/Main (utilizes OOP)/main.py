# import GUI

from prediction_functions import *

# make_dict()

# with open("Prediction_storage\\keywords.txt", "r") as file:
# 	create_symptoms_database(file)

with open("Prediction_storage\\keywords.txt", "r") as file:
	check_symptoms_database(file)


import basic_app