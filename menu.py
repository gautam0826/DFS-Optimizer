import sys
import os

# for running Python 3.X
if sys.version_info >= (3,0):
	import tkinter as tk
	from tkinter import *
	from tkinter import messagebox
	from tkinter import filedialog
# for running Python 2.X
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
# File 
#===================

# save Settings
def Save():
	fileName = filedialog.asksaveasfilename(
		defaultextension=".txt",
		filetypes=[('Text File (*.txt)', '*.txt'),('All Files (*.*)','*.*')],
		title='Select file')
	print(fileName)
	# Should use the write function to copy the variables to the fileName file
	# for a cleaner way
	copyfile('configurations.txt', fileName)

# load Settings
def Load():
	fileName = filedialog.askopenfilename()
	copyfile(fileName, 'configurations.txt')

# not currently needed, but available
def Options():
	print("Options")

#==================
# CSV drop down 
#==================

# import csv file into the program
# also populatetes drop down menus
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
		gui.capDropDown.children['menu'].add_command(label='Select One',command=lambda heading='Select One': gui.capDropDown.dropDownVar.set(heading))
		for h in headers: #adds headers into drop down menu
			globalVars.headerList.append(h)
			globalVars.capHeaderList.append(h)
			gui.budgetDropMenu.children['menu'].add_command(label=h,command=lambda heading=h: gui.budgetDropMenu.dropDownVar.set(heading))
			gui.capDropDown.children['menu'].add_command(label=h,command=lambda heading=h: gui.capDropDown.dropDownVar.set(heading))

# after information optimized it will be written to a csv file		
def Export():
	if settings.app.imported == True:
		print("Export File")
	else:
		messagebox.showinfo('Note', 'You must import a file before exporting!')

#=======================
# help menu dropdown 
#=======================

# redirects to team GitHub 
def GitHub():
	print("GitHub")
	webbrowser.open('https://github.com/gautam0826/DFS-Optimizer') # Links to Git Repo

# textbox about the application and team
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

# remove Setting
# small button located to the left of each optional setting
# to remove the constraint
def Remove(event):
	print('remove ' + repr(id))
	event.widget.grid_forget()

# add Setting
def Add():
	print('add')

# after adding file, have the information optimized and printed out
def Optimize():
	if settings.app.imported == True:
		print('optimize')
	else:
		messagebox.showinfo('Note', 'You must import a file before optimizing a lineup!')
