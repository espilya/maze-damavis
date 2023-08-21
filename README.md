# maze-damavis

## - Structure
- main.py 
  - Main file 
- controller.py
  - Controls the search algorithm and runs the simulation
- simulation.py
  - Simulates the maze 
- rod.py
  - Rod object


## - Usage
Add or select mazes inside `main.py` and execute the file.

### Input:
Add new input as list python
```
labyrinth_5 = [[".", ".", ".", ".", ".", "#", ".", ".", "."],
               [".", ".", ".", ".", ".", "#", ".", ".", "."],
               [".", ".", ".", ".", ".", "#", ".", ".", "."],
               [".", ".", ".", "#", "#", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."]]

```
### Example
```
labyrinth_3 = [[".", ".", "."],
               [".", ".", "."],
               [".", ".", "."]]
               
...

c = Controller(labyrinth_3)
print(c.search())              
```
```
$ python3 main.py
$ 3
```

