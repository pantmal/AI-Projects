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
    "*** YOUR CODE HERE ***"

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    from util import Stack

    fringe = Stack()
    visited = Stack()
    visited_nodes = Stack()
    right_path = Stack()
    node_dir = (problem.getStartState(),None)

    fringe.push(node_dir) 
    
    c = 0
    while 1:
        print "C IS"
        print c
        #if c == 41:
        #    print visited_nodes.list
        #    break
        if fringe.isEmpty():
            print "Exception"
        
        node_dirl = fringe.pop()
        visited_nodes.push(node_dirl[0])
        right_path.push(node_dirl[0])

        if node_dirl[1] != None:
            visited.push(node_dirl[1])
        if problem.isGoalState(node_dirl[0]) == True:
            break
        
        
        successors = problem.getSuccessors(node_dirl[0])
        lenv = len(right_path.list)
        prev_node = node_dirl[0]

        
        lenv = lenv - 1
        while 1:

            successors = problem.getSuccessors(prev_node)
            lens = len(successors)

            vis_succ = 0
            for k,l,m in successors:
                if  k in visited_nodes.list:
                    vis_succ = vis_succ + 1

            if vis_succ == lens:
                
                if len(visited.list) != 0:
                    del visited.list[-1]
                    del right_path.list[-1]
                lenv = lenv - 1
                prev_node = right_path.list[lenv]
            else:
                break
                                      

        #if c == 32:
        print successors    
        
        for x,y,z in reversed(successors):   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            fringe.push(temp_tup) 
        
        print fringe.list
        c += 1

    print "VISITED"
    print visited.list
    return visited.list
    

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    util.raiseNotDefined()