import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.information = tkinter.Button(self.main_window, text ='Information', command = self.info, relief = 'raised')
        self.quit = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy, relief = 'sunken')


        self.information.pack(side = 'left')
        self.quit.pack(side = 'left')


        tkinter.mainloop()


    def info(self):
        tkinter.messagebox.showinfo('Name and address', 'Owen Eigen, Mahtomedi Minnesota, 440 Glenmar Ave')



        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()