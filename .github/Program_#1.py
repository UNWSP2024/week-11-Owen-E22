import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('My favorite phrase')

        self.label = tkinter.Label(self.main_window, text = 'The pain you feel today, will be the strength you feel tomorrow')
        self.label.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()