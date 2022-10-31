"""This is a tic-tac-toe game
coded my Marina Kreibring for
cse210-20 fall 2022 BYU-I
"""
print("Welcome to the Tic-Tac-Toe!")
# set the board for 9 cells
board=list(range(1,10))

# the function to draw a board
# parameters: board
# return: none
def draw_board(board):
    print("-"*13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-"*13)

# function to take users' input, has while loop
# include input validation with prompts
# parameters: player token
# return: none
def take_input(player_token):
    valid=False
    while not valid:
        player_choice=input(f"{player_token}'s turn to choose a square (1-9): ")
        # check for valid input (integer)
        try:
            player_choice=int(player_choice)
        except:
            print("Invalid input! Please enter an integer.")
            continue
        if player_choice>=1 and player_choice<=9:
            # check if the cell is vacant (cells count from 0, that's why (-1))
            if (str(board[player_choice-1]) not in "XO"):
                board[player_choice-1]=player_token
                valid=True
            else:
                print("This cell is already taken.")
        else:
            print("Wrong input. Please enter a number between 1 and 9.")

# function to check if a player wins
# cell coordinations start from 0
# parameters: board
# return: winner's token or "false"
def check_win(board):
    win_cells=((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for cell in win_cells:
        if board[cell[0]]==board[cell[1]]==board[cell[2]]:
            return board[cell[0]]
    return False

# main function
# parameters: board
def main(board):
    # take turns 
    counter=0
    win=False
    while not win:
        draw_board(board)
        if counter%2==0:
            take_input("X")
        else:
            take_input("O")
        counter +=1
        # check for winner after 4 tries (earlier there's no sense)
        if counter>4:
            winner=check_win(board)
            if winner:
                print(f"{winner} has won! Congratulations!!!")
                win=True
                break
        # if a draw
        if counter==9:
            print("It's a draw!")
            break
    draw_board(board)
main(board)