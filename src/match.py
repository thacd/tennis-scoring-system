from src.player import Player
from src.game import Game


class Match:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.game = Game(self.player1, self.player2)

    def set_winner(self):
        if self.player1.set_point == 7:
            return self.player1
        if self.player2.set_point == 7:
            return self.player2
        if (self.player1.set_point == 6) & (self.player2.set_point <= 4):
            return self.player1
        if (self.player2.set_point == 6) & (self.player1.set_point <= 4):
            return self.player2
        return None

    def score(self):
        game_score = self.game.game_score()
        return "{0}-{1}{2}".format(
            self.player1.set_point, self.player2.set_point, game_score)

    def point_won_by(self, player):
        if player is self.player1:
            self.__adjust_point(self.player1)
        else:
            self.__adjust_point(self.player2)

    def __adjust_point(self, player):
        player.game_point += 1
        if self.game.game_winner():
            player.set_point += 1
            self.player1.game_point = 0
            self.player2.game_point = 0
