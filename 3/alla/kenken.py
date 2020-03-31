from csp import *
import sys
import time


class Clique:

    def __init__(self, op, val):
        self.cells = []  # list of (x,y) tuples with cell coords
        self.operation = op
        self.value = val

    def addCell(self, coords):
        self.cells.append((coords[0],coords[1]))

    def print(self):
        #clique(/3): (0,1) (1,1)...
        print("clique(",self.operation,self.value,"): ",end='')
        for cell in self.cells:
            print("(",cell[0],",", cell[1],")",end='')
        print()

class KenKen(CSP):

    def __init__(self, filename):
        self.cliques = []  # list of clique objects
        self.dimension = int()  # board dimensions
        self.board = []  # 2d list of lists, every cell holds the position of the clique it belongs to
        #open file
        try:
            fp = open(filename,'r')
        except IOError:
            raise IOError("Couldn't open file:"+filename)
        #first line of file has an int that specifies the dimensions of the board
        try:
            self.dimension = int(fp.readline())
        except ValueError:
            raise ValueError("First line wasn't a int. This specifies the dimensions of the board.")
        #initialize board
        self.board = [[None for j in range(self.dimension)] for i in range(self.dimension)]
        #initialize variables
        variables = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                variables.append((i,j))
        #initialize domains
        domains = {v: [x+1 for x in range(self.dimension)] for v in variables}
        #every following line in file describes a clique
        self.read_cliques(fp)
        fp.close()
        CSP.__init__(self, variables, domains, self.find_neighbors(variables), self.constraints)

    def read_cliques(self,fp):
        """Given a file pointer fp read it line-by-line. Each line describes a clique.
            i.e.: (0,0) (0,1) (1,1) * 16 """
        clique_pos = 0  #object pos in cliques
        for line in fp.readlines():
            if line=="": continue
            line = line.strip().split(" ")  #clean string
            clique = Clique(line[-2], int(line[-1])) #init Clique object with op and value
            # add cells to Clique
            for cell_coords in line[:-2]:
                coords = [int(x) for x in cell_coords.strip("()").split(",")]
                clique.addCell(coords)
                if self.board[coords[0]][coords[1]]!=None: raise Exception("Bad formatting: A cell appears more than once in input file.")
                self.board[coords[0]][coords[1]] = clique_pos   #update board
            # add clique to list
            self.cliques.append(clique)
            clique_pos += 1

    def print_board(self):
        """"Print the board image, where each cell holds the position(in self.cliques)
            of the clique it belongs to. """
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.board[i][j],end='')
            print()

    def find_neighbors(self,variables):
        """Find the neighbors in the same row,col and clique.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints. """
        neighbors = dict()
        for var in variables:
            _neighbors = set()
            #add row neighbors
            for j in range(self.dimension):
                if j==var[1]: continue
                _neighbors.add((var[0],j))
            #add col neighbors
            for i in range(self.dimension):
                if i==var[0]: continue
                _neighbors.add((i,var[1]))
            #add clique neighbors
            for clique_member in self.get_Clique(var).cells:
                if clique_member==var: continue
                _neighbors.add(clique_member)
            neighbors[var] = _neighbors
        return neighbors

    def get_Clique(self,cell):
        """Get the Clique this cell belongs to"""
        clique_id = self.board[cell[0]][cell[1]]
        return self.cliques[clique_id]

    def constraints(self, A, a, B, b):
        same_row = lambda x,y: True if x[0]==y[0] else False
        same_col = lambda x,y: True if x[1]==y[1] else False
        #Just like in Sudoku row and col alldiff. Note: in Cliques numbers can repeat themselves
        if same_row(A,B) and a==b:
            return False
        if same_col(A,B) and a==b:
            return False
        cliqueA = self.get_Clique(A)
        cliqueB = self.get_Clique(B)
        #clique oparation satisfactions
        if cliqueA==cliqueB:
            assignments = self.infer_assignment()
            if cliqueA.operation=="+":
                sum = a+b
                #check if clique sum hold against already assigned values
                for n in cliqueA.cells:
                    if n==A or n==B: continue   #skip A,B
                    try:
                        sum += assignments[n]
                    except KeyError:
                        return True #n is not assigned yet, theres a chance constraint holds
                if sum!=cliqueA.value:
                    return False    #sum calculated but doesn't match
            elif cliqueA.operation=="-":
                if (a-b)!=cliqueA.value and (b-a)!=cliqueA.value:
                    return False
            elif cliqueA.operation=="*":
                mult = a*b
                # check if clique mult hold against already assigned values
                for n in cliqueA.cells:
                    if n == A or n == B: continue  # skip A,B
                    try:
                        mult *= assignments[n]
                    except KeyError:
                        return True #n is not assigned yet, theres a chance constraint holds
                if mult != cliqueA.value:
                    return False     # mult calculated but doesn't match
            elif cliqueA.operation=="/":
                try:
                    if a/b!=cliqueA.value and b/a!=cliqueA.value:
                        return False
                except ZeroDivisionError:
                    return False
        return True #all no constsraints broken

    def display(self,result):
        if result is None:
            print("No Result.")
            return
        """Display the resulting solution for KenKen puzzle."""
        #display the board
        print()
        print("Solution:")
        for index,var in enumerate(self.variables):
            assignments = self.infer_assignment()
            print("Assignment here:",assignments[var])
            #print()
            print()
            print(result[var],end='')
            if (index+1)%self.dimension==0:
                print()
        #display every clique
        print()
        for clique in self.cliques:
            clique.print()
        print()


if __name__=='__main__':
    try:
        kenken = KenKen(sys.argv[1])
        print("algorithm: ",sys.argv[2])
    except IndexError:
        raise IndexError("python3 kenken.py <filename> <algorithm_name>")

    if sys.argv[2]=="BT":
        start_time = time.clock()
        kenken.display((backtracking_search(kenken)))
    elif sys.argv[2] == "BT+MRV":
        start_time = time.clock()
        kenken.display((backtracking_search(kenken,select_unassigned_variable=mrv)))
    elif sys.argv[2] == "FC":
        start_time = time.clock()
        kenken.display((backtracking_search(kenken,inference=forward_checking)))
    elif sys.argv[2] == "FC+MRV":
        start_time = time.clock()
        kenken.display((backtracking_search(kenken,select_unassigned_variable=mrv,inference=forward_checking)))
    elif sys.argv[2] == "MAC":
        start_time = time.clock()
        kenken.display((backtracking_search(kenken,inference=mac)))
    elif sys.argv[2] == "min" or sys.argv[2]=="MinConflicts":
        start_time = time.clock()
        kenken.display(min_conflicts(kenken))
    else:
        print("Incorrect algorithm. (try BT,BT+MRV,FC,FC+MRV,MAC)")
    print("Done in: ", time.clock() - start_time, "sec")
    print("Number of assignments: ", kenken.nassigns)