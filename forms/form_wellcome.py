import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import utils.generic as utl
from forms.form_names import PanelNames

class App:
    def check_number_players(self):
        try:
            players = int(self.number_players.get())
            if players < 2 :
                messagebox.showerror(message='No es posible jugar con menos de dos jugadores. Ingresa un número entre 2 y 7', title='Error')
            elif players >= 8:
                messagebox.showerror(message=f'No es posible jugar con ' + str(players) + ' jugadores. Ingresa un número entre 2 y 7', title='Error')
            else:
                self.window.destroy()
                PanelNames(players)
        except ValueError:
            messagebox.showerror(message='Ingresa un número valido', title='Error')
 
    
    
    def __init__(self):    
        self.window = tk.Tk()
        self.window.title('Bienvenido')
        self.window.geometry('800x300')
        self.window.resizable(0,0)
        self.window.config(background='#1f1e30')
                
        # frame logo
        frame_logo = ttk.Frame(self.window, width=250, style='My.TFrame')
        frame_logo.pack(side='left', expand=tk.YES, fill=tk.BOTH)
        label = ttk.Label(frame_logo, text='\u2681',font=('Helvetica', 50), style='LabelLogo.TLabel')
        label.pack(fill=tk.BOTH, expand=tk.YES, padx=20)
        
        label = ttk.Label(frame_logo, text='\u2683',font=('Helvetica', 50), style='LabelLogo.TLabel')
        label.pack( expand=tk.NO, pady=30)
        
        # frame form
        frame_form = ttk.Frame(self.window)
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        
        # frame top 
        frame_form_top = ttk.Frame(frame_form, height= 50, style='My.TFrame')
        frame_form_top.pack(side='top', fill=tk.X)
        title = ttk.Label(frame_form_top, text='Bienvenido al juego : ¿Por que siempre yo?', font=('Helvetica', 18), style='My.TLabel')
        title.pack(expand=tk.YES, fill=tk.BOTH,padx=20, pady=50)
        
        
        # frame form fill
        frame_form_fill = ttk.Frame(frame_form, height= 50, style='My.TFrame')
        frame_form_fill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        
        label_number_players = ttk.Label(frame_form_fill, text='Ingrese la cantidad de jugadores que desean jugar (2 - 7):', font=('Helvetica', 14), style='My.TLabel')
        label_number_players.pack(fill=tk.X, padx=20, pady=5)
        self.number_players = ttk.Entry(frame_form_fill, font=('Helvetica', 14))
        self.number_players.pack(fill=tk.X, padx=20, pady=10)
        
        
        enter = ttk.Button(frame_form_fill, text='Entrar', style='My.TButton')
        enter.config(command=self.check_number_players)
        enter.pack(fill=tk.X, padx=20, pady=20)
        
        
        # Establecer estilos
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        style.configure('My.TLabel', foreground='#666a88', background='#fff')
        style.configure('LabelLogo.TLabel', foreground='#3a7ff6', background='#fff')

        style.configure('My.TButton', background='#3a7ff6', foreground='#fff')
        
        self.window.mainloop()
        
        



