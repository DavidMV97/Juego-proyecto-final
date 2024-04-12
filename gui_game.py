import tkinter as tk 
from tkinter import ttk, messagebox
from players import Players
import random
from board import draw_divided_circle
class Game:
    
     
    
    def __init__(self, names):
        self.window = tk.Tk()
        self.window.title('Inicio Juego')
        self.window.geometry('800x500')
        self.window.resizable(0, 0)

        self.number_balls = 30
        self.players_list = []
        
        # number of balls for each player
        balls_per_player = self.number_balls // len(names)
        
        frame_top_names = ttk.Frame(self.window)
        frame_top_names.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        
        label_title_name_players = ttk.Label(frame_top_names, text='Jugadores')
        label_title_name_players.pack()
        #self.window.config(bg='#fcfcfc')
        
        for name in names:
            player = Players(name, balls_per_player)
            self.players_list.append(player)
        
            label_name = ttk.Label(frame_top_names, text=f'{name} | Bolas restantes : {player.amount}')
            label_name.pack()
        
        
        frame_board = ttk.Frame(self.window, relief=tk.SOLID)
        frame_board.pack()
        
        canvas = tk.Canvas(frame_board, width=400, height=400)
        canvas.pack()
        
        # Datos para los elementos en cada parte del círculo
        list_one = [0]
        list_two = [0,0]
        list_three = [0,0,0]
        list_four = [0,0,0,0]
        list_five = [0,0,0,0,0]
        data = [list_one, list_two, list_three, list_four, list_five]
        draw_divided_circle(canvas, 200, 200, 150, data)

                
        frame_bottom = ttk.Frame(self.window, relief=tk.SOLID)
        frame_bottom.pack()
        
        imagen_inicial = tk.PhotoImage(file="img/dado.png")  # Suponiendo que la imagen del dado se llama dado.png
        self.label_dado = tk.Label(frame_bottom, image=imagen_inicial)
        self.label_dado.pack()
        
        # start game button
        start_game = ttk.Button(frame_bottom, text='Lanzar dado', command=lanzar_dado )
        start_game.pack()
        self.window.mainloop()
    
    
        def lanzar_dado(self):
            # Genera un número aleatorio entre 1 y 6 (cara del dado)
            numero = random.randint(1, 6)
            
            # Carga la imagen correspondiente al número obtenido
            imagen_path = f"img/dado{numero}.png"  # Suponiendo que tengas imágenes llamadas dado1.png, dado2.png, ..., dado6.png
            imagen_dado = tk.PhotoImage(file=imagen_path)
            
            # Cambia la imagen del Label que muestra el dado
            self.label_dado.config(image=imagen_dado)
            self.label_dado.image = imagen_dado 
            