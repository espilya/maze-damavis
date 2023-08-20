from rod import *


class Simulation:
    """
         _  _  _  _
    3 |  r  r  r  . |
    2 |  .  .  .  . |
    1 |  .  .  .  . |
    0 |  #  .  #  . |
         _  _  _  _
         0  1  2  3
    """

    def __init__(self, lab):
        self.lab_size_y = len(lab)
        self.lab_size_x = len(lab[0])
        self.lab = [[0 if item == '.' else 1 for item in x] for x in lab]
        self.rod = Rod()
        self.update_rod()

    def print(self):
        for y in self.lab:
            for x in y:
                print(x, end=" ")
            print()
        print()

    def update_rod(self, old_positions=None):
        if old_positions is not None:
            for i in old_positions:
                y, x = i
                self.lab[y][x] = 0

        for i in self.rod.positions:
            y, x = i
            self.lab[y][x] = "r"

    def rotate_rod(self):
        rod_center = self.rod.positions[1]
        y, x = rod_center

        # check for possibility to rotate
        ok = True
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                ok &= self.check_action(y + i, x + j)

        if ok:
            old_position = self.rod.positions.copy()
            self.rod.rotate()
            self.update_rod(old_position)
            return True
        else:
            return False

    def move_rod(self, move):
        new_rod_pos = self.rod.positions.copy()
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

            if not self.check_action(y, x):
                return False
            else:
                new_rod_pos[i] = (y, x)

        old_position = self.rod.positions.copy()
        self.rod.move(move)
        # self.rod.positions = new_rod_pos
        self.update_rod(old_position)
        return True

    def check_action(self, y, x):
        correct_action = (0 <= y < self.lab_size_y) and (0 <= x < self.lab_size_x)
        return correct_action and self.lab[y][x] != 1

    def check_end(self):
        for i in self.rod.positions:
            if i[0] == self.lab_size_y - 1 and i[1] == self.lab_size_x - 1:
                return True
        return False
