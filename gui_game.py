import tkinter as tk 
from tkinter import ttk, messagebox

class Game:
       
    def __init__(self, names):
        self.window = tk.Tk()
        self.window.title('Inicio Juego')
        
        #w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        w, h = 800, 500
        self.window.geometry('800x500')
        # utl.center_window(self.window, w, h)

        #self.window.config(bg='#fcfcfc')
        self.window.resizable(0, 0)
        
        self.window.mainloop()
   
        