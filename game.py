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

# used to randomize appearance of new tiles and tile value (i.e 2 or 4)
import random
# used for Type Annotation in has_game_ended method
from typing import Tuple 

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

        # keeps track of change of board due to player's
        # previous move.
        # Initially it is set to true because we need to add
        # a new tile at the start of the game.
        self.is_board_changed = True

    # double underscore '_ _' at start indicates it's private
    def __add_new_tile(self) -> None:
        '''
        Add a tile of value 2 or 4 to any random empty location
        on the playboard.
        '''
        # If previous player moved didn't change the
        # playboard, then do not add a new tile
        if not self.is_board_changed:
            return None

        # randomly select either 2 or 4
        tile = random.choice((2,4))

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
        # add a new random tile
        self.__add_new_tile()
        # go through each row and display it
        for row in self.playboard:
            print(row)

    def has_game_ended(self) -> Tuple[bool, str]:
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
                    if i != left_available_pos:
                        row[i] = 0
                    left_available_pos += 1

    def __merge_cells(self) -> None:
        '''Merge cells in left direction'''

        # create a temporary playboard
        temp_playboard = list()

        # go through each row in playboard
        for row in self.playboard:
            # create a temporary row
            temp_row = list()
            # add the first tile of row to
            # temporary row
            temp_row.append(row[0])
            # to check if merge happend in
            # previous iteration
            merged_in_prev_iter = False

            # go through remaining elements of row
            # i.e. from index 1 to index Game.board_size - 1
            for i in range(1, len(row)):
                # if the last element of temporary row
                # matches the current tile and we didn't
                # merge 2 tiles in previous iteration
                if temp_row[-1] == row[i] and not merged_in_prev_iter:
                    # merge the last element of temporary row
                    # and current element and make merged_in_prev_iter
                    # True
                    merged_in_prev_iter = True
                    tile = temp_row.pop() + row[i]
                    temp_row.append(tile)
                # if the last element of temporary row
                # does not match the current tile or if we
                # performed a merge operation in previous
                # iteration
                else:
                    # add current element to end of temporary row
                    # and make merged_in_prev_iter False
                    temp_row.append(row[i])
                    merged_in_prev_iter = False
            
            # append zeros at the end of temporary row
            # till its length does not equal the board_size
            while len(temp_row) != Game.board_size:
                temp_row.append(0)
            
            # add this temporary row to temporary
            # playboard 
            temp_playboard.append(temp_row)
        
        # set playboard equal to temporary playboard
        self.playboard = temp_playboard

    def __reverse_playboard_rows(self) -> None:
        '''Reverse the rows playboard'''
        
        temp_playboard = list()
        for row in self.playboard:
            # list[::-1] creates a slice of whole list in reverse
            # order
            temp_playboard.append(row[::-1])
        
        self.playboard = temp_playboard

    def __transform_playboard(self) -> None:
        '''Apply matrix transformation to playboard'''
        temp_playboard = list()

        for col_index in range(len(self.playboard[0])):
            temp_row = list()
            # read all the tiles in column and add them to temp_row
            for row_index in range(len(self.playboard)):
                temp_row.append(self.playboard[row_index][col_index])
            # add temp_row to temp_playboard
            temp_playboard.append(temp_row)
        # update the playboard
        self.playboard = temp_playboard

    def left_move(self) -> None:
        '''Execute a left move on playboard'''
        # Since all the other three moves namely
        # right_move, up_move and down_move use
        # left_move, we only need to track
        # playboard change in this method and not
        # the others.
        prev_playboard = self.playboard

        # move all the tiles left
        self.__move_left()
        # combine mergable tiles
        self.__merge_cells()

        # If the move did not result in a board change
        # set is_board_changed to False else set it to
        # True
        if prev_playboard == self.playboard:
            self.is_board_changed = False
        else:
            self.is_board_changed = True

    def right_move(self) -> None:
        '''Execute a right move on playboard'''
        # doing a right move is same as doing
        # left move on reversed rows

        # reverse the rows
        self.__reverse_playboard_rows()
        # do a left move
        self.left_move()
        # reverse the rows again to get
        # negate the first revarsal
        self.__reverse_playboard_rows()

    def up_move(self) -> None:
        '''Execute a up move on playboard'''
        # up move is same as doing left
        # move after applying matrix
        # transformation to playboard

        # transform the playboard
        self.__transform_playboard()
        # execute left move
        self.left_move()
        # transfor the playboard again to negate
        # previous transformation
        self.__transform_playboard()
    
    def down_move(self) -> None:
        '''Execute a down move on playboard'''
        # down move can be done by doing a left
        # move on the transform of playboard
        # with reversed rows

        # transform playboard
        self.__transform_playboard()
        # reverse the rows of transformed playboard
        self.__reverse_playboard_rows()
        # execute a left move
        self.left_move()
        # negate the previous row reversal
        self.__reverse_playboard_rows()
        # negate the previous tranform operation
        self.__transform_playboard()
