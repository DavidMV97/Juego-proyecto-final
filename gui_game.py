import tkinter as tk 
import random
import pygame
from tkinter import ttk, messagebox
from players import Players
from utils.generic import main_color

pygame.mixer.init()

class Game:    
    def __init__(self, names):
        #### Main ttk frames ####
        self.window = tk.Tk()
        self.window.title('Inicio Juego')
        self.window.geometry('800x400')
        self.window.resizable(0, 0)
        style = ttk.Style()
        self.main_color = main_color()
        style.configure('TFrame', background=self.main_color)
        # Main frame
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        # frame left        
        self.frame_top_names = ttk.Frame(self.main_frame)
        self.frame_top_names.pack(side='left', expand=tk.NO, fill=tk.BOTH, pady=10)
        self.label_title_name_players = ttk.Label(self.frame_top_names, text='Jugadores')
        self.label_title_name_players.config(background='white')
        self.label_title_name_players.pack()
        # Frame right top 
        self.frame_right_top = ttk.Frame(self.main_frame, relief=tk.FLAT)
        self.frame_right_top.pack(side='right', fill=tk.BOTH, expand=tk.YES)
        # Frame right (Board)   
        self.frame_board = ttk.Frame(self.main_frame, relief=tk.FLAT)
        self.frame_board.pack(side='right', expand=tk.YES)
        # Frame botton
        self.frame_bottom = ttk.Frame(self.frame_board)
        self.frame_bottom.grid(row=6, columnspan=4,  pady=20)
        # start game button
        start_game = tk.Button(self.frame_bottom, text='Lanzar dado',cursor="hand1", command=lambda:self.roll_dice())
        start_game.config(bg='#3a7ff6', fg='white', activebackground="white", activeforeground='#3a7ff6')
        start_game.grid(row=1, columnspan=4)
        #### End Main ttk frames ####
        
        
        #### Game variables ####
        self.first_round = True
        self.number_balls = 30
        self.current_player_index = 0
        self.balls_per_player = self.number_balls // len(names)
        # Obtain the indexes of all the players along with the number they obtained
        self.get_all_number_players = []
        self.players_list = []
        self.player_labels = [] 
        self.dice_values = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.labels = {}
        # Label number six
        self.label_top_right = tk.Label(self.frame_right_top, text="6", font=("Arial 30 bold"))
        self.label_top_right.config(bg='white', fg='#666a88')
        self.label_top_right.pack()
        
        self.lists = {i: ['\u25CB'] * i for i in range(1, 6)}

        for key, value in self.lists.items():
            row_label = key // 3 
            column_label = (key - 1) % 3
            formatted_value = ' '.join(map(str, value))
            self.labels[key] = tk.Label(self.frame_board, text=f"{formatted_value}", font=("Arial 30 bold"))
            self.labels[key].configure(background='white', foreground='#3a7ff6')
            self.labels[key].grid(row=row_label, column=column_label, pady=12, padx=20)
        
        
        for name in names:
            player = Players(name, self.balls_per_player)
            self.players_list.append(player)
            label_name = tk.Label(self.frame_top_names, text=f'{name} | Total Bolas : {player.amount}')
            label_name.config(background='white', pady=2, padx=5)
            label_name.pack()
            self.player_labels.append(label_name) 
        
 
        self.label_dado = tk.Label(self.frame_bottom, text='\u2684')
        self.label_dado.config(bg='white', fg='#3a7ff6', font=('Helvetica', 50))
        self.label_dado.grid(row=0, columnspan=4, pady=10)
       
        self.window.mainloop()
    
    
    
    def number_random(self):
            return random.randint(1, 6)


    def fill_space(self, list_num):
            for i, num in enumerate(list_num):
                if num == '\u25CB':
                    list_num[i] = '\u25CF'
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
        self.player_labels[self.current_player_index - 1]['foreground'] = 'black'
        self.player_labels[self.current_player_index]['background'] = '#3a7ff6' 
        self.player_labels[self.current_player_index]['foreground'] = 'white'   
    
    
    def end_game(self):
        for player in self.players_list:
            if player.amount == 0:
                pygame.mixer.music.load("sounds/success.mp3")
                pygame.mixer.music.play(loops=0)
                messagebox.showinfo("Juego terminado",f"{player.names} ha ganado el juego")
                self.window.destroy()
                break
    
    # Only the label changes to indicate that the player has obtained a six
    def get_six_number(self, number):
        if number == 6:
            self.label_top_right.config(fg='#3a7ff6')
            pygame.mixer.music.load("sounds/get-six.mp3")
            pygame.mixer.music.play(loops=0)
        else:
            self.label_top_right.config(fg='#666a88')
    
    
    def  player_highest_number(self, players_numbers):
        if len(self.get_all_number_players) > 0 :
            # Highest random number obtained
            greatest_tuple = max(players_numbers, key=lambda x: x[1])
            # Get the first number of the found tuple (player index)
            player_index = greatest_tuple[0]
            self.current_player_index = player_index
            for i in range(len(self.player_labels)):
                self.player_labels[i]['background'] = 'white'
                self.player_labels[i]['foreground'] = 'black'
                
            pygame.mixer.music.load("sounds/winner-first-round.mp3")
            pygame.mixer.music.play(loops=0)
            self.change_current_label_player()
            messagebox.showinfo("Turno obtenido",f"El jugador que lanza primero es : {self.players_list[player_index].names}")

    
    def roll_dice(self):
        random_num = self.number_random()
        self.change_current_label_player()
        self.label_dado.config(text=self.dice_values[random_num - 1])
        pygame.mixer.music.load("sounds/click.mp3")
        pygame.mixer.music.play(loops=0)
        if self.first_round:
            # First round
            if self.current_player_index + 1 >= len(self.players_list):
                self.first_round = False
            # Player index and number obtained
            get_number_player = (self.current_player_index, random_num)
            self.get_all_number_players.append(get_number_player)
        else:
            # Second round
            self.get_six_number(random_num)
            self.player_highest_number(self.get_all_number_players)
            self.get_all_number_players = []
            if random_num in self.lists:
                if all(element == '\u25CF' for element in self.lists[random_num]):
                    # The list is full. The player takes a ball.
                    self.lists[random_num][-1] = '\u25CB'
                    self.update_amount_player('+=')
                else:
                    # The player leaves a ball.
                    self.fill_space(self.lists[random_num])
                    self.update_amount_player('-=')
                formatted_value = ' '.join(map(str, self.lists[random_num]))
                self.labels[random_num].config(text=f"{formatted_value}")
            else:
                # The random number is 6. The player leaves a ball in the hole.
                self.update_amount_player('-=')
                #self.labels[self.current_player_index].config(text=f"{self.current_player_index}: {self.lists[self.current_player_index]}")

            self.end_game()

        # Update the current player's index
        self.current_player_index = (self.current_player_index + 1) % len(self.players_list)


