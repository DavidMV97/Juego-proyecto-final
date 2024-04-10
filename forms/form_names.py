import tkinter as tk 
from tkinter import ttk
from tkinter.font import BOLD
import utils.generic as utl 

class PanelNames: 
    
    def get_entry_values(self):
        values = [entry.get() for entry in self.entries]
        print(values)
        #return values  
        
    
    def __init__(self, names):
        self.window = tk.Tk()
        self.window.title('Nombre de los jugadores')
        self.entries = []

        #w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        w, h = 800, 500
        utl.center_window(self.window, w, h)

        #self.window.config(bg='#fcfcfc')
        self.window.resizable(0, 0)
   
        
        for i in range(names):
            print(i)
            label_name = ttk.Label(self.window, text=f'Ingrese el nombre del jugador {i+1}')
            label_name.pack()
            entry = ttk.Entry(self.window, font=('Times', 14))
            entry.pack(fill=tk.X, padx=20, pady=10)
            self.entries.append(entry)       
            
        
        #logo = utl.read_img("./img/logo.jpg", (200, 200))
        
        button_continue = ttk.Button(self.window, text='Entrar', style='My.TButton')
        button_continue.config(command=self.get_entry_values)
        button_continue.pack(fill=tk.X, padx=20, pady=20)
        
        # Establecer estilos
        style = ttk.Style()
        style.configure('Logo.TLabel', background='#3a7ff6')
        
        #label = ttk.Label(self.window, image=logo, style='Logo.TLabel')
        #label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        self.window.mainloop()
        
    
        