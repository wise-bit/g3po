import glob ## for going through every file in a directory
from pathlib import Path   # for extracting simply the file name


def list_available_organisms():
	for filename in glob.glob('..\\DNA_collection\\*.txt'):
		fname = Path(filename).name
		fname = fname.replace(".txt", "")
		print(fname)

list_available_organisms()