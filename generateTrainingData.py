import os
from os import listdir
from os.path import isfile, join, isdir
import random

def listFiles(mypath = "Annotations"):
	return [mypath + "/" + f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith("xml")]

name = dict()
files = listFiles()
for file in files:
	fullName = file[file.index('[')+1 : file.index(']')]
	file = file.replace("Annotations/", "").replace(".xml","")
	if fullName in name:
		name[fullName].append(file)
	else:
		name[fullName] = [file]

test = []
tranning = []

for key in name:
	testSize = int(len(name[key]) * 0.1)	
	testSet = random.sample(name[key], testSize)
	trainningSet = [f for f in name[key] if f not in testSet]
	test += testSet
	tranning += trainningSet

with open('trainval.txt', 'w') as out:
	for t in tranning:
		out.write(t+'\n')

with open('test.txt', 'w') as out:
	for t in test:
		out.write(t+'\n')