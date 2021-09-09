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
    x_value = 0
    o_value = 0

    # Finding total X and O on the board
    for x in board:
        for y in x:
            if y == X:
                x_value += 1
            elif y == O:
                o_value += 1

    # If there are more X than O on the board, it's O turn
    # If there are the same amount of X and O on the board, it's X turn
    if (x_value > o_value):
        return O
    elif (x_value < o_value):
        return X
    return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()

    # Add all the (i,j) of empty elements
    i = 0
    for x in board:
        j = 0
        for y in x:
            if y == EMPTY:
                available.add((i, j))
            j += 1
        i += 1
    return available
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    # Create a copy of the board
    test_board = copy.deepcopy(board)

    # Allow the move if the action is empty
    if (test_board[i][j] != EMPTY):
        raise NotImplementedError
    else:
        test_board[i][j] = player(board)

    return test_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        #Horizontal checks
        if board[x][0] == board[x][1] == board[x][2]:
            if player(board) == X:
                return O
            else:
                return X

        #Vertical checks
        if board[0][x] == board[1][x] == board[2][x]:
            if player(board) == X:
                return O
            else:
                return X

    #Diagonal checks
    if board[0][0] == board[1][1] == board[2][2]:
        if player(board) == X:
            return O
        else:
            return X
    if board[0][2] == board[1][1] == board[2][0]:
        if player(board) == X:
            return O
        else:
            return X
    return None
    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for x in range(3):
        # Horizontal checks
        if board[x][0] == board[x][1] == board[x][2] != EMPTY:
            return True

        # Vertical checks
        if board[0][x] == board[1][x] == board[2][x] != EMPTY:
            return True

    # Diagonal checks
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True

    # Check if the board has run out of moves
    empty = 0

    for x in board:
        for y in x:
            if y == EMPTY:
                empty += 1

    if empty == 0:
        return True
    else:
        return False
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # X has won (1)
    if (winner(board)==X):
        return 1

    # O has won (-1)
    elif (winner(board)==O):
        return -1
    # Tie (0)
    elif (winner(board)==None):
        return 0
    raise NotImplementedError

def maxFunction(test_board):
    # Declared a really low value
    value = -2

    # Check if the game is over
    if (terminal(test_board) == True):
        return utility(test_board)

    # Find the best move by recurs between players and take the move with the highest value
    for x in actions(test_board):
        value = max(value, minFunction(result(test_board,x)))
    return value

def minFunction(test_board):
    # Declared a really high value
    value = 2

    # Check if the game is over
    if (terminal(test_board) == True):
        return utility(test_board)

    # Find the best move by recurs between players and take the move with the lowest value
    for x in actions(test_board):
        value = min(value, maxFunction(result(test_board,x)))
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Return move with highest value if the player is X
    if player(board) == X:
        max = -2
        move = None

        # Check the value of all available moves
        for x in actions(board):

            # Keep track of the move with highest value
            if (minFunction(result(board, x))) > max:
                max = (minFunction(result(board, x)))

                # Highest value move at the moment
                move = x
        # print(move)
        return move

    # Return move with lowest value if the player is O
    else:
        min = 2
        move = None

        # Check the value of all available moves
        for x in actions(board):

            # Keep track of the move with lowest value
            if (maxFunction(result(board, x))) < min:
                min = (maxFunction(result(board, x)))

                # Highest value move at the moment
                move = x
        # print(move)
        return move
    raise NotImplementedError
