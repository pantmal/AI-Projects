# This is what a comment looks like 
fruits = ['apples','oranges','pears','bananas']
for othervar in fruits:
    print othervar + ' for sale'
    
fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
print fruitPrices.items()
for first, second in fruitPrices.items():
    if second < 2.00:
        print '%s cost %f a pound' % (first, second)
    else:
        print first + ' are too expensive!'