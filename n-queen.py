# coding=utf-8

import math
import random
import time

class NQState(object):
    def __init__(self, b=None, c=None):
        self.board = [i[:] for i in b]
        self.queen_positions = []
        NQState.generate_queen_positions(self.board, self.queen_positions)
        self.heuristic_value = NQState.heuristic(self.queen_positions)

    def get_queen_position(self, index):
        return self.queen_positions[index]

    @staticmethod
    def generate_queen_positions(board, q):
        for i in range(8):
            for j in range(8):
                if board[i][j]==1:
                    q.append((i,j))

    @staticmethod
    def heuristic(queen_positions):
        # heuristic for N queen
        # no of pairs that attack each other either directly
        # or indirectly
        heur_value=0
        for i in range(8):
            for j in range(8):
                if i!=j:
                    if queen_positions[i][0]==queen_positions[j][0] or queen_positions[i][1]==queen_positions[j][1]:
                        heur_value+=1
                    if abs(queen_positions[i][0]-queen_positions[j][0])==abs(queen_positions[i][1]-queen_positions[j][1]):
                        heur_value+=1
        #print heur_value
        return heur_value/2

def generate_successors(current_state):
    successors=[]
    for i in range(8):
        current_queen = current_state.get_queen_position(i)
        for j in range(8):
            for k in range(8):
                if current_state.board[j][k]==1:
                    continue
                _ = [l[:] for l in current_state.board]
                _[current_queen[0]][current_queen[1]] = 0
                _[j][k] = 1
                new_state = NQState(_)
                successors.append(new_state)
    return successors


def lowest_valued_successor(current):
    lvs = None
    for state in generate_successors(current):
        if lvs is None:
            lvs = state
        elif lvs.heuristic_value > state.heuristic_value:
            lvs = state
    return lvs

def generate_board():
    qset=set()
    while True:
        if len(qset)==8:
            break
        x=random.randint(0,7)
        y=random.randint(0,7)
        if (x,y) not in qset:
            qset.add((x,y))
    board=[[0]*8 for i in range(8)]
    for i in qset:
        board[i[0]][i[1]] = 1
    return NQState(board)

def hill_climb(problem):
    current = problem
    it=0
    while True:
        print "H(n): ", current.heuristic_value
        successor = lowest_valued_successor(current)
        if successor.heuristic_value > current.heuristic_value:
            return current
        elif it==7:
            current = generate_board()
            print "RESTARTING..."
        else:
            current = successor
        it=(it+1)%8

if __name__=='__main__':
    problem = generate_board()
    print hill_climb(problem).board
