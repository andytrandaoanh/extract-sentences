import sys
import system_handler as sysHandle
from extracts import extractSentences




def processText(pathIn, dirOut):
	pathOut = sysHandle.getRawPath(pathIn, dirOut)
	
	#print(pathIn)
	#print(pathOut)
	extractSentences(pathIn, pathOut)
	#print(cleanList)
	#sysHandle.writeListToFile(cleanList, pathOut)
	sysHandle.openDir(dirOut)
	sys.exit()
