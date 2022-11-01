import random # used to assign random mine positions
import pyfiglet
from pyfiglet import figlet_format # used for aesthetically pleasing titles
from format import * #used for clear function


class GameLayout:
    """
    This class will be used to define the levels grid and check user inputs against assigned mines and cell value and return the board to the user.
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
        Create list of lists (list length = self.board_size).
        Underscore each list item.
        """
        grid = [["_" for col in range(self.board_size)] for row in range(self.board_size)]
    
        return grid
    

    def reset_gameplay(self, board):
        """
        Reset board function to address validation errors made before any guesses or flags placed.
        Set reset as a condition for __str__ function to only run if True
        Then turn reset_board to false before calling string so that if called 
        and no guesses and no flags the board format won't be alterd. 
        """
        cls()
        print(figlet_format("           GAME PLAY", font = "standard"))
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
        This number will then be assigned to the centeral cell if it is not a mine.
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


    def selected_space(self, x, y, f):
        """
        Add guess to self.guesses for a record of all guesses
        Check coordinates against final board
            - if mine return false
            - if > 0 return true
            - if 0 use a recursion loop to expand out until all conected 0 coordinates have been added to guesses list. This will
            never reach a mine as i will always encounter a surounding number first.
        Run through the recorded guesses and for each coordinate on the user board make it equal to the final board
       
        Stop acceibility while f on cell
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
        """
        Replace first and last dividers when cells on first and last columns are guessed.
        """
        if y == 0:
            self.user_board[x][y] = f"  {str(x +1)}  |  {str(self.user_board[x][y])}"
        elif y == self.board_size-1:
            self.user_board[x][y] = str(self.user_board[x][y]) + "  |"

    
    def underscore(self):
        """
        Create dividers between cells dependant on the board_size.
        """
        side_lines_str = "     |"
        underscore_str = "     |"
        for cell in range(self.board_size):

            side_lines_str = side_lines_str + "     |"
            underscore_str = underscore_str + "_____|"
        
        return underscore_str, side_lines_str


    def __str__(self):
        """
        Called when class is printed.
        Present a string version of the user_board.
        """
        if self.guesses == [] and self.flags_placed == 0 and self.reset_board:
            row = 1
            for list in self.user_board:
                list[0] = f"  {str(row)}  |  {list[0]}"
                list[-1] = list[-1] + "  |"
                row += 1

        str_layout = ["  |  ".join(item) for item in self.user_board]
        grid_layout = f"\n{self.row_seperator}\n{self.side_lines}\n".join(str_layout)

        """
        Create the top of the grid and column numbers.
        """
        column_no = "        1   "
        top_of_grid = "      _____"
        for i in range(self.board_size-1):
            top_of_grid = top_of_grid + "______"
            column_no = column_no + "  " + str(i+2) + "   "
        

        return f"{column_no}\n{top_of_grid}\n{self.side_lines}\n{grid_layout}\n{self.row_seperator}"