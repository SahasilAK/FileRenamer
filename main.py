import os
import tkinter

def renamer(f_path,new_name):

    n = 1
    for file in os.listdir(f_path):
        ext = file.split('.')[1]
        old = f'{f_path}\{file}'
        new = f'{f_path}\{new_name} {n}.{ext}'
        os.rename(old,new)
        n+=1








path = input()
name = input()

x = renamer(path,name)




# D:/Work/Codes/Projects/FileRenamer/data
