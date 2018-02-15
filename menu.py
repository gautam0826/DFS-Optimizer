import sys
import os
# For running Python 3.X
if sys.version_info >= (3,0):
	import tkinter as tk
	from tkinter import *
	from tkinter import messagebox
	from tkinter import filedialog
# For running Python 2.X
else:
	import Tkinter as tk
	from Tkinter import *
	import tkMessageBox
	from Tkinter import tkFileDialog
from shutil import copyfile
import webbrowser
import settings
import globalVars
from gui import *
import gui

#===================
# Top Bar Functions
#===================

# File =============

# Save Settings
def Save():
	fileName = filedialog.asksaveasfilename(
		defaultextension=".txt",
		filetypes=[('Text File (*.txt)', '*.txt'),('All Files (*.*)','*.*')],
		title='Select file')
	print(fileName)
	# Should use the write function to copy the variables to the fileName file
	# for a cleaner way
	copyfile('configurations.txt', fileName)

# Load Settings
def Load():
	fileName = filedialog.askopenfilename()
	copyfile(fileName, 'configurations.txt')

def Options():
	print("Options")

# CSV ==============
def Import():
	fileName = filedialog.askopenfilename()
	fileChosen = os.path.basename(fileName)

	if fileName != '': 
		settings.app.imported = True
		with open('configurations.txt', 'a') as configurations:
                        configurations.write('6 ' + fileName + '\n')
		gui.makeConfigFile()
	headers = []
	if fileChosen == '': #checks if a file has been chosen
		globalVars.headerList = ['Select One']
		globalVars.capHeaderList = ['Select One']
		print(fileChosen + 'empty')
	else:
		gui.budgetDropMenu.children['menu'].delete(0, 'end') #empty list
		gui.capDropDown.children['capOptions'].delete(0, 'end')
		with open(fileName,newline='') as csvfile:
			headings = csv.reader(csvfile)
			headers = next(headings)
		globalVars.headerList.append('Select One')
		globalVars.capHeaderList.append('Select One')
		gui.budgetDropMenu.children['menu'].add_command(label='Select One',command=lambda heading='Select One': gui.budgetDropMenu.dropDownVar.set(heading))
		gui.capDropDown.children['menu'].add_command(label='Select One',command=lambda heading='Select One': gui.capDropDown.dropDownVari.set(heading))
		for h in headers: #adds headers into drop down menu
			globalVars.headerList.append(h)
			globalVars.capHeaderList.append(h)
			gui.budgetDropMenu.children['menu'].add_command(label=h,command=lambda heading=h: gui.budgetDropMenu.dropDownVar.set(heading))
			gui.capDropDown.children['menu'].add_command(label=h,command=lambda heading=h: gui.capDropDown.dropDownVari.set(heading))
		
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
	else:
		messagebox.showinfo('Note', 'You must import a file before optimizing a lineup!')
