
easy = [['*',       '*',  '*',    [6, ''], [3, '']],
        ['*',     [4, ''],[3, 3], '_',      '_'],
        [['', 10], '_',   '_',    '_',      '_'],
        [['', 3],  '_',   '_',    '*',     '*']]



for i, element in enumerate(easy):
    for j, v in enumerate(element):
        if j == 3:
            if v == [6,'']: 
                (x,y) = i,j
            if (i,j) == (3,3):
                (k,l) = i-1,j
                break
            #print(v)

i = x
while i<k+1:
    print(i,l)
    i = i + 1
        

for i in easy:
    print(i)
    #for j in i:
    #    print(j)

variables = [(1,2),(2,3),(3,3)]
domains = {v: [x for x in range(10)] for v in variables}



