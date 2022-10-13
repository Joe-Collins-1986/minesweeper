"""
To use google sheets api will need to install 
- google-auth
- gspread
Instruction video (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/?child=first)
"""


def start_game():
    """ Opens the game
    Introduce game
    Offer play or rules through user input
        - show rules (r)
            - return with anykey
        - call difficulty function (p)
        - error with feedback for invalid enteries
    Call difficulty function to define board_size and no_mines variables
    Call play function with defined valriables as arguments
    Function to recycle on play function completion
    """
    pass


def difficulty():
    """ Define difficulty of the game
    Explain difficulty settings
    Take user input
        - easy(e) will return (5, 7) 
        - medium(m) will return (10, 9) 
        - hard(h) will return (20, 12) 
        - error with feedback for invalid enteries
    """
    pass

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
    pass

def win(board):
    """ Check if user has won
    Check if the users guesses have met the available spaces (board - bombs)
    If it has return True else return False
    """
    pass

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

        # self.empty_board = self.set_board()
        # self.mines_board = self.add_mines()
        # self.final_board = self.add_values()

        self.guesses = []
    
    def set_board(self):
        """
        Create list of lists (list length = self.board_size)
        Underscore each list item.
        """
        pass

    def add_mines(self):
        """
        Use import random to run through empty board (nested for loop) to place mines randomly
        In loop check that the mine is not being placed on another mine. If it is bypass it and continue the for loop.
        """
        pass

    def add_values(self):
        """
        Loop through grid checking each cells neighboring cells. For each neighboring cell with a mine increase mines_detected variable by 1.
        This number will then be assigned to the centeral cell
        """
        mines_detected = 0
        pass

    def selected_space(self):
        """
        Add guess to self.guesses for a record of all guesses
        Check coordinates against final board
            - if mine return false
            - if > 0 return true
            - if 0 use a recursion loop to expand out until all conected 0 coordinates have been added to guesses list. This will
            never reach a mine as i will always encounter a surounding number first.
        """
        pass

    def __str__(self):
        """
        Called when class is printed
        Create a user_board
        Run through the recorded guesses and for each coordinate on the user board make it equal to the final board
        """
        pass


