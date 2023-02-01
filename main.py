import argparse, time, datetime
from termcolor import colored
from game import Game


BOARD_WIDTH = 4
BOARD_HEIGHT = 3
HUMAN_MOVE_SPEED = 0.6
MOVE_SPEED = HUMAN_MOVE_SPEED



parser = argparse.ArgumentParser()
parser.add_argument('--width', dest='width', type=int, help='number of piles (4-16)')
parser.add_argument('--height', dest='height', type=int, help='number of blocks in a pile (3-99)')
parser.add_argument('--speed', dest='speed', type=float, help='seconds between each move (0.0+)')
args = parser.parse_args()



if __name__ == "__main__":
    useDefaultSettings = False

    if args.width == None or args.width < 4 or args.width > 16 \
            or args.height == None or args.height < 3 or args.height > 99 \
            or args.speed == None or args.speed < 0:
        useDefaultSettings = True
    
    if useDefaultSettings:
        parser.print_help()
        print(f"\nDefaulting to 4x3 at {MOVE_SPEED}s/move. Starting in 5s.")
        time.sleep(5)
    else:
        BOARD_WIDTH = args.width
        BOARD_HEIGHT = args.height
        MOVE_SPEED = args.speed

    game = Game((BOARD_WIDTH, BOARD_HEIGHT), MOVE_SPEED)
    game.play()

    humanSeconds = game.moveCount * HUMAN_MOVE_SPEED
    humanTime = datetime.timedelta(seconds=humanSeconds) 
    print(f"\n\nThis would take a human about {humanTime}.")