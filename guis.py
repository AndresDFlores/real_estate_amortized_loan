import tkinter as tk
from tkinter import filedialog as tkfd
from tkcalendar import Calendar
import datetime as dt

import os

class GUIs:


    def __init__(self):
        self.parent_directory = os.getcwd()


    #  files and directories

    def select_directory(self, title=''):
        tk.Tk().withdraw()
        return tkfd.askdirectory(initialdir=self.parent_directory, title=title)

    def open_file(self, title='', file_types=[('All Files', '*.*')]):
        tk.Tk().withdraw()
        return tkfd.askopenfilename(initialdir=self.parent_directory, title=title, filetypes=file_types)

    def save_file(self, title='', file_types=[('All Files', '*.*')]):
        tk.Tk().withdraw()
        return tkfd.asksaveasfilename(initialdir=self.parent_directory, title=title, filetypes=file_types)


    #  GUIs

    def calendar(self, birth_year=dt.datetime.today().year, box_title_text=''):

        root=tk.Tk()
        root.title(box_title_text)

        cal = Calendar(root, selectmode = 'day',
               year = birth_year, month = 1,
               day = 1)

        cal.pack(pady = 20)
 
        def submit_entries():
            self.selection = dt.datetime.strptime(cal.get_date(), '%m/%d/%y')
            root.destroy()
        
        tk.Button(root, text = "Get Date",
            command = submit_entries).pack(pady = 20)
        
        date = tk.Label(root, text = "")
        date.pack(pady = 20)
        
        root.mainloop()
        return self.selection

    
    def dialogue_box(self, fields=['field_1'], box_title_text=''):

        root=tk.Tk()
        root.title(box_title_text)


        def submit_entries():
            self.selection = {field:(entries[field].get()) for field in list(entries)}
            root.destroy()
            

        entries = dict()
        for idx, field in enumerate(fields):
            tk.Label(root, 
                    text=field,
                    width=20).grid(row=idx, column=0)

            entries[field]=tk.Entry(root)
            entries[field].grid(row=idx, column=1)

        tk.Button(
            root, 
            text='Submit', 
            width=10,
            command=submit_entries
            ).grid(
                row=idx+1, 
                column=1, 
                sticky=tk.W, 
                pady=4)

        tk.mainloop()
        return self.selection


    def radio_button_selection(self, fields=['field_1'], box_title_text='', prompt_text=''):

        root=tk.Tk()
        root.title(box_title_text)

        v = tk.IntVar()

        def submit_entries():
            self.selection = v.get()
            root.destroy()

        tk.Label(root, 
                text=prompt_text,
                justify = tk.LEFT,
                padx = 20).pack()

        for field, val in fields:
            tk.Radiobutton(
                root, 
                text = field, 
                variable = v,
                value = val, 
                indicatoron = 0,
                width = 20,
                padx = 20, 
                command=submit_entries
                ).pack(anchor=tk.W, ipadx=20, ipady = 5)

        root.mainloop()
        return self.selection


if __name__=='__main__':
    guis_class=GUIs()