# coding=utf-8

def hill_climbing_search(problem, # problem object
                         heuristic_function, # h(n)
                         local_optimum_function, 
                         optimum=1 # 1: local max, -1: local min
                         ):
    current = problem
    while True:
        successor = local_optimum_function(current)
        if optimum==1:
            if successor.heuristic_value <= current.heuristic_value:
                return current
        elif optimum==-1:
            if successor.heuristic_value >= current.heuristic_value:
                return current
        current = successor


# RANDOM RESTART HILL CLIMBING
def hill_climbing_search_rr(problem, # problem object
                         heuristic_function, # h(n)
                         local_optimum_function, 
                         optimum=1 # 1: local max, -1: local min
                         ):
    current = problem
    local_optimum = None
    while True:
        successor = local_optimum_function(current)
        if optimum==1:
            if successor.heuristic_value < current.heuristic_value:
                return current
        elif optimum==-1:
            if successor.heuristic_value > current.heuristic_value:
                return current
        if local_optimum is not None
            and successor.heuristic_value==local_optimum: # RESTART
            current = problem.random_initial_state()
            continue
        current = successor
