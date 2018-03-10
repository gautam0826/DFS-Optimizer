import sys
# For running Python 3.X
if sys.version_info >= (3,0):
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    from tkinter.filedialog import askopenfilename
# For running Python 2.X
else:
    import Tkinter as tk
    from Tkinter import *
    import tkMessageBox
    from tkFileDialog import askopenfilename
import settings
import os
import csv
from menu import *

# Starting variables for fixed settings
#lineups, players, maxCost = 0, 0, 0
lineups = StringVar()
players = StringVar()
maxCost = StringVar()
numPos = StringVar()
lineups.set('0')
players.set('0')
maxCost.set('0')
numPos.set('0')

#===========

def loadPresetConfig():
    fileName = ("presets/" + presetDropMenu.dropDownVar.get())
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
                lineups.set(line[1])    # Variable 1
            elif line[0] is '2':
                players.set(line[1])    # Variable 2
            elif line[0] is '3':
                projections_column = line[1]
            elif line[0] is '4':
                maxCost.set(line[1])    # Variable 4
            elif line[0] is '5':
                budget_column = line[1]
            elif line[0] is '6':
                input_csv_location = line[1]
            elif line[0] is '7':
                numPos.set(line[1])        # Variable 7

def makeConfigFile():
        csv_location = 'n/a'
        # needed to read if no file in the first place
        with open('configurations.txt', 'a') as f:
                f.write("9 writesomething\n")
        # check if there is a file location already, takes the last one
        with open('configurations.txt', 'r') as config:
                content = config.readlines()
        config.close()
        content = [line.strip() for line in content]
	   # splits each input line into 1) an identifying number 2) variable
        for line in content:
                line = line.split(' ', 1)
                if line[0] is '6':
                        csv_location = line[1]
        # rewrite a new config file
        with open('configurations.txt', 'w') as configurations:
                configurations.write('1 ' + str(lineups.get()) + '\n')
                configurations.write('2 ' + str(players.get()) + '\n')
                configurations.write('3 ' + str(projectionsDropMenu.dropDownVar.get()) + '\n')
                configurations.write('4 ' + str(maxCost.get()) + '\n')
                configurations.write('5 ' + str(budgetDropMenu.dropDownVar.get()) + '\n')
                configurations.write('6 ' + csv_location + '\n')
                configurations.write('7 ' + str(maxCat.get()) + ' ' + str(capDropDown.dropDownVar.get()) + '\n')


# saves variable when enter is pressed
# only accepts numerical values for input
def enterPressed(event,variable):
        try:
            float(event.get())
            variable.set(event.get())
            #makeConfigFile()
        except ValueError:
            messagebox.showinfo('Error', 'Inputs must be a number!')

# class to create drop down menus 
# Usage: [name] = CreateDropMenu(root(in this case top), 
# default Display of menu, options to be listed(separated by commas))
class CreateDropMenu(OptionMenu):
    def __init__(self, master, startingDisplay, *dropDownList):
        self.dropDownVar = StringVar(master)
        self.dropDownVar.set(startingDisplay)
        OptionMenu.__init__(self, master, self.dropDownVar, *dropDownList)
        self.config(width= 20)
        self.config(background = 'SteelBlue1')

#=============
#    Menu
#=============
menu = Menu(settings.app.root)
settings.app.root.config(menu=menu, background='snow4')

#=============
#    FILE
#=============
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save Settings", command=Save)
filemenu.add_command(label="Load Settings", command=Load)
filemenu.add_command(label="Options", command=Options)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=settings.app.root.destroy)

#=============
#    CSV
#=============
csvmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="CSV", menu=csvmenu)
csvmenu.add_command(label="Import", command=Import)
csvmenu.add_command(label="Export", command=Export)

#=============
#    HELP
#=============
helpmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="GitHub", command=GitHub)
helpmenu.add_command(label="About", command=About)

frame = Frame(settings.app.root, width=settings.app.w, height=settings.app.h, background='white')
frame.pack(fill=BOTH)
frame.pack_propagate(False) # Stop frame from resizing to widgets

#=============
# Top Frame
#=============
top = Frame(frame, width=settings.app.w, height=settings.app.h/2.2, background='white')
top.grid(row=0)
top.grid_propagate(False) # Stop frame from resizing to widgets
top.configure(background = '#212121') # controls back ground for top window---------------------------------------------------------------

for i in range(0,17):
    top.grid_rowconfigure(i, weight=1)
for j in range(0,49):
    top.grid_columnconfigure(j, weight=1)

#================
# Drop Down List
#================
# Display drop down
displayLabel = Label(top, text='Display Column : ', bg="#212121", fg='#FFFFFF')
displayLabel.grid(row = 11, column = 0, sticky = W)
displayDropMenu = CreateDropMenu(top, 'Select Status', settings.headerList) #list of headers from imported file
displayDropMenu.grid(row = 11, column = 1, sticky = W)
#selectedDisplay = displayDropMenu.dropDownVar.get() #gets selected
#chosenIndex = displayDropMenu.dropDownVar.trace('w',selectedOption(displayDropMenu,settings.headerList))


# budget drop down
budgetLabel = Label(top, text='Budget Column: ', bg="#212121", fg='#FFFFFF')
budgetLabel.grid(row = 12, column = 0, sticky = W)
budgetDropMenu = CreateDropMenu(top, 'Select Status',settings.budgetHeaderList)
budgetDropMenu.grid(row = 12, column = 1, sticky = W)
# projections drop down
projectionsLabel = Label(top, text='Projections Column: ', bg="#212121", fg='#FFFFFF')
projectionsLabel.grid(row = 13, column = 0,sticky = W)
projectionsDropMenu = CreateDropMenu(top, 'Select Status',settings.projectionsHeaderList)
projectionsDropMenu.grid(row = 13, column = 1, sticky = W)
# setting 4 drop down
capDropDown = CreateDropMenu(top, 'Select Status', settings.capHeaderList) #list of headers from imported file
capDropDown.grid(row = 6, column = 4, rowspan=3, columnspan=3, sticky=N)   

# =============
# Top Widgets
# =============
saveSetting = Button(top, text=' Save Settings ', command=Save, background="SteelBlue1")
saveSetting.grid(row=0, column=16, sticky=E)
loadSetting = Button(top, text=' Load Settings ', command=Load, background="SteelBlue1")
loadSetting.grid(row=0, column=17,columnspan=2, sticky=W)
# addSetting = Button(top, text='Add Setting', command=Add)
# addSetting.grid(row=0, column=21)

importBtn = Button(top, text='  Import CSV   ', command=Import, background="SteelBlue1")
importBtn.grid(row=0, column=19, columnspan=2, sticky=E)
exportBtn = Button(top, text='   Export CSV   ', command=Export, background="SteelBlue1")
exportBtn.grid(row=0, column=21, sticky=W)

optimizeBtn = Button(top, text='Optimize', font=('Times New Roman',15, 'bold'),
     height=2, width=25, command=Optimize, background='SteelBlue1')
optimizeBtn.grid(row=12, rowspan=4, column=16, columnspan=5)

# number of lineup setting
setting1 = Label(top, text='Number of Lineups:', bg="#212121", fg='#FFFFFF')
setting1.grid(row=3, sticky=W)
settingLineupsNum = Label(top,textvariable=lineups, bg="#212121", fg='#FFFFFF')
settingLineupsNum.grid(row=3,column = 1, sticky=W)

# user input for lineup setting
lineupNumInput = Entry(top)
lineupNumInput.grid(row=3, column=2, sticky=W)
lineupNumInput.bind('<Return>',(lambda event: enterPressed(lineupNumInput,lineups)))

# number of player setting
setting2 = Label(top, text='Number of Players: ', bg="#212121", fg='#FFFFFF')
setting2.grid(row=4, sticky=W)
displayPlayersNum = Label(top,textvariable=players, bg="#212121", fg='#FFFFFF')
displayPlayersNum.grid(row=4,column = 1, sticky=W)

# user input max player setting
playerNumInput = Entry(top)
playerNumInput.grid(row=4, column=2,sticky=W)
playerNumInput.bind('<Return>',(lambda event: enterPressed(playerNumInput,players)))

# max spending cost setting
setting3 = Label(top, text='Max Cost: ', bg="#212121", fg='#FFFFFF')
setting3.grid(row=5, sticky=W)
displayCostNum = Label(top,textvariable=maxCost, bg="#212121", fg='#FFFFFF')
displayCostNum.grid(row=5,column = 1, sticky=W)

# user input for max spending cost setting
costNumInput = Entry(top)
costNumInput.grid(row=5, column=2,sticky=W)
costNumInput.bind('<Return>',(lambda event: enterPressed(costNumInput,maxCost)))

# max for specified category setting
setting4 = Label(top, text='Max for specified category: ', bg="#212121", fg='#FFFFFF')
setting4.grid(row = 6, sticky = W)
setting4MaxNum = Label(top, text = '>', bg="#212121", fg='#FFFFFF')
setting4MaxNum.grid(row = 6, column = 3, sticky = W)

# for test purposes can delete later
displayPosAmount = Label(top, textvariable = numPos, bg="#212121", fg='#FFFFFF')
displayPosAmount.grid(row = 6, column = 1, sticky = W)

# user input for max specified category
maxCat = Entry(top)
maxCat.grid(row = 6, column = 2, sticky = W)
maxCat.bind('<Return>',(lambda event: enterPressed(maxCat, numPos)))

#manually create a config.txt file
createConfig = Button(top, text='     Stage Changes     ', command=makeConfigFile)
createConfig.config(background="SteelBlue1")
createConfig.grid(row=10,column=17, columnspan=1, rowspan=3, sticky=W)

#Load Preset configuration from drop down menu
presetLabel = Label(top, text='Setting Presets: ',bg="#212121", fg='#FFFFFF')
presetLabel.grid(row = 0,column = 0, sticky = W)
presetDropMenu = CreateDropMenu(top, 'Select Status',settings.presetConfigList)
presetDropMenu.grid(row = 0, column = 1, sticky = W)
for file in [txt for txt in os.listdir("presets")
if txt.endswith(".txt")]:
    presetDropMenu.children['menu'].add_command(label=file,command=lambda heading=file: presetDropMenu.dropDownVar.set(heading))
loadPreset = Button(top, text='Load Presets', command=loadPresetConfig, background="SteelBlue1")
loadPreset.grid(row=0, column=2, sticky = E)

#=============
# Split Frame
#=============
# Solid line that separates top from bottom frames
split = Frame(frame, width=settings.app.w, height=1, background='black')
split.grid(row=18)

#=============
# Bot Frame
#=============
# Used to show the data after optimization
bot = Frame(frame, width=settings.app.w, height=settings.app.h/2.5, background='white')
bot.grid_propagate(False) # Stop frame from resizing to widgets
for i in range(19,36):
    bot.grid_rowconfigure(i, weight=1)

bottom = Frame(bot, width=settings.app.w, height=settings.app.h/2.5, background='white')
bottom.pack_propagate(False)

# addition of scollbar
# scrollbar = Scrollbar(bottom)
# scrollbar.pack(side=RIGHT, fill=Y)

settings.app.root.mainloop()

# writing to text file    
##-------------------------------------------------------------------------

