# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState()) #Keep this in mind

    class Node:
        def __init__(self, parent, action, state):
            self.state = state
            self.parent = parent
            self.action = action

    from util import Stack

    fringe = Stack()
    #visited = Stack()
    visited_nodes = Stack()
    #right_path = Stack()
    node_dir = (problem.getStartState(),None)
    
    curr = Node(None,None,node_dir[0])

    fringe.push(curr) 
    
    c = 0
    while 1:
        print "C IS"
        print c
        #if c == 41:
        #    print visited_nodes.list
        #    break
        if fringe.isEmpty():
            print "Exception"

        already_in = 0 #TRy this in DFS
        curr_node = fringe.pop()
        curr_state = curr_node.state
        
        
        for x in visited_nodes.list:
            if curr_state[0] == x:
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(curr_state)
            
        
        #visited_nodes.push(curr_state)   

        #node_dirl = fringe.pop()
        #visited_nodes.push(node_dirl[0]) #Search for those visited twice

        #right_path.push(node_dirl[0])

        #if node_dirl[1] != None:
        #    visited.push(node_dirl[1])
        if problem.isGoalState(curr_state) == True:
            break
        
        #lenv = len(right_path.list)
        #prev_node = node_dirl[0]                            

        #if c == 32:
        successors = problem.getSuccessors(curr_state)
        print successors    
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            #is_in =0
            #for i in fringe.list: #NOT SURE yet about this
            #    if x == i.state:
            #        is_in = 1
            #        break
            #if is_in == 0:
            ### CHECK AUTO AURIO ###
            sub_node = Node(curr_node,y,x) 
            fringe.push(sub_node)
            

    
    path = []
    while curr_node.action != None:
        path.insert(0, curr_node.action)
        curr_node = curr_node.parent

    return path
    

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    

    from util import Queue, Stack

    class Node:
        def __init__(self, parent, action, state):
            self.state = state
            self.parent = parent
            self.action = action

    #from util import Stack

    fringe = Queue()
    #visited = Stack()
    visited_nodes = Stack()
    #right_path = Stack()
    node_dir = (problem.getStartState(),None)
    
    curr = Node(None,None,node_dir[0])

    fringe.push(curr) 
    
    c = 0
    while 1:
        print "C IS"
        print c
        #if c == 41:
        #    print visited_nodes.list
        #    break
        if fringe.isEmpty():
            print "Exception"

        already_in = 0 #TRy this in DFS
        curr_node = fringe.pop()
        curr_state = curr_node.state
        
        
        for x in visited_nodes.list:
            if curr_state == x:
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(curr_state)   
        
        #visited_nodes.push(curr_state)  

        #node_dirl = fringe.pop()
        #visited_nodes.push(node_dirl[0]) #Search for those visited twice

        #right_path.push(node_dirl[0])

        #if node_dirl[1] != None:
        #    visited.push(node_dirl[1])
        if problem.isGoalState(curr_state) == True:
            break
        
        #lenv = len(right_path.list)
        #prev_node = node_dirl[0]                            

        #if c == 32:
        successors = problem.getSuccessors(curr_state)
        print successors    
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            #is_in =0
            #for i in fringe.list: #NOT SURE yet about this
            #    if x == i.state:
            #        is_in = 1
            #        break
            #if is_in == 0:
                #fringe.push(temp_tup)
            sub_node = Node(curr_node,y,x) 
            fringe.push(sub_node)
            
        
        #print fringe.list
        c += 1

    
    path = []
    while curr_node.action != None:
        path.insert(0, curr_node.action)
        curr_node = curr_node.parent

    return path
    
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    #Here we go!
    
    from util import PriorityQueue, Stack

    class Node_Cost:
        def __init__(self, parent, action, state, cost):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost

    #from util import Stack

    fringe = PriorityQueue()
    #visited = Stack()
    visited_nodes = Stack()
    #right_path = Stack()
    node_dir = (problem.getStartState(),None)
    
    curr = Node_Cost(None,None,node_dir[0],0)

    fringe.push(curr,curr.cost) 
    
    c = 0
    while 1:
        #print "C IS"
        #print c
        
        if fringe.isEmpty():
            print "Exception"

        already_in = 0 #TRy this in DFS
        curr_node = fringe.pop()
        curr_state = curr_node.state
        curr_cost = curr_node.cost
        
        
        for x in visited_nodes.list:
            if curr_state == x:
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(curr_state)   
        

        if problem.isGoalState(curr_state) == True:
            break
        
        successors = problem.getSuccessors(curr_state)
         #print successors    
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            #is_in =0
            #for i,j,k in fringe.heap: #NOT SURE yet about this
            #    if x == k.state:
            #        is_in = 1
            #        break
            #if is_in == 0:
            #    fringe.push(temp_tup)
            sub_node = Node_Cost(curr_node,y,x,z+curr_cost) 
            fringe.push(sub_node, sub_node.cost)
            
        
        #print fringe.list
        c += 1

    
    path = []
    while curr_node.action != None:
        path.insert(0, curr_node.action)
        curr_node = curr_node.parent

    return path



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    from util import PriorityQueue, Stack

    class Node_Star:
        def __init__(self, parent, action, state, cost, hn):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost
            self.hn = hn

    #from util import Stack

    fringe = PriorityQueue()
    #visited = Stack()
    visited_nodes = Stack()
    #right_path = Stack()
    node_dir = (problem.getStartState(),None)
    
    start_hn = heuristic(node_dir[0],problem)
    curr = Node_Star(None,None,node_dir[0],0,start_hn)

    fringe.push(curr,curr.cost+start_hn) 
    
    c = 0
    while 1:
        #print "C IS"
        #print c
        
        if fringe.isEmpty():
            print "Exception"

        already_in = 0 #TRy this in DFS
        curr_node = fringe.pop()
        curr_state = curr_node.state
        curr_cost = curr_node.cost
        curr_hn = curr_node.hn
        
        
        for x in visited_nodes.list:
            if curr_state == x:      ###Erwtima gia ola: curr_state[0]???
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(curr_state)   
        

        if problem.isGoalState(curr_state) == True:
            break
        
        successors = problem.getSuccessors(curr_state)
         #print successors    
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            #is_in =0
            #for i,j,k in fringe.heap: #NOT SURE yet about this
            #    if x == k.state:
            #        is_in = 1
            #        break
            #if is_in == 0:
            #    fringe.push(temp_tup)
            sub_hn = heuristic(x,problem)
            sub_node = Node_Star(curr_node,y,x,z+curr_cost, sub_hn) 
            fringe.push(sub_node, sub_node.cost + sub_node.hn)
            
        
        #print fringe.list
        c += 1

    
    path = []
    while curr_node.action != None:
        path.insert(0, curr_node.action)
        curr_node = curr_node.parent

    return path

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
