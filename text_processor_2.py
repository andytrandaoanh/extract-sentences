import os, sys
import system_handler as sysHandle
from mysql_data import getWordList
from database_handler import upload_data

def uploadData(pathIn, bookID):
	#print(pathIn, bookID)
	upload_data(pathIn, bookID)
	#sysHandle.openDir(outDir)
	sys.exit()

