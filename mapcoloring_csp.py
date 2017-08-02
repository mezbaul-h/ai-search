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

C1 = 11
C2 = 12
C3 = 13
C4 = 14
C5 = 15
C6 = 16
C7 = 17
C8 = 18
C9 = 19

graph1 = {
    NT: [WA, SA, Q],
    WA: [SA, NT],
    SA: [WA, NT, Q, NSW, V],
    Q: [NT, SA, NSW],
    V: [NSW, SA],
    NSW: [V, SA, Q],
    T: []
}

graph2 = {
    C1: [C2, C4],
    C2: [C1, C3, C4, C5],
    C3: [C2, C5, C6],
    C4: [C1, C2, C5, C7],
    C5: [C2, C3, C4, C6, C7, C8],
    C6: [C3, C5, C8, C9],
    C7: [C4, C5, C8],
    C8: [C5, C6, C7, C9],
    C9: [C6, C8]
}

# state
"""
{
    city: color,
    ....
}
"""
def assignment_valid(city, color, state):
    global graph2
    for adj_city in graph2[city]:
        if color == state[adj_city]:
            return False
    return True


def assignment_complete_and_valid(state):
    if state is None:
        return False
    for city in state:
        if state[city] == NO_COLOR:
            return False
        elif not assignment_valid(city, state[city], state):
            return False
    return True


def assignment_complete(state):
    if state is None:
        return False
    for city in state:
        if state[city] == NO_COLOR:
            return False
    return True


def unassigned_city(state):
    for city in state:
        if state[city] == NO_COLOR:
            return city
    return None

def coloring(state): # recursive map coloring, backtrack
    global NO_COLOR, RED, GREEN, BLUE
    if assignment_complete(state):
        print "STATEC:", state
        return state
    else:
        city = unassigned_city(state)
        print "CITY:", city
        for color in [RED, GREEN, BLUE]:
            if assignment_valid(city, color, state):
                state[city] = color
                result = coloring(state)
                if assignment_complete(result):
                    return result
                state[city] = NO_COLOR

initial_state1 = {
    NT: NO_COLOR,
    WA: NO_COLOR,
    SA: NO_COLOR,
    Q: NO_COLOR,
    V: NO_COLOR,
    NSW: NO_COLOR,
    T: NO_COLOR
}
initial_state2 = {
    C1: NO_COLOR,
    C2: NO_COLOR,
    C3: NO_COLOR,
    C4: NO_COLOR,
    C5: NO_COLOR,
    C6: NO_COLOR,
    C7: NO_COLOR,
    C8: NO_COLOR,
    C9:NO_COLOR
}
print rmap_coloring(initial_state2)
