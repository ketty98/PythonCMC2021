from tkinter import Tk, Button
from random import choice, randint


class Game(Tk):
    def __init__(self):
        super().__init__()

        self.button_exit = Button(self, text = 'EXIT', command = self.quit)
        self.button_new = Button(self, text='NEW', command = self.shake)
        self.button_new.grid(column = 1, row = 0)
        self.button_exit.grid(column = 2, row = 0)

        self.massivButtons = []
        for i in range (1,16):
            def number_button(number = i):
                self.move_button(number, True)
            self.massivButtons.append(Button(self, text = i, command = number_button))
            self.massivButtons[i-1].grid(row = (i-1) // 4 + 1, column = (i-1) % 4 , sticky = 'WSNE')
        for i in range(5):
            weightcolumn = 1
            weightrow = 1
            if i == 0 :
                weightrow = 0
            if i != 4:
                self.columnconfigure(i, weight = weightcolumn)
            self.rowconfigure(i, weight = weightrow)
        self.empty_row = 4
        self.empty_column = 3

    def move_button(self, i, flag):
        this_button = self.massivButtons[i-1]
        position = this_button.grid_info()
        column = position['column']
        row = position['row']
        if abs(self.empty_column - column) + abs(self.empty_row - row) == 1:
            this_button.grid(row = self.empty_row, column = self.empty_column)
            self.empty_row = row
            self.empty_column = column
        if flag and self.check():
            newWindow = Tk()
            newWindow.mainloop()
            newWindow.Button(text='EXIT', command=self.quit)

    def shake(self):
        for i in range(1000):
            self.move_button(randint(1,15), False)

    def check(self):
        cool = True
        for i in range(1,16):
            row = (i - 1) // 4 + 1
            column = (i - 1) % 4
            this_button = self.massivButtons[i - 1]
            position = this_button.grid_info()
            column_real = position['column']
            row_real = position['row']
            if column_real != column or row_real != row:
                cool = False
                break
        return cool

game = Game()
game.mainloop()