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
    

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

   

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
        """
        already_in = 0 
        for x in visited_nodes.list:
            if node_dirl[0] == x:
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(node_dirl[0])   

        """
        visited_nodes.push(node_dirl[0]) #Search for those visited twice
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
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list: #NOT SURE yet about the or
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

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    

    from util import Queue, Stack

    fringe = Queue()
    visited = Stack()
    visited_nodes = Stack()
    #right_path = Stack()
    ListofPaths = []

    node_dir = (problem.getStartState(),None)
    start_succs = problem.getSuccessors(problem.getStartState())
    for x,y,z in start_succs:
        temp_tup = (x,y)
        temp_path = []
        temp_path.append(temp_tup)
        ListofPaths.append(temp_path)


    # start_state = node_dir


    fringe.push(node_dir) 

    c = 0
    while 1:
        print "C IS"
        print c
        #if c == 200:
        #    print visited_nodes.list
        #    break
        
        if fringe.isEmpty():
            print "Exception"
        
        already_in = 0 #TRy this in DFS
        node_dirl = fringe.pop()
        
        for x in visited_nodes.list:
            if node_dirl[0] == x:
                already_in = 1        

        if already_in == 1:
            continue
        else:
            visited_nodes.push(node_dirl[0])    
        
        #visited_nodes.push(node_dirl[0])  
        
        found_last = 0  
        if node_dirl[1] != None: ###Let's try here!
            if c > 2:
                for i in ListofPaths: #For every path
                    if found_last == 1:
                            break
                    for x,y in i: #for every tuple in the path
                        if found_last == 1:
                            break
                        temp_node = i[-1][0] #Getting last node (i.e 5,2)
                        temp_succs = problem.getSuccessors(temp_node)
                        for x,y,z in temp_succs:
                            if x == node_dirl[0]:
                                found_last = 1
                                i.append(node_dirl)
                                break          
                if found_last == 0:
                    for i in ListofPaths: #For every path
                        if found_last == 1:
                            break
                        for x,y in i: #for every tuple in the path
                            if found_last == 1:
                                break
                            temp_node = i[-2][0] #Getting second last node (i.e 5,2)
                            temp_succs = problem.getSuccessors(temp_node)
                            for x,y,z in temp_succs:
                                if x == node_dirl[0]:
                                    found_last = 1
                                    new_list = list(i)
                                    del new_list[-1] 
                                    new_list.append(node_dirl)
                                    ListofPaths.append(new_list)
                                    break
                               

        #^^^ Is slow.. Sigh....                                        

        if problem.isGoalState(node_dirl[0]) == True:
            break
        
        successors = problem.getSuccessors(node_dirl[0])
        lens = len(successors)
                         
        print successors

        
        
        for x,y,z in successors:   
            temp_tup = (x,y)
            if x in visited_nodes.list:
                continue
            is_in =0
            for i,j in fringe.list: #NOT SURE yet about this
                if x == i:
                    is_in = 1
                    break
            if is_in == 0:
                fringe.push(temp_tup) 


        
        print fringe.list
        c += 1



    #print ListofPaths
    for i in ListofPaths:
        for x,y in i:
            if problem.isGoalState(x) == True:
                copy_path = list(i)
                break

    actions = []
    for x,y in copy_path:
        actions.append(y)

    return actions
    
    
    util.raiseNotDefined()