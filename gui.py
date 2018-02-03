import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import settings
from menu import *
#===========
def enterPressed(event,var):
	with open('configurations.txt', 'a') as configurations:
		configurations.write('1 ' + str(event.get()+ '\n'))
	var = event.get()
	#configurations.write('2 ' + str(playerNumEntry))
	#print(event.widget.get())
	#return (event.widget.get())
	#var = event.get()


#=========
# Starting variables for fixed settings

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

frame = Frame(settings.app.root, width=settings.app.w, height=settings.app.h, background='red')
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

# Top Widgets
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

text1 = 'Number of Lineups: ' + repr(lineups)
setting1 = Label(top, text=text1)
setting1.grid(row=1, columnspan=10, sticky=W)
##user input
lineupNumInput = Entry(top)
lineupNumInput.grid(row=1, column=2, sticky=W) 
lineupNumInput.bind('<Return>',(lambda event: enterPressed(lineupNumInput,lineups)))

text2 = 'Number of Players: ' + repr(players)
setting2 = Label(top, text=text2)
setting2.grid(row=2, columnspan=10, sticky=W)
##user input
playerNumInput = Entry(top)
playerNumInput.grid(row=2, column=2,sticky=W)
playerNumInput.bind('<Return>',(lambda event: enterPressed(playerNumInput)))
#playerNumEntry =''
#playerNumInput.bind('<Return>', enterPressed(playerNumInput, playerNumEntry ))
#playerNumInput.pack()
#playerNumInput.focus_set()
#playerNumInput.bind('<Return>',(lambda event: enterPressed(playerNumInput,playerNumEntry)))

#enterPressed(entered, var)
#playerNumEntry = playerNumInput.get() ##function to retrieve number of players

text3 = 'Max Cost: ' + repr(maxCost)
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

=======
bottom = Frame(bot, width=settings.app.w, height=settings.app.h/2, background='white')
bottom.pack()
bottom.pack_propagate(False)

scrollbar = Scrollbar(bottom)
scrollbar.pack(side=RIGHT, fill=Y)

settings.app.root.mainloop()

##writing to text file
##-------------------------------------------------------------------------
#f = open('configurations.txt','w')
#with open('configurations.txt', 'w') as configurations:
	#configurations.write('1 ' + str(lineupNumEntry))
	#configurations.write('2 ' + str(playerNumEntry))
#f.write('3 ' + projections_column)
#f.write('4 ' + str(budget))
#f.write('5 ' + budget_column)
#f.write('6 ' + input_csv_location)
#f.close()


settings.app.root.mainloop()

