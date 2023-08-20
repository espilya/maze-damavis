from simulation import *


class Controller:

    def __init__(self, labyrinth):
        self.maze = labyrinth

    def search(self):
        pass

    def manual(self):
        sim = Simulation(self.maze)
        sim.print()
        steps = 0
        end = False
        try:
            while not end:
                value = input("Please enter an action (wasd-move, r-rotate, e-exit):\n")
                steps += 1
                if value not in ["w", "a", "s", "d", "r", "e"]:
                    continue

                if value == "w":
                    sim.move_rod("UP")
                elif value == "a":
                    sim.move_rod("LEFT")
                elif value == "s":
                    sim.move_rod("DOWN")
                elif value == "d":
                    sim.move_rod("RIGHT")
                elif value == "r":
                    sim.rotate_rod()
                elif value == "e":
                    end = True

                sim.print()
                if sim.check_end():
                    print("Maze finished in ", steps, " movements!")
                    end = True

        except KeyboardInterrupt:
            pass
