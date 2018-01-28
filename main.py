import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from menu import *

class DFS():
	def __init__(self):
		self.root = tk.Tk()
		self.version = "QuickPick v0.1"
		self.root.title(self.version)
		
		self.buttons = []
		self.settings = []
app=DFS()

def setting(id, text):
	b = tk.Button(setFrame, text='X', height=1, width=2, command=remove(id))
	app.buttons.append(b)
	app.buttons[id].grid(row=0)
	#app.buttons[id].pack(side=LEFT)
	s = tk.Label(setFrame, text=text)
	app.settings.append(s)
	app.settings[id].grid(row=0)
	#app.settings[id].pack(side=LEFT)


def remove(id):
	print(id)

#=============
#    Menu
#=============
menu = Menu(app.root)
app.root.config(menu=menu)

#=============
#    FILE
#=============
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save Settings", command=Save)
filemenu.add_command(label="Load Settings", command=Load)
filemenu.add_command(label="Options", command=Options)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=app.root.destroy)

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

#=============
# Top Frame
#=============

def AddSetting():
	print("Add Setting")

topFrame = tk.Frame(app.root, width=1400, height=350)
topFrame.pack()
topFrame.pack_propagate(False) # Stop frame from resizing to widgets

# Save Settings Button
saveSetting = tk.Button(topFrame, text='Save Settings', command=Save, width=15, height=2)
saveSetting.pack(side=LEFT)

# Load Settings Button
loadSetting = tk.Button(topFrame, text='Load Settings', command=Load, width=15, height=2)
loadSetting.pack(side=LEFT)

# Add Settings Button
addSetting = tk.Button(topFrame, text="Add Setting", command=AddSetting, width=15, height=2)
addSetting.pack(side=LEFT)

# Settings Frame
# Contains all of the settings into 1 frame to easily format
setFrame = tk.Frame(topFrame, width=1400, height=250)
setFrame.grid(row=0, rowspan=5)

setting(0, 'Setting 0')
setting(1, 'Setting 1')

#=============
# Bot Frame
#=============

sepFrame = tk.Frame(app.root, width=1400, height=1, background='#000')
sepFrame.pack()

botFrame = tk.Frame(app.root, width=1400, height=400)
botFrame.pack()
botFrame.pack_propagate(False)

botLabel = tk.Label(botFrame, text='Bottom')
botLabel.pack()

#=============
# Scrollbar
#=============
scrollbar = tk.Scrollbar(botFrame)
scrollbar.pack(side=RIGHT, fill=Y)

app.root.mainloop()