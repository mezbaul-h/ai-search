# coding=utf-8
import sys


def UTILITY(state):
    """returns the heuristic value of a state"""
    rows = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    score = 0
    for row in rows:
        if state[row[0]] == state[row[1]] != '-':
            if state[row[2]] == '-': # two in a row + empty
                if state[row[0]] == 'X':
                    score += 10
                else:
                    score -= 10
        if state[row[0]] == state[row[1]] == '-': # one in a row + two empty
            if state[row[2]] == 'X':
                score += 1
            elif state[row[2]] == 'O':
                score -= 1
        if state[row[0]] == state[row[1]] == state[row[2]] != '-':
            # three in a row
            if state[row[0]] == 'X':
                score += 100
            else:
                score -= 100
    return score


def TERMINAL_TEST(state):
    """returns True if someone has won or no more empty space on board"""
    moves_left = 0
    rows = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for row in rows:
        if state[row[0]] == state[row[1]] == state[row[2]] != '-':
            return True
    for cell in state:
        if cell == '-':
            moves_left += 1
    if moves_left > 0:
        return False
    else:
        return True



def RESULT(state, action, player_mark):
    """performs an action on a state and returns resulting state"""
    #state = _state[:]
    state[action] = player_mark
    return state


def ACTIONS(state):
    """returns a list of valid actions (empty cells) on a state"""
    nofill = []
    for i in range(9):
        if state[i] == '-':
            nofill.append(i)
    return nofill


def minimax(state, depth, maximizing_player):
    if TERMINAL_TEST(state):# or depth == 0:
        return [UTILITY(state), -1]

    best_position = -1

    if maximizing_player:
        best_value = -sys.maxint
        for action in ACTIONS(state):
            v = minimax(RESULT(state, action, 'X'), depth, False)
            #best_value = max(best_value, v)
            if v[0] > best_value:
                best_value = v[0]
                best_position = action
            state[action] = '-'
        return [best_value, best_position]
    else:
        best_value = sys.maxint
        for action in ACTIONS(state):
            v = minimax(RESULT(state, action, 'O'), depth, True)
            #best_value = min(best_value, v)
            if v[0] < best_value:
                best_value = v[0]
                best_position = action
            state[action] = '-'
        return [best_value, best_position]


def print_state(state):
    for i in range(3):
        print state[i*3+0], state[i*3+1], state[i*3+2]


if __name__=='__main__':
    MAX = 'X'
    MIN = 'O'
    NIL = '-'
    state = [NIL, NIL, NIL,
             NIL, NIL, NIL,
             NIL, NIL, NIL]
    game_over = False
    turn = MAX
    i = None
    while not game_over:
        print("**********************************************")
        if turn == MIN:
            i = input('> ')
            turn = MAX
            state[i] = MIN
        else:
            r = minimax(state, -1, True)
            turn = MIN
            state[r[1]] = MAX
        print_state(state)
