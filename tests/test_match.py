from src.match import Match
from src.player import Player


class TestSetWinner(object):
    SET_WIN_POINT = 6

    match = Match("Thiem", "Nadal")

    def test_set_winner_for_no_winner(self):
        self.match.player1.set_point = self.SET_WIN_POINT - 1
        self.match.player2.set_point = self.match.player1.set_point - 2
        actual = self.match.set_winner()
        message = self.__test_message(None, actual)
        assert actual is None, message

    def test_set_winner_for_no_winner_6_5(self):
        self.match.player1.set_point = self.SET_WIN_POINT - 1
        self.match.player2.set_point = self.SET_WIN_POINT
        actual = self.match.set_winner()
        message = self.__test_message(None, actual)
        assert actual is None, message

    def test_set_winner_for_Thiem_7_5(self):
        self.match.player1.set_point = self.SET_WIN_POINT + 1
        self.match.player2.set_point = self.SET_WIN_POINT - 1
        actual = self.match.set_winner()
        message = self.__test_message(self.match.player1, actual)
        assert actual is self.match.player1, message

    def test_set_winner_for_Nadal_7_5(self):
        self.match.player1.set_point = self.SET_WIN_POINT - 1
        self.match.player2.set_point = self.SET_WIN_POINT + 1
        actual = self.match.set_winner()
        message = self.__test_message(self.match.player2, actual)
        assert actual is self.match.player2, message

    def test_set_winner_for_tie_break_Thiem_win(self):
        self.match.player1.set_point = self.SET_WIN_POINT + 1
        self.match.player2.set_point = self.SET_WIN_POINT
        actual = self.match.set_winner()
        message = self.__test_message(self.match.player1, actual)
        assert actual is self.match.player1, message

    def test_set_winner_for_tie_break_Nadal_win(self):
        self.match.player1.set_point = self.SET_WIN_POINT
        self.match.player2.set_point = self.SET_WIN_POINT + 1
        actual = self.match.set_winner()
        message = self.__test_message(self.match.player2, actual)
        assert actual is self.match.player2, message

    def test_set_winner_for_Thiem_win(self):
        self.match.player1.set_point = self.SET_WIN_POINT
        self.match.player2.set_point = self.SET_WIN_POINT - 2
        actual = self.match.set_winner()
        message = self.__test_message(self.match.player1, actual)
        assert actual is self.match.player1, message

    def test_set_winner_for_Nadal_win(self):
        self.match.player1.set_point = self.SET_WIN_POINT - 2
        self.match.player2.set_point = self.SET_WIN_POINT
        actual = self.match.set_winner()
        message = self.__test_message(self.match.player2, actual)
        assert actual is self.match.player2, message

    def __test_message(self, expected, actual):
        return (
                "Test Set Winner - Expected return value: {0}, "
                "Actual return value: {1}.".format(expected, actual)
            )


class TestScore(object):
    match = Match("Thiem", "Nadal")

    def test_score_new_game(self):
        actual = self.match.score()
        message = self.__test_message("0-0", actual)
        assert actual == "0-0", message

    def test_score_deuce(self):
        self.match.player1.game_point = 3
        self.match.player2.game_point = 3
        actual = self.match.score()
        message = self.__test_message("0-0, Deuce", actual)
        assert actual == "0-0, Deuce", message

    def test_score_advantage(self):
        self.match.player1.game_point = 4
        self.match.player2.game_point = 3
        actual = self.match.score()
        message = self.__test_message("0-0, Advantage Thiem", actual)
        assert actual == "0-0, Advantage Thiem", message

    def test_score_normal_score(self):
        self.match.player1.game_point = 3
        self.match.player2.game_point = 2
        actual = self.match.score()
        message = self.__test_message("0-0, 40-30", actual)
        assert actual == "0-0, 40-30", message

    def test_score_tie_break_score(self):
        self.match.player1.set_point = 6
        self.match.player2.set_point = 6
        self.match.player1.game_point = 3
        self.match.player2.game_point = 2
        actual = self.match.score()
        message = self.__test_message("6-6, 3-2", actual)
        assert actual == "6-6, 3-2", message

    def __test_message(self, expected, actual):
        return (
                "Test Score - Expected return value: {0}, "
                "Actual return value: {1}.".format(expected, actual)
            )


class TestPointWonBy(object):
    match = Match("Thiem", "Nadal")

    def test_point_won_by_Thiem(self):
        self.match.point_won_by(self.match.player1.name)
        assert self.match.player1.game_point == 1
        assert self.match.player2.game_point == 0
        assert self.match.player1.set_point == 0
        assert self.match.player2.set_point == 0

    def test_point_won_by_Thiem_set_point(self):
        self.match.player1.game_point = 3
        self.match.player2.game_point = 2
        self.match.point_won_by(self.match.player1.name)
        assert self.match.player1.game_point == 0
        assert self.match.player2.game_point == 0
        assert self.match.player1.set_point == 1
        assert self.match.player2.set_point == 0

    def test_point_won_by_Nadal(self):
        self.match.point_won_by(self.match.player2.name)
        assert self.match.player1.game_point == 0
        assert self.match.player2.game_point == 1
        assert self.match.player1.set_point == 1
        assert self.match.player2.set_point == 0

    def test_point_won_by_Nadal_set_point(self):
        self.match.player1.game_point = 2
        self.match.player2.game_point = 3
        self.match.point_won_by(self.match.player2.name)
        assert self.match.player1.game_point == 0
        assert self.match.player2.game_point == 0
        assert self.match.player1.set_point == 1
        assert self.match.player2.set_point == 1

    def test_point_won_by_Nadal_tie_break(self):
        self.match.player1.set_point = 6
        self.match.player2.set_point = 6
        self.match.player1.game_point = 2
        self.match.player2.game_point = 3
        self.match.point_won_by(self.match.player2.name)
        assert self.match.player1.game_point == 2
        assert self.match.player2.game_point == 4
        assert self.match.player1.set_point == 6
        assert self.match.player2.set_point == 6

    def test_point_won_by_Nadal_tie_break_set_point(self):
        self.match.player1.game_point = 5
        self.match.player2.game_point = 6
        self.match.point_won_by(self.match.player2.name)
        assert self.match.player1.game_point == 0
        assert self.match.player2.game_point == 0
        assert self.match.player1.set_point == 6
        assert self.match.player2.set_point == 7
