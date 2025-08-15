import pytest
from othello import Othello


def test_initial_board():
    game = Othello()
    assert game.board[3][3] == Othello.WHITE
    assert game.board[3][4] == Othello.BLACK
    assert game.board[4][3] == Othello.BLACK
    assert game.board[4][4] == Othello.WHITE


def test_valid_moves_start():
    game = Othello()
    moves = set(game.valid_moves(Othello.BLACK))
    expected = {(2, 3), (3, 2), (4, 5), (5, 4)}
    assert moves == expected


def test_move_flips():
    game = Othello()
    assert game.make_move(2, 3)
    assert game.board[3][3] == Othello.BLACK
    assert game.board[2][3] == Othello.BLACK
    assert game.current == Othello.WHITE


def test_board_str():
    game = Othello()
    expected = (
        "  0 1 2 3 4 5 6 7\n"
        "0 . . . . . . . .\n"
        "1 . . . . . . . .\n"
        "2 . . . . . . . .\n"
        "3 . . . W B . . .\n"
        "4 . . . B W . . .\n"
        "5 . . . . . . . .\n"
        "6 . . . . . . . .\n"
        "7 . . . . . . . ."
    )
    assert game.board_str() == expected
