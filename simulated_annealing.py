# coding=utf-8

def simulated_annealing_search(problem, schedule):
    current = problem
    while True:
        if T==0:
            return current
        successor = current.get_random_successor()
        E = successor.heuristic_value - current.heuristic_value
        if E > 0:
            current = successor
