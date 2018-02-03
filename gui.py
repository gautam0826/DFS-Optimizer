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
from menu import *

#===========
def enterPressed(event,var):
	# with open('configurations.txt', 'a') as configurations:
	# 	configurations.write('1 ' + str(event.get()+ '\n'))
	# var = event.get()
	if event == 'lineupNumInput':
		settings.app.lineups = var
		#setting1.grid(row=1, columnspan=10, sticky=W)
	elif event == 'playerNumInput':
		settings.app.players = var
		#setting2.grid(row=2, columnspan=10, sticky=W)
	elif event == 'maxCostNumInput':
		settings.app.maxCost = var
		#setting3.grid(row=3, columnspan=10, sticky=W)
	else:
		print('Undefined enterPressed variable: ' + repr(var) + '\n')
		print(event)
	
	#configurations.write('2 ' + str(playerNumEntry))
	#print(event.widget.get())
	#return (event.widget.get())
	#var = event.get()


#=========

#=============
#    Menu
#=============
menu = Menu(settings.app.root)
settings.app.root.config(menu=menu)

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
for i in range(0,17):
	top.grid_rowconfigure(i, weight=1)
for j in range(0,49):
	top.grid_columnconfigure(j, weight=1)

#================
# Top Widgets
#================
saveSetting = Button(top, text='Save Settings', command=Save)
saveSetting.grid(row=0, column=19)
loadSetting = Button(top, text='Load Settings', command=Load)
loadSetting.grid(row=0, column=20)
addSetting = Button(top, text='Add Setting', command=Add)
addSetting.grid(row=0, column=21)

importBtn = Button(top, text='Import CSV', command=Import)
importBtn.grid(row=16, column=0)
exportBtn = Button(top, text='Export CSV', command=Export)
exportBtn.grid(row=16, column=1)

optimizeBtn = Button(top, text='Optimize', height=2, width=20, command=Optimize)
optimizeBtn.grid(row=15, rowspan=2, column=19, columnspan=3)

# SETTING 1
text1 = 'Number of Lineups: ' + repr(settings.app.lineups)
setting1 = Label(top, text=text1)
setting1.grid(row=1, columnspan=10, sticky=W)
##user input
lineupNumInput = Entry(top, textvariable=settings.app.lineups)
lineupNumInput.grid(row=1, column=2, sticky=W)
lineupNumInput.bind('<Return>',(lambda event: enterPressed('lineupNumInput',settings.app.lineups))) 

# SETTING 2
text2 = 'Number of Players: ' + repr(settings.app.players)
setting2 = Label(top, text=text2)
setting2.grid(row=2, columnspan=10, sticky=W)
##user input
playerNumInput = Entry(top, textvariable=settings.app.players)
playerNumInput.grid(row=2, column=2,sticky=W)
playerNumInput.bind('<Return>',(lambda event: enterPressed('playerNumInput',settings.app.players)))
#playerNumInput.get() ##function to retrieve number of players

# SETTING 3
text3 = 'Max Cost: ' + repr(settings.app.maxCost)
setting3 = Label(top, text=text3)
setting3.grid(row=3, columnspan=10, sticky=W)

#================
# Drop Down List
#================
f = open("test.txt","r") #change name of text file
lst = f.readline().split()
f.close()
var = tk.StringVar() 
drop = tk.OptionMenu(top ,var,*lst)
drop.config(width= 20)
drop.grid()

#=============
# Split Frame
#=============
split = Frame(frame, width=settings.app.w, height=1, background='black')
split.grid(row=18)

#=============
# Bot Frame
#=============
bot = Frame(frame, width=settings.app.w, height=settings.app.h/2, background='white')
bot.grid(row=19)
bot.grid_propagate(False) # Stop frame from resizing to widgets
for i in range(19,36):
	bot.grid_rowconfigure(i, weight=1)

bottom = Frame(bot, width=settings.app.w, height=settings.app.h/2, background='white')
bottom.pack()
bottom.pack_propagate(False)

scrollbar = Scrollbar(bottom)
scrollbar.pack(side=RIGHT, fill=Y)

settings.app.root.mainloop()

##writing to text file
##-------------------------------------------------------------------------

