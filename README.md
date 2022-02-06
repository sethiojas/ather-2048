# ather-2048
## Problem Statement
### Frontend & Dashboard developer
## Submitted by
### Ojas Sethi
## Aim
### To build a console-based working replica of 2048 game using Python
## Assumptions
- If a move (i.e., left, right, up, down) done by player does not result in a change in playboard, i.e., playboard is same before and after the move, then no new tile is added to the playboard.

- Methods beginning with double underscore ('```__```') are assumed to be private.

## Discussion Objectives
- ### Design principles used
    **Modular programming** is used, which is a software design principle that emphasizes on separating the functionality of a program into independent modules, along with **Object Oriented Programming paradigm**.

    **Modular Programming** - Driver code which runs the game is in ```main.py``` & the logic for the game itself is contained in ```game.py```

    **OOP** – All game logic is contained with ```Game``` class, which has public, private functions in addition to static and object variables to do the necessary tasks.

- ### Thoughts / Probable solutions / Problems faced while designing the solution
    - 
        **Problem**: First problem was independent implementation of each move.

        **Thought work**: which was quickly solved owed to 11th grade mathematics. 

        **Solution**: The use of row reversal and matrix transformation led to only one of the player move being independently implemented (I selected the left move in my case).

    -
        **Problem**: Next problem was the incorrect implementation of``` __merge_left``` method. The original implementation left empty tiles in between and did not move every tile to the leftmost available position.

        **Thought work**: In the beginning, I thought this was the case only when moving the ```0th``` index element, but as I would later discover It was caused at every index ```i``` where ```i``` was equal to ```leftmost available position```, because I was setting ```row[i] = 0``` after moving it.

        **Solution**: set ```row[i] = 0``` only when ```i is not equal to leftmost available position```.

    -
        **Problem**: The problem which took most of the time was my incorrect implementation of ```__merge_cells``` method which not only left empty cells in between but would also merge the resultant of two tiles with a third tile.

        **Thought work**: I initially thought of maintaining a ```Boolean``` condition to solve this problem, however this approach was incomplete. Next I moved to use of ```stack``` for combining tiles much like the famous unequal parenthesis problem.

        **Solution**: The solution which worked was the combined use of both the above ideas along with a use of temporary playboard and temporary rows.

- ### Code walkthrough
1. ``game.py``

    ``Game`` class
    It encapsulates the data of the game and abstracts how the moves are executed. It also contains *three static variables*:
    i. ``play_instructions`` – stores the instructions which are displayed at the start of the game.

    ii. ```board_size``` – It stores the size of the square board on which the game is played.

    iii. ```game_max_value``` – It stores the maximum attainable value within the game

    •	```__init__``` - Initial the object of the game class, make a new empty playboard on which the game will be played and sets the is_board_changed value to True initially

    •	```__add_new_tile``` – Add a new tile to the playboard after a move by the player. Tile is added only if the is_board_changed variable is set to True.

    •	```show_playboard``` – Calls the __add_new_tile method and then displays the playboard to STDOUT

    •	```has_game_ended``` – Check if the game has ended. If it has then based upon the conditions decide if player won or lost.

    •	```__move_left``` – Move all the tiles in a row to leftmost possible position and do this to every row of playboard

    •	```__merge_cells``` – Combine two adjacent tiles in a row if they can be combined.
    e.g.: ```row [4,4,2,0]``` can be reduced to ```row [8, 2, 0, 0]```

    •	```__reverse_playboard_rows``` – Reverse all the rows of playboard.
    A reversal of a ```row[2, 0, 2, 4]``` would be ```row[4, 2, 0, 2]```

    •	```__transform_playboard``` – Apply matrix transformation operation to playboard. After a transform operation, the rows and columns of a matrix are interchanged.

    •	```left_move``` – Execute a left move on playboard.

    •	```right_move``` – Execute a right move on playboard.

    •	```up_move``` – Execute a up move on playboard.

    •	```down_move``` – Execute a down move on playboard.

2. ```main.py``` – It contains the driver code which run the game. Player is displayed instructions to play and is then asked to enter their choice of move. The choice is played out then an updated playboard is shown. This process continues until player wins, looses, or quits

- ### Scope of making this an 8x8 from 4x4
    Changing the static variable ```Game.board_size``` should suffice for this change as the board size is not hard-coded into the program.
- ### Change from 2048 to 4096 as end number 
    Changing the static variable ```Game.game_max_value``` should suffice for this change as the max attainable value is not hard-coded into the program.
