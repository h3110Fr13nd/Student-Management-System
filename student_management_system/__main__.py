from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import json
from tkinterdnd2 import DND_FILES, TkinterDnD

class StudentManagementSystem(TkinterDnD):

    def __init__(self):
        super().__init__()
        self.data='data/data.json'
        self.title('Student Management System')
        self.geometry('1350x700+0+0')
        self.configure(bg='black')
        lbl=Label(self.root, text='Student Management System', font=('arial', 40, 'bold'), bg='black', fg='powder blue')
        lbl.place(x=0, y=0, relwidth=1)
        self.root.mainloop()

if __name__ == '__main__':
    StudentManagementSystem()
