from termcolor import colored

# All the possible colors of termcolor excluding black.
COLORS = ["yellow", "magenta", "cyan", "green", "red", "blue", "white", "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan"]

# Represents the physical piece with a unique color and number combination.
class Block:
    def __init__(self, colorIndex, number):
        self.color = COLORS[colorIndex]
        self.number = number

    # The block's unique name to make it easy to compare blocks.
    def name(self):
        return f"{self.color}{self.number}"
    
    # The String to print to the console.
    def toStr(self):
        return colored(f" {(self.number+1):02} ", "black", f"on_{self.color}")