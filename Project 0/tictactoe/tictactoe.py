"""
Tic Tac Toe Player
"""

import copy
import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    if len(actions(board)) % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append((i, j))
    actions = set(actions)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    plr = player(board)
    copied_board = copy.deepcopy(board)
    copied_board[action[0]][action[1]] = plr

    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    moves = actions(board)
    first_moves = [(0, 0), (2, 2), (2, 0), (0, 2)]
    if board == initial_state():
        move = first_moves[random.randint(0, 3)]
    return move
