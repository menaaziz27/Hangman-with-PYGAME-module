import os
from time import sleep 
#----Global Variables----

#Drawing the board..
board = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-',
        ]

#who wins 
winner = None

#First player starts
current_player = "X"

#While the game in progress 
game_progress = True

#Run the game
def play_game():

    global winner
    display_board()
    #While game is still going
    while game_progress:

        #make current_player global to write to it 
        global current_player

        #take input from current player
        handle_turn(current_player)

        #Check if someone win or a tie!
        winner = check_game()

        #change turns
        current_player = flip_player(current_player)

    if winner == "X" or winner == "O":
        print(winner + " won!\n")

    else:
        print("Tie!")

    play_again()


#suggestion to play again 
def play_again():

    global winner,game_progress,current_player,board

    print("Do you want to play again?\nPress y if yes and n if no")

    play = True

    while play:

        inp = input()
        if inp.lower() == "y":

            #resetting all global variables to its default
            winner = None
            game_progress = True
            current_player = "X"
            board = [
                    '-', '-', '-',
                    '-', '-', '-',
                    '-', '-', '-',
                    ]
            play_game()
            play = False

        elif inp.lower() == 'n':

            print("Hope you enjoyed :)!")
            play = False

        else:
            print("invalid input, input y or n only")


def display_board():

    #for clearing the screen after each input 
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\n')
    print(" | " + board[0] + ' | ' + board[1] + " | " + board[2] + " | " + " | 1 | 2 | 3 |")
    print(" | " + board[3] + ' | ' + board[4] + " | " + board[5] + " | " + " | 4 | 5 | 6 |")
    print(" | " + board[6] + ' | ' + board[7] + " | " + board[8] + " | " + " | 7 | 8 | 9 |")
    print('\n')


#takes input from the player whatever X or O and putting it on the board
def handle_turn(player):
    print(current_player + '\'s turn')
    #try clause for catching any input that invalids as strings for example
    try:
        position = int(input("Enter position from 1-9: "))
        
        if position in range(1,10):
            position = int(position) - 1

            if board[position] == '-':
                board[position] = player
                display_board()

            else:
                print("You can't go there, try again!")
                sleep(3)
                display_board()

                handle_turn(player)
        else:
            print('Number not valid, try again!')
            handle_turn(player)
        # display_board()

    except Exception:

        print("Enter numbers only.")
        handle_turn(player)

#check if the game is over or not 
def check_game():

    winner = check_win()

    check_tie()

    return winner
#check if someone win
def check_win():

    global winner

    winner = check_rows()

    winner = check_columns()

    winner = check_diagnols()

    return winner

def check_rows():

    global winner,game_progress

    if board[0] == board[1] == board[2] != '-':
        winner = board[0]
        game_progress = False

    elif board[3] == board[4] == board[5] != '-':
        winner = board[3]
        game_progress = False

    elif board[6] == board[7] == board[8] != '-':
        winner = board[6]
        game_progress = False

    return winner

def check_columns():

    global winner,game_progress

    if board[0] == board[3] == board[6] != '-':
        winner = board[0]
        game_progress = False

    elif board[1] == board[4] == board[7] != '-':
        winner = board[1]
        game_progress = False

    elif board[2] == board[5] == board[8] != '-':
        winner = board[2]
        game_progress = False

    return winner

def check_diagnols():

    global winner,game_progress

    if board[0] == board[4] == board[8] != '-':
        winner = board[0]
        game_progress = False

    elif board[2] == board[4] == board[6] != '-':
        winner = board[2]
        game_progress = False

    return winner


def check_tie():
    global game_progress
    if "-" not in board and winner == None:
        game_progress = False

def flip_player(current):

    if current == "X":
        current = "O"

    else:
        current = "X"

    return current


if __name__ == "__main__":
    play_game()