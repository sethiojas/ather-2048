from game import Game

# execute the code if this script was run
# directly
if __name__ == '__main__':
    # print game name as header
    print("+"*5, 2048, "+"*5)
    
    # print instrcutions to play the game
    print(Game.play_instructions)
    
    # wait for user input to continue
    input("\nPress any key to continue")

    # initialize Game object
    my_game = Game()
    play_hint = "1-Left, 2-Right, 3-Up, 4-Down, 5-Exit.: "
    
    # to track if game has ended
    game_end = (False, '')

    # while game doesn't end continue playing
    while not game_end[0]:
        # output a newline to STDOUT
        print()
        # output the playboard
        my_game.show_playboard()
        # get player's move
        choice = input(play_hint)

        # while choice entered is not valid
        # keep asking for it
        while choice not in ("1", "2", "3", "4", "5"):
            print("Invalid input")
            choice = input(play_hint)
        
        # do left move on 1
        if choice == "1":
            my_game.left_move()
        
        # do right move on 2
        elif choice == "2":
            my_game.right_move()
       
        # do up move on 3
        elif choice == "3":
            my_game.up_move()
       
        # do down move on 4
        elif choice == "4":
            my_game.down_move()

        # if choice is 5 assign (True, "Quit") to game_end
        # else assign return value of my_game.has_game_ended()
        game_end = (True, "Quit") if choice == "5" else my_game.has_game_ended()
    
    # output the result of the game
    print(f"Player {game_end[1]}")
