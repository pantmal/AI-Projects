            """
            end = 0
            sum = 0
            if A[1] == B[1] + 1: #B is his left neighbor
                try:
                    assig = assignments[B]
                    sum = a + b
                except KeyError:
                    return True
                
                #going back
                new_coords0, new_coords1  = A[0], B[1] - 1 
                while (new_coords0,new_coords1) != row_sum_coords:
                    #print(A,a)
                    try:
                        assig = assignments[new_coords0,new_coords1]
                        if assig == a:
                            return False
                        sum = sum + assig
                    except KeyError: #possible changes
                        return True
                
                    new_coords0, new_coords1 = A[0], new_coords1 - 1 

                #going front
                if (A[0], A[1] + 1) not in self.variables:
                    end = 1 
            
            if end == 0:
                if sum <= row_sum: #use of end
                    return True
                else:
                    return False

            if end == 1:
                if sum == row_sum: #use of end
                    return True
                else:
                    return False           
            """


            """
            end = 0
            sum = 0
            #new_coords = (0,0)
            if A[0] == B[0] + 1: #B is his top neighbor
                try:
                    assig = assignments[B]
                    sum = a + b
                except KeyError:
                    return True

                new_coords0, new_coords1  = B[0] - 1, A[1]
                while (new_coords0,new_coords1) != col_sum_coords:
                    #print(A,a)
                    try:
                        assig = assignments[new_coords0,new_coords1]
                        if assig == a:
                            return False
                        sum = sum + assig
                    except KeyError:
                        return True
                
                    new_coords0, new_coords1 = new_coords0 - 1 , A[1]
                
                if (A[0] + 1, A[1]) not in self.variables:
                    end = 1 
            

            if end == 0:
                if sum <= col_sum: #use of end
                    return True
                else:
                    return False

            if end == 1:
                if sum == col_sum: #use of end
                    return True
                else:
                    return False 

           """

           def display2(self):
        
        assignments = self.infer_assignment()
        for i,lst in enumerate(self.board):
            for j, element in enumerate(lst):
                if (i,j) in self.variables:
                    try:
                        assig = assignments[(i,j)]
                        str_ass = str(assig)
                        a, b = '_', str_ass
                        lst[j] = element.replace(a, b)
                    except KeyError:
                        print()
                    

        for i in self.board:
            print(i)