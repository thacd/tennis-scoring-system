from src.game import Game
from src.player import Player


class TestTieBreakGameWinner(object):
    MIN_TIE_BREAK_WIN_POINT = 7

    player1 = Player("Thiem")
    player2 = Player("Nadal")
    tie_break_game = Game(player1, player2)

    def test_tie_break_game_winner_for_both_players_not_reach_points(self):
        self.player1.game_point = self.MIN_TIE_BREAK_WIN_POINT - 1
        self.player2.game_point = self.MIN_TIE_BREAK_WIN_POINT - 1
        actual = self.tie_break_game.game_winner()
        message = self.__test_message(None, actual)
        assert actual is None, message

    def test_tie_break_game_winner_for_points_difference_not_enough(self):
        self.player1.game_point = self.MIN_TIE_BREAK_WIN_POINT
        self.player2.game_point = self.player1.game_point - 1
        actual = self.tie_break_game.game_winner()
        message = self.__test_message(None, actual)
        assert actual is None, message

    def test_tie_break_game_winner_for_player1(self):
        self.player1.game_point = self.MIN_TIE_BREAK_WIN_POINT
        self.player2.game_point = self.player1.game_point - 2
        actual = self.tie_break_game.game_winner()
        message = self.__test_message(self.player1, actual)
        assert actual is self.player1, message

    def test_tie_break_game_winner_for_player2(self):
        self.player2.game_point = self.MIN_TIE_BREAK_WIN_POINT + 4
        self.player1.game_point = self.player2.game_point - 2
        actual = self.tie_break_game.game_winner()
        message = self.__test_message(self.player2, actual)
        assert actual is self.player2, message

    def __test_message(self, expected, actual):
        return (
                "Test Tie Break Game Win - Expected return value: {0}, "
                "Actual return value: {1}.".format(expected, actual)
            )


class TestNormalGameWinner(object):
    MIN_NORMAL_WIN_POINT = 4

    player1 = Player("Thiem")
    player2 = Player("Nadal")
    normal_game = Game(player1, player2)

    def test_normal_game_winner_for_both_players_not_reach_points(self):
        self.player1.game_point = self.MIN_NORMAL_WIN_POINT - 1
        self.player2.game_point = self.MIN_NORMAL_WIN_POINT - 1
        actual = self.normal_game.game_winner()
        message = self.__test_message(None, actual)
        assert actual is None, message

    def test_normal_game_winner_for_points_difference_not_enough(self):
        self.player1.game_point = self.MIN_NORMAL_WIN_POINT
        self.player2.game_point = self.MIN_NORMAL_WIN_POINT - 1
        actual = self.normal_game.game_winner()
        message = self.__test_message(None, actual)
        assert actual is None, message

    def test_normal_game_winner_for_player1(self):
        self.player1.game_point = self.MIN_NORMAL_WIN_POINT
        self.player2.game_point = self.player1.game_point - 2
        actual = self.normal_game.game_winner()
        message = self.__test_message(self.player1, actual)
        assert actual is self.player1, message

    def test_normal_game_winner_for_player2(self):
        self.player2.game_point = self.MIN_NORMAL_WIN_POINT
        self.player1.game_point = self.player2.game_point - 2
        actual = self.normal_game.game_winner()
        message = self.__test_message(self.player2, actual)
        assert actual is self.player2, message

    def __test_message(self, expected, actual):
        return (
                "Test Normal Game Win - Expected return value: {0}, "
                "Actual return value: {1}.".format(expected, actual)
            )


class TestGameDeuce(object):
    DEUCE_POINT = 3
    player1 = Player("Thiem")
    player2 = Player("Nadal")

    normal_game = Game(player1, player2)

    def test_game_deuce_for_deuce_points(self):
        self.player1.game_point = self.DEUCE_POINT
        self.player2.game_point = self.DEUCE_POINT
        actual = self.normal_game.game_deuce()
        message = self.__test_message(True, actual)
        assert actual is True, message

    def test_game_deuce_for_different_points(self):
        self.player1.game_point = self.DEUCE_POINT
        self.player2.game_point = self.DEUCE_POINT - 1
        actual = self.normal_game.game_deuce()
        message = self.__test_message(False, actual)
        assert actual is False, message

    def test_game_deuce_for_same_points_but_not_deuce(self):
        self.player1.game_point = self.DEUCE_POINT - 1
        self.player2.game_point = self.DEUCE_POINT - 1
        actual = self.normal_game.game_deuce()
        message = self.__test_message(False, actual)
        assert actual is False, message

    def __test_message(self, expected, actual):
        return (
                "Test Game Deuce - Expected return value: {0}, "
                "Actual return value: {1}.".format(expected, actual)
            )


class TestGameAdvantage(object):
    ADVANTAGE_POINT = 3
    player1 = Player("Thiem")
    player2 = Player("Nadal")

    normal_game = Game(player1, player2)

    def test_game_advantage_not_reach_advantage_points(self):
        self.player2.game_point = self.ADVANTAGE_POINT - 1
        self.player1.game_point = self.player2.game_point + 1
        actual = self.normal_game.game_advantage()
        message = self.__test_message(self.player1, actual)
        assert actual is None, message

    def test_game_advantage_for_player1(self):
        self.player2.game_point = self.ADVANTAGE_POINT
        self.player1.game_point = self.player2.game_point + 1
        actual = self.normal_game.game_advantage()
        message = self.__test_message(self.player1, actual)
        assert actual is self.player1, message

    def test_game_advantage_for_player2(self):
        self.player1.game_point = self.ADVANTAGE_POINT
        self.player2.game_point = self.player1.game_point + 1
        actual = self.normal_game.game_advantage()
        message = self.__test_message(self.player2, actual)
        assert actual is self.player2, message

    def __test_message(self, expected, actual):
        return (
                "Test Game Advantage - Expected return value: {0}, "
                "Actual return value: {1}.".format(expected, actual)
            )
