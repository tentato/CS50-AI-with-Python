"""
Tic Tac Toe Player
"""

import copy
from json.encoder import INFINITY
import math
from pickle import FALSE
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

    # return [[EMPTY, "X", "O"],
    #         ["O", "X", EMPTY],
    #         ["X", EMPTY, "O"]]
    

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
    i, j = action[0], action[1]
    copied_board[i][j] = plr

    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check ROWS
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O

    # check COLUMNS
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return O

    # check diagonal
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O

    # check second diagonal
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check ROWS
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == X) or (board[i][0] == board[i][1] == board[i][2] == O):
            return True

    # check COLUMNS
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j] == X) or (board[0][j] == board[1][j] == board[2][j] == O):
            return True

    # check diagonal
    if (board[0][0] == board[1][1] == board[2][2] == X) or (board[0][0] == board[1][1] == board[2][2] == O):
        return True

    # check second diagonal
    if (board[0][2] == board[1][1] == board[2][0] == X) or (board[0][2] == board[1][1] == board[2][0] == O):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # check ROWS
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return 1
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return -1

    # check COLUMNS
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return 1
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return -1

    # check diagonal
    if board[0][0] == board[1][1] == board[2][2] == X:
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return -1

    # check second diagonal
    if board[0][2] == board[1][1] == board[2][0] == X:
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # to ensure best first step with no effort
    if board == initial_state():
        first_moves = [(0, 0), (2, 2), (2, 0), (0, 2)]
        move = first_moves[random.randint(0, 3)]
        return move

    action_to_make = None
    plr = player(board)

    if plr == X:
        val = -2
        for action in actions(board):
            value = min_value(result(board, action))
            if val < value:
                val = value
                action_to_make = action
    else:
        val = 2
        for action in actions(board):
            print(action)
            value = max_value(result(board, action))
            print(value)
            if val > value:
                val = value
                action_to_make = action

    # print(val)
    # print(val)
    return action_to_make


def min_value(board):
    """
    Returns the min value for the current board.
    """
    if terminal(board):
        return utility(board)
        
    value = 2

    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


def max_value(board):
    """
    Returns the max value for the current board.
    """
    if terminal(board):
        return utility(board)

    value = -2

    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value