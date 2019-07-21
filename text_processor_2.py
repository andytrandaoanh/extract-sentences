import os, sys
import system_handler as sysHandle
from mysql_data import getWordList
from database_handler import upload_data

def uploadData(pathIn, bookID, dirLog):
	
	filePrefix = "Upload_Sentences_To_MySQL_on_"
	pathLog = sysHandle.getDatedFilePath(filePrefix, dirLog)

	logData = []
	dateStamp = sysHandle.getDateStamp()
	logData.append("Starting to upload sentences at " + dateStamp)
	logData.append("BookID being uploaded: " + str(bookID))
	#print(pathIn, bookID)
	sentence_total = upload_data(pathIn, bookID)

	logData.append("Total sentences written to MySQL " + str(sentence_total))
	#sysHandle.openDir(outDir)
		
	dateStamp = sysHandle.getDateStamp()
	logData.append("Sentence uploading completed at " + dateStamp)


	sysHandle.writeListToFile(logData, pathLog)
	sys.exit()