import tkinter as tk 
from tkinter import ttk, messagebox
from gui_game import Game

class PanelNames: 
    
    def get_entry_values(self):
        values = []
        error = False

        for entry in self.entries:
            if entry.get() == '':
                error = True
                messagebox.showerror('Campos en blanco', 'Por favor llena todos los campos')
                break
            elif not entry.get().isalpha():
                error = True
                messagebox.showerror('Solo letras', '¡Solo se permiten letras!')
                break
            else:
                error = False
                values.append(entry.get())
                 
        if not error:
            self.window.destroy()
            Game(values)
    
    def __init__(self, names):
        self.window = tk.Tk()
        self.window.title('Nombre de los jugadores')
        self.entries = []
        self.window.resizable(0, 0)
        
        bg_color = '#fff'
        fg_color = '#666a88'
        button_color = '#3a7ff6'
        self.window.configure(bg=bg_color)
        # Estilos de fuente
        font_style = ('Helvetica', 12)
        title_font_style = ('Helvetica', 14, 'bold')
        
        for i in range(names):
            label_name = ttk.Label(self.window, text=f'Ingrese el nombre del jugador {i+1}', font=title_font_style, foreground=fg_color, background=bg_color)
            label_name.pack(fill=tk.X,padx=30, pady=10)
            entry = ttk.Entry(self.window, font=font_style)
            entry.pack(fill=tk.X, padx=30)
            self.entries.append(entry)       
            
        button_continue = ttk.Button(self.window, text='Entrar', style='My.TButton', command=self.get_entry_values)
        button_continue.pack(fill=tk.X, padx=20, pady=20)
        
        # Establecer estilos
        style = ttk.Style()
        style.configure('My.TButton', background=button_color, foreground='white', activebackground='white', activeforeground=button_color, font=font_style)
    
        self.window.mainloop()
