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

    def move_button(self, i):
        print(i)

game = Game()
game.mainloop()