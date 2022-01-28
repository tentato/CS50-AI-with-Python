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
    # check ROWS
    # for i in range(3):
    #     if board[i][0] == board[i][1] == board[i][2] == X:


    # for i in range(3):
    #     sum = 0
    #     for j in range(3):
    #         if board[i][j] == "X":
    #             sum += 1
    #         elif board[i][j] == "O":
    #             sum -= 1

    #     if sum == 3 or sum == -3:
    #         return True


    # # check COLUMNS
    # for i in range(3):
    #     sum = 0
    #     for j in range(3):
    #         if board[j][i] == "X":
    #             sum += 1
    #         elif board[j][i] == "O":
    #             sum -= 1

    #     if sum == 3 or sum == -3:
    #         return True

    # # check diagonal
    # if board[0][0] == 
    # if sum == 3 or sum == -3:

    # # check anti-diagonal    
    # sum = table_array[0, 2] + table_array[1, 1] + table_array[2, 0]
    # if sum == 3:
    #     result = "X wins"
    #     finished = True
    #     p1 = (100, 500)
    #     p2 = (500, 100)
    # elif sum == -3:
    #     result = "O wins"
    #     finished = True
    #     p1 = (100, 500)
    #     p2 = (500, 100)

    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] == None:
    #             return False

    # return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    print("Game over")
    return 1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    moves = actions(board)
    if board == initial_state():
        first_moves = [(0, 0), (2, 2), (2, 0), (0, 2)]
        move = first_moves[random.randint(0, 3)]
        return move
    

    
    return move


def min_value(board):
    """
    Returns the min value for a current board.
    """
    if terminal(board):
        return utility(board)
        
    value = +INFINITY

    for action in actions(board):
        value = max(value, max_value(result(board, action)))
    return value


def max_value(board):
    """
    Returns the max value for a current board.
    """
    if terminal(board):
        return utility(board)

    value = -INFINITY

    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value