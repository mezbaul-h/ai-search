# coding=utf-8

NO_COLOR = 0
RED = 1
GREEN = 2
BLUE = 3

NT = 4
WA = 5
SA = 6
Q = 7
NSW = 8
V = 9
T = 10

graph = {
    NT: [WA, SA, Q],
    WA: [SA, NT],
    SA: [WA, NT, Q, NSW, V],
    Q: [NT, SA, NSW],
    V: [NSW, SA],
    NSW: [V, SA, Q],
    T: []
}

# state
"""
{
    city: color,
    ....
}
"""
def assignment_consistent(city, color, state):
    global graph
    consistent = True
    for adj_city in graph[city]:
        if color == state[adj_city]:
            consistent = False
            break
    return consistent


def assignment_complete_and_valid(state):
    complete = True
    for city in state:
        if state[city] == NO_COLOR:
            complete = False
            break
        elif not assignment_consistent(city, state[city], state):
            complete = False
            break
    return complete


def assignment_complete(state):
    complete = True
    for city in state:
        if state[city] == NO_COLOR:
            complete = False
            break
    return complete


def unassigned_city(state):
    for city in state:
        if state[city] == NO_COLOR:
            return city
    return None

def rmap_coloring(state): # recursive map coloring, backtrack
    global NO_COLOR, RED, GREEN, BLUE
    if assignment_complete(state):
        return state

    city = unassigned_city(state)
    for color in [RED, GREEN, BLUE]:
        if assignment_consistent(city, color, state):
            state[city] = color
            return rmap_coloring(state)
            #if assignment_complete_and_valid(result):
            #    return result
            state[city] = NO_COLOR
initial_state = {
    NT: NO_COLOR,
    WA: NO_COLOR,
    SA: NO_COLOR,
    Q: NO_COLOR,
    V: NO_COLOR,
    NSW: NO_COLOR,
    T: NO_COLOR
}
print rmap_coloring(initial_state)
