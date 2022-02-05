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

    def has_game_ended(self) -> tuple(bool, str):
        '''
        Check if the game has ended, if so then decide if player has
        Won or Lost.
        Empty string is returned for win-loss verdict if game hasn't
        ended.
        '''
        # to check for empty cells on playboard
        is_any_cell_empty = False

        # In each row
        for row in self.playboard:
            # check if Game.game_max_value is present
            if Game.game_max_value in row:
                # If present then game has ended and player has won
                return (True, 'Won')
            
            # check for any empty cells side-by-side while
            # checking for max value
            if not is_any_cell_empty and 0 in row:
                is_any_cell_empty = True

        # if any of the cell of playboard is empty
        # then game hasn't ended
        if is_any_cell_empty:
            return (False, '')

        # If any of the adjacent cells have same values and
        # hence can be merged, then game hasn't ended

        # check for mergable values in (board_size-1) x (board_size-1)
        # playboard
        for row in range(0,Game.board_size - 1):
            for col in range(0,Game.board_size - 1):
                if (self.playboard[row][col] == self.playboard[row][col+1] or
                    self.playboard[row][col] == self.playboard[row+1][col]):
                    # mergable value found, game hasn't ended
                    return(False, '')
        
        # check for mergable values in last column of playboard
        for row in range(Game.board_size - 1):
            if self.playboard[row][Game.game_max_value - 1] == self.playboard[row+1][Game.game_max_value]:
                # mergable value found, game hasn't ended
                return (False, '')
        
        # check for mergable values in last row of playboard
        for col in range(Game.board_size - 1):
            if self.playboard[Game.game_max_value - 1][col] == self.playboard[Game.game_max_value - 1][col+1]:
                # mergable value found, game hasn't ended
                return (False, '')

        # the game has ended and player has lost if these conditions are met
        # 1. playboard has no empty cells remaining
        # 2. None of the adjacent cells can be merged
        # 3. game_max_value is not present on the board in addition to
        #    both of the above mentioned conditions

        return (True, 'Lost')

    def __move_left(self) -> None:
        '''Move every tile to its leftmost mostion'''

        for row in self.playboard:
            # track leftmost position which is currently
            # available
            left_available_pos = 0
            for i in range(len(row)):
                if row[i] != 0:
                    row[left_available_pos] = row[i]
                    left_available_pos += 1

    def __merge_cells(self) -> None:
        '''Merge cells in left direction'''

        for row in self.playboard:
            for i in range(1, len(row)):
                # merge and shift left
                # This code works as follows:
                # E.g let row be 2 2 2 0
                # after 1st iteration: 4 0 2 0 (because of row[i] == row[i-1])
                # after 2nd : 4 2 0 0 (because of row[i-1] == 0)
                # after 3rd : 4 2 0 0
                if row[i] == 0:
                    continue
                elif row[i] == row[i-1] or row[i-1] == 0:
                    row[i-1] += row[i]
                    row[i] = 0

    def __reverse_playboard_rows(self) -> None:
        '''Reverse the rows playboard'''
        
        temp_playboard = list()
        for row in self.playboard:
            temp_playboard.append(row[::-1])
        
        self.playboard = temp_playboard

