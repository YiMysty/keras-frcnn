import xml.etree.ElementTree as ET
import os
from os import listdir
from os.path import isfile, join, isdir

imageAnnotationDestinationPath = "/Users/mingziyi/Desktop/annotation"
imageDestinationPath = "/Users/mingziyi/Desktop/image"
writeFile = False

def listFiles(mypath):
	return [mypath + "/" + f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith("xml")]

def listReadyFolders(mypath):
	return [mypath + "/" + f for f in listdir(mypath) if isdir(join(mypath, f)) and f.find("ready") >=0]

def listFolders(mypath):
	return [mypath + "/" + f for f in listdir(mypath) if isdir(join(mypath, f))]

def doRename(folder):
	global imageDestinationPath, writeFile
	files = listFiles(folder)
	imageFolder = listReadyFolders(folder)

	for file in files:
		tree = ET.parse(file)
		root = tree.getroot()
		prefix = file.split("/")[-2]
		for child in root:
			if child.tag == "filename":
				newName = prefix + child.text
				imagePath = imageFolder[0] + "/" + child.text
				newImagePath = imageDestinationPath + "/" + newName
				if isfile(imagePath):
					if writeFile:
						os.rename(imagePath, newImagePath)
				else:
					print imagePath
				child.text = newName
		if writeFile:
			tree.write(file)
	doRenameXml(folder)

def doRenameXml(folder):
	global imageAnnotationDestinationPath,writeFile
	files = listFiles(folder)
	for file in files:
		prefix = file.split("/")[-2]
		fileName = file.split("/")[-1]
		newFileName = prefix + fileName
		newFilePath = imageAnnotationDestinationPath + "/" + newFileName
		if writeFile:
			os.rename(file, newFilePath)


mainFolderPath = "/Users/mingziyi/Desktop/"
mainFolders = listFolders(mainFolderPath)
for folder in mainFolders:
	doRename(folder)
#doRename("/Users/mingziyi/Desktop/annotation[Strawberry] 4")

