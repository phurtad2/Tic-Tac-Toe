#! ~/PycharmProjects/TicTacToe minimax.py
# ---------------------#
# These are the methods used when it is the "ai"'s turn in TicTacToeGUI.py. They were moved into a separate file for
# easier reading.
# ---------------------#

__author__ = "Patrick Hurtado"

def minimax(state, first): # The minimax algorithm is mostly done in the travel method. This merely returns a state.
    allMoves = []
    scores = []
    # Goes theough all the positions in the board
    for x in range(len(state)):
        for y in range(len(state[x])):
            if state[x][y] == 0:    # if this in a possible move
                z = []
                z.extend((list(state[0]), list(state[1]), list(state[2]))) # Create a copy of the board, but...
                z[x][y] = 2     # Set the empty place to an ai move (denoted as a 2 in the array of the board)
                allMoves.append(list(z))    # Append it to one of the moves it can make
                scores.append(travel(z, 1, first))      # Calculates the score as it traverses down the tree

    if (scores == []):  # Essentially, if we're at the final state, where there are no more moves to make.
        return []

    else:
        return allMoves[scores.index(max(scores))]     # Take the max score and return the state that brought it.


def score(board, depth, first):     # Method to calculate the score of a given final state.
    if isGameOver(board) and not isTie(board) and whowins(board) == 1:      # If there is a winner and it's the user...
        return depth - 10   # The depth is subtracted for the ai to take plays that bring more immediate victory
    if isGameOver(board) and not isTie(board) and whowins(board) == 2:      # If there is a winner and it's the ai...
        return 10 - depth   # The depth is subtracted for the ai to take plays that bring more immediate victory
    else: # Else if there's a tie...
        return 0 # No points either way (so, basically, it could be worse, but it could've been better)


def isGameOver(win):    # Checks all possible winning outcomes (sans if there is a tie)
    return win[0][0] == win[1][0] == win[2][0] != 0 or \
           win[0][1] == win[1][1] == win[2][1] != 0 or \
           win[0][2] == win[1][2] == win[2][2] != 0 or \
           win[0][0] == win[0][1] == win[0][2] != 0 or \
           win[1][0] == win[1][1] == win[1][2] != 0 or \
           win[2][0] == win[2][1] == win[2][2] != 0 or \
           win[0][0] == win[1][1] == win[2][2] != 0 or \
           win[2][0] == win[1][1] == win[0][2] != 0


def whowins(win):   # Checks who specifically won (1 = user, and 2 = ai)
    if isGameOver(win) and not isTie(win):
        if win[0][0] == win[1][0] == win[2][0] != 0:
            return win[0][0]
        if win[0][1] == win[1][1] == win[2][1] != 0:
            return win[0][1]
        if win[0][2] == win[1][2] == win[2][2] != 0:
            return win[0][2]
        if win[0][0] == win[0][1] == win[0][2] != 0:
            return win[0][0]
        if win[1][0] == win[1][1] == win[1][2] != 0:
            return win[1][0]
        if win[2][0] == win[2][1] == win[2][2] != 0:
            return win[2][0]
        if win[0][0] == win[1][1] == win[2][2] != 0:
            return win[0][0]
        if win[2][0] == win[1][1] == win[0][2] != 0:
            return win[2][0]
    else:
        return 0


def isTie(win): # Checks if the end state is a tie
    return sum(x.count(0) for x in win) == 0


def travel(board, depth, first):    # the recursion part of the minimax method
    newscores = []
    if isGameOver(list(board) or isTie(board)):     # If we've reached a final state...(BASE CASE)
        return score(list(board), depth, first)     # return the score for the given state
    depth += 1      # Depth counter
    # For every spot in the current board...
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:    # If this spot is a viable playing spot...
                comp = sum(x.count(0) for x in board) % 2 == 1      # This helps check if the first player is going
                z = []
                z.extend((list(board[0]), list(board[1]), list(board[2])))

                if first:   # If the ai went first originally...
                    if comp:    # and if it' the first player's turn...
                        z[x][y] = 2     # Set the available space as an X
                    else:
                        z[x][y] = 1     # Otherwise, and O
                else:
                    if comp:
                        z[x][y] = 1
                    else:
                        z[x][y] = 2

                newscores.append(travel(z, depth, first)) # Keep going until all scores have been calculated
    if not newscores:   # if we're trying to recurse on an end state
        return 1
    if (comp and first) or (not comp and not first):    # If it's the ai's turn...
        return newscores[newscores.index(max(newscores))]   # take the max of all the next set of scores.
    else:
        return newscores[newscores.index(min(newscores))]   # Otherwise, take the min of all the next set of scores.
