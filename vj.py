import os
import json
import codecs
import collections
from xml.sax.saxutils import escape

#python 3.4.3
# scan current dir and detect if all *.json file are structure valid
def main():
	for root,dirs,files in os.walk(os.getcwd()):
		for fileName in files:
			if os.path.splitext(fileName)[1] == '.json':
				jsonFilePath = root+'\\'+fileName
				if(isJson(jsonFilePath)):
					print("VALID: " + fileName)

#validate if a json file is correct
def isJson(filePath):
	try:
		fileData = codecs.open(filePath, 'r', 'utf-8-sig').read()
		data = json.loads(fileData)
	except ValueError as e:
		print('JSON FILE ERROR: ' + filePath)
		print(ValueError)
		print(e)
		return False
	return True

if __name__=='__main__':
    main()
