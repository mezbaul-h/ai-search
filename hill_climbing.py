# coding=utf-8
import n_queen


def hill_climbing_search(problem):
    current = problem
    while True:
        successor = n_queen.NQueenState.best_successor(current)
        if successor.heuristic_value <= current.heuristic_value:
            return successor
        current = successor


def hill_climbing_search_rr(problem):
    current = problem
    N = len(problem.board)
    while True:
        successor = n_queen.NQueenState.best_successor(current)
        if successor.heuristic_value > current.heuristic_value:
            return current
        elif successor.heuristic_value == current.heuristic_value:
            successor = n_queen.NQueenState.random_state(N)
        current = successor


# RANDOM RESTART HILL CLIMBING
def hill_climbing_search_rr2(problem):
    current = problem
    N = len(problem.board)
    while current.heuristic_value != 0:
        successor = n_queen.NQueenState.best_successor(current)
        if successor.heuristic_value <= current.heuristic_value:
            successor = n_queen.NQueenState.random_state(N)
        current = successor
    return current
