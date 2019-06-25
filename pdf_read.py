#!/usr/bin/env python
import tika
tika.initVM()
from tika import parser
import json



file_path = "E:/FULLTEXT/ORIGINAL/BOOK 001_[BELKER Loren 2012] The First Time Manager 6th Edition.pdf"

file_path2 = "E:/FULLTEXT/ORIGINAL/BOOK 003 [COVEY Stephen 2004] The-7-habits-of-highly-effective-people.epub"

parsed = parser.from_file(file_path2)
#print(parsed["metadata"])
#print(parsed["content"])

textout = parsed["content"]
#print(textout.encode("utf-8"))


output_path = "epub_extract.txt"
with open(output_path, 'w', encoding="utf-8") as file:    
    #file.write(json.dumps(parsed))
    file.write(parsed["content"])

