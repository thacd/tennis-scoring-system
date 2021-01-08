from .player import Player


class Game:
    POINT_MAP = {0: '0', 1: '15', 2: '30', 3: '40'}

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def game_winner(self):
        win_point = 4
        if self.__is_tie_break():
            win_point = 7
        if (self.player1.game_point >= win_point) & \
           (self.player1.game_point - self.player2.game_point >= 2):
            return self.player1
        if (self.player2.game_point >= win_point) & \
           (self.player2.game_point - self.player1.game_point >= 2):
            return self.player2
        return None

    def game_deuce(self):
        return (self.player1.game_point == self.player2.game_point) & \
            (self.player1.game_point >= 3)

    def game_advantage(self):
        if ((self.player1.game_point - self.player2.game_point) == 1) & \
           (self.player2.game_point >= 3):
            return self.player1
        if ((self.player2.game_point - self.player1.game_point) == 1) & \
           (self.player1.game_point >= 3):
            return self.player2
        return None

    def game_score(self):
        if self.__is_new_game():
            return ""
        if self.__is_tie_break():
            return ", {0}-{1}".format(
                    self.player1.game_point, self.player2.game_point)
        else:
            if self.game_deuce():
                return ", Deuce"
            advantage = self.game_advantage()
            if advantage is not None:
                return ", Advantage {0}".format(advantage.name)
            return ", {0}-{1}".format(
                    self.POINT_MAP[self.player1.game_point],
                    self.POINT_MAP[self.player2.game_point]
                )

    def __is_new_game(self):
        return (self.player1.game_point == 0) & (self.player2.game_point == 0)

    def __is_tie_break(self):
        return (self.player1.set_point == 6) & (self.player2.set_point == 6)
