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
    # Initialize counter for X and O
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
    """
    Each action should be represented as a tuple (i, j) 
    where i corresponds to the row of the move (0, 1, or 2) 
    and j corresponds to which cell in the row corresponds 
    to the move (also 0, 1, or 2).
    """
    # Create a empty set o all possible actions
    AllPossibleActions = set()

    # Possible moves are any cells on the board that do not already have an X or an O in them.
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
    # If action is not a valid action for the board, your program should raise an exception.
    if action not in actions(board):
        raise Exception('Action is not a valid action for the board!')

    # You’ll likely want to make a deep copy of the board first before making any changes.
    """A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original"""
    board_copy = copy.deepcopy(board)

    # The returned board state should be the board that would result from taking the original input board, 
    # and letting the player whose turn it is make their move at the cell indicated by the input action.
    x, y = action
    board_copy[x][y] = player(board)
    return board_copy


# One can win the game with three of their moves in a row horizontally.
def checkRow(board,player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


# One can win the game with three of their moves in a row vertically.
def checkColumn(board,player):
    for column in range(len(board)):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    return False


# One can win the game with three of their moves in a row diagonally.
def checkBottomTopDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            # I need to change this part
            if row == column and board[row][len(board) - row - 1] == player:
                count += 1
    return count == 3


# One can win the game with three of their moves in a row diagonally.
def checkTopBottomDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            if row == column and board[row][column] == player:
                count += 1
    return count == 3    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # If the X player has won the game, your function should return X. 
    if checkRow(board,X) or checkColumn(board,X) or checkTopBottomDiagonal(board,X) or checkBottomTopDiagonal(board,X):
        return X 
    
    # If the O player has won the game, your function should return O.
    elif checkRow(board,O) or checkColumn(board,O) or checkTopBottomDiagonal(board,O) or checkBottomTopDiagonal(board,O):
        return O

    # If there is no winner of the game (either because the game is in progress, or because it ended in a tie), 
    # the function should return None.
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    
    # Otherwise, the function should return False if the game is still in progress (there are cells EMPTY).
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                return False

    # For the case if there was a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    You may assume utility will only be called on a board if terminal(board) is True
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
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    If multiple moves are equally optimal, any of those moves is acceptable.
    """
    # If the board is a terminal board, the minimax function should return None.
    if terminal(board):
        return None
    
    # Case of player is X
    elif player(board) == X:
        plays = []
        # Loop over the action to get the max value for X and min value for O
        for action in actions(board):
            # Add in plays a tupple with the min_value and the action that results to its value
            plays.append([min_value(result(board,action)), action])
        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    # Case of player is O
    elif player(board) == O:
        plays = []
        for action in actions(board):
            # Add in plays a tupple with the max_value and the action that results to its value
            plays.append([max_value(result(board,action)), action])
        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0])[0][1]
