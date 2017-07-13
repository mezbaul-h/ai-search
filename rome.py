import time
import random

map_data = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}


class Queue_p(object):
    """Simple priority queue"""
    def __init__(self, el=None):
        self._data = []
        if el:
            self._data.append(el)

    def empty(self):
        return True if len(self._data)==0 else False

    def insert(self, el):
        self._data.append(el)
        self._data = sorted(self._data, key = lambda k:k["Cost"])

    def first(self):
        return self._data[0]

    def remove_first(self):
        return self._data.pop(0)

    def has_higher_cost_than(self, s):
        for i in self._data:
            if i["State"] == s["State"] and i["Cost"] > s["Cost"]:
                return True
            else:
                return False
        return False

    def replace_node(self, s):
        for n,i in enumerate(self._data):
            if i["State"] == s["State"]:
                self._data[n] = s
                self._data = sorted(self._data, key = lambda k:k["Cost"])

    def __contains__(self, k):
        return k in map(lambda x:x["State"], self._data)

    def __str__(self):
        s=""
        for i in self._data:
            if s:
                s+=(", ("+i["State"]+", "+str(i["Cost"])+")")
            else:
                s+=("("+i["State"]+", "+str(i["Cost"])+")")
        return "["+s+"]"


def UCS(problem):
    fringe = Queue_p(problem)
    explored_states = set()
    n=1
    while not fringe.empty():
        #print("ITERATION %d: %s" % (n, fringe))
        node = fringe.remove_first()
        explored_states.add(node["State"])
        n+=1
        if problem["Goal"] == node["State"]: # GOAL TEST
            return (node,n)
        # EXPAND CURRENT NODE
        for state in sorted(map_data[node["State"]].keys()):
            child = {
                "State": state,
                "Parent": node["State"],
                "Cost": node["Cost"] + map_data[node["State"]][state],
                "Path": node["Path"] + [state+"("+str(node["Cost"] + map_data[node["State"]][state])+")"]
            }
            if (child["State"] not in explored_states):# and (child["State"] not in fringe):
                if child["State"] == problem["Goal"]:
                    return (child,n)
                fringe.insert(child)
            elif (child["State"] in fringe) and fringe.has_higher_cost_than(child):
                fringe.replace_node(child)
    return (False,0)


class Queue_f(object):
    """Simple FIFO queue"""
    def __init__(self, el=None):
        self._data = []
        if el:
            self._data.append(el)

    def empty(self):
        return True if len(self._data)==0 else False

    def insert(self, el):
        self._data.append(el)

    def insert_all(self, el):
        for i in el:
            self._data.append(i)

    def first(self):
        return self._data[0]

    def remove_first(self):
        return self._data.pop(0)

    def __str__(self):
        s=""
        for i in self._data:
            if s:
                s+=(", ("+i["State"]+", "+str(i["Cost"])+")")
            else:
                s+=("("+i["State"]+", "+str(i["Cost"])+")")
        return "["+s+"]"


def BFS(problem):
    fringe = Queue_f(problem)
    explored_states = set()
    n=1
    while not fringe.empty():
        #print("ITERATION %d: %s" % (n, fringe))
        node = fringe.remove_first()
        explored_states.add(node["State"])
        n+=1
        if problem["Goal"] == node["State"]: # GOAL TEST
            return (node,n)
        # EXPAND CURRENT NODE
        for state in sorted(map_data[node["State"]].keys()):
            child = {
                "State": state,
                "Parent": node["State"],
                "Cost": node["Cost"] + map_data[node["State"]][state],
                "Path": node["Path"] + [state+"("+str(node["Cost"] + map_data[node["State"]][state])+")"]
            }
            if child["State"] not in explored_states:
                if child["State"] == problem["Goal"]:
                    return (child,n)
                fringe.insert(child)
    return (False,0)



class Queue_l(object):
    """Simple LIFO queue"""
    def __init__(self, el=None):
        self._data = []
        if el:
            self._data.append(el)

    def empty(self):
        return True if len(self._data)==0 else False

    def insert(self, el):
        self._data.append(el)

    def insert_all(self, el):
        for i in el:
            self._data.append(i)

    def first(self):
        return self._data[0]

    def remove_first(self):
        return self._data.pop()

    def __str__(self):
        s=""
        for i in self._data:
            if s:
                s+=(", ("+i["State"]+", "+str(i["Cost"])+")")
            else:
                s+=("("+i["State"]+", "+str(i["Cost"])+")")
        return "["+s+"]"


def DFS(problem):
    fringe = Queue_l(problem)
    explored_states = set()
    n=1
    while not fringe.empty():
        #print("ITERATION %d: %s" % (n, fringe))
        node = fringe.remove_first()
        explored_states.add(node["State"])
        n+=1
        if problem["Goal"] == node["State"]: # GOAL TEST
            return (node,n)
        # EXPAND CURRENT NODE
        for state in sorted(map_data[node["State"]].keys(), reverse=True):
            child = {
                "State": state,
                "Parent": node["State"],
                "Cost": node["Cost"] + map_data[node["State"]][state],
                "Path": node["Path"] + [state+"("+str(node["Cost"] + map_data[node["State"]][state])+")"]
            }
            if child["State"] not in explored_states:
                if child["State"] == problem["Goal"]:
                    return (child,n)
                fringe.insert(child)
    return (False,0)

def DLS(problem, limit):
    fringe = Queue_l(problem)
    explored_states = set()
    n=0
    cutoff=False
    while not fringe.empty():
        #print("ITERATION %d: %s" % (n, fringe))
        node = fringe.remove_first()
        explored_states.add(node["State"])
        n+=1
        if node["Depth"]==limit: #limit reached
            cutoff=True
            continue
        if problem["Goal"] == node["State"]: # GOAL TEST
            return (node,n)
        # EXPAND CURRENT NODE
        for state in sorted(map_data[node["State"]].keys(), reverse=True):
            child = {
                "State": state,
                "Parent": node["State"],
                "Depth": node["Depth"]+1,
                "Cost": node["Cost"] + map_data[node["State"]][state],
                "Path": node["Path"] + [state+"("+str(node["Cost"] + map_data[node["State"]][state])+")"]
            }
            if child["State"] not in explored_states:
                if child["State"] == problem["Goal"]:
                    return (child,n)
                fringe.insert(child)
    if cutoff:
        return ("cutoff",n)
    return (False,n)


def IDS(problem):
    n=1
    it=0
    while True:
        result = DLS(problem, n)
        it+=result[1]
        if result[0]!="cutoff":
            return (result[0],it)
        n+=1


def print_result(algorithm,result,t):
    if not result[0]:
        print ("%s:\n\tFailure!"%(algorithm))
        return
    elif result[0]=="cutoff":
        print ("%s:\n\tCutoff!"%(algorithm))
        return
    print ("%s:\n\tIterations: %d"%(algorithm,result[1]))
    print ("\tPath: %s\n\tCost: %d"%(" --> ".join(result[0]["Path"]), result[0]["Cost"]))
    print ("\tTime: %f"%(t))

map_data_keys = list(map_data)
def generate_problems():
    explored=set()
    for i in range(10):
        c1=random.choice(map_data_keys) #initial
        c2=random.choice(map_data_keys) #goal
        while True:
            if c1==c2:
                c2=random.choice(map_data_keys)
            elif (c1,c2) in explored:
                c1=random.choice(map_data_keys)
                c2=random.choice(map_data_keys)
            else:
                break
        explored.add((c1,c2))
        print("***********************************************************")
        print("INITIAL: %s, GOAL: %s"%(c1,c2))
        print("***********************************************************")
        problem = {
            "Goal": c2,
            "Cost": 0,
            "State": c1,
            "Parent": None,
            "Path": [c1+"(0)"],
            "Depth": 0
        }
        t1=time.clock()
        result = BFS(problem)
        t2=time.clock()
        print_result("Breadth-firtst Search",result,t2-t1)
        t1=time.clock()
        result = UCS(problem)
        t2=time.clock()
        print_result("Uniform-cost Search",result,t2-t1)
        t1=time.clock()
        result = DFS(problem)
        t2=time.clock()
        print_result("Depth-firtst Search",result,t2-t1)
        t1=time.clock()
        result = IDS(problem)
        t2=time.clock()
        print_result("Iterative deepening depth first Search",result,t2-t1)

generate_problems()
