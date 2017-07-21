# coding=utf-8
import math
import random
import time
import hill_climbing as HC
import simulated_annealing as SA


def generate_board(N=4):
    board = [i for i in range(N)]
    random.shuffle(board)
    return board


class NQueenState(object):
    def __init__(self, _board):
        self.board = _board
        self.heuristic_value = NQueenState.heuristic(self.board)

    @staticmethod
    def heuristic(board):
        # heuristic for N queen
        # no of pairs that attack each other either directly
        # or indirectly
        h = 0
        N = len(board)
        for i in range(N):
            for j in range(i+1, N):
                if board[i] == board[j]:
                    h+=1
                if ((board[i] == board[j] + (j-i))
                    or (board[i] == board[j] - (j-i))):
                    h+=1
        return h

    @staticmethod
    def successors(current_state):
        successors = []
        N = len(current_state.board)
        for i in range(N):
            for j in range(N):
                if current_state.board[i] != j:
                    L = current_state.board[:]
                    L[L.index(current_state.board[i])] = j
                    successors.append(NQueenState(L))
        return successors

    @staticmethod
    def best_successor(current):
        lowest_successor = None
        for successor in NQueenState.successors(current):
            if lowest_successor is None:
                lowest_successor = successor
            elif lowest_successor.heuristic_value > successor.heuristic_value:
                lowest_successor = successor
        return lowest_successor

    @staticmethod
    def random_successor(current):
        successors = NQueenState.successors(current)
        return random.choice(successors)

    @staticmethod
    def random_state(N):
        return NQueenState(generate_board(N))


if __name__=='__main__':
    N = 8 #int(raw_input('Enter value of N:\n> '), 10)
    problem = NQueenState(generate_board(N))
    print "PROBLEM:", problem.board
    t1 = time.clock()
    hc_rr = HC.hill_climbing_search_rr(problem)
    t2 = time.clock()
    #sa = SA.simulated_annealing_search(problem)
    print "HC RR: H = {}, TIME = {}s".format(hc_rr.heuristic_value, t2-t1)
    #print "SA: H = {}, B = {}".format(sa.heuristic_value, sa.board)
