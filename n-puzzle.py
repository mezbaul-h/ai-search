# coding: utf-8
# n-puzzle using A*

goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

start = [
    [1,2,3],
    [6,0,8],
    [4,7,5]
]

h = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]]

def state_to_string(state):
    result=""
    for i in state:
        for j in i:
            result+=str(j)
    return result

def string_to_state(s):
    s=list(s)
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            result[i][j] = int(s.pop(0), 10)
    return result

def heuristic_cost_estimate(start, goal=None):
    # h1: the sum of the distances of the tiles from their goal positions
    #     also known as the manhattan distance
    global h
    h1=0
    for i in range(3):
        for j in range(3):
            if start[i][j]==0:
                continue
            h1+=abs(h[start[i][j]][0]-i)
            h1+=abs(h[start[i][j]][1]-j)
    return h1

def state_with_lowest_fscore(openSet, fScore):
    lowest=[None,None]
    for i in openSet:
        if lowest[0] is None:
            lowest[0] = i
            lowest[1] = fScore[i]
        elif lowest[1] >= fScore[i]:
            lowest[0] = i
            lowest[1] = fScore[i]

    return lowest

def move_left(state):
    _ = [i[:] for i in state]
    for i in range(3):
        for j in range(3):
            if _[i][j]==0:
                if (j-1)<0:
                    return -1
                else:
                    a = _[i][j]
                    _[i][j]=_[i][j-1]
                    _[i][j-1]=a
                    return _

def move_right(state):
    _ = [i[:] for i in state]
    for i in range(3):
        for j in range(3):
            if _[i][j]==0:
                if (j+1)>2:
                    return -1
                else:
                    a = _[i][j]
                    _[i][j]=_[i][j+1]
                    _[i][j+1]=a
                    return _

def move_up(state):
    _ = [i[:] for i in state]
    for i in range(3):
        for j in range(3):
            if _[i][j]==0:
                if (i-1)<0:
                    return -1
                else:
                    a = _[i][j]
                    _[i][j]=_[i-1][j]
                    _[i-1][j]=a
                    return _

def move_down(state):
    _ = [i[:] for i in state]
    for i in range(3):
        for j in range(3):
            if _[i][j]==0:
                if (i+1)>2:
                    return -1
                else:
                    a = _[i][j]
                    _[i][j]=_[i+1][j]
                    _[i+1][j]=a
                    return _

def generate_states(state):
    state = string_to_state(state)
    successors = [move_down(state),move_up(state),move_left(state),move_right(state)]
    successors = filter(lambda x:x!=-1, successors)
    successors = map(lambda x:state_to_string(x), successors)
    return successors

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path

def solve(start, goal):
    openSet = [start] # states to be evaluated
    closedSet = [] # states already evaluated

    cameFrom = {}
    gScore = {} # g(n)
    gScore[state_to_string(start)] = 0
    fScore = {} # f(n)
    fScore[state_to_string(start)] = heuristic_cost_estimate(string_to_state(start))

    while openSet:
        current, _ = state_with_lowest_fscore(openSet, fScore)
        if current==goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.append(current)

        for neighbor in generate_states(current):
            if neighbor in closedSet:
                continue

            if neighbor not in openSet:
                openSet.append(neighbor)

            tentative_gscore = gScore[current] + 1 #dist_between(current, neighbor)=1 always for A*
            if  (neighbor in gScore) and (tentative_gscore >= gScore[neighbor]):
                continue

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gscore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(string_to_state(neighbor))

    return False



if __name__=='__main__':
    print solve(state_to_string(start), state_to_string(goal))
