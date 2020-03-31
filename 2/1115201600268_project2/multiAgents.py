# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


        "*** YOUR CODE HERE ***"

        #I used the reciprocal of important values as it was noted in the assignment's presentation
        reciprocal_food = 0
        reciprocal_ghosts = 0
        reciprocal_capsule = 0
        
        remaining_Food = newFood
        food_lst = remaining_Food.asList() 

        food_close = 0
        food_distances = [] 
        for k in food_lst: #Getting the Manhattan distances from Pacman's current position to the remaining food states
          food_mh = manhattanDistance(newPos,k)
          if(food_mh==0): #Here, the next state is a food state, so don't calculate any distance
            food_close = 1 
          else:  
            food_distances.append(food_mh)

        if len(food_distances) > 0:
          if(food_close!=1):
            min_food = min(food_distances) 
            reciprocal_food = (1/float(min_food)) #The important value we need here is the reciprocal of closest available food state
        

        ghost_close = 0
        ghost_distances = [] 
        is_scared = 0
        for g in newGhostStates: #Doing similar work for the ghost states
          if newScaredTimes[0] > 0: #If this variable is greater than 0, this means the ghosts in the maze are scared because Pacman has eaten a capsule
            is_scared = 1
          ghost_mh = manhattanDistance(newPos,g.getPosition())
          if(ghost_mh==0): 
            ghost_close = 1
          ghost_distances.append(ghost_mh)
          
        if (ghost_close!=1):
          min_ghost = min(ghost_distances)
          reciprocal_ghosts = (1/float(min_ghost)) #Here, we get the reciprocal of the closest ghost 
        
          
        caps_close = 0
        caps_distances = [] 
        for c in currentGameState.getCapsules(): #Finally, we also get the distances of the capsules
          caps_mh = manhattanDistance(newPos,c)
          if(caps_mh==0):
            caps_close = 1
          caps_distances.append(caps_mh)

        min_capsule = 0
        if len(caps_distances) > 0:
          if (caps_close!=1):
            min_capsule = min(caps_distances)
            reciprocal_capsule = 1/float(min_capsule) #Getting the reciprocal of the closest capsule
          else:
            reciprocal_capsule = 1 #If the next state is capsule state set this value to 1 so Pacman may eat the capsule
          
        if is_scared==0: #To get the result we need, this evaluation function returns our current score, plus the closest food, subtracting the closest ghost distance (so Pacman can avoid it), and we also add the closest capsule.  
          return successorGameState.getScore() + reciprocal_food - reciprocal_ghosts + reciprocal_capsule 
        else: #However if the ghosts are scared, there's no need to avoid them, so return the other values.
          return successorGameState.getScore() + reciprocal_food + reciprocal_capsule 
        
     

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
       
        totalAgents = gameState.getNumAgents() 
                
        def MiniMax_Decision(state): #This function simply sets the algorithm in motion, it has almost the exact same body as the Max_Val function since the root node is Max node.
          
          index = 0 #Index is 0 because Pacman is at the starting state
          depth = 0
          minimax_action = None #Final action that will be returned
          
          temp_node_value = float('-inf')
          legal_Moves = state.getLegalActions(index)
          for move in legal_Moves: #For every successor state, call the Min_Val function to get its value and return the action of the successor state with the greatest value
            successor = state.generateSuccessor(index,move)
            
            succ_val = Min_Val(successor, index + 1, depth)[0]
            if succ_val > temp_node_value:
              temp_node_value, minimax_action = succ_val, move
            
          return minimax_action

        def Max_Val(state, index, depth): #Max_Val is called for the states that Pacman is in
          
          #If we are at a terminal state call the evaluation function to assign a value
          if state.isWin() or state.isLose() or depth == self.depth:
            return (self.evaluationFunction(state),None)

          index = 0
          v_node = float('-inf') #V_node represents the value at each node
          next_action = None
          legal_Moves = state.getLegalActions(index)
          
          for move in legal_Moves: #For every successor state, call the Min_Val function to get its value and return the action of the successor state with the greatest value
            successor = state.generateSuccessor(index,move)
            
            succ_val = Min_Val(successor, index + 1, depth)[0]
            if succ_val > v_node:
              v_node, next_action = succ_val, move
            
          return (v_node, next_action) #Returning the maximum value as well as the action that brings us to this node 



        def Min_Val(state, index, depth): #Min_Val is called for the ghost states

          #If we are at a terminal state call the evaluation function to assign a value
          if state.isWin() or state.isLose() or depth == self.depth:
            return (self.evaluationFunction(state),None)

          v_node = float('inf')
          next_action = None
          legal_Moves = state.getLegalActions(index)
          
          #For each ghost we have two cases
          if index == totalAgents - 1: #If it is the last agent we have, this means every other ghost has received its Minimax value so it's time to call Max_Val so Pacman may continue.  
            for move in legal_Moves: #For every successor state, call the Max_Val function to get its value and return the action of the successor state with smallest value
              successor = state.generateSuccessor(index,move)

              succ_val = Max_Val(successor, index, depth+1)[0] #Depth is incremented only after every other ghost has received its Minimax value 
              if succ_val < v_node:
                v_node, next_action = succ_val, move
            
          else: #Otherwise, call Min_Val again because there are ghosts that haven't received their Minimax values
            for move in legal_Moves:
              successor = state.generateSuccessor(index,move)
            
              succ_val = Min_Val(successor, index + 1, depth)[0]
              if succ_val < v_node:
                v_node, next_action = succ_val, move
            
          return (v_node, next_action) #Returning the minimum value as well as the action that brings us to this node 
      

        return MiniMax_Decision(gameState) #The execution of the algorithm begins here
        
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        #The algorithm is almost the exact same as in Minimax, only here the alpha and beta values are taken into account.

        totalAgents = gameState.getNumAgents()
        alpha = float("-inf")
        beta = float("inf")
                
        def AlphaBeta_Decision(state,alpha,beta): #Alpha and beta are passed in every function call
          
          index = 0
          depth = 0
          ab_action = None 
          
          temp_node_value = float('-inf')
          legal_Moves = state.getLegalActions(index)
          for move in legal_Moves:
            successor = state.generateSuccessor(index,move)
            
            succ_val = Min_Val(successor, index + 1, depth, alpha, beta)[0]
            if succ_val > temp_node_value:
              temp_node_value, ab_action = succ_val, move

            if temp_node_value > beta:
              return ab_action    

            alpha = max(alpha, temp_node_value)
            
          return ab_action

        def Max_Val(state, index, depth, alpha, beta):
          
          if state.isWin() or state.isLose() or depth == self.depth:
            return (self.evaluationFunction(state),None)

          index = 0
          v_node = float('-inf')
          next_action = None
          legal_Moves = state.getLegalActions(index)
          
          for move in legal_Moves:
            successor = state.generateSuccessor(index,move)
            
            succ_val = Min_Val(successor, index + 1, depth, alpha, beta)[0] 
            if succ_val > v_node:
              v_node, next_action = succ_val, move

            if v_node > beta: #If the value of the successor state is greater than beta there's no need to explore the successors, so we prune them by returning the (v_node, next_action) tuple
              return (v_node, next_action)    

            alpha = max(alpha, v_node) #Alpha value is updated if need be
            
          return (v_node, next_action)


        def Min_Val(state, index, depth, alpha, beta):
          if state.isWin() or state.isLose() or depth == self.depth:
            return (self.evaluationFunction(state),None)

          v_node = float('inf')
          next_action = None
          legal_Moves = state.getLegalActions(index)
          
          if index == totalAgents - 1:
            for move in legal_Moves:
              successor = state.generateSuccessor(index,move)

              succ_val = Max_Val(successor, index, depth+1, alpha, beta )[0]
              if succ_val < v_node: 
                v_node, next_action = succ_val, move

              if v_node < alpha: #If the value of the succesor state is less than alpha there's no need to explore the successors, so we prune them by returning the (v_node, next_action) tuple
                return (v_node, next_action)

              beta = min(beta,v_node) #Beta value is updated if need be
            
          else:
            for move in legal_Moves:
              successor = state.generateSuccessor(index,move)
            
              succ_val = Min_Val(successor, index + 1, depth, alpha, beta)[0]
              if succ_val < v_node:
                v_node, next_action = succ_val, move

              if v_node < alpha: #If the value of the succesor state is less than alpha there's no need to explore the successors, so we prune them by returning the (v_node, next_action) tuple
                return (v_node, next_action)

              beta = min(beta,v_node) #Beta value is updated if need be
            
          return (v_node, next_action)
      
        
        return AlphaBeta_Decision(gameState,alpha,beta) #The execution of the algorithm begins here

        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """

        #The algorithm is almost the exact same as in Minimax, only here the Exp_Val function is defined for the ghost states.
        
        totalAgents = gameState.getNumAgents()
                
        def Expectimax_Decision(state):
          
          index = 0
          depth = 0
          expectimax_action = None 
          
          temp = float('-inf')
          legal_Moves = state.getLegalActions(index)
          for move in legal_Moves:
            successor = state.generateSuccessor(index,move)
            
            succ_val = Exp_Val(successor, index + 1, depth)[0]
            if succ_val > temp:
              temp, expectimax_action = succ_val, move
            
          return expectimax_action

        def Max_Val(state, index, depth): #Max_Val is the same as in the Minimax Agent
          
          if state.isWin() or state.isLose() or depth == self.depth:
            return (self.evaluationFunction(state),None)

          index = 0
          v_node = float('-inf')
          next_action = None
          legal_Moves = state.getLegalActions(index)
          
          for move in legal_Moves:
            successor = state.generateSuccessor(index,move)
            
            succ_val = Exp_Val(successor, index + 1, depth)[0]
            if succ_val > v_node:
              v_node, next_action = succ_val, move
            
          return (v_node, next_action)



        def Exp_Val(state, index, depth): #Exp_Val is defined for the ghost states

          if state.isWin() or state.isLose() or depth == self.depth:
            return (self.evaluationFunction(state),None)

          v_node = 0
          next_action = None
          legal_Moves = state.getLegalActions(index)
          
          if index == totalAgents - 1:
            for move in legal_Moves:
              successor = state.generateSuccessor(index,move)
              
              probability = 1.0/len(legal_Moves) #The value we need is calculated by getting the average from the values of each successor state.
            
              succ_val = Max_Val(successor, index, depth+1)[0]
              v_node = v_node + (succ_val*probability)
              
            
          else:
            for move in legal_Moves:
              successor = state.generateSuccessor(index,move)

              probability = 1.0/len(legal_Moves)
            
              succ_val = Exp_Val(successor, index + 1, depth)[0] #Calling Exp_Val for every other ghost
              v_node = v_node + (succ_val*probability)
            
          return (v_node, next_action)
      

        return Expectimax_Decision(gameState) #The execution of the algorithm begins here
        

        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: I used an evaluation function that is quite similar to the one I implemented in the Reflex Agent. However in this one, the max values are used instead of min values.
    """

    #The evaluation function is quite similar to the one I implemented in the Reflex Agent. In this one, I decided to use max values since they provided better scores.
    
    position = currentGameState.getPacmanPosition()
    remaining_Food = currentGameState.getFood()
    food_lst = remaining_Food.asList() 
    food_check = list(food_lst)

    max_food = 1
    if len(food_lst)==0: 
        max_food = 1

    food_distances = [] 
    for k in food_lst: #Getting the Manhattan distances from Pacman's current position to the remaining food states
        food_dis = manhattanDistance(k,position)
        food_distances.append(food_dis)

    if len(food_distances)>0: 
      max_food = 1/float(max(food_distances)) #The best value we need is the reciprocal of the furthest food state
    

    ghost_distances = [] 
    newGhostStates = currentGameState.getGhostStates()

    max_ghost = 1
    ghost_close = 0
    for g in newGhostStates: #Same thing for the ghost states
      ghost_mh = manhattanDistance(position,g.getPosition())
      if(ghost_mh==0):
        ghost_close = 1
      ghost_distances.append(ghost_mh)
      
    if (ghost_close!=1):
      max_ghost = 1/float(max(ghost_distances)) #Getting the reciprocal of the furthest ghost state
        
  
    max_caps = 1
    caps_close = 0
    caps_distances = [] 
    for c in currentGameState.getCapsules(): #Finally, getting the distances of the capsules
      caps_mh = manhattanDistance(position,c)
      if(caps_mh==0):
        caps_close = 1
      caps_distances.append(caps_mh)

    c_val = 0
    if len(caps_distances) > 0:
      if (caps_close!=1):
        max_caps = 1/float(max(caps_distances)) #Getting the reciprocal of the furthest capsule state
    
    #This evaluation function will return our current score as well as the max values we just calculated
    return currentGameState.getScore() + max_food + max_ghost + max_caps

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

