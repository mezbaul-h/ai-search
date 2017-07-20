# coding=utf-8

import math
import random
import time
import hill_climbing as HC

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
                if (board[i] == board[j] + (j-i))                              \
                    or (board[i] == board[j] - (j-i)):
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

def generate_board(N=4):
    board = [i for i in range(N)]
    random.shuffle(board)
    return board

if __name__=='__main__':
    problem = NQueenState(generate_board())
    print HC.hill_climbing_search_rr(problem, generate_board, -1).board
