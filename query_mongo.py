import datetime
import json
import pprint
from pymongo import MongoClient


client = MongoClient('localhost', 27017)


DB_NAME = 'lexicon'
COLLECTION_NAME = 'vol_a'

db = client[DB_NAME]
examples = db[COLLECTION_NAME]

eg = examples.find_one({'key_word':'abbreviations'})

print(eg)


#ex_id = '5d01f654a09ce8b25f89cf33'

#pprint.pprint(examples.find_one({"_id": ex_id}))