from csp import *
import time
import sys


#Various puzzles of varying difficulty. Taken from csp.py.

easy = [['*',       '*',  '*',    [6, ''], [3, '']],
        ['*',     [4, ''],[3, 3], '_',      '_'],
        [['', 10], '_',   '_',    '_',      '_'],
        [['', 3],  '_',   '_',    '*',     '*']]

medium = [
    ['*', [10, ''], [13, ''], '*'],
    [['', 3], '_', '_', [13, '']],
    [['', 12], '_', '_', '_'],
    [['', 21], '_', '_', '_']]

hard = [
    ['*', [17, ''], [28, ''], '*', [42, ''], [22, '']],
    [['', 9], '_', '_', [31, 14], '_', '_'],
    [['', 20], '_', '_', '_', '_', '_'],
    ['*', ['', 30], '_', '_', '_', '_'],
    ['*', [22, 24], '_', '_', '_', '*'],
    [['', 25], '_', '_', '_', '_', [11, '']],
    [['', 20], '_', '_', '_', '_', '_'],
    [['', 14], '_', '_', ['', 17], '_', '_']]


#Function which prints the starting board, with the blank spaces.
def print_board(puzzle):

    for i in puzzle:
        print(i)
            

#I implemented a Kakuro class which inherits the CSP class from csp.py.
class Kakuro(CSP):

    def __init__(self, puzzle):
        
        self.board = puzzle

        variables = []
        self.row_sums = []
        self.col_sums = []

        #Storing the variables(every blank spot) as well as the row and column sums.
        for i,lst in enumerate(self.board):
            for j, element in enumerate(lst):
                if element == '_':
                    variables.append((i,j))
                if element != '_' and element != '*':
                    if element[0] == '':
                        self.row_sums.append(element)
                    elif element[1] == '':
                        self.col_sums.append(element)
                    else:
                        self.row_sums.append(element)
                        self.col_sums.append(element)
                                
        #For every variable, the domain consists of values ranging from 1 to 9.
        domains = {v: [x+1 for x in range(9)] for v in variables}

        #Storing the row sum of each variable. For example variable (1,1) will have the row sum of 3 stored in the coordinates: (0,1)
        #So each item in the following array consists of a tuple like: ((1,1),3,(0,1))
        self.row_positions = []
        for var in variables:
            for i,lst in enumerate(self.board):
                if var[0] == i:
                    for j, element in enumerate(lst):
                        if element in self.row_sums: 
                            row_sum_coords = i,j
                            row_sum = element[1]       
                        if (i,j) == var :#or (i,j+1) == B:
                            if var not in self.row_positions:
                                self.row_positions.append((var,row_sum,row_sum_coords))
                            break
            
        #Same thing for column sums
        self.col_positions = []
        for var in variables:
            for i,lst in enumerate(self.board):
                if i == var[0]:
                    if var not in self.col_positions:
                        self.col_positions.append((var, col_sum,col_sum_coords))
                    break
                for j, element in enumerate(lst):
                    if var[1] == j:
                        if element in self.col_sums: 
                            col_sum_coords = i,j
                            col_sum = element[0]
                            
           
        CSP.__init__(self, variables, domains, self.find_neighbors(variables), self.constraints)

    #Each variable may have up to four neighbors. The variables at the same line (left and right) or at the same column (up and down)
    def find_neighbors(self, variables):

        neighbors_dict = dict()
        for var in variables:
            neighbors = []

            left = var[1] - 1
            right = var[1] + 1
            up = var[0] - 1
            down = var[0] + 1

            if (var[0],left) in variables:
                neighbors.append((var[0],left))
            if (var[0],right) in variables:
                neighbors.append((var[0],right)) 
            if (up,var[1]) in variables:
                neighbors.append((up,var[1]))
            if (down,var[1]) in variables:
                neighbors.append((down,var[1]))
            
            neighbors_dict[var] = neighbors
        return neighbors_dict

    #Defining the Constraints of our CSP problem. 
    #Each line has to add up to the row sum which is closest. Also every value has to be different for every sum.
    #Same thing with columns 
    def constraints(self, A, a, B, b):

        
        assignments = self.infer_assignment()
        if A[0] == B[0]: #Neighbor variable is at the same row
            
            #Acquiring the row sum and its coordinates of the variable A
            for x,y,z in self.row_positions:
                if A == x:
                    row_sum = y
                    row_sum_coords = z
                    break
            
            #Getting the coordinates from the first variable in this line
            coords_check1, coords_check2 = row_sum_coords[0], row_sum_coords[1] + 1
            unbound = 0
            sum=0
            
            #Adding up a and b, which have to be different (only if B has an assigned value)
            try:
                assig = assignments[B]
                if assig == a:
                    return False
                sum = a + b
            except KeyError:
                unbound = 1
            

            count = 2  
            #The idea is to keep adding up every assigned variable in this line until we reach a cell with no variable in it.
            while (coords_check1, coords_check2) in self.variables:
                #Skip A and B    
                if (coords_check1, coords_check2) == A or (coords_check1, coords_check2) == B:
                    coords_check1, coords_check2 = coords_check1, coords_check2 + 1
                    continue
                
                count = count + 1

                #Get the assignment of this variable and add it to the sum. If it has the same value with a we have an unsatisfied constraint, so return False
                try:
                    assig = assignments[coords_check1,coords_check2]
                    if assig == a :
                        return False
                    sum = sum + assig
                except KeyError: #Variable has not been assigned yet.
                    unbound = 1
                
                #Proceed to the next variable in this line
                coords_check1, coords_check2 = coords_check1, coords_check2 + 1
            
            #Corner case if we have only two variables in this line
            if count == 2:
                if unbound == 1: #If B is unassigned, no constraint has been broken
                    return True
                if unbound == 0: #Otherwise if both a and b add up to the row sum return True. If not, return false.
                    if sum == row_sum: 
                        return True
                    else:
                        return False 
            
            #Some variables don't have an assigned value yet, so check if our sum up to this point is less or equal to the row sum
            if unbound == 1:
                if sum <= row_sum:
                    return True
                else:
                    return False
            
            #Every variable has a value here. So check if all of them add up to the row sum.
            if unbound == 0:
                if sum == row_sum: 
                    return True
                else:
                    return False 
            

        if A[1] == B[1]: #Neighbor variable is at the same column
            
            #Acquiring the column sum and its coordinates of the variable A      
            for x,y,z in self.col_positions:
                if A == x:
                    col_sum = y
                    col_sum_coords = z
                    break
                
            #Getting the coordinates from the first variable in this column                
            coords_check1, coords_check2 = col_sum_coords[0] + 1, col_sum_coords[1]
            sum = 0
            unbound = 0

            #Adding up a and b, which have to be different (only if B has an assigned value)
            try:
                assig = assignments[B]
                if assig == a:
                    return False
                sum = a + b
            except KeyError:
                unbound = 1
            

            count = 2
            #The idea is to keep adding up every assigned variable in this column until we reach a cell with no variable in it.
            while (coords_check1, coords_check2) in self.variables:
                #Skip A and B    
                if (coords_check1, coords_check2) == A or (coords_check1, coords_check2) == B:
                    coords_check1, coords_check2 = coords_check1 + 1, coords_check2 
                    continue
                
                count = count + 1
                #Get the assignment of this variable and add it to the sum. If it has the same value with a we have an unsatisfied constraint, so return False
                try:
                    assig = assignments[coords_check1,coords_check2]
                    if assig == a:
                        return False
                    sum = sum + assig
                except KeyError: #Variable has not been assigned yet.
                    unbound = 1
                    break
            
                #Proceed to the next variable in this line    
                coords_check1, coords_check2 = coords_check1 + 1, coords_check2

            #Corner case if we have only two variables in this column
            if count == 2:
                if unbound == 1: #If B is unassigned, no constraint has been broken
                    return True
                if unbound == 0: #Otherwise if both a and b add up to the column sum return True. If not, return false.
                    if sum == col_sum: 
                        return True
                    else:
                        return False 
            
            #Some variables don't have an assigned value yet, so check if our sum up to this point is less or equal to the column sum
            if unbound == 1:
                if sum <= col_sum: 
                    return True
                else:
                    return False
            
            #Every variable has a value here. So check if all of them add up to the column sum.
            if unbound == 0:
                if sum == col_sum: 
                    return True
                else:
                    return False
            
        #Return true if we have no unsatisfied constraint up to this point                                                           
        return True 


    #Function used to display the board with every assigned variable
    def display(self, result):
        
        assignments = self.infer_assignment()
        for i,lst in enumerate(self.board):
            for j, element in enumerate(lst):
                if (i,j) in self.variables: #Replace blank spots with the assigned values
                    assig = assignments[(i,j)]
                    str_ass = str(assig)
                    a, b = '_', str_ass
                    lst[j] = element.replace(a, b)

        for i in self.board:
            print(i)
            

if __name__=='__main__':

    #First argument from the command line is the difficulty of the puzzle (easy,medium,etc)
    difficulty = str(sys.argv[1])
    if difficulty == "easy":
        puzzle = easy
    elif difficulty == "medium":
        puzzle = medium
    elif difficulty == "hard":
        puzzle = hard
    else:
        print("Invalid puzzle. Choose between easy, medium and hard")
        sys.exit()
    
    print("Starting board: ")
    print_board(puzzle)

    #Initialize the Kakuro class
    kakuro = Kakuro(puzzle)

    #Execute the algorithm that was provided in the command line
    if (sys.argv[2] == "BT"):
        start_time = time.clock()
        result = backtracking_search(kakuro)
        end_time = time.clock()
    elif (sys.argv[2] == "BT+LCV"):
        start_time = time.clock()
        result = backtracking_search(kakuro, order_domain_values=lcv)
        end_time = time.clock()    
    elif (sys.argv[2] == "FC"):
        start_time = time.clock()
        result = backtracking_search(kakuro, inference=forward_checking)
        end_time = time.clock()
    elif (sys.argv[2] == "FC+LCV"):
        start_time = time.clock()
        result = backtracking_search(kakuro, order_domain_values=lcv, inference=forward_checking)
        end_time = time.clock()
    elif (sys.argv[2] == "MAC"):
        start_time = time.clock()
        result = backtracking_search(kakuro, inference=mac)
        end_time = time.clock()
    elif (sys.argv[2] == "MAC+LCV"):
        start_time = time.clock()
        result = backtracking_search(kakuro, order_domain_values=lcv, inference=mac)
        end_time = time.clock()
    else:
        print("Invalid algorithm. Choose between BT, FC, FC+LCV, MAC and MAC+LCV")
        sys.exit()
    
    
    final_time = end_time - start_time

    #Print the board with every assigned variable
    print()
    print("Final result: ")
    kakuro.display(result)

    #Print its total time
    print()
    print("Finished in", final_time , "seconds")

    