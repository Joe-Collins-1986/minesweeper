"""
To use google sheets api will need to install 
- google-auth
- gspread
Instruction video (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/?child=first)

NEED TO REVERSE COORDINATES FOR USER EXPERIENCE
"""

import os #used to clear console
import random # used to assign random mine positions
import re
from pyfiglet import figlet_format


def cls(): # function to clear console for cross-platform: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')


def start_game():
    """ Opens the game - done
    Introduce game - done
    Offer play or rules through user input - done
        - call rules function (r)
        - call difficulty function (p)
        - error with feedback for invalid enteries
    Call difficulty function to define board_size and no_mines variables - done
    Call play function with defined valriables as arguments - done
    Function to recycle on play function completion
    """
    cls()
    # Link to ASCII character instruction https://theasciicode.com.ar/extended-ascii-code/block-graphic-character-ascii-code-219.html
    # copied █ symbol from windows accoss to mac for use
    
    print(figlet_format("    MINESWEEPER", font = "standard"))
    print("""
                                    _________
                █                 /  _______  \                 █
             █  █  █             /  /       \  \             █  █  █
              █████             /  / warning \  \             █████
           ██ █████ ██         /  /   mines   \  \         ██ █████ ██
              █████           /  /    ahead!   \  \           █████
             █  █  █         /  /_______________\  \         █  █  █
                █            \_____________________/            █  

                              WELCOME TO MINSWEEPER

................................................................................
................................................................................
        """)
    print("\U0001F4A5")
    print("\U0001F6A9")

    print(" _____ _____ _____ _____ _____ _____ _____ _____ _____ ")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|  _  |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|     |     |     |     |     |     |     |     |     |")
    print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|")


    print("For a 10 X 10 grid the size would requie a screen (61 X 30)\nnot including instructions and user input area")
    print("...................................\n")

    home_page = True
    while home_page:
        intro_nav = input("Enter 'P' to play,\nor enter 'R' to see the rules.\n\n").lower()
        cls()
        if intro_nav == "r":
            home_page = False
            rules()
        elif intro_nav == "p":
            home_page = False
            difficulty()
        else:
            print(f"I'm sorry {intro_nav} is not a valid entry.\n")

def rules(): 
    """ Present rules to user
    Set anykey to return to inital page
    """
    cls()
    print(figlet_format("RULES", font = "standard"))
    rules = True
    print("""Game Objective:\n\n
    **** type in the rules ***
    """)
    leave_rules = input("Enter anykey to reurn to the main page\n\n").lower()
    cls()

    start_game()

def difficulty():
    """ Define difficulty of the game
    Explain difficulty settings
    Take user input
        - easy(e) will return (5, 6) 
        - medium(m) will return (10, 9) 
        - hard(h) will return (20, 12) 
        - error with feedback for invalid enteries
    """
    cls()
    print(figlet_format("DIFFICULTY", font = "standard"))
    evaluating_dificulty = True
    while evaluating_dificulty:
        print("There are 3 difficulty settings in this game")
        print("easy - This will present you with a 6X6 grid and there will be 5 hidden mines")
        print("medium - This will present you with a 8X8 grid and there will be 10 hidden mines")
        print("easy - This will present you with a 10X10 grid and there will be 20 hidden mines\n")
        print("Please enter the difficulty you would like to play:")
        difficulty = input("Enter 'e' for easy,\nenter 'm' or medium,\nor enter 'h' for hard.\n").lower()

        if difficulty == "e":
            board_size = 6
            no_mines = 5
            evaluating_dificulty = False
        elif difficulty == "m":
            board_size = 8
            no_mines = 10
            evaluating_dificulty = False
        elif difficulty == "h":
            board_size = 10
            no_mines = 20
            evaluating_dificulty = False
        else:
            cls()
            print(f"\nI'm sorry {difficulty} is not a valid entry.\n")
    cls()
    play(board_size, no_mines)



def play(board_size, no_mines):
    """ Initiate game play
    Define the grid
    Run while loop for game when not lost
        - present board
        - feedback from last guess and provide instructions for next guess
        - take user input and record as arguments for select space function
            - error with feedback for invalid enteries
    Define win stauts by calling win function
        - If win status is True inform user and break out of function.
    If game status lost inform user and break out of function.  
    """
    board = GameLayout(board_size, no_mines)

    game_active = True
    while game_active:
        
        print(figlet_format("GAME PLAY", font = "standard"))
        print(board)
        
        xy_inputs = True
        while xy_inputs:
            try:
                x_axis, y_axis = map(int, input("\nEnter the row & column with a space seperating them (e.g. 3 5)\n").split())
                
                if (x_axis < 0 or x_axis >= board_size) and (y_axis < 0 or y_axis >= board_size):
                    raise Exception (f"x_axis ({x_axis}) and y_axis ({y_axis}) are not in range (0:{board_size})")
                elif x_axis < 0 or x_axis >= board_size:
                    raise Exception (f"x_axis ({x_axis}) is not in range (0:{board_size})")
                elif y_axis < 0 or y_axis >= board_size:
                    raise Exception (f"y_axis ({y_axis}) is not in range (0:{board_size})")
                
                if board.user_board[int(x_axis)][int(y_axis)] not in ("| _", "_", "_ |", "| F", "F", "F |"):
                    raise Exception (f"You have already dug {x_axis} {y_axis}\n")

            except ValueError as e:
                board.reset_gameplay(board)
                print("\nInvalid Entry:\n - Do not type letters\n - Do not type special characters\n - Ensure you entered 2 coordinates")
                print(f"\nIssue: {e}")
            except Exception as e:
                board.reset_gameplay(board)
                print(f"\nIssue: {e}")
            else:
                xy_inputs = False

        if board.user_board[int(x_axis)][int(y_axis)] in ("| F", "F", "F |"):
    
            dig_input = True
            while dig_input:
                try:
                    print("\nThis position has a flag on it")
                    dig = input("Would you like to dig anyway? (Y/N)\n")    
                    if dig.lower() not in ("y", "yes", "d", "dig", "n", "no"):
                        raise Exception (f"That is not a valid entry.")
                except Exception as e:
                    print(f"Issue: {e}")
                else:
                    dig_input = False
            if dig.lower() not in ("y", "yes", "d", "dig"):
                flag = "leave_flag"
            else:
                flag = "d"

        else:
            flag_input = True
            while flag_input:
                try:
                    flag = input("\nWould you like to place a flag on this location (Y/N)\n")
                    if flag.lower() not in ("y", "yes", "f", "flag", "n", "no"):
                        raise Exception (f"That is not a valid entry.")
                except Exception as e:
                    board.reset_gameplay(board)
                    print("\nEnter the row & column with a space seperating them (e.g. 3 5)")
                    print(x_axis, y_axis)
                    print(f"\nIssue: {e}")
                else:
                    flag_input = False

        game_active = board.selected_space(x_axis, y_axis, flag)

        win(board)
        cls()
    
    cls()
    print(figlet_format("GAME OVER", font = "standard"))
    print("\nGAME OVER, YOU LOSE")
    print(f"\nRow: {x_axis}, Column: {y_axis} had a mine")
    print(board)
    input("\nBetter luck next time, press anykey to continue\n")

    start_game()


def win(board):
    """ Check if user has won
    Check if the users guesses have met the available spaces (board - bombs)
    If it has return True else return False
    """
    print(figlet_format("YOU WIN", font = "standard"))
    if len(board.guesses) == (board.board_size ** 2) - board.no_mines:
        print("YOU WON")
        input("Hit anykey to play again")
        start_game()
        #return game won to play function in final version so it does not run a function within a function each new game


class GameLayout:
    """
    This class will be used to define the levels grid and check user inputs against assigned mines and cell values.
    """

    def __init__(self, board_size, no_mines):
        """
        Initialize the object state
        """
        self.board_size = board_size
        self.no_mines = no_mines

        self.board_layout = self.set_board()
        self.add_mines()
        self.add_values()

        self.user_board = [["_" for col in range(self.board_size)] for row in range(self.board_size)] # use to compare with board_layout on user guess
        self.row_seperator = self.underscore()
        self.guesses = []

        self.flags_placed = 0
        self.flages_left = self.no_mines - self.flags_placed

        self.reset_board = True


    
    def set_board(self):
        """
        Create list of lists (list length = self.board_size)
        Underscore each list item.
        """
        grid = [["_" for col in range(self.board_size)] for row in range(self.board_size)]
    
        return grid
    

    def reset_gameplay(self, board):
        """
        reset board for validation errors
        """
        cls()
        print(figlet_format("GAME PLAY", font = "standard"))
        self.reset_board = False
        print(board)
        self.reset_board = True


    def add_mines(self):
        """
        Use import random to select random coordinates in the empty board_layout and place mines
        Check coordinated to ensure a mine is not being placed on another mine. 
        If it is bypass it and continue the while loop.
        """
        mines_placed = 0
        while mines_placed < self.no_mines:
            rand_row = random.randint(0, self.board_size - 1)
            rand_col = random.randint(0, self.board_size - 1)
            if self.board_layout[rand_row][rand_col] == "*":
                continue
            elif self.board_layout[rand_row][rand_col] == "_":
                self.board_layout[rand_row][rand_col] = "*"
                mines_placed += 1

    def add_values(self):
        """
        Loop through grid checking each cells neighboring cells. For each neighboring cell with a mine increase mines_detected variable by 1.
        This number will then be assigned to the centeral cell
        """
        # place max min to stop going outside of board perameters
        # https://stackoverflow.com/questions/5996881/how-to-limit-a-number-to-be-within-a-specified-range-python

        for row in range(self.board_size):
            for col in range(self.board_size):
                
                mines_detected = 0
                for r in range(max(0, row-1), min(self.board_size, row+2)):
                    for c in range(max(0, col-1), min(self.board_size, col+2)):
                        if r == row and c == col:
                            continue
                        elif self.board_layout[r][c] == "*":
                            mines_detected += 1

                if self.board_layout[row][col] != "*":
                    self.board_layout[row][col] = mines_detected
    
        for i in self.board_layout: # for testing
            print(i) # for testing
        print("\n.............\n")  # for testing


    def selected_space(self, x, y, f):
        """
        Add guess to self.guesses for a record of all guesses
        Check coordinates against final board
            - if mine return false
            - if > 0 return true
            - if 0 use a recursion loop to expand out until all conected 0 coordinates have been added to guesses list. This will
            never reach a mine as i will always encounter a surounding number first.
        Run through the recorded guesses and for each coordinate on the user board make it equal to the final board
       
        stop acceibility while f on cell
        """

        f = f.lower()

        if f == "y" or f == "yes" or f == "f" or f == "flag":
            print("YOU HAVE PLANTED A FLAG")
            self.user_board[x][y] = "F"
            self.space_edge_guesses(x, y)
            self.flags_placed += 1
            
            return True
        elif f == "leave_flag":
            return True

        elif f == "d":
            self.flags_placed -= 1
        

        self.guesses.append((x, y))
        

        if self.board_layout[x][y] == "*":
            for row in range(self.board_size):
                for col in range(self.board_size):
                    self.user_board[row][col] = str(self.board_layout[row][col])
                    self.space_edge_guesses(row, col)

            return False

        elif self.board_layout[x][y] > 0:
            self.user_board[x][y] = str(self.board_layout[x][y])
            self.space_edge_guesses(x, y)
            
            return True

        elif self.board_layout[x][y] == 0:

            self.user_board[x][y] = str(self.board_layout[x][y])
            self.space_edge_guesses(x, y)

            for r in range(max(0, x-1), min(self.board_size, x+2)):
                for c in range(max(0, y-1), min(self.board_size, y+2)):
                    if (r, c) in self.guesses:
                        continue
                    else:
                        self.selected_space(r, c, f)
            return True

    def space_edge_guesses(self, x, y):
        if y == 0:
            self.user_board[x][y] = "| " + str(self.user_board[x][y])
        elif y == self.board_size-1:
            self.user_board[x][y] = str(self.user_board[x][y]) + " |"


    def underscore(self):
        """
        Create dividers between cells dependant on the board_size
        """
        underscore_str = "|"
        for cell in range(self.board_size):
            underscore_str = underscore_str + "___|"
        
        return underscore_str


    def __str__(self):
        """
        Called when class is printed
        Create a user_board
        """

        if self.guesses == [] and self.flags_placed == 0 and self.reset_board:
            for list in self.user_board:
                list[0] = "| " + list[0]
                list[-1] = list[-1] + " |" 

        str_layout = [" | ".join(item) for item in self.user_board]
        grid_layout = f"\n{self.row_seperator}\n".join(str_layout)

        underscore = " "
        for us in range(self.board_size-1):
            underscore = underscore + "____"
        underscore = underscore + "___"

        return f"{underscore}\n{grid_layout}\n{self.row_seperator}"

start_game()