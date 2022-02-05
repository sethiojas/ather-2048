# 2048 game implemenation in Python
# Made by Ojas Sethi for Ather Hackathon

# Implementation details of Game as per FrontEnd and Dashboard
# Developer pdf document
#
# 1. Print the 4 x 4 board on each turn in the console and wait for user input. This will initially
# have two cells populated at random with a 2 or 4.
#
# 2. User will input 1, 2, 3, 4 for left, right, up and down movements
#
# 3. Program will then merge all the tiles in given direction and show the latest sums
# according to rules mentioned above
#
# 4. Next it should select a random empty location in tiles and place a 2 or a 4
#
# 5. Repeat steps 1 - 4 till one of the cell reaches 2048

import random # used to randomize appearance of new tiles and tile value (i.e 2 or 4)

class Game():
    board_size = 4
    game_max_value = 2048
    play_instructions = '''Play the game via following commands,
    Enter:
    1 - To move tiles Left.
    2 - To move tiles Right.
    3 - To move tiles Up.
    4 - To move tiles Down.
    '''
    
    def __init__(self) -> None:
        '''Set the playboard for a new game'''
        # make a board_size x board_size empty playboard.
        # [0] * number results in a list whose length is
        # equal to number and every entry in that list is
        # 0.
        self.playboard = list()
        for i in range(Game.board_size):
            self.playboard.append([0] * Game.board_size)

        # add a new tile to the playboard
        self.__add_new_tile()

    # double underscore '_ _' at start indicates it's private
    def __add_new_tile(self) -> None:
        '''
        Add a tile of value 2 or 4 to any random empty location
        on the playboard.
        '''

        # randomly select either 2 or 4
        tile = random.choice({2,4})

        # select a random cell
        row_index = random.randint(0, 3)
        col_index = random.randint(0, 3)

        # if the randomly selected cell isn't empty
        # keep selecting other cells till one of them
        # is empty.
        while self.playboard[row_index][col_index] != 0:
            row_index = random.randint(0, 3)
            col_index = random.randint(0, 3)
        
        # add the tile to randomly selected cell
        self.playboard[row_index][col_index] = tile

    def show_playboard(self) -> None:
        '''Display playboard on STDOUT'''

        # go through each row and display it
        for row in self.playboard:
            print(row)

