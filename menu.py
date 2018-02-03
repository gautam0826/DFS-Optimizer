import sys
# For running Python 3.X
if sys.version_info >= (3,0):
	import tkinter as tk
	from tkinter import *
	from tkinter import messagebox
# For running Python 2.X
else:
	import Tkinter as tk
	from Tkinter import *
	import tkMessageBox
import webbrowser
import settings
from globalVars import *
from gui import *
import subprocess
import gui
import csv
#===================
# Top Bar Functions
#===================

# File =============

# Save Settings
def Save():
	print("Save")

# Load Settings
def Load():
	print("Load")

def Options():
	print("Options")

# CSV ==============
def Import():
	fileName = filedialog.askopenfilename()
	print(fileName)
	if fileName != '':
		settings.app.imported = True

def Export():
	if settings.app.imported == True:
		print("Export File")
	else:
		messagebox.showinfo('Note', 'You must import a file before exporting!')

# Help =============
def GitHub():
	print("GitHub")
	webbrowser.open('https://github.com/gautam0826/DFS-Optimizer') # Links to Git Repo

def About():
	print("About")
	about = Toplevel()

	about.protocol("WM_DELETE_WINDOW", about.destroy)

	frame = Frame(about, width=500, height=300)
	frame.pack()
	frame.pack_propagate(False)
	
	var1 = StringVar()
	text1 = Label(frame, textvariable=var1)
	var1.set("Desktop application that reads an Excel file\n" +
	    "and lets users select what to maximize, minimize,\n" +
	    " and constraints to add.\n")
	text1.pack()

	text = Label(frame, text="Created by:", font='Helvetica 16 bold')
	text.pack()

	var2 = StringVar()
	text2 = Label(frame, textvariable=var2, font='Helvetica 12 bold', justify=LEFT)
	var2.set("Gautam Sarkar, Joseph Casteloes, Joelle Steichen,\n" +
	    "Ben Sherriff, Nagie Khant, Edmund Yu")
	text2.pack()
	
	about.mainloop()

#===================
#   GUI Functions
#===================

# Remove Setting
# Small button located to the left of each optional setting
# to remove the constraint
def Remove(event):
	print('remove ' + repr(id))
	event.widget.grid_forget()

# Add Setting
def Add():
	print('add')

def Optimize():
    if settings.app.imported == True:
        print('optimize')
        #Run the optomizer using Popen
        subprocess.Popen('python lineups.py').wait()
        #display the results from the csv file using labels in tkinter. currently not optimized. Need to set up for non-windows devices
        with open("temp_folder/temp_output.csv", newline = "") as file:
            reader = csv.reader(file)
            r = 0
            for col in reader:
                c = 0
                for row in col:
                    label = tk.Label(gui.bot, width = 10, height = 2, \
                                          text = row, relief = tk.RIDGE)
                    label.grid(row = r, column = c)
                    c += 1
                r += 1
    else:
        messagebox.showinfo('Note', 'You must import a file before optimizing a lineup!')