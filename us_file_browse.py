import tkinter as tki
from tkinter import ttk
from tkinter import filedialog

class Filebrowser(tki.Tk):
    def __init__(self):
        super(Filebrowser, self).__init__()
        self.title("Text Reader")
        self.minsize(800,600)

        self.labelFrame = ttk.LabelFrame(self, text= 'Open A Text File')
        self.labelFrame.grid(column=0, row=0, padx = 20, pady = 20)

        self.textbox()
        self.buttons()
        self.textarea()

    #adding a textbox
    def textbox(self):
        self.filepath = tki.StringVar()
        self.path = ttk.Entry(self.labelFrame, width=90, textvariable = self.filepath)
        self.path.grid(column = 0, row = 1, sticky = "w")
        
        
    def buttons(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File", command=self.fileDialog)
        self.button.grid(column = 1, row = 1, sticky = "w")
        self.button2 = ttk.Button(self.labelFrame, text = "Read File", command=self.readFile, state = "disabled")
        self.button2.grid(column = 2, row = 1, sticky = "w")

    

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
        self.filepath.set(self.filename) #set the textbox to the file path
        self.button2.config(state = "normal")

    def readFile(self):
        self.f = open(self.filename, "r") 
        self.textarea.insert(tki.INSERT, self.f.read())
        self.button2.config(state = "disabled")
        

    #adding a textarea
    def textarea(self):
        self.textarea = tki.Text(self.labelFrame, borderwidth=1, relief="sunken")
        self.textarea.config(font=("consolas", 12), undo=True, wrap='word')
        self.textarea.grid(row=2, column=0, sticky="w", padx = 2, pady = 2, columnspan = 3)
    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(self.labelFrame, command=self.textarea.yview)
        scrollb.grid(row=2, column=4, sticky='nsew')
        self.textarea['yscrollcommand'] = scrollb.set        
        
        

if __name__=='__main__':
    win = Filebrowser()
    win.mainloop()
