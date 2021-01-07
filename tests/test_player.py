import pytest
from src.player import Player


class TestPlayer(object):
    def test_player_init_with_negative_set_point(self):
        with pytest.raises(ValueError):
            player1 = Player("Nadal", -1, 0)

    def test_player_init_with_negative_game_point(self):
        with pytest.raises(ValueError):
            player1 = Player("Nadal", 0, -1)

    def test_player_assign_with_negative_set_point(self):
        player1 = Player("Nadal")
        with pytest.raises(ValueError):
            player1.set_point = -1

    def test_player_assign_with_negative_game_point(self):
        player1 = Player("Nadal")
        with pytest.raises(ValueError):
            player1.game_point = -1
