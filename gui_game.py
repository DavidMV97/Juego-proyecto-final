import tkinter as tk 
import random
from tkinter import ttk, messagebox
from players import Players
from utils.generic import main_color


class Game:
    
    def number_random(self):
            return random.randint(1, 5)


    def replace_zero(self, list_num):
            for i, num in enumerate(list_num):
                if num == 0:
                    list_num[i] = 1
                    break


    def process_list(self):
        random_num = self.number_random()
        if random_num in self.lists:
            if all(element == 1 for element in self.lists[random_num]):
                #The list is full
                self.lists[random_num][-1] = 0
                self.labels[random_num].config(text=f"{random_num}: {self.lists[random_num]}")
            else:
                self.replace_zero(self.lists[random_num])
                self.labels[random_num].config(text=f"{random_num}: {self.lists[random_num]}")

        
    
    
    def __init__(self, names):
        #### Main ttk frames ####
        self.window = tk.Tk()
        self.window.title('Inicio Juego')
        self.window.geometry('800x500')
        self.window.resizable(0, 0)
        style = ttk.Style()
        self.main_color = main_color()
        style.configure('TFrame', background=self.main_color)
        # Main frame
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        # frame left        
        self.frame_top_names = ttk.Frame(self.main_frame)
        self.frame_top_names.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        self.label_title_name_players = ttk.Label(self.frame_top_names, text='Jugadores')
        self.label_title_name_players.pack()
        # Frame right (Board)   
        self.frame_board = ttk.Frame(self.main_frame, relief=tk.SOLID)
        self.frame_board.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        # Frame botton
        self.frame_bottom = ttk.Frame(self.frame_board, relief=tk.SOLID)
        self.frame_bottom.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        # start game button
        start_game = ttk.Button(self.frame_bottom, text='Lanzar dado', command=lambda:self.process_list())
        start_game.pack(fill=tk.X)
        #### End Main ttk frames ####
        
        
        #### Game variables ####
        self.number_balls = 30
        self.players_list = []
        self.balls_per_player = self.number_balls // len(names)
        self.lists = {
            1: [0],
            2: [0, 0],
            3: [0, 0, 0],
            4: [0, 0, 0, 0],
            5: [0, 0, 0, 0, 0]
        }
        
        self.labels = {}
        for key, value in self.lists.items():
            self.labels[key] = ttk.Label(self.frame_board, text=f"{key}: {value}")
            self.labels[key].pack(fill=tk.X)
        
        for name in names:
            player = Players(name, self.balls_per_player)
            self.players_list.append(player)
            label_name = ttk.Label(self.frame_top_names, text=f'{name} | Bolas restantes : {player.amount}')
            label_name.pack()
        

       
        #imagen_inicial = tk.PhotoImage(file="img/logo.jpg")
        self.label_dado = tk.Label(self.frame_bottom, text=1)
        self.label_dado.pack()
       
        self.window.mainloop()
    
     
   