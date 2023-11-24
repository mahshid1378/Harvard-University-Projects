"""
Tic Tac Toe Player for me mahshid moulaei
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    raise NotImplementedError


def actions(board):
    raise NotImplementedError


def result(board, action):
    raise NotImplementedError


def winner(board):
    raise NotImplementedError


def terminal(board):
    raise NotImplementedError


def utility(board):
    raise NotImplementedError


def minimax(board):
    raise NotImplementedError
