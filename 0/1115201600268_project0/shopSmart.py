# shopSmart.py
# ------------
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


import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops

        This function calculates the cost of the orderList from each shop (through the use of the getPriceOfOrder function).
        Then it proceeds to append the cost in a ListofCosts list which contains every shop name along with its price of the order.
        After that it finds the cheapest cost from the prices we have and it returns the shop name that contains this price. 
        If something went wrong and we didn't find any cheap cost the function returns None.
    """

    ListofCosts = []
    for shop_name in fruitShops:
        shop_price = shop_name.getPriceOfOrder(orderList)
        ListofCosts.append((shop_name, shop_price))        

    cheap_shop, cheap_cost = ListofCosts[0]
    for i, j in ListofCosts:
        if j < cheap_cost:
            cheap_shop = i
            cheap_cost = j

    if cheap_cost != -1: 
        return cheap_shop        


    return None

if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
  orders = [('apples',3.0)]
  print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
