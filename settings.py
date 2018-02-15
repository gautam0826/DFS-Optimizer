import sys
# For running Python 3.X
if sys.version_info >= (3,0):
	import tkinter as tk
	from tkinter import *
# For running Python 2.X
else:
	import Tkinter as tk
	from Tkinter import *
import os

def init():
	global app



class DFS():
	def __init__(self):
		self.root = tk.Tk()

		# For running Windows
		if os.name == 'nt':
			# Set root size to maximized screen size
			self.root.wm_state('zoomed')
		# For not running Windows
		else:
			# Set root size to maximized screen size
			m = self.root.maxsize()
			self.root.geometry('{}x{}+0+0'.format(*m))

		#Maximize Application to Screen
		self.w = self.root.winfo_screenwidth()
		self.h = self.root.winfo_screenheight()
		#self.root.geometry("%dx%d+0+0" % (self.w, self.h))

		self.version = "QuickPick v0.1"
		self.root.title(self.version)

		self.buttons = []
		self.settings = []

		# Cannot optimize or export until file is imported
		self.imported = False

		# Disable Resize
		#self.root.resizable(False, False)
		

app=DFS()