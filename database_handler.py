import os, sys
import json
from mysql_handler import prepare_data_for_update 





def upload_data(inPath, bookID):
	#print('inPath:', inPath, 'dbDir:', dbDir, 'bookID:', bookID)
	#print(pathNin, pathSin)
	jsonPath = inPath
	#print(jsonPath)
	with open(jsonPath) as f:
		sentences = json.load(f)
	
	dbData = []
	for sentence in sentences:
		temp = sentence[0]
		dbData.append((int(bookID), temp['sent_cont'], temp['sent_num']))
		
	prepare_data_for_update(dbData)
