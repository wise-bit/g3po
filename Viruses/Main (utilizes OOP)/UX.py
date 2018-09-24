import numpy as np
from PIL import Image
import os

# Clear screen
def clear():
	os.system('cls')
	return None


# Return width 
def get_width():
	hw = os.get_terminal_size()
	return(hw[0]-3)


def artist(shape):
	chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
	f, SC, GCF, WCF = ("..\\Drawing_samples\\" + shape + ".png"), 0.08, 3, 7/4
	img = Image.open(f)
	S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
	img = np.sum( np.asarray( img.resize(S) ), axis=2)
	img -= img.min()
	img = (1.0 - img/img.max())**GCF*(chars.size-1)
	print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) )) # does not center
	return(0)

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



