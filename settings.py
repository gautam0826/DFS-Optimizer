# Global file for dealing with adding the GUI and having it all connect.
# Not dependant on other files, all other files depend on settings.py.

import sys
# for running Python 3.X
if sys.version_info >= (3,0):
	import tkinter as tk
	from tkinter import *
# for running Python 2.X
else:
	import Tkinter as tk
	from Tkinter import *
import os

fileName = ''

# ====================
# Variables
# ====================
# arrays currently used for drop down menus
headerList = []
capHeaderList = []
budgetHeaderList = []
projectionsHeaderList = []
presetConfigList = []

def init():
	global app

# Main DFS class used to build GUI
class DFS():
	def __init__(self):
		self.root = tk.Tk()

		# maximize Application to Screen
		self.w = self.root.winfo_screenwidth() // 1.5
		self.h = self.root.winfo_screenheight()
		#self.root.geometry("%dx%d+0+0" % (self.w, self.h))

		# for running Windows
		if os.name != 'nt':
			# set root size to maximized screen size
			m = self.root.maxsize()
			self.root.geometry('{}x{}+0+0'.format(*m))
		
		self.version = "QuickPick"
		self.root.title(self.version)

		self.root.iconbitmap(r'qp32.ico')

		self.buttons = []
		self.settings = []

		# cannot optimize or export until file is imported
		self.imported = False

		# Disable Resize
		self.root.resizable(False, False)
		
# Run DFS and build GUI
app=DFS()
