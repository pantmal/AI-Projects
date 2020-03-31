

listoflists = []
a_list = []
b_list = []
new_list = []

temp_tup0 = ((5,3),'Tstring')
temp_tup1 = ((5,4),'Tstring2')

temp_tup2 = ((6,3),'Tstring')
temp_tup3 = ((6,4),'Tstring2')

new_tup = ((7,3),'New')

a_list.append(temp_tup0)
a_list.append(temp_tup2)
b_list.append(temp_tup1)
b_list.append(temp_tup3)

listoflists.append(a_list)
listoflists.append(b_list)

c =0 
for i in listoflists:
    print i
    if c == 1:
        break
    for x,y in i:
        if temp_tup0 == i[-2]:
            print i[-2][0]
            c = c + 1
            new_list = list(i)
            del new_list[-1] 
            new_list.append(new_tup)
            listoflists.append(new_list)
            
            #i.append(new_tup)
            if c == 1:
                break
        else:
            break

"""
for i in range(0,10):
    a_list.append(i)
    if len(a_list)>3:
        a_list.remove(a_list[0])
        listoflists.append((list(a_list), a_list[0]))
"""

print listoflists
for i in listoflists:
    for x,y in i:
        if x == (7,3):
            print "found"
            copy_list = list(i)
            break

actions = []
for x,y in copy_list:
    actions.append(y)

print actions

