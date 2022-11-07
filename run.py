import gspread  # read and update google sheets
# allow API link to google sheets
from google.oauth2.service_account import Credentials

import game_layout  # used to access class - other sheet
from format import *  # used to clear screen - other sheet

import time  # used to time game
import math  # round down seconds
import pyfiglet
from pyfiglet import figlet_format  # for aesthetically pleasing titles

import colorama
from colorama import Fore, Style  # Used to color warnings
colorama.init(autoreset=True)  # reset color to default after use

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

try:
    SHEET = GSPREAD_CLIENT.open("Minesweeper_scoreboard")
except BaseException:
    cls()
    print(
        f"{Fore.RED}{Style.BRIGHT}We seem to be having an issue "
        "accessing google sheets.\n"
        "You will be able to play the game but your score won't be recorded.")
    input("\nHit 'Enter' to continue\n")
    cls()


def home_page_img():
    """
    Present home page image
    """
    print(figlet_format("    MINESWEEPER", font="standard"))
    print("""
                                    _________
                █                 /  _______  \\                 █
             █  █  █             /  /       \\  \\             █  █  █
              █████             /  / warning \\  \\             █████
           ██ █████ ██         /  /   mines   \\  \\         ██ █████ ██
              █████           /  /    ahead!   \\  \\           █████
             █  █  █         /  /_______________\\  \\         █  █  █
                █            \\_____________________/            █

                              WELCOME TO MINESWEEPER

................................................................................
................................................................................
        """)


def get_username():
    """
    Run in a while loop
    Take user input and stores as username
    Add spacing to the end of name to present consistantly in scoreboard
    Validate user input
    """
    cls()
    name_page = True
    home_page_img()
    intro_msg = ("Welcome Sergeant, thank you for coming. We have a mission "
                 "of the utmost urgency.\n\n"
                 "The enemy has littered the following field with mines. We "
                 "need your expertise\nto excavate the area and identify "
                 "where the mines are to allow us to safely run\nour supply "
                 "lines across.\n\n"
                 "Good luck, we are all behind you... a long, long way "
                 "behind you.\n\n")

    print(intro_msg)
    while name_page:
        user_name = input(
            "Please enter your name (maximum 10 characters)\n").strip().lower()

        if len(user_name) > 0 and len(user_name) <= 10:
            while len(user_name) < 10:
                user_name = user_name + " "
            name_page = False
            start_game(user_name)

        elif len(user_name) == 0:
            cls()
            home_page_img()
            print(intro_msg)
            print(
                f"{Fore.RED}{Style.BRIGHT}You have to enter something, "
                "how will we recognise you?\n")

        else:
            cls()
            home_page_img()
            print(intro_msg)
            print(
                f"{Fore.RED}{Style.BRIGHT}I'm sorry, the name you "
                f"entered was too long ('{len(user_name)}' characters).\n")


def start_game(user_name):
    """
    Offer play, rules or score through user input
        - call rules function (r)
        - call difficulty function (p)
        - call scoreboard function (s)
        - error with feedback for invalid enteries
    Call difficulty function to define board_size and no_mines variables
    Function to recycle on play function completion
    """
    cls()
    home_page = True
    home_page_img()
    while home_page:
        print("                 Enter the following keys to navigate "
              "the game:\n")
        intro_nav = input(
            "  'P' to Play                    "
            "'R' for Rules                 "
            "'S' for Scores\n\n").strip().lower()
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
            print(
                f"{Fore.RED}{Style.BRIGHT}I'm sorry "
                f"'{intro_nav}' is not a valid entry.\n")


def rules(user_name):
    """
    Present rules to user
    Set 'Enter' to return to start_game function
    """
    print(figlet_format("                      RULES", font="standard"))
    print("\033[4m" + "Instructional Video:\n")
    print("https://www.youtube.com/watch?v=dvvrOeITzG8\n\n")
    print("\033[4m" + "Mission Objective:")
    print("""
The objective of Minesweeper is to select every cell on the presented grid
without selecting one that is hiding a mine.\n\n""")

    input("Hit 'Enter' to move onto the instructions\n")
    cls()
    print(figlet_format("                      RULES", font="standard"))
    print("\033[4m" + "Instructions:")
    print("""
1. First select the difficulty you wish to play. Harder settings will have a
   larger grid and more mines.\n
2. You will then be presented with an empty grid.\n
3. Select two coordinates (row, column) on the board.\n
    - Once selected the grid cell will either display a number or a mine.\n
    - If the cell has a mine, you lose.\n
    - If the cell has a number, it will inform you of surrounding mines to
      help you make educated decisions on your next guess.\n
    - If for example the cell presents the number 2 it means there are two
      mines next to the numbered cell.\n
    - If there are no mines next to the selected cell then the number will
      present as a 0 and it will open up the cells next to it
      until it reaches cells that are next to a mine.\n
4. If the numbers indicate that a cell has a mine it is good practice to mark
   this with a flag to stop yourself forgetting later.\n
    - You will be asked each time you select a cell if you wish to plant a
      flag or dig.\n
    - If a flag already exists on the cell that you select you will be asked
      if you want to dig the spot or leave the flag.\n
5. If you uncover every available cell without selecting those with mines
   you win.\n
6. And the most important step. Have fun...happy mining
""")
    input("\nHit 'Enter' to return to home page\n")

    start_game(user_name)


def scoreboard_selection(user_name):
    """
    Select the scoreboard the user wishes to see
    Validate entry
    Call return_scorecard function passing validated input
    """
    score_select_page = True
    print(figlet_format("         SCOREBOARD", font="standard"))
    print(figlet_format("              SELECTION", font="standard"))
    print("                    Which scoreboard would you like to see?\n")
    while score_select_page:
        score_nav = input(
            "  'E' for Easy                   "
            "'M' for Medium                 "
            "'H' for Hard\n\n").strip().lower()
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
            print(figlet_format("         SCOREBOARD", font="standard"))
            print(figlet_format("              SELECTION", font="standard"))
            print(
                f"{Fore.RED}{Style.BRIGHT}I'm sorry "
                f"'{score_nav}' is not a valid entry.\n")


def return_scoreboard(level, user_name):
    """
    Retrive data from google sheets and present as a scorecard
    Sort order using recorded time at index 3 of each list in sheets list
    Drop unessecary info (difficulty and time in seconds)
    Set 'Enter' to return to start_game function
    """
    try:
        scoreboard_data = SHEET.worksheet(level)
        all_scoreboard_data = scoreboard_data.get_all_values()

        # https://stackoverflow.com/questions/36955553/sorting-list-of-lists-by-the-first-element-of-each-sub-list
        all_scoreboard_data.sort(key=lambda x: int(x[3]))

        print(figlet_format(level.capitalize() + " - Top 5", font="standard"))

        for i in range(5):
            all_scoreboard_data[i].pop(1)
            all_scoreboard_data[i].pop(2)
            str_all_scoreboard_data = "  |  ".join(all_scoreboard_data[i])
            print(f"{i+1}. {str_all_scoreboard_data}")
    except BaseException:
        print(
            f"{Fore.RED}{Style.BRIGHT}We seem to be having an issue "
            "accessing the scoreboard at this time.\n"
            "Please try again later after reloading the game.")

    input("\n\nHit 'Enter' to return to home page\n")

    start_game(user_name)


def difficulty(user_name):
    """
    Define difficulty of the game
    Explain difficulty settings
    Take user input to set size of board and number of mines
    Validate entry
    Call play function
    """
    print(figlet_format("            DIFFICULTY", font="standard"))
    print("There are 3 difficulty settings in this game:\n")
    print(" - Easy - This will present you with a 5X5 grid and 4 mines.")
    print(" - Medium - This will present you with a 7X7 grid and 8 mines.")
    print(" - Hard - This will present you with a 9X9 grid and 15 mines.\n")
    evaluating_dificulty = True
    while evaluating_dificulty:
        print("              Please enter the difficulty you would "
              "like to play:\n")

        difficulty = input(
            "  'E' for Easy                 "
            "'M' for Medium                    "
            "'H' for Hard\n\n").strip().lower()
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
            print(figlet_format("            DIFFICULTY", font="standard"))
            print("There are 3 difficulty settings in this game:\n")
            print(" - Easy - This will present you with a 5X5 grid "
                  "and 4 mines.")
            print(" - Medium - This will present you with a 7X7 grid "
                  "and 8 mines.")
            print(" - Hard - This will present you with a 9X9 grid and "
                  "15 mines.\n")
            print(
                f"{Fore.RED}{Style.BRIGHT}\nI'm sorry '{difficulty}' "
                "is not a valid entry.\n")
    cls()
    play(board_size, no_mines, user_name)


def play(board_size, no_mines, user_name):
    """
    Assign GameLayout class to the variable 'board' using board size and
    number of mines:
        - This will define the board, mine placment and cell values
    Set the game to active and won to False to run a while loop until game
    is won or lost.
    Initialte start time of game to be used in scoreboard
    Run while loop for game when not lost/won:
        - Present board
        - Take and validate user guesses and asign to x y axis variables
        (Validation dependant on if cell is available, has flag or has
        been dug)
        - Pass x, y and flag inputs to the selected_space function in
        the GameLayout class to update
        board and define if game still active and break out of while
        loop if not
        - Run win function to see if game won. If it is function will
        print congratulations and break out of while loop if it is.
    If won status true call start_game function
    If won status false print game over info and set input 'Enter' to
    call start_game function
    """
    board = game_layout.GameLayout(board_size, no_mines)
    game_active = True
    won = False
    start_time = (time.time())
    while game_active and not won:

        print(figlet_format("           GAME PLAY", font="standard"))
        print(board)

        """
        While loop to validate coodinate inputs to check the numbers
        are in range, the correct number of int values are entered.
        """
        xy_inputs = True
        while xy_inputs:
            try:
                x_axis, y_axis = map(int, input(
                    "\nEnter the row & column with a space seperating "
                    "them (e.g. 3 5)\n").split())

                if (x_axis < 1 or x_axis > board_size) and (
                        y_axis < 1 or y_axis > board_size):
                    raise Exception(
                        f"x_axis ({x_axis}) and y_axis ({y_axis}) are "
                        f"not in range (1:{board_size})")
                elif x_axis < 1 or x_axis > board_size:
                    raise Exception(
                        f"x_axis ({x_axis}) is not in range (1:{board_size})")
                elif y_axis < 1 or y_axis > board_size:
                    raise Exception(
                        f"y_axis ({y_axis}) is not in range (1:{board_size})")

                x_indices = x_axis - 1
                y_indices = y_axis - 1

                if board.user_board[int(x_indices)][int(y_indices)] not in (
                        f"  {str(x_axis)}  |  _", "_", "_  |",
                        f"  {str(x_axis)}  |  F", "F", "F  |"):
                    raise Exception(
                        f"You have already dug {x_axis} {y_axis}\n")

            except ValueError as e:
                board.reset_gameplay(board)
                print(f"{Fore.RED}{Style.BRIGHT}\nInvalid Entry:\n"
                      " - Do not type letters\n"
                      " - Do not type special characters\n"
                      " - Ensure you entered 2 coordinates")
            except Exception as e:
                board.reset_gameplay(board)
                print(f"{Fore.RED}{Style.BRIGHT}\nIssue: {e}")
            else:
                xy_inputs = False

        """
        if statement looking for a flag on the cell selcted which will
        active one of 2 while loops:
            1. validation if a flag exists on the selected cell
            2. If the cell is empty
        """
        if board.user_board[int(x_indices)][int(y_indices)] in (
                f"  {str(x_axis)}  |  F", "F", "F  |"):
            dig_input = True
            while dig_input:
                try:
                    print(
                        f"\nThis position ({x_axis}, "
                        f"{y_axis}) has a flag on it")
                    dig = input("Would you like to dig anyway? "
                                "(Y/N)\n").strip()
                    if dig.lower() not in ("y", "yes", "d", "dig", "n", "no"):
                        raise Exception("That is not a valid dig entry.")
                except Exception as e:
                    board.reset_gameplay(board)
                    print(f"{Fore.RED}{Style.BRIGHT}\nIssue: {e}")
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
                    flag = input(
                        "\nWould you like to place a flag on this "
                        "location (Y/N)\n").strip()
                    if flag.lower() not in ("y", "yes", "f",
                                            "flag", "n", "no"):
                        raise Exception(f"That is not a valid flag entry.")
                except Exception as e:
                    board.reset_gameplay(board)
                    print(
                        "\nEnter the row & column with a space seperating "
                        "them (e.g. 3 5)")
                    print(x_axis, y_axis)
                    print(f"{Fore.RED}{Style.BRIGHT}\nIssue: {e}")
                else:
                    flag_input = False

        game_active = board.selected_space(x_indices, y_indices, flag)
        won = win(board, start_time, user_name)
        cls()

    if won:
        start_game(user_name)

    if not won:
        cls()
        print(figlet_format("           GAME OVER", font="standard"))
        print(board)
        print(
            f"\n\nOh dear!!! It appears that Row: {x_axis}, "
            f"Column: {y_axis} had a mine")
        input("\nBetter luck next time, hit 'Enter' to play again\n")

    start_game(user_name)


def win(board, start_time, user_name):
    """
    Check if the users guesses have met the available spaces (board - bombs)
        - If true take stop time and take deference from start time
        - Print Congratulation info and time taken
        - Call update scoreboard function
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
        secs = math.floor(duration % 60)
        cls()
        print(figlet_format("                YOU WIN", font="standard"))
        print(
            f"\nWell done.\n\nYou completed {level} "
            f"in {mins}mins : {secs}secs")

        scoreboard_new_data = [
            user_name,
            level,
            f"{mins}mins {secs}secs",
            int(duration)]
        update_scoreboard(scoreboard_new_data, level)
        input("Hit 'Enter' to play again\n")
        return True
    else:
        return False


def update_scoreboard(data, level):
    """
    Update scoreboard with name, score, time, and int time(to order)
    """
    print("\n............................................."
          "...................................\n")
    try:
        print("\nUpdating scoreboard...\n")
        scoreboard_colate_data = SHEET.worksheet(level)
        scoreboard_colate_data.append_row(data)
        print("Scoreboard updated successfully\n")
    except BaseException:
        print(
            f"{Fore.RED}{Style.BRIGHT}We have been unable to "
            "update the scoreboard due to connectivity issues.\n"
            "We appologise for this inconvenience.")
    print("\n............................................."
          "...................................\n")


get_username()
