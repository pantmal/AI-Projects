#if tup in remaining_Corners:
            #    remaining_Corners.remove(tup)


αλγόριθμο πρώτα σεβάθος με επαναληπτική εκβάθυνση

Αναζήτηση πρώτα σε βάθος με επαναληπτική εκβάθυνση
Άπληστη αναζήτηση πρώτα στον καλύτερο

Checking if the current state is already visited. If so, we skip it and pop the next node from the fringe.

Uniform Cost Search Corners Problem: Representation

For BFS, the idea is pretty much the exact same thing as in DFS except we use a Queue for the fringe, since the algorithm follows a FIFO policy.
Similar idea also implemented, except we use the PriorityQueue structure in order to prioritize the actions with the smaller costs.
PriorityQueue is also used here, only it prioritizes the sum of both the cost and the result of the heuristic function, since we're using A*.

The idea for the Corners Problem: Each state is comprised of the coordinates of Pacman's position and the corners that Pacman has not travelled. 
        allCorners = list(self.corners_lst) # For the starting state we place all the corners as part of the state since Pacman hasn't reached any corner yet. 
If the position is one of the goals and we haven't any other corners remaining, this means we have reached our goal state so the algorithm ends here.
Copying the list of our current remaining corners, to see what will be passed in the successor state. If successor's position is one of the corners
We remove it from our list. So the successor state will know that Pacman has reached one of the desired corners. #So the successor state is comprised of the new coordinates along with the remaining corners.

Corners Problem: Heuristic Eating All The Dots: Heuristic
Using the manhattanDistance function from util.py so we can calcuate the desired distances. Since we have a grind and 4 available directions, the Manhattan Distance is our best choice.
If we have no remaining corners we have reached our goal state, so the heuristic function returns 0
Here we get the shortest Manhattan Distance from our current position to the remaining corners.
In addition, we have to calculate the shortest Manhattan Distances from each corner combination and add them.
    #Example: if we have corners[a,b,c,d], we get the shortest of distances (a,b), (a,c), (a,d), the shortest of (b,c), (b,d), and the only distance of (c,d))
    #Since our problem is similar to shortest path problem, I used a logic similar to Dijkstra's algorithm to get the desired distances.
return the sum of all these distances. Notice how suma already has the shortest distance from our current position to the remaining corners.

Getting a list of our remaining food If we have no remaining dots we have reached our goal state, so the heuristic function returns 0
For this heuristic, I used the mazeDistance function provided in this file. Manhattan Distances didn't provide good enough solutions and since mazeDistance can be used here, it was a better option overall.
    #In addition, mazeDistance takes care of the walls in the maze, contrary to the manhattanDistance function.
So, in the first loop we get the distance from our current position to the furthest food.
    #Tried minimum distance at first, but since we're dealing with a problem similar to the Travelling Salesman Problem, the longest distance is preferable, contrary to the shortest one as we used in cornersHeuristic.  
In addition, we also get the longest distance from each food combination. Similar to what we did in cornersHeuristic
If the longest distance of the current combinations is larger than the one from currentState to the furthest food, or larger than the distance from the previous combinations, it is a preferable solution so we return it as the result of the heuristic function.

For finding the path to closest dot I used the UCS algorithm since it is a greedy algorithm

