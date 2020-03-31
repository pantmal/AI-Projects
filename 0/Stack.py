#Stack.py

import sys

class Stack:
    """Defining a simple class Stack"""

    def __init__(self):
       self.stuff = []
        
    def Empty(self):
        return self.stuff == []

    def Pop(self):
        return self.stuff.pop()

    def Push(self, item):
        self.stuff.append(item)

# Main Method
if __name__ == '__main__':
    
    mainStack = Stack()

    """We store the second command line argument, which is our desired string and we print it """
    desired_string = str(sys.argv[1])
    print desired_string

    """ Checking that our string contains only the characters we want"""
    for i in desired_string:
        if i != "(" and i != ")" and i != "{" and i != "}" and i != "[" and i != "]":
            print "We have undesired characters. Exiting..."
            sys.exit()

    """If our string begins with a closing bracket, we can't have equal weight, so the program quits its execution """
    if desired_string[0] == ')' or desired_string[0] == '}' or desired_string[0] == ']':
        print "Our string begins with a closing bracket. We can't have equal weight. Exiting..."
        sys.exit()

    """ If the programs sees an opening bracket it pushes it in our Stack
        If it sees a closing bracket it pops the item at the top, if the Stack is not empty.
        It also compares the item it popped with the closing bracket to see if they are of the same type, i.e. [ with ]
        If it's not, we can't have equal weight so the program exits. 
        Also if our Stack is empty and we have a closing bracket this means our string is not of equal weight.
    """
    for i in desired_string:
        if i == '(' or i == '{' or i == '[':
            mainStack.Push(i)
        if i == ')' or i == '}' or i == ']':
            if mainStack.Empty() != True:
                character_ret = mainStack.Pop()
                if i == ')' and character_ret != '(' :
                    print "Too bad! Wrong opening..."
                    sys.exit()
                if i == '}' and character_ret != '{' :
                    print "Too bad! Wrong opening..."
                    sys.exit()
                if i == ']' and character_ret != '[' :
                    print "Too bad! Wrong opening..."
                    sys.exit()    
            else:
                print "Too bad! Closing bracket without an opening one..."
                sys.exit()

    if mainStack.Empty() == True :
        print "Great. Our string is of equal weight."
    else:
        print "Too bad! There are still items in our stack, so we don't have equal weight..."
    