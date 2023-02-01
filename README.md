# Number Rumba Solver
Creates a virtual game of Number Rumba and solves it in the console.

Number Rumba is an old game where the aim is to recreate the board on the card before your opponent does. But you're only allowed to move one block at a time.
![screenshot](https://raw.githubusercontent.com/JakesMD/Number-Rumba-Solver/main/number_rumba.jpg)

## Usage
To run with the default settings and the traditional board size:
```
python main.py
```
![screenshot](https://raw.githubusercontent.com/JakesMD/Number-Rumba-Solver/main/screenshot-4x3.png)

To run with a custom board size and speed:

```
python main.py --width 16 --height 15 --speed 0.01
```
```
  --width WIDTH    number of stacks (4-16)
  --height HEIGHT  number of blocks in a stack (3-99)
  --speed SPEED    seconds between each move (0.0+)
```

![screenshot](https://raw.githubusercontent.com/JakesMD/Number-Rumba-Solver/main/screenshot-16x15.png)