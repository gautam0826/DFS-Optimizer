import sys
import os

# for running Python 3.X
if sys.version_info >= (3,0):
	import tkinter as tk
	from tkinter import *
	from tkinter import messagebox
	from tkinter import filedialog
	from pathlib import Path
# for running Python 2.X
else:
	import Tkinter as tk
	from Tkinter import *
	import tkMessageBox
	from Tkinter import tkFileDialog
	from pathlib2 import Path
from shutil import copyfile
import shutil
import webbrowser
import settings
import settings
from gui import *
import gui
import subprocess
import csv
import pandas

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
	# If a file was selected, run load. Otherwise do nothing
	if fileName != '':
		copyfile(fileName, 'configurations.txt')
		# Load values from configurations.txt into variables
		with open('configurations.txt') as f:
			content = f.readlines()
		f.close()
		content = [line.strip() for line in content]
		for line in content:
			line = line.split(' ', 1)
			if line[0] is '1':
				lineups = line[1]
				gui.lineups.set(lineups)	# Variable 1
			elif line[0] is '2':
				players = line[1]
				gui.players.set(players)	# Variable 2
			elif line[0] is '3':
				projections_column = line[1]
			elif line[0] is '4':
				maxCost = line[1]
				gui.maxCost.set(maxCost)	# Variable 4
			elif line[0] is '5':
				budget_column = line[1]
			elif line[0] is '6':
				input_csv_location = line[1]
			elif line[0] is '7':
				numPos = line[1]
				gui.numPos.set(numPos)		# Variable 7

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
		settings.headerList = ['Select One']
		settings.capHeaderList = ['Select One']
		settings.budgetHeaderList = ['Select One']
		settings.projectionsHeaderList = ['Select One']
		print(fileChosen + 'empty')
	else:
		gui.displayDropMenu.children['menu'].delete(0, 'end') #empty list
		gui.capDropDown.children['menu'].delete(0, 'end')
		gui.budgetDropMenu.children['menu'].delete(0, 'end')
		gui.projectionsDropMenu.children['menu'].delete(0, 'end')
		with open(fileName,newline='') as csvfile:
			headings = csv.reader(csvfile)
			headers = next(headings)
		settings.headerList.append('Select One')
		settings.capHeaderList.append('Select One')
		for h in headers: #adds headers into drop down menu
			settings.headerList.append(h)
			settings.capHeaderList.append(h)
			gui.displayDropMenu.children['menu'].add_command(label=h,command=lambda heading=h: gui.displayDropMenu.dropDownVar.set(heading))
			gui.capDropDown.children['menu'].add_command(label=h,command=lambda heading=h: gui.capDropDown.dropDownVar.set(heading))
			gui.budgetDropMenu.children['menu'].add_command(label=h,command=lambda heading=h: gui.budgetDropMenu.dropDownVar.set(heading))
			gui.projectionsDropMenu.children['menu'].add_command(label=h,command=lambda heading=h: gui.projectionsDropMenu.dropDownVar.set(heading))

# after information optimized it will be written to a csv file		
def Export():
    if settings.app.imported == True:
        print("Export File")
        fileName = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[('CSV File (*.csv)', '*.csv'),('All Files (*.*)','*.*')],
        title='Select file')
        filePath = Path(os.path.join('temp_folder', 'temp_output.csv'))
        if (filePath.is_file()):
            copyfile(os.path.join('temp_folder', 'temp_output.csv'), fileName)
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

def QuickPickHelp():
    #locates it in the menu bar up top
    about = Toplevel()

    about.protocol("WM_DELETE_WINDOW", about.destroy)

    frame = Frame(about, width=500, height=300)
    frame.pack()
    frame.pack_propagate(False)
    
    titleName = StringVar()
    titleText = Label(frame, textvariable=titleName,font='Helvetica 18')
    titleName.set("Welcome to Quick Pick Help Center.\n")
    titleText.grid(column =0, row = 1)
  
    getGeneralTitle = Label(frame, text='General Questions', font='Helvetica 16 bold')
    getGeneralTitle.grid(column = 0, row = 2, sticky = W)

    # Question 1
    generalQuestionOne =  Label(frame, text='Why can’t I click the optimize button?', font='Helvetica 14 italic')
    generalQuestionOne.grid(column = 0, row = 3, sticky = W)
    generalAnswerOne =  Label(frame, text='    You must first stage your settings before the optimizer can your input ' +
    	'file.', font='Helvetica 14')
    generalAnswerOne.grid(column = 0, row = 4, sticky = W)
    # Question 2
    generalQuestionTwo =  Label(frame, text='How do I save my configurations for later use', font='Helvetica 14 italic')
    generalQuestionTwo.grid(column = 0, row = 5, sticky = W)
    generalAnswerTwo =  Label(frame, text='    You can use the ‘Save settings’ button which saves your settings as a text ' +
    	'file. You can use the ‘Load settings’ button and find your text file', font='Helvetica 14')
    generalAnswerTwo.grid(column = 0, row = 6, sticky = W)
    # Question 3
    generalQuestionThree =  Label(frame, text='Why can’t I type in my settings?', font='Helvetica 14 italic')
    generalQuestionThree.grid(column = 0, row = 7, sticky = W)
    generalAnswerThree =  Label(frame, text='    You must import your csv first before you can touch the settings, as ' +
    	'that’ll help us show you what columns to pick and choose.', font='Helvetica 14')
    generalAnswerThree.grid(column = 0, row = 8, sticky = W)
    # Question 4
    generalQuestionFour =  Label(frame, text='What about a setting for _____?', font='Helvetica 14 italic')
    generalQuestionFour.grid(column = 0, row = 9, sticky = W)
    generalAnswerFour =  Label(frame, text='    This project was developed in under 10 weeks by six UC Santa Cruz ' +
    	'students; our team didn’t have enough time to completely implement our \n vision for the functionality ' +
    	'of our product, but the framework is there to build and improve the product.', font='Helvetica 14')
    generalAnswerFour.grid(column = 0, row = 10, sticky = W)
    # Question 5
    generalQuestionFive =  Label(frame, text='Does my csv file need to be in the same directory as the program or on' +
    ' the Desktop?', font='Helvetica 14 italic')
    generalQuestionFive.grid(column = 0, row = 11, sticky = W)
    generalAnswerFive =  Label(frame, text='    No, anywhere is fine.', font='Helvetica 14')
    generalAnswerFive.grid(column = 0, row = 12, sticky = W)
    # Question 6
    generalQuestionSix =  Label(frame, text='Can it read TSV or .xlsx files?', font='Helvetica 14 italic')
    generalQuestionSix.grid(column = 0, row = 13, sticky = W)
    generalAnswerSix =  Label(frame, text='    Sorry, we can’t read anything other than a csv file. However, ' +
    	'there are converters online for tsv and xlsx files.', font='Helvetica 14')
    generalAnswerSix.grid(column = 0, row = 14, sticky = W)

   
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

# add Setting, not used currently
def Add():
	print('add')

# after adding file, have the information optimized and printed out
def Optimize():
	if os.path.exists('temp_folder'):
		shutil.rmtree('temp_folder')
	# print(gui.lineups.get()) example on how to use global variable
	if settings.app.imported == True:
		print('optimize')
		gui.bot.grid(row=19)
		gui.bottom.pack()
		#scrollbar = Scrollbar(gui.bottom)
		#scrollbar.pack(side=RIGHT, fill=Y)
		# run the optomizer using Popen
		subprocess.Popen('python lineups.py').wait()
		import pandas as pd
		pandaInput = pd.read_csv("temp_folder/temp_output.csv")
		# display the results from the csv file using labels in tkinter. currently not optimized. Need to set up for non-windows devices
		# if an option is selected, display that first
		if gui.displayDropMenu.dropDownVar.get() != 'Select One' and gui.displayDropMenu.dropDownVar.get() != 'Select Status':
			displayColumn = pandaInput[gui.displayDropMenu.dropDownVar.get()]
			label = tk.Label(gui.bot, width = 20, height = 2, \
						text = gui.displayDropMenu.dropDownVar.get(), relief = tk.RIDGE)
			label.grid(row = 0, column = 0)
			x = 0
			while x < displayColumn.__len__():
				label = tk.Label(gui.bot, width = 20, height = 2, \
							text = displayColumn[x], relief = tk.RIDGE)
				x +=1
				label.grid(row = x, column = 0)
				
		# by default, display all columns with 'lineup_' in them
		playerColumns = [col for col in pandaInput.columns if 'lineup_' in col]
		x = 0
		y = 1
		for col in playerColumns:
			displayColumn = pandaInput[col]
			label = tk.Label(gui.bot, width = 10, height = 2, \
						  text = col, relief = tk.RIDGE)
			label.grid(row = 0, column = y)
			while x < displayColumn.__len__():
				label = tk.Label(gui.bot, width = 10, height = 2, \
						  text = displayColumn[x], relief = tk.RIDGE)
				x +=1
				label.grid(row = x, column = y)
			x = 0
			y +=1
	else:
		messagebox.showinfo('Note', 'You must import a file before optimizing a lineup!')
