import os

for file in os.listdir():
	if file != "rename.py":
		os.rename(file, file + ".HEIC")

#this program took me like 30s to write its literally just to add file extensions to the files that dont have file extensions. they were all heic files so yea i just put it in the 2 folders that had broken file names and it fixed it lol
