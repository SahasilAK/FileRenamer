import os
from tkinter import *
from tkinter import filedialog, messagebox

BACKGROUND_COLOR ="#3282b8"
TITLE_FONT_COLOR ="#f5f5f5"
BUTTON_COLOR_BG ="#111f4d"
BUTTON_COLOR_FG ="#f2f4f7"
TEXT_BOX_COLOR_BG = "#e4f9f5"
TEXT_BOX_COLOR_FG = "#222831"
FONT = ("Courier", 12, "normal")


def renamer():
    current_directory = filedialog.askdirectory()
    new_name = input_list.get(1.0,"end").strip()
    
    n = 1
    m = 0
    for file in os.listdir(current_directory):
        ext = file[::-1].split('.')[0][::-1]
        old = f'{current_directory}\{file}'
        new = f'{current_directory}\{new_name} {n}.{ext}'
        os.rename(old,new)
        n+=1
        m+=1

    messagebox.showinfo(title='Completed',message=f'Renamed {m} files')



def about():
    messagebox.showinfo(title = "About", message = 'Instruction:\nEg: old_name = ep 1.mp4 input = Episode\nOutput will be Episode 1.mp4,Episode 2.mp4,..etc \n<------------------------------------------------------------->\nV1.0\nCreated by Sahasil\ngithub.com/SahasilAK')

window = Tk()

window.config(padx=50,pady=40,bg=BACKGROUND_COLOR)
window.title("FileRenamer")

label_1 = Label(text='Input the new file name')
label_1.config(pady=5,fg=TITLE_FONT_COLOR,bg=BACKGROUND_COLOR,font=FONT)
label_1.grid(row=1,column=2,columnspan=4)



input_list = Text(height=1,width=50)
input_list.config(fg = TEXT_BOX_COLOR_FG, bg = TEXT_BOX_COLOR_BG, borderwidth=0)
input_list.focus()
input_list.grid(row = 4,column = 2, columnspan = 4,pady = 5)

about_button = Button(text='About', command = about)
about_button.config(highlightthickness = 0, fg = BUTTON_COLOR_FG, bg= BUTTON_COLOR_BG, font = FONT, borderwidth=0)
about_button.grid(row = 0,column = 6, columnspan = 2,pady = 5)

rename_button = Button(text='Rename', command=renamer)
rename_button.config(fg = BUTTON_COLOR_FG, bg= BUTTON_COLOR_BG,font = FONT, highlightthickness = 0, borderwidth=0)
rename_button.grid(row = 6,column = 3, columnspan = 2,pady = 5)



window.mainloop()
