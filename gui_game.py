import tkinter as tk 
import random
from tkinter import ttk, messagebox
from players import Players
from utils.generic import main_color

class Game:
    
    def number_random(self):
            return random.randint(1, 6)


    def replace_zero(self, list_num):
            for i, num in enumerate(list_num):
                if num == 0:
                    list_num[i] = 1
                    break

    
    def update_amount_player(self, operator):
        if (self.current_player_index + 1) <= len(self.players_list):
            if operator == '+=':
                self.players_list[self.current_player_index].amount += 1
            else: 
                self.players_list[self.current_player_index].amount -= 1
            # Update the label corresponding to the player
            self.player_labels[self.current_player_index]['text'] = f'{self.players_list[self.current_player_index].names} | Bolas restantes : {self.players_list[self.current_player_index].amount}'

    
    
    def change_current_label_player(self):
        self.player_labels[self.current_player_index - 1]['background'] = 'white'
        self.player_labels[self.current_player_index]['background'] = 'red'    
    
    
    def end_game(self):
        for player in self.players_list:
            if player.amount == 0:
                messagebox.showinfo("Juego terminado",f"{player.names} ha ganado el juego")
                break

    
    def process_list(self):
        random_num = self.number_random()
        self.change_current_label_player()
        if self.first_round:
            print('we are in the first round ')
            # First round
            if self.current_player_index + 1 >= len(self.players_list):
                self.first_round = False
            print(self.players_list[self.current_player_index].names, 'número', random_num)
        else:
            # Second round
            print('we are in second round')
            if random_num in self.lists:
                if all(element == 1 for element in self.lists[random_num]):
                    # The list is full. The player takes a ball.
                    self.lists[random_num][-1] = 0
                    self.update_amount_player('+=')
                else:
                    # The player leaves a ball.
                    self.replace_zero(self.lists[random_num])
                    self.update_amount_player('-=')

                self.labels[random_num].config(text=f"{random_num}: {self.lists[random_num]}")
            else:
                # The random number is 6. The player leaves a ball in the hole.
                self.update_amount_player('-=')
                #self.labels[self.current_player_index].config(text=f"{self.current_player_index}: {self.lists[self.current_player_index]}")

            self.end_game()

        # Update the current player's index
        self.current_player_index = (self.current_player_index + 1) % len(self.players_list)

    
    
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
        self.first_round = True
        self.number_balls = 30
        self.current_player_index = 0
        self.balls_per_player = self.number_balls // len(names)
        self.players_list = []
        self.player_labels = [] 
        self.labels = {}
        self.lists = {
            1: [0],
            2: [0, 0],
            3: [0, 0, 0],
            4: [0, 0, 0, 0],
            5: [0, 0, 0, 0, 0]
        }
        
        for key, value in self.lists.items():
            self.labels[key] = ttk.Label(self.frame_board, text=f"{key}: {value}")
            self.labels[key].pack(fill=tk.X)
        
        
        for name in names:
            player = Players(name, self.balls_per_player)
            self.players_list.append(player)
            label_name = ttk.Label(self.frame_top_names, text=f'{name} | Bolas restantes : {player.amount}')
            label_name.config(background='white')
            label_name.pack()
            self.player_labels.append(label_name) 
        

       
        #imagen_inicial = tk.PhotoImage(file="img/logo.jpg")
        self.label_dado = tk.Label(self.frame_bottom, text=1)
        self.label_dado.pack()
       
        self.window.mainloop()
    
     
   