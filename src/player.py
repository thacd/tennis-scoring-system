class Player:
    def __init__(self, name, set_point=0, game_point=0):
        self.name = name
        self.set_point = set_point
        self.game_point = game_point

    @property
    def set_point(self):
        return self.__set_point

    @set_point.setter
    def set_point(self, value):
        if value < 0:
            raise ValueError("Negative set point is impossible!")
        self.__set_point = value

    @property
    def game_point(self):
        return self.__game_point

    @game_point.setter
    def game_point(self, value):
        if value < 0:
            raise ValueError("Negative game point is impossible!")
        self.__game_point = value
