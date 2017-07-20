# coding=utf-8
from n_queen import NQueenState

def hill_climbing_search(problem, # problem object
                         optimum=-1 # 1: local max, -1: local min
                        ):
    current = problem
    while True:
        successor = NQueenState.best_successor(current)
        if optimum==1:
            if successor.heuristic_value <= current.heuristic_value:
                return current
        elif optimum==-1:
            if successor.heuristic_value >= current.heuristic_value:
                return current
        current = successor


# RANDOM RESTART HILL CLIMBING
def hill_climbing_search_rr(problem, # problem object,
                            random_initial_state,
                            optimum=-1 # 1: local max, -1: local min
                           ):
    current = problem
    local_optimum = None
    while True:
        successor = NQueenState.best_successor(current)
        if optimum==1:
            if successor.heuristic_value < current.heuristic_value:
                return current
        elif optimum==-1:
            if successor.heuristic_value > current.heuristic_value:
                return current
        if local_optimum is not None                                           \
            and successor.heuristic_value==local_optimum: # RESTART
            current = NQueenState(random_initial_state())
            local_optimum = None
            continue
        current = successor
        local_optimum = current.heuristic_value
