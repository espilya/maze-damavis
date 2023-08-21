from simulation import *

import copy

# global best_steps
best_steps = 2000

# global best_path
best_path = []

# global DEBUG
DEBUG = 0  # 0, 1, 2

# Upper limit for steps
MOVEMENT_LIMIT = 1000000
# total steps counter
total_steps = 0


def search_recursive_bruteforce(sim, steps, last_action):
    """
    Recursive bruteforce solution. Tries all possible movements.
    Not the best possible solution for this problem.
    """
    actions_list = ["RIGHT", "DOWN", "UP", "LEFT", "ROTATE"]
    ok = False
    for action in actions_list:
        if action == "ROTATE" and last_action != "ROTATE":
            ok = sim.rotate_rod()
        elif action == "RIGHT" and last_action != "LEFT":
            ok = sim.move_rod(action)
        elif action == "LEFT" and last_action != "RIGHT":
            ok = sim.move_rod(action)
        elif action == "DOWN" and last_action != "UP":
            ok = sim.move_rod(action)
        elif action == "UP" and last_action != "DOWN":
            ok = sim.move_rod(action)
        if ok:
            if DEBUG == 2:
                print(action)
                sim.print()
            if sim.check_end():
                global best_steps
                global best_path

                end = False
                if steps < best_steps:
                    # best_steps = steps
                    best_steps = len(sim.last_actions) - 1
                    best_path = sim.last_actions
                    if DEBUG >= 1:
                        print("Found new best solution!")
                        print(best_steps)
                        print(best_path)
                        print()
                return sim, steps, end, action
            else:
                # hard limit for steps
                global total_steps
                if total_steps > MOVEMENT_LIMIT:
                    return sim, steps, False, action
                total_steps = total_steps + 1

                # new recursive iteration
                search_recursive_bruteforce(copy.deepcopy(sim), copy.deepcopy(steps) + 1, copy.deepcopy(action))

                if DEBUG == 2:
                    print("Backtrack!")
                sim.move_rod_back()

                ok = False
    return sim, steps, False, action


class Controller:
    """
    Controller for the rod
    """

    def __init__(self, labyrinth):
        self.maze = labyrinth

    def search(self):
        """
        Automatic search
        """
        # Init simulation
        sim = Simulation(self.maze)
        steps = 0

        # Set a hard limit based on the size of the maze
        global MOVEMENT_LIMIT
        MOVEMENT_LIMIT = sim.lab_size_y * sim.lab_size_x * 200

        # Start search
        try:
            search_recursive_bruteforce(sim, steps, None)
        except Exception as e:
            print("An exception occurred: ", e)

        global best_steps
        if best_steps == 2000:
            best_steps = -1
        return best_steps
        # print(best_path)

    def manual(self):
        """
        Manual controller version
        """
        sim = Simulation(self.maze)
        sim.print()
        steps = 0
        end = False
        try:
            while not end:
                value = input("Please enter an action (wasd-move, r-rotate, b-back, e-exit):\n")
                steps += 1
                if value not in ["w", "a", "s", "d", "r", "b", "e"]:
                    continue

                if value == "w":
                    sim.move_rod("UP")
                elif value == "a":
                    sim.move_rod("LEFT")
                elif value == "s":
                    sim.move_rod("DOWN")
                elif value == "d":
                    sim.move_rod("RIGHT")
                elif value == "b":
                    sim.move_rod_back()
                elif value == "r":
                    sim.rotate_rod()
                elif value == "e":
                    end = True

                sim.print()
                if sim.check_end():
                    return steps
                    print("Maze finished in ", steps, " movements!")
                    end = True

        except KeyboardInterrupt:
            pass
