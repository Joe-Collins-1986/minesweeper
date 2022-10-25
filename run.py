"""
To use google sheets api will need to install 
- google-auth
- gspread
Instruction video (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/?child=first)

"""
import gspread
from google.oauth2.service_account import Credentials

import os #used to clear console
import random # used to assign random mine positions
import time # used to time game
import pyfiglet
from pyfiglet import figlet_format # used for aesthetically pleasing titles

import colorama #colorama tuorial - https://www.youtube.com/watch?v=u51Zjlnui4Y
from colorama import Fore, Style #Used to color warnings
colorama.init(autoreset=True) #reset color to default after use



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Minesweeper_scoreboard")




def cls(): # function to clear console for cross-platform: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')

def home_page_img():
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

                              WELCOME TO MINESWEEPER

................................................................................
................................................................................
        """)

def get_username():

    cls()
    name_page = True
    home_page_img()
    print("Welcome to Minesweeper.\n")
    while name_page:

            user_name = input("Please enter your name (maximum 10 characters)\n").lower()

            if len(user_name) > 0 and len(user_name) <= 10:
                while len(user_name) < 10:
                    user_name = user_name + " "
                name_page = False
                start_game(user_name)
            
            elif len(user_name) == 0:
                cls()
                home_page_img()
                print(f"{Fore.RED}{Style.BRIGHT}You have to enter something, how will we recognise you?\n")

            else:
                cls()
                home_page_img()
                print(f"{Fore.RED}{Style.BRIGHT}I'm sorry, the name you entered was too long ({len(user_name)} characters).\n")

def start_game(user_name):
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

    home_page = True
    home_page_img()
    while home_page:
  
        intro_nav = input("Enter 'p' to play,\nEnter 'r' to see the rules\nEnter 's' to see the scoreboard.\n\n").lower()
        cls()
        if intro_nav == "r":
            home_page = False
            rules(user_name)
        elif intro_nav == "p":
            home_page = False
            difficulty(user_name)
        elif intro_nav == "s":
            home_page = False
            scoreboard_selection(user_name)
        else:
            cls()
            home_page_img()
            print(f"{Fore.RED}{Style.BRIGHT}I'm sorry {intro_nav} is not a valid entry.\n")


def rules(user_name): 
    """ Present rules to user
    Set anykey to return to inital page
    """
    cls()
    print(figlet_format("RULES", font = "standard"))
    rules = True
    print("""Game Objective:\n\n
    **** type in the rules ***
    """)
    input("Enter anykey to reurn to the main page\n\n").lower()
    cls()

    start_game(user_name)


def scoreboard_selection(user_name):
    """
    select the scoreboard the user wishes to see
    """
    score_select_page = True
    print(figlet_format("SCOREBOARD SELECTION", font = "standard"))
    print("Each difficulty level has it's own scoreboard. Which scoreboard would you like to see?")
    while score_select_page:

        score_nav = input("Enter 'e' to view the easy scoreboard,\nEnter 'm' to view the medium scoreboard\nEnter 'h' to view the hard scoreboard.\n\n").lower()
        cls()
        if score_nav in ("e", "m", "h"):
            if score_nav == "e":
                score_nav = "easy"
            elif score_nav == "m":
                score_nav = "medium"
            else:
                score_nav = "hard"

            score_select_page = False
            return_scoreboard(score_nav, user_name)
        else:
            cls()
            print(figlet_format("SCOREBOARD SELECTION", font = "standard"))
            print(f"{Fore.RED}{Style.BRIGHT}I'm sorry {score_nav} is not a valid entry.\n")
                

def return_scoreboard(level, user_name):
    """
    retrive data from google sheets and present as a scorecard
    """
    scoreboard_data = SHEET.worksheet(level)
    all_scoreboard_data = scoreboard_data.get_all_values()

    all_scoreboard_data.sort(key=lambda x: int(x[3])) #https://stackoverflow.com/questions/36955553/sorting-list-of-lists-by-the-first-element-of-each-sub-list

    print(figlet_format(level.capitalize() + " - Top 5", font = "standard"))

    for i in range(5):
        all_scoreboard_data[i].pop(1)
        all_scoreboard_data[i].pop(2)
        str_all_scoreboard_data = "  |  ".join(all_scoreboard_data[i])
        print(f"{i+1}. {str_all_scoreboard_data}")

    input("\nHit any key to return to home page").lower()

    #REMINDER - when entering the name creat a function that adds spaces to short names taking them to 10 characters
    cls()
    start_game(user_name)



def difficulty(user_name):
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
    print("There are 3 difficulty settings in this game")
    print("easy - This will present you with a 5X5 grid and there will be 4 hidden mines")
    print("medium - This will present you with a 7X7 grid and there will be 8 hidden mines")
    print("easy - This will present you with a 9X9 grid and there will be 15 hidden mines\n")
    evaluating_dificulty = True
    while evaluating_dificulty:
        print("Please enter the difficulty you would like to play:")
        difficulty = input("Enter 'e' for easy,\nenter 'm' or medium,\nor enter 'h' for hard.\n").lower()
        if difficulty == "e":
            board_size = 5
            no_mines = 4
            evaluating_dificulty = False
        elif difficulty == "m":
            board_size = 7
            no_mines = 8
            evaluating_dificulty = False
        elif difficulty == "h":
            board_size = 9
            no_mines = 15
            evaluating_dificulty = False
        else:
            cls()
            print(figlet_format("DIFFICULTY", font = "standard"))
            print("There are 3 difficulty settings in this game")
            print("easy - This will present you with a 5X5 grid and there will be 5 hidden mines")
            print("medium - This will present you with a 7X7 grid and there will be 10 hidden mines")
            print("easy - This will present you with a 9X9 grid and there will be 20 hidden mines\n")
            print(f"{Fore.RED}{Style.BRIGHT}\nI'm sorry {difficulty} is not a valid entry.\n")
    cls()
    play(board_size, no_mines, user_name)



def play(board_size, no_mines, user_name):
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
    won = False
    start_time = (time.time())
    while game_active and not won:
        
        print(figlet_format("GAME PLAY", font = "standard"))
        print(board)
        
        xy_inputs = True
        while xy_inputs:
            try:
                x_axis, y_axis = map(int, input("\nEnter the row & column with a space seperating them (e.g. 3 5)\n").split())

                if (x_axis < 1 or x_axis > board_size) and (y_axis < 1 or y_axis > board_size):
                    raise Exception (f"x_axis ({x_axis}) and y_axis ({y_axis}) are not in range (1:{board_size})")
                elif x_axis < 1 or x_axis > board_size:
                    raise Exception (f"x_axis ({x_axis}) is not in range (1:{board_size})")
                elif y_axis < 1 or y_axis > board_size:
                    raise Exception (f"y_axis ({y_axis}) is not in range (1:{board_size})")

                x_axis -= 1
                y_axis -= 1
                
                if board.user_board[int(x_axis)][int(y_axis)] not in (str(x_axis +1)+" |  _", "_", "_  |", str(x_axis +1)+" |  F", "F", "F  |"):
                    raise Exception (f"You have already dug {x_axis +1} {y_axis +1}\n")


            except ValueError as e:
                board.reset_gameplay(board)
                print("\nInvalid Entry:\n - Do not type letters\n - Do not type special characters\n - Ensure you entered 2 coordinates")
                print(f"{Fore.RED}{Style.BRIGHT}\nIssue: {e}")
            except Exception as e:
                board.reset_gameplay(board)
                print(f"{Fore.RED}{Style.BRIGHT}\nIssue: {e}")
            else:
                xy_inputs = False

        if board.user_board[int(x_axis)][int(y_axis)] in (str(x_axis +1)+" |  F", "F", "F  |"):
    
            dig_input = True
            while dig_input:
                try:
                    print("\nThis position has a flag on it")
                    dig = input("Would you like to dig anyway? (Y/N)\n")    
                    if dig.lower() not in ("y", "yes", "d", "dig", "n", "no"):
                        raise Exception (f"That is not a valid entry.")
                except Exception as e:
                    print(f"{Fore.RED}{Style.BRIGHT}Issue: {e}")
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
                    print(x_axis+1, y_axis+1)
                    print(f"{Fore.RED}{Style.BRIGHT}\nIssue: {e}")
                else:
                    flag_input = False

        game_active = board.selected_space(x_axis, y_axis, flag)
        won = win(board, start_time, user_name)
        cls()

    if won:
        start_game(user_name)

    if not won:
        cls()
        print(figlet_format("GAME OVER", font = "standard"))
        print(board)
        print(f"\nOh dear!!! It appears that Row: {x_axis+1}, Column: {y_axis+1} had a mine")
        input("\nBetter luck next time, press any key to continue\n")

    start_game(user_name)


def win(board, start_time, user_name):
    """ Check if user has won
    Check if the users guesses have met the available spaces (board - bombs)
    If it has return True else return False
    """
    if len(board.guesses) == (board.board_size ** 2) - board.no_mines:
        level = ""
        if board.board_size == 9:
            level = "hard"
        elif board.board_size == 7:
            level = "medium"
        else:
            level = "easy"
        stop_time = (time.time())
        duration = stop_time - start_time

        mins = int(duration // 60)
        secs = round(duration % 60)
        cls()
        print(figlet_format("YOU WIN", font = "standard"))
        print(f"Well done. You completed {level} in {mins}mins : {secs}secs")
    
        scoreboard_new_data = [user_name, level, f"{mins}mins {secs}secs", int(duration)]
        update_scoreboard(scoreboard_new_data, level)
        input("Hit any key to play again")
        return True
    else:
        return False
     
def update_scoreboard(data, level):
    """
    Update scoreboard with name, score, time, and int time(to order)
    """
    print("\nupdating scoreboard...\n")
    scoreboard_colate_data = SHEET.worksheet(level)
    scoreboard_colate_data.append_row(data)
    print("Scoreboard updated successfully\n")


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

        self.user_board = self.set_board() # use to compare with board_layout on user guess
        self.row_seperator, self.side_lines = self.underscore()
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

        """
        for i in self.board_layout: # for testing
            print(i) # for testing
        print("\n.............\n")  # for testing
        """


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
            self.user_board[x][y] = str(x +1) + " |  " + str(self.user_board[x][y])
        elif y == self.board_size-1:
            self.user_board[x][y] = str(self.user_board[x][y]) + "  |"

    
    def underscore(self):
        """
        Create dividers between cells dependant on the board_size
        """
        side_lines_str = "  |"
        underscore_str = "  |"
        for cell in range(self.board_size):

            side_lines_str = side_lines_str + "     |"
            underscore_str = underscore_str + "_____|"
        
        return underscore_str, side_lines_str


    def __str__(self):
        """
        Called when class is printed
        Create a user_board
        """

        if self.guesses == [] and self.flags_placed == 0 and self.reset_board:
            row = 1
            for list in self.user_board:
                list[0] = str(row) + " |  " + list[0]
                list[-1] = list[-1] + "  |"
                row += 1

        str_layout = ["  |  ".join(item) for item in self.user_board]
        grid_layout = f"\n{self.row_seperator}\n{self.side_lines}\n".join(str_layout)

        """Creat for top of grid"""
        column_no = "     1   "
        top_of_grid = "   _____"
        for i in range(self.board_size-1):
            top_of_grid = top_of_grid + "______"
            column_no = column_no + "  " + str(i+2) + "   "
        

        return f"{column_no}\n{top_of_grid}\n{self.side_lines}\n{grid_layout}\n{self.row_seperator}"

get_username()
#start_game()