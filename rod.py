class Rod:
    """
    Rod object
    """

    def __init__(self):
        self.length = 3
        self.wide = 1
        self.positions = [(0, item) for item in range(self.length)]
        self.vertical_orientation = False


    def move(self, move):
        """
        MOves the Rod
        """
        if move == "UP":    # up
            self.positions = [(item[0] - 1, item[1]) for item in self.positions]
        elif move == "DOWN":  # down
            self.positions = [(item[0] + 1, item[1]) for item in self.positions]
        elif move == "RIGHT":  # right
            self.positions = [(item[0], item[1] + 1) for item in self.positions]
        elif move == "LEFT":  # left
            self.positions = [(item[0], item[1] - 1) for item in self.positions]

    def rotate(self):
        """
        Rotates the rod
        """
        # TODO: simplificar y hacer independiente del tamano del ROD
        if self.vertical_orientation:
            self.positions[0] = (self.positions[1][0], self.positions[1][1]-1)
            self.positions[1] = (self.positions[1][0], self.positions[1][1])
            self.positions[2] = (self.positions[1][0], self.positions[1][1]+1)
        else:
            self.positions[0] = (self.positions[1][0]-1, self.positions[1][1])
            self.positions[1] = (self.positions[1][0],   self.positions[1][1])
            self.positions[2] = (self.positions[1][0]+1, self.positions[1][1])

        # print(self.positions)
        # for i in range(self.length):
        #     self.positions[i] = (self.positions[i][1], self.positions[i][0])
        # print(self.positions)
        self.vertical_orientation = not self.vertical_orientation
