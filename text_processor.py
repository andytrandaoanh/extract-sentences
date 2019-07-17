import sys
import system_handler as sysHandle
from extracts import extractSentences




def processText(pathIn, dirOut, dirLog):
	
	#print('pathIn', pathIn, '\ndirOut', dirOut, '\ndirLog', dirLog)
	pathOut = sysHandle.getRawPath(pathIn, dirOut)
	pathLog = sysHandle.getDatedFilePath(dirLog)
	#print('pathLog:', pathLog)
	
	#print(pathIn)
	#print(pathOut)

	logData = []
	dateStamp = sysHandle.getDateStamp()
	logData.append("Starting to extract sentences at " + dateStamp)


	#print('dateStamp:', dateStamp)


	extractSentences(pathIn, pathOut)
	#print(cleanList)
	
	dateStamp = sysHandle.getDateStamp()
	logData.append("Sentence extracting completed at " + dateStamp)


	sysHandle.writeListToFile(logData, pathLog)
	sysHandle.openDir(dirOut)
	sys.exit()
