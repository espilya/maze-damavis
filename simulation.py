from rod import *
import copy

"""
Las coordenadas estan al revez ya que la entrada viene por [y][x], para no complicar la solucion lo deje tal cual
"""

# Variables for representation
WALL = "#"
EMPTY = "."
MY_PATH = ":"
ROD = "r"


class Simulation:
    """
    Simulation of the maze.
    Movements, walls, prints ...
    """

    """
         0  1  2  3
         _  _  _  _
    0 |  :  :  :  . |
    1 |  r  r  r  . |
    2 |  .  .  .  . |
    3 |  #  .  #  . |
         _  _  _  _

    """

    def __init__(self, lab):
        self.lab_size_y = len(lab)
        self.lab_size_x = len(lab[0])
        # self.lab = [[0 if item == '.' else 1 for item in x] for x in lab]
        self.lab = lab
        self.rod = Rod()
        self.update_rod()
        self.last_actions = ["START"]

        self.last_pos = []

    def print(self):
        """
        Print the maze
        """
        for y in self.lab:
            for x in y:
                print(x, end=" ")
            print()
        print()

    def update_rod(self, old_positions=None, back=False, last_pos_rotate=None):
        """
        Update our Rod on the maze
        """
        if back:
            self.lab = last_pos_rotate
        else:
            if old_positions is not None:
                for i in old_positions:
                    y, x = i
                    self.lab[y][x] = MY_PATH
            for i in self.rod.positions:
                y, x = i
                self.lab[y][x] = ROD

    def rotate_rod(self):
        """
        Check action and rotate our rod
        """
        rod_center = self.rod.positions[1]
        y, x = rod_center

        # check for possibility to rotate
        ok = True
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                ok = ok and self.check_action(y + i, x + j)

        # if at least one cell position is invalid then cancel rotation
        if ok:
            old_position = self.rod.positions.copy()
            self.last_pos.append(copy.deepcopy(self.lab))
            self.rod.rotate()
            self.update_rod(old_position)
            self.last_actions.append("ROTATE")
            return True
        else:
            return False

    def move_rod(self, move):
        """
        Check action and move our rod
        """
        new_rod_pos = self.rod.positions.copy()

        # iterate through rod cells and move them temporarily (new_rod_pos) to new position
        for i in range(len(self.rod.positions)):
            y, x = self.rod.positions[i]

            # move and check
            if move == "UP":
                y -= 1
            elif move == "RIGHT":
                x += 1
            elif move == "DOWN":
                y += 1
            elif move == "LEFT":
                x -= 1

            # if at least one cell position is invalid then cancel action
            if not self.check_action(y, x):
                return False
            else:
                new_rod_pos[i] = (y, x)

        # Check if the new position was already visited
        previous_pos = 0
        for i in range(len(new_rod_pos)):
            if self.lab[new_rod_pos[i][0]][new_rod_pos[i][1]] in [MY_PATH, ROD]:
                previous_pos += 1
        if previous_pos == 3:
            return False

        # if everything is OK then move to new position
        old_position = self.rod.positions.copy()
        self.last_pos.append(copy.deepcopy(self.lab))
        self.rod.move(move)
        self.update_rod(old_position)
        self.last_actions.append(move)
        return True

    def move_rod_back(self):
        """
        Backtrack the rod. Move the rod to its previous position
        """
        old_position = self.rod.positions.copy()

        action = self.last_actions.pop()
        if action == "ROTATE":
            self.rod.rotate()
            self.update_rod(old_position, True, self.last_pos.pop())
        else:
            if action == "DOWN":
                self.rod.move("UP")
            elif action == "UP":
                self.rod.move("DOWN")
            elif action == "RIGHT":
                self.rod.move("LEFT")
            elif action == "LEFT":
                self.rod.move("RIGHT")
            self.update_rod(old_position, True, self.last_pos.pop())

    def check_action(self, y, x):
        """
        Used to check if the legality of the movement (outside the maze and inside the walls)
        """
        correct_action = (0 <= y < self.lab_size_y) and (0 <= x < self.lab_size_x)
        return correct_action and self.lab[y][x] != WALL

    def check_end(self):
        """
        Check if it is the end of the maze
        """
        for i in self.rod.positions:
            if i[0] == self.lab_size_y - 1 and i[1] == self.lab_size_x - 1:
                return True
        return False
