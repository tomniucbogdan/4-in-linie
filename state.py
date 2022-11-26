class State:
    def __init__(self):
        self.player = 'Red'
        self.sloturi = [0] * 7
        self.culori = [[None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]

    def reset(self):
        self.sloturi = [0] * 7
        self.culori = [[None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]
