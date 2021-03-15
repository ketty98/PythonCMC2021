from tkinter import Tk, Button






class Game(Tk):
    def __init__(self):
        super().__init__()


        self.button_exit = Button(self, text = 'EXIT', command = self.quit)
        self.button_new = Button(self, text='NEW')

        self.button_new.grid(column = 1, row = 0)
        self.button_exit.grid(column = 2, row = 0)

        self.massivButtons = []
        for i in range (1,16):
            def number_button(number = i):
                self.move_button(number)
            self.massivButtons.append(Button(self, text = i, command = number_button))
            self.massivButtons[i-1].grid(row = i // 4 + 1, column = i % 4, sticky = 'WSNE')
        for i in range(5):
            weightcolumn = 1
            weightrow = 1
            if i == 0 :
                weightrow = 0
            if i != 4:
                self.columnconfigure(i, weight = weightcolumn)
            self.rowconfigure(i, weight = weightrow)
        self.empty_row = 1
        self.empty_column = 0

    def move_button(self, i):
        this_button = self.massivButtons[i-1]
        position = this_button.grid_info()
        column = position['column']
        row = position['row']
        if abs(self.empty_column - column) + abs(self.empty_row - row) == 1:
            print(column, row)
            this_button.grid(row = self.empty_row, column = self.empty_column)
            self.empty_row = row
            self.empty_column = column

game = Game()
game.mainloop()