import tkinter as tk


class Oval:
    def __init__(self, c_id: int, coords: list, b_width: int, b_color: str, f_color: str):
        self.c_id = c_id
        self.coords = coords
        self.b_width = b_width
        self.b_color = b_color
        self.f_color = f_color

    @classmethod
    def build_from_str(cls, line):
        elems = line.split(';')
        if len(elems) == 5:
            c_id = int(elems[0])
            coords = list(map(int, elems[1].split(' ')))
            if len(coords) != 4:
                return None
            b_width = int(elems[2])
            b_color = elems[3]
            f_color = elems[4]
            return Oval(c_id, coords, b_width, b_color, f_color)

    def __str__(self):
        return f'{self.c_id};{" ".join(map(str, self.coords))};{self.b_width};{self.b_color};{self.f_color}\n'


class Drawer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ovals_l = []
        self.crate_text_editor()
        self.create_graph_editor()

        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def crate_text_editor(self):
        self.text_f = tk.Frame(self)
        self.text_f.grid(column=0, row=0)

        self.text_f.update_b = tk.Button(self.text_f, text='Update', command=self.update_draw)
        self.text_f.update_b.grid(column=0, row=0, sticky='NE')

        self.text_f_text = tk.Text(self.text_f)
        self.text_f_text.grid(column=0, row=1)
        self.text_f_text.tag_config('wrong', background="red")

    def update_draw(self):
        text = self.text_f_text.get(1.0, tk.END)
        length = 0
        for number, line in enumerate(text.split('\n'), start=1):
            if line:
                try:
                    oval = Oval.build_from_str(line)
                    if oval:
                        self.graph_f_graph.coords(oval.c_id, *oval.coords)
                        self.graph_f_graph.itemconfigure(oval.c_id, width=oval.b_width, outline=oval.b_color,
                                                         fill=oval.f_color)
                        self.text_f_text.tag_remove('wrong', f'{number}.0', f'{number}.end+1c')
                    else:
                        raise Exception
                except Exception as e:
                    self.text_f_text.tag_add('wrong', f'{number}.0', f'{number}.end+1c')
            length += len(line)

    def create_graph_editor(self):
        self.graph_f = tk.Frame(self)
        self.graph_f.grid(column=1, row=0)
        self.start_coord = None

        self.graph_f_graph = tk.Canvas(self.graph_f)
        self.graph_f_graph.bind('<ButtonPress-1>', self.on_press)
        self.graph_f_graph.bind('<B1-Motion>', self.on_motion)
        self.graph_f_graph.bind('<ButtonRelease-1>', self.on_release)
        self.graph_f_graph.grid(column=0, row=0)

    def on_press(self, event):
        self.over = self.graph_f_graph.find_overlapping(event.x, event.y, event.x, event.y)
        self.pos = event.x, event.y
        if not self.over:
            self.last_id = self.graph_f_graph.create_oval(event.x, event.y, event.x, event.y,
                                                          width=5, outline='green', fill='grey')
            self.ovals_l.append(Oval(self.last_id, [event.x, event.y, event.x, event.y],
                                     5, 'green', 'grey'))

    def on_motion(self, event):
        if self.over:
            for candidate in self.ovals_l:
                if candidate.c_id == self.over[-1]:
                    self.last_oval = candidate
                    shift = event.x - self.pos[0], event.y - self.pos[1]
                    self.last_oval.coords[0] += shift[0]
                    self.last_oval.coords[1] += shift[1]
                    self.last_oval.coords[2] += shift[0]
                    self.last_oval.coords[3] += shift[1]
                    self.pos = event.x, event.y
                    break
        else:
            self.last_oval = self.ovals_l[-1]
            self.last_oval.coords[2] = event.x
            self.last_oval.coords[3] = event.y
        self.graph_f_graph.coords(self.last_oval.c_id, *self.last_oval.coords)

    def on_release(self, event):
        if not self.over:
            self.text_f_text.insert(tk.END, str(self.last_oval))
        else:
            text = self.text_f_text.get(1.0, tk.END)
            self.text_f_text.delete(1.0, tk.END)
            for number, line in enumerate(text.split('\n')):
                if line:
                    if f'{self.over[-1]};' == line[:len(f'{self.over[-1]};')]:
                        self.text_f_text.insert(tk.END, str(self.last_oval))
                    else:
                        self.text_f_text.insert(tk.END, line + '\n')


app = Drawer()
app.mainloop()
