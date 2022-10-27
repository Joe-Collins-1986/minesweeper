import os # used to clear screen - other sheet


def cls(): 
    """
    Clear console for cross-platform: 
    https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system('cls' if os.name=='nt' else 'clear')

