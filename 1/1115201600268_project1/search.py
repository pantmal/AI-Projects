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
    
    class Node: #Class Node is used to keep some helpful information regarding each state. Such as its parent state, the action that got us there etc.
        def __init__(self, parent, state, action): 
            self.parent = parent
            self.state = state
            self.action = action

    from util import Stack #Since we're using DFS, we need an LIFO stucture, so we use the Stack from util.py

    fringe = Stack()
    visited_nodes = Stack()
    
    curr = Node(None,problem.getStartState(),None)
    fringe.push(curr) #The fringe gets the starting node here
    
    while 1:
        if fringe.isEmpty(): #Something went really wrong if we reached an empty fringe.
            print "Exception: Pop from empty fringe!"

        already_in = 0 
        curr_node = fringe.pop() #Popping a node from the fringe
        curr_state = curr_node.state
        
        for x in visited_nodes.list: #Checking if the current state is already visited. If so, we skip it and pop the next node from the fringe.
            if curr_state == x:
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(curr_state)
            
            
        if problem.isGoalState(curr_state) == True: #If we reach the goal state, the algorithm ends here
            break
        
        successors = problem.getSuccessors(curr_state) #Getting successors from our current state 
        
        for x,y,z in successors:   
            if x in visited_nodes.list: #If a successor node is already visited don't push him in the fringe
                continue
            sub_node = Node(curr_node,x,y) #Otherwise place the successor state in the fringe along with its parent (our current state) and the action that brough us there.
            fringe.push(sub_node)
            

    path = [] 
    while curr_node.action != None: #Constructing the path. The idea, which is the same for all algorithms, is to follow parent states back to the starting state and insert each action at the start of the list in order to create the path.
        path.insert(0, curr_node.action)
        curr_node = curr_node.parent

    return path
    

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    
    from util import Queue, Stack

    class Node:
        def __init__(self, parent, state, action):
            self.parent = parent
            self.state = state
            self.action = action


    fringe = Queue() #For BFS, the idea is pretty much the exact same thing as in DFS except I used a Queue for the fringe, since the algorithm follows a FIFO policy.
    visited_nodes = Stack()
    
    curr = Node(None,problem.getStartState(),None)
    fringe.push(curr) 

    while 1:
        
        if fringe.isEmpty():
            print "Exception: Pop from empty fringe!"

        already_in = 0 
        curr_node = fringe.pop()
        curr_state = curr_node.state
        
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
        
        for x,y,z in successors:   
            if x in visited_nodes.list:
                continue
            sub_node = Node(curr_node,x,y) 
            fringe.push(sub_node)
            

    path = []
    while curr_node.action != None:
        path.insert(0, curr_node.action)
        curr_node = curr_node.parent


    return path
    
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    from util import PriorityQueue, Stack

    class Node_Cost: #Node_Cost is a variant of the Node class from the previous algorithms. It also uses the cost of each state, since it is needed for UCS.
        def __init__(self, parent, state, action, cost):
            self.parent = parent
            self.state = state
            self.action = action
            self.cost = cost


    fringe = PriorityQueue() #Similar idea also implemented, except I used the PriorityQueue structure in order to prioritize the actions with the smaller costs.
    visited_nodes = Stack()
    
    curr = Node_Cost(None,problem.getStartState(),None,0)
    fringe.push(curr,curr.cost) 
    
    while 1:
        
        if fringe.isEmpty():
            print "Exception: Pop from empty fringe!"

        already_in = 0 
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
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            sub_node = Node_Cost(curr_node,x,y,z+curr_cost) #Notice how in the fringe we push the cost of the current node along with cost of all the previous actions.
            fringe.push(sub_node, sub_node.cost)

    
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

    class Node_Star: #Another variant of the Node Class. For A* we add the cost along with the heuristic function (the hn argument)
        def __init__(self, parent, state, action, cost, hn):
            self.parent = parent
            self.state = state
            self.action = action
            self.cost = cost
            self.hn = hn


    fringe = PriorityQueue() #PriorityQueue is also used here, only it prioritizes the sum of both the cost and the result of the heuristic function, since we're using A*.
    visited_nodes = Stack()
    
    start_hn = heuristic(problem.getStartState(),problem)
    curr = Node_Star(None,problem.getStartState(),None,0,start_hn)

    fringe.push(curr,curr.cost+start_hn) 
    
    while 1:
        
        if fringe.isEmpty():
            print "Exception: Pop from empty fringe!"

        already_in = 0 
        curr_node = fringe.pop()
        curr_state = curr_node.state
        curr_cost = curr_node.cost
        curr_hn = curr_node.hn
        
        
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
        
        for x,y,z in successors:   
            if x in visited_nodes.list:
                continue
            sub_hn = heuristic(x,problem)
            sub_node = Node_Star(curr_node,x,y,z+curr_cost, sub_hn) 
            fringe.push(sub_node, sub_node.cost + sub_node.hn) #The fringe prioritizes the nodes that have the least f(n) (where f(n)=g(n)+h(n)).
            

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
