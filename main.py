# 2048 game implemenation in Python
# Made by Ojas Sethi for Ather Hackathon

'''
Implementation details of Game as per FrontEnd and Dashboard
Developer pdf document

1. Print the 4 x 4 board on each turn in the console and wait for user input. This will initially
have two cells populated at random with a 2 or 4.

2. User will input 1, 2, 3, 4 for left, right, up and down movements

3. Program will then merge all the tiles in given direction and show the latest sums
according to rules mentioned above

4. Next it should select a random empty location in tiles and place a 2 or a 4

5. Repeat steps 1 - 4 till one of the cell reaches 2048
'''

import random # used to randomize appearance of new tiles and tile value (i.e 2 or 4)

