import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import json
from tkinterdnd2 import DND_FILES, TkinterDnD

class StudentManagementSystem(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title('Student Management System')
        self.geometry('1350x700+0+0')
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        #self.menu_bar = MenuBar(parent=self)
        #self.config(menu=self.menu_bar)
        self.StudentDetailsFrame = StudentDetailsFrame(parent=self.main_frame)
        self.StudentDetailsFrame.pack(fill=tk.BOTH, expand=True)
class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label='Import Student Data', command=self.import_student_data)
        self.file_menu.add_command(label='Export Student Data', command=self.export_student_data)
        self.add_cascade(label='File', menu=self.file_menu)

class StudentDetailsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        style = ttk.Style(self)
        style.layout('arrowless.Vertical.TScrollbar', 
         [('Vertical.Scrollbar.trough',
           {'children': [('Vertical.Scrollbar.thumb', 
                          {'expand': '1', 'sticky': 'nswe'})],
            'sticky': 'ns'})])
        style.layout('arrowless.Horizontal.TScrollbar',
            [('Horizontal.Scrollbar.trough',
                {'children': [('Horizontal.Scrollbar.thumb',
                                 {'expand': '1', 'sticky': 'nswe'})],
                    'sticky': 'we'})])
        
        # set ttk theme to "clam" which support the fieldbackground option
        style.theme_use("clam")
        style.configure("Treeview", 
                        background="#040f20",
                        fieldbackground="#010409", 
                        foreground="white", 
                        bordercolor="#30363d",
                        font=('arial', 12), 
                        rowheight=30
                        )
        style.configure("Treeview.Heading", 
                        background="#040f20", 
                        fieldbackground="#010409", 
                        foreground="#d2a8ff",
                        font=('arial', 13, 'bold'), 
                        rowheight=30
                        )
        style.configure("Vertical.TScrollbar", 
                        background="#040f20", 
                        bordercolor="#0d1117", 
                        arrowcolor="darkgray",
                        )
        style.map("Vertical.TScrollbar",
                  background=[('active', 'black')],
                foreground=[('active', 'white')]
                    )
        style.map("Horizontal.TScrollbar",
                  background=[('active', 'black')],
                  foreground=[('active', 'white')]
                  )
        style.configure("Horizontal.TScrollbar", 
                        background="#040f20", 
                        bordercolor="#0d1117", 
                        arrowcolor="white"
                        )
        style.map("Treeview.Heading",
                  background=[('active', '#1d4a70')],
                  foreground=[('active', '#d2a8ff')]
                  ) 
        # style.map("Treeview",
        #           background=[('selected', 'blue')],
        #           foreground=[('selected', 'white')]
        #           )

        self.label = tk.Label(self, text='Student Details', font=('arial', 20, 'bold'), bg='#0d1117', fg='white')
        self.label.pack(side=tk.TOP, fill=tk.X)
        
        
        self.student_details = StudentDetails(parent=self)
        

        


class StudentDetails(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent)
        scroll_Y = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview,style='arrowless.Vertical.TScrollbar')

        scroll_X = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview,style='arrowless.Horizontal.TScrollbar')
        self.configure(yscrollcommand=scroll_Y.set, xscrollcommand=scroll_X.set)
        scroll_Y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_X.pack(side=tk.BOTTOM, fill=tk.X)
        self.stored_dataframe = pd.read_excel('./data/student_data.xlsx')
        self.tag_configure('oddrow', background='#0d1117')
        self.tag_configure('evenrow', background='#010409')
        self._draw_table()
        
    def _draw_table(self):
        self['columns'] = list(self.stored_dataframe.columns)
        self['show'] = 'headings'
        for column in self['columns']:
            self.heading(column, text=column)
            self.column(column, anchor=tk.CENTER)
        for i, row in enumerate(self.stored_dataframe.itertuples()):
            self.insert('', tk.END, values=row[1:],tags='oddrow' if i % 2 else 'evenrow')
        self.pack(fill=tk.BOTH, expand=True)
if __name__ == '__main__':
    root = StudentManagementSystem()
    root.mainloop()

