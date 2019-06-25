import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import config_handler
import text_processor
import database_handler
import extracts



class LexGUI:



    def __init__(self, win):
    	self.master = win
    	



    def createTabs(self):
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [40, 10],
                                        "font" : ('URW Gothic L', '11', 'bold')},}})
        s.theme_use("MyStyle")
        s.configure('TButton', relief='raised', padding= 6)
        

        self.tabControl = ttk.Notebook(self.master)
        
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Input')
        self.tabControl.add(self.tab2, text = 'Output')      
        self.tabControl.add(self.tab3, text = 'Extract')
        self.tabControl.add(self.tab4, text = 'Upload')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("PDF files", "*.pdf"), ("EPUB files", "*.epub"), ("all files", "*.*")))
        if (self.filename):
            self.filepath.set(self.filename) #set the textbox to the file path
            #self.button2.config(state = "normal")
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE,self.filename)

     
 
    def createTab1(self):
        #frame

        self.labelFrame = ttk.LabelFrame(self.tab1, text= 'Open An Ebook')
        self.labelFrame.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox
        self.filepath = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE)
        self.filepath.set(value)
        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)


        self.path = ttk.Entry(self.labelFrame, width=90, textvariable = self.filepath)
        self.path.grid(column = 0, row = 1, sticky = "w")

        #button
        self.button = ttk.Button(self.labelFrame, text = "Browse A File", command=self.fileDialog)
        self.button.grid(column = 1, row = 1, sticky = "w")
        

        

    def dirDialog(self):
        self.filename2 = filedialog.askdirectory()
        if (self.filename2):
            self.filepath2.set(self.filename2) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR,self.filename2)


    def dirDialog2(self):
        self.filename3 = filedialog.askdirectory()
        if (self.filename3):
            self.filepath3.set(self.filename3) #set the textbox to the file path
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_UPLOAD_DIR,self.filename3)

    def dirDialog3(self):
        self.filename5 = filedialog.askdirectory()
        if (self.filename5):
            self.filepath5.set(self.filename5) #set the textbox to the file path
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_DICTIONARY_DIR,self.filename5)

    def dirDialog4(self):
        self.filename6 = filedialog.askdirectory()
        if (self.filename6):
            self.filepath6.set(self.filename6) #set the textbox to the file path
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_CORRECT_DIR,self.filename6)

        
    def processText(self):
        if(self.filepath.get() and self.filepath2.get()):
            text_processor.processText(self.filepath.get(), self.filepath2.get())
        else:
            messagebox.showwarning("Error", "Missing input file or output directory")
            

    def uploadData(self):
        if(self.filepath.get() and self.filepath3.get() and self.bookid.get()):
            database_handler.uploadData(self.filepath.get(), self.filepath3.get(), self.bookid.get() )
        else:
            messagebox.showwarning("Error", "Missing input file or upload directory or book ID")
   
    def checkData(self):
        if(self.filepath5.get()):
            extracts.extractSentences(self.filepath.get(), self.filepath2.get(), self.filepath5.get())
            
        else:
            messagebox.showwarning("Error", "Missing dictionary or correct directory")


    def createTab2(self):
        self.labelFrame2 = ttk.LabelFrame(self.tab2, text= 'Select Ouput Directory')
        self.labelFrame2.grid(column=0, row=0, padx = 20, pady = 20)

      #button 3
        self.button3 = ttk.Button(self.labelFrame2, text = "Browse Directory", command=self.dirDialog)
        self.button3.grid(column = 1, row = 1, sticky = "w")
  

       #textbox 2
        self.filepath2 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR)
        self.filepath2.set(value) 
        self.path2 = ttk.Entry(self.labelFrame2, width=90, textvariable = self.filepath2)
        self.path2.grid(column = 0, row = 1, sticky = "w")
        

        #label 5
        self.label5 = ttk.Label(self.labelFrame2, text="Click button to start extracting text:")
        self.label5.grid(column = 0, row = 6, sticky = "w")
        #button no 5
        self.button5 = ttk.Button(self.labelFrame2, text = "Start Process", command=self.processText)
        self.button5.grid(column = 0, row = 7)


    def saveBookID(self):       
        cf = config_handler.ConfigHandler()
        cf.set_config_value(cf.RECENT_BOOK_ID,str(self.bookid.get()))

  

    def createTab3(self):
        self.labelFrame4 = ttk.LabelFrame(self.tab3, text= 'Select Directory for Output Sentences')
        self.labelFrame4.grid(column=0, row=0, padx = 20, pady = 20)
               #textbox 3
        self.filepath5 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_DICTIONARY_DIR)
        self.filepath5.set(value) 
        self.textbox5 = ttk.Entry(self.labelFrame4, width=90, textvariable = self.filepath5)
        self.textbox5.grid(column = 0, row =1, sticky = "w")
        
        #button 8
        self.button8 = ttk.Button(self.labelFrame4, text = "Browse Directory", command=self.dirDialog3)
        self.button8.grid(column = 1, row = 1, sticky = "w")

  

       #label 10
        self.label11 = ttk.Label(self.labelFrame4, text="Click to split:")
        self.label11.grid(column = 0, row = 4, sticky = "w")
      #button 9
        self.button9 = ttk.Button(self.labelFrame4, text = "Extract Sentences", command=self.checkData)
        self.button9.grid(column = 0, row = 5, sticky = "w")

    def createTab4(self):
        self.labelFrame3 = ttk.LabelFrame(self.tab4, text= 'Select Upload Directory')
        self.labelFrame3.grid(column=0, row=0, padx = 20, pady = 20)
        
        #textbox 3
        self.filepath3 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_UPLOAD_DIR)
        self.filepath3.set(value) 
        self.path3 = ttk.Entry(self.labelFrame3, width=90, textvariable = self.filepath3)
        self.path3.grid(column = 0, row =1, sticky = "w")
        
   
        #button 6
        self.button6 = ttk.Button(self.labelFrame3, text = "Browse Directory", command=self.dirDialog2)
        self.button6.grid(column = 1, row = 1, sticky = "w")


 
        #label 7
        self.label7 = ttk.Label(self.labelFrame3, text="Book ID:")
        self.label7.grid(column = 0, row = 2, sticky = "w")

        #textbox 4
        self.bookid = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_BOOK_ID)

        self.bookid.set(value) 
        self.textbox4 = ttk.Entry(self.labelFrame3, width=90, textvariable = self.bookid)
        self.textbox4.grid(column = 0, row = 3, sticky = "w")
      
        #button no 6
        self.button6 = ttk.Button(self.labelFrame3, text = "Save ID", command=self.saveBookID)
        self.button6.grid(column = 1, row = 3, sticky = "w")

         #label 7
        self.label8 = ttk.Label(self.labelFrame3, text="Click button to start processing text:")
        self.label8.grid(column = 0, row = 4, sticky = "w")
        #button no 7
        self.button7 = ttk.Button(self.labelFrame3, text = "Start Upload", command=self.uploadData)
        self.button7.grid(column = 0, row = 5)

  

    def createGUI(self):
        self.createTabs()    
        self.createTab1()
        self.createTab2()
        self.createTab3()
        self.createTab4()