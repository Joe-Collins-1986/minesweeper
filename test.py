

print("\U0001F4A5")
print("\U0001F6A9")


#colorama tuorial - https://www.youtube.com/watch?v=u51Zjlnui4Y

import colorama #colorama tuorial - https://www.youtube.com/watch?v=u51Zjlnui4Y
from colorama import Fore, Style #Used to color warnings
colorama.init(autoreset=True) #reset color to default after use

print(f"{Fore.RED}Some text")
print("normal text")

