import random
import numpy as np
from termcolor import colored
from block import Block



class Board:
    def __init__(self, name, size):
        self.name = name
        self.width, self.height = size
        self.generateBlocks()
        self.regenerate()

    
    
    # Returns the block in the given position.
    def getBlock(self, pos):
        return self.state[pos[0]][pos[1]]



    # Returns the position of the given block.
    def getBlockPos(self, block):
        pos = np.where(self.state == block)
        return pos[0][0], pos[1][0]



    # Returns the next free space from the end of the board
    # while avoiding the given stack.
    def getFreeSpace(self, avoidStack):
        for col in range(self.width-1, -1, -1):
            if col != avoidStack:
                for row in range(0, self.height):
                    if self.state[col][row] == None:
                        return col, row
        return 0, 0



    # Returns the next free space at the top of a stack
    # from the end of the board while avoiding the given stacks.
    def getFreeSpaceAtTop(self, avoidStack1, avoidStack2):
        for col in range(self.width-1, -1, -1):
            if col != avoidStack1 and col != avoidStack2:
                if self.state[col][self.height-2] != None and self.state[col][self.height-1] == None:
                    return col, self.height-1
        return None



    # Returns the next block at the top of a stack
    # from the end of the board while avoiding the given stacks.
    def getBlockPosOnTop(self, avoidStack1, avoidStack2):
        for col in range(self.width-1, -1, -1):
            if col != avoidStack1 and col != avoidStack2:
                if self.state[col][self.height-1] != None:
                    return col, self.height-1
        return None



    # Checks whether the given position is free.
    def isPosFree(self, pos):
        return self.state[pos[0]][pos[1]] == None



    # Moves a block at one given position to another given position.
    def moveBlock(self, fromPos, toPos):
        self.state[toPos[0]][toPos[1]] = self.state[fromPos[0]][fromPos[1]]
        self.state[fromPos[0]][fromPos[1]] = None



    # Generates a new random state from the blocks.
    def regenerate(self):
        random.shuffle(self.blocks)
        self.state = np.array(self.blocks).reshape(self.width - 1, self.height)
        self.state = np.concatenate([self.state, [[None] * self.height]])
        
        

    # Generates a list of all the available blocks.
    def generateBlocks(self):
        blocks = []
        for col in range(0, self.width - 1):
            for row in range (0, self.height):
                blocks.append(Block(col, row))
        self.blocks = blocks


    # Prints the current state to the console.
    def display(self):
        print("\n")
        for row in range(self.height-1, -1, -1):
            rowText = " "
            for block in self.state[:, row]:
                if block != None:
                    rowText += block.toStr() + " "
                else:
                    rowText += " " + colored("  ", "white", "on_white") + "  "
            print(rowText)
        titleIndent = " " * int(self.width*5 / 2 - len(self.name) / 2)
        print(colored(" "+titleIndent + self.name + titleIndent, "black", "on_white"))