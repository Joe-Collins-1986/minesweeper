import os  # used to clear screen - other sheet


def cls():
    """
    Clear console for cross-platform:
    https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


intro_img = ("""
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

rules_txt = ("""
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
