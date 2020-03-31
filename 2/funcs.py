a = 0

def func1():
    print "f1"
    func2()

def func2():
    print "f2"
    #func1()
    

if __name__ == "__main__":
    func1()
    a = a + 1