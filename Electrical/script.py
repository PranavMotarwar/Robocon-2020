import os
import pandas as pd 

def make_folders(filename):
	data = pd.read_csv(filename)
	names = data["Names"]
	for name in names:
		os.mkdir(name)


make_folders("elec.csv")