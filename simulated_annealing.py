# coding=utf-8
import random
import math
import n_queen


def simulated_annealing_search(problem):
    # annealing parameters
    alpha = 0.99
    T = 10000.0
    T_min = 3.95
    current = problem
    while T > T_min:
        T = T * alpha
        successor = n_queen.NQueenState.random_successor(current)
        E = current.heuristic_value - successor.heuristic_value
        #print "E: ", E
        if E > 0:
            # (old-new) > 0 is ``good`` trade for n-queen
            current = successor
        elif math.exp(E/T) > random.random():
            current = successor
        if current.heuristic_value == 0:
            return current
    return current
