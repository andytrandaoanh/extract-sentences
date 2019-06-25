FILE_NAME = 'exclusion.txt'

exclusion = ['a', 'b', 'c']

def write_list_to_file(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:
        	if (str(item) != ''):
        		file.write(item + "\n")

def clean_list(inputlist):
	result = inputlist
	result = list( dict.fromkeys(result))
	result.sort()
	return result


 

#newlist = clean_list(exclusion)
#write_list_to_file(newlist, FILE_NAME)
def open_exc_file():
	try:
	    fh = open(FILE_NAME, 'r', encoding ='utf-8')
	    # Store configuration file values
	    data = fh.read()
	    fh.close()   
	    mylist = data.split('\n')
	    return mylist
	    #print(mylist)
	    #print("file found!")
	    
	    
	except FileNotFoundError:
		print('file not found')
		return None

def rebuild_exclution_file():
	mylist = open_exc_file()
	mylist = clean_list(mylist)
	write_list_to_file(mylist, FILE_NAME)
	


rebuild_exclution_file()
