import tkinter as tk
from tkinter import *

def init():
	global app

class DFS():
	def __init__(self):
		self.root = tk.Tk()
		self.root.wm_state('zoomed')

		#Maximize Application to Screen
		self.w = self.root.winfo_screenwidth()
		self.h = self.root.winfo_screenheight()
		#self.root.geometry("%dx%d+0+0" % (self.w, self.h))

		self.version = "QuickPick v0.1"
		self.root.title(self.version)

		self.buttons = []
		self.settings = []
		self.imported = False

		# Disable Resize
		#self.root.resizable(False, False)
app=DFS()