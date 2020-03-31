# buyLotsOfFruit.py
# -----------------
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

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """This function takes an orderList as an argument, meaning a list with tuples of two items: fruit type and its cost.
        It checks if a fruit is not in the fruitPrices dictionary in order to quit its execution. Otherwise it calculates
        the cost of each fruit by multiplying its price from the orderList and its value from the fruitPrices dictionary.
        It then adds each cost to the total amount that will be returned. 
    """
    totalCost = 0.0
    for fruit, price in orderList:
        if fruit not in fruitPrices:
            return None 
        else:
            actualCost = price * fruitPrices[fruit]
            totalCost += actualCost
    return totalCost

# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"

    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    for fruit, price in orderList: #The desired message of when a fruit is not in fruitPrices simply appears before the function is called. 
        if fruit not in fruitPrices: #It will exit normally if the fruit is not in fruitPrices
            print "Sorry this type of fruit is not in the desired list" 
    print 'Cost of', orderList, 'is', buyLotsOfFruit(orderList) 
