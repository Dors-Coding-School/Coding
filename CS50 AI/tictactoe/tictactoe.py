"""
Tic Tac Toe Player
"""

import math
import copy

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
    counterX = 0
    counterO = 0

    # Count how many X and O there are in the board
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == X:
                counterX += 1
            if board[row][column] == O:
                counterO += 1

    # If there are more X then O, next turn is O
    if counterX > counterO:
        return O
    # If there is O == X, next turn is X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create an empty set of all possible actions
    AllPossibleActions = set()

    # Possible moves are any cells that are EMPTY
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                AllPossibleActions.add((row,column))

    # Return the set
    return AllPossibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If action is not a valid action for the board, raise an exception.
    if action not in actions(board):
        raise Exception('Action is not a valid action for the board!')

    # Make a deep copy of the board before making any changes.
    board_copy = copy.deepcopy(board)

    # Update the copied board for the current player's move
    x, y = action
    board_copy[x][y] = player(board)
    return board_copy


def checkRow(board,player):
    # Checks for three in a row horizontally.
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def checkColumn(board,player):
    # Checks for three in a row vertically.
    for column in range(len(board)):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    return False


def checkBottomTopDiagonal(board, player):
    # Updated: Checks for three in a row in the anti-diagonal.
    return board[0][2] == board[1][1] == board[2][0] == player


def checkTopBottomDiagonal(board, player):
    # Updated: Checks for three in a row in the main diagonal.
    return board[0][0] == board[1][1] == board[2][2] == player


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # If the X player has won the game, return X.
    if checkRow(board, X) or checkColumn(board, X) or checkTopBottomDiagonal(board, X) or checkBottomTopDiagonal(board, X):
        return X

    # If the O player has won the game, return O.
    elif checkRow(board, O) or checkColumn(board, O) or checkTopBottomDiagonal(board, O) or checkBottomTopDiagonal(board, O):
        return O

    # If there is no winner of the game, return None.
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If the game is over due to a win, return True
    if winner(board) == X or winner(board) == O:
        return True

    # Check if any cells are EMPTY, indicating the game is still in progress
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                return False

    # For the case if there was a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # If X has won the game, the utility is 1.
    if winner(board) == X:
        return 1
    # If O has won the game, the utility is -1.
    elif winner(board) == O:
        return -1
    # If the game has ended in a tie, the utility is 0.
    else:
        return 0


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None

    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:
        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

    return best_action
