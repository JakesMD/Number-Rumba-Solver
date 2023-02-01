import os, time, datetime
from board import Board
from termcolor import colored



class Game:
    def __init__(self, boardSize, moveSpeed):
        self.boardWidth, self.boardHeight = boardSize
        self.moveSpeed = moveSpeed
        self.targetBoard = Board("TARGET", boardSize)
        self.playerBoard = Board("PLAYER", boardSize)



    # Resets the game ready to play
    def reset(self):
        self.playerBoard.state = self.targetBoard.state
        self.targetBoard.regenerate()
        self.targetPos = 0, 0
        self.currentBlockPos = 0, 0
        self.moveCount = 0
        self.startTime = time.perf_counter()
        self.display()



    # Performs the move in the console.
    def move(self):
        time.sleep(self.moveSpeed)
        self.moveCount += 1
        self.display()



    # Runs the algorithm that solves the puzzle.
    def play(self):
        self.reset()

        # Loop through all the blocks in the target board from bottom left to top right.
        for col in range(0, self.boardWidth - 1):
            for row in range(0, self.boardHeight):
                self.targetPos = col, row
                targetBlock = self.targetBoard.getBlock(self.targetPos)

                # 1. Locate the position of the target block on the player's board.
                self.currentBlockPos = self.playerBoard.getBlockPos(targetBlock)

                # 2. Check that the current block is not already at the target position.
                if self.currentBlockPos != self.targetPos:

                    # 3. Move all the blocks above the current block to free locations
                    #    on other stacks
                    self.freeUpCurrentBlock()

                    # 4. Check that the target position is not already free.
                    if self.playerBoard.isPosFree(self.targetPos) == False:

                        # 5. Make space for and put the current block at the top of a stack
                        #    (not the target stack)
                        self.storeCurrentBlock()

                        # 6. Move all the blocks at and above the target position 
                        #    to other free locations on different stacks.
                        self.freeUpTargetPos()

                    # 7. Move the current block to the target position.
                    self.moveCurrentBlockToTargetPos()

        # In some cases a single block is left at the end of the board.
        # Move this block to its target location.
        self.currentBlockPos = self.boardWidth - 1, 0
        leftOverBlock = self.playerBoard.getBlock(self.currentBlockPos)
        if (leftOverBlock != None):
            self.targetPos = self.targetBoard.getBlockPos(leftOverBlock)
            self.moveCurrentBlockToTargetPos()



    # Moves all the blocks above the current block
    # to free locations on other stacks.
    def freeUpCurrentBlock(self):

        # Loop through all the positions above the current block from top to bottom.
        for x in range(self.boardHeight - 1, self.currentBlockPos[1], -1):

            # Check that the position is not already free.
            if self.playerBoard.getBlock((self.currentBlockPos[0], x)) != None:

                # Find a free space on another stack and move the block in this position there.
                freeSpace = self.playerBoard.getFreeSpace(self.currentBlockPos[0])
                self.playerBoard.moveBlock([self.currentBlockPos[0], x], freeSpace)
                self.move()



    # Moves all the blocks at and above the target position
    # to free locations on other stacks.
    def freeUpTargetPos(self):

        # Loop through all the positions above and at
        # the target position from top to bottom.
        for x in range(self.boardHeight - 1, self.targetPos[1] - 1, -1):

            # Check that the position is not already free.
            if self.playerBoard.getBlock((self.targetPos[0], x)) != None:

                # Find a free space on another stack and move the block in this position there.
                freeSpace = self.playerBoard.getFreeSpace(self.targetPos[0])
                self.playerBoard.moveBlock([self.targetPos[0], x], freeSpace)
                self.move()



    # Free up the top of another stack that's not the target stack
    # and move the current block there.
    def storeCurrentBlock(self):

        # Check that the current block is not already at the top of a stack
        # that isn't the target stack.
        if self.currentBlockPos[1] != self.boardHeight - 1 or self.currentBlockPos[0] == self.targetPos[0]:

            # Find a free space at the top of another stack that isn't the target stack.
            freeSpaceAtTop = self.playerBoard.getFreeSpaceAtTop(self.currentBlockPos[0], self.targetPos[0])

            # Check that no space was found.
            if freeSpaceAtTop == None:

                # Find a block at the top of a different stack that isn't the target stack.
                blockPosOnTop = self.playerBoard.getBlockPosOnTop(self.currentBlockPos[0], self.targetPos[0])

                # Find a free space for the block to go that's not in the current stack and move it there.
                freeSpace = self.playerBoard.getFreeSpace(self.currentBlockPos[0])
                self.playerBoard.moveBlock(blockPosOnTop, freeSpace)
                self.move()

                # Set the free space to be where the block was.
                freeSpaceAtTop = blockPosOnTop

            # Move the current block to the free space.
            self.playerBoard.moveBlock(self.currentBlockPos, freeSpaceAtTop)
            self.currentBlockPos = freeSpaceAtTop
            self.move()



    # Moves the current block to the target position.
    def moveCurrentBlockToTargetPos(self):
        self.playerBoard.moveBlock(self.currentBlockPos, self.targetPos)
        self.move()



    # Prints the current state of the game to the console.
    def display(self):
        elaspedTime = datetime.timedelta(seconds=(time.perf_counter()-self.startTime))

        infoText = colored(f" MOVE {self.moveCount} ", "white", "on_green")
        infoText += colored(f" TARGET {self.targetPos} ", "white", "on_red")
        infoText += colored(f" ELAPSED {elaspedTime} ", "white", "on_blue")
        infoText += colored(f" SIZE {self.boardWidth}x{self.boardHeight} ", "white", "on_magenta")
        infoText += colored(f" SPEED {self.moveSpeed}s/move ", "white", "on_cyan")

        os.system('cls' if os.name == 'nt' else 'clear')
        print(infoText)
        self.targetBoard.display()
        self.playerBoard.display()