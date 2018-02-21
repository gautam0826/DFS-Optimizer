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

# arrays currently used for drop down menus
headerList = []
capHeaderList = []
budgetHeaderList = []
projectionsHeaderList = []

def init():
	global app


class DFS():
	def __init__(self):
		self.root = tk.Tk()

		# for running Windows
		if os.name == 'nt':
			# set root size to maximized screen size
			self.root.wm_state('zoomed')
		# for not running Windows
		else:
			# set root size to maximized screen size
			m = self.root.maxsize()
			self.root.geometry('{}x{}+0+0'.format(*m))

		# maximize Application to Screen
		self.w = self.root.winfo_screenwidth()
		self.h = self.root.winfo_screenheight()
		#self.root.geometry("%dx%d+0+0" % (self.w, self.h))

		self.version = "QuickPick v0.1"
		self.root.title(self.version)

		self.buttons = []
		self.settings = []

		# cannot optimize or export until file is imported
		self.imported = False

		# Disable Resize
		#self.root.resizable(False, False)
		

app=DFS()