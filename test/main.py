import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from menu import *

class DFS():
	def __init__(self):
		self.root = tk.Tk()
app=DFS()
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

button = tk.Button(topFrame, text="Add Setting", command=AddSetting, width=15, height=2)
button.pack()

setting0 = tk.Label(topFrame, text='Setting 0')
setting0.pack()
setting1 = tk.Label(topFrame, text='Setting 1')
setting1.pack()
setting2 = tk.Label(topFrame, text='Setting 2')
setting2.pack()

#=============
# Bot Frame
#=============

frameSep = tk.Frame(app.root, width=1400, height=1, background='#000')
frameSep.pack()

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
