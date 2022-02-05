# Unit tests for main.py

import unittest
import game

class TestGame(unittest.TestCase):
    def test_static_variables(self) -> None:
        '''Test static variables of Game class'''
        
        self.assertEqual(game.Game.board_size, 4, "Board Size does not match")
        self.assertEqual(game.Game.game_max_value, 2048, "Game max value does not match")

        # Do not change the indentation inside multi-line string
        # as it will interpret it as space in actual string, which
        # in turn will make unit test fail.
        play_instruction = '''Play the game via following commands,
    Enter:
    1 - To move tiles Left.
    2 - To move tiles Right.
    3 - To move tiles Up.
    4 - To move tiles Down.
    '''
        self.assertEqual(game.Game.play_instructions, play_instruction, "Play instructions do not match")