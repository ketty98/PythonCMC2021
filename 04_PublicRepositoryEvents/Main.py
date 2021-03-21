import tkinter as tk
from tkinter import font

WIDTH = 7

class InputLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self['font'] = 'fixed'
        self.bind('<Button>', self.react_click)
        self.bind('<Key>', self.reaction)
        self.cursor = tk.Frame(self, width=1, height=10, background="black")
        self.bind('<FocusIn>', self.foc_in)
        self.bind('<FocusOut>', self.foc_out)

    def react_click(self, event):
        print(self.winfo_width() / len(self['text']))
        self.focus_set()
        place = round(event.x/ WIDTH)* WIDTH + 5
        #print("cursor", place)
        self.cursor.place(x=place , y=5)

    def reaction(self, event):
        print(self.cursor.winfo_x())
        pos = (self.cursor.winfo_x()-5)//WIDTH -1
        if event.keysym == 'BackSpace' and pos >= 0:
            print(pos)
            if pos == 0:
                self['text'] = self['text'][1:]
            else:
                self['text'] = self['text'][0:pos]  +  self['text'][pos+1:]
            self.cursor.place(x = WIDTH *(pos) + 5, y = 5)
        elif event.keysym == 'Left' and pos >= 0:
            self.cursor.place(x=WIDTH * (pos) +5, y=5)
        elif event.keysym == 'Right' and pos <= len(self['text'])-2:
            self.cursor.place(x=WIDTH * (pos+2)+5, y=5)
        elif event.keysym == 'Home':
            self.cursor.place(x=5, y=5)
        elif event.keysym == 'End':
            self.cursor.place(x=len(self['text'])*WIDTH + 5, y=5)
        elif event.char and event.char.isprintable():
            self['text'] = self['text'][0:pos+1] + event.char +self['text'][pos + 1:]
            self.cursor.place(x=WIDTH * (pos + 2)+5, y=5)

    def foc_in(self, event):
        self['relief'] = 'sunken'

    def foc_out(self, event):
        self['relief'] = 'flat'





my_frame = tk.Frame()
my_frame.grid()
my_label = InputLabel(my_frame, text='fsdhughrughuff', font = 'TkFixedFont')
my_label.grid(column=0, row=0)

exit_b = tk.Button(my_frame.master, text='Quit', command=my_frame.quit)
exit_b.grid(column=0, row=1, sticky='E')
my_frame.master.mainloop()
