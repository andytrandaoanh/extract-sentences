import os, sys
import tika
tika.initVM()
from tika import parser
import json

def open_dir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)
def getNormalPath(outfile, outdir):
	TEXT_EXT = ".txt"
	
	temp_path = outfile
	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	normal_path =  os.path.join(outdir, fname +  TEXT_EXT) 
	return(normal_path)


def processText(path1, path2):
	output_path = getNormalPath(path1, path2)
	parsed = parser.from_file(path1)
	textout = parsed["content"]
	with open(output_path, 'w', encoding="utf-8") as file:    
		file.write(parsed["content"])
	open_dir(path2)
	sys.exit()
