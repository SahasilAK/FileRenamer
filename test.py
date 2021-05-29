from tkinter import Tk
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory()
print(current_directory)
file_name = "test.txt"
