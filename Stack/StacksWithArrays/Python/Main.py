from Stack import Stack

def main():
    
    myStack = Stack()
    
    firstVal = 1
    secondVal = 2
    thirdVal = 3

    print(myStack.isEmpty())
    myStack.push(firstVal)
    print(myStack.top())
    myStack.push(secondVal)
    print(myStack.top())
    print(myStack.isEmpty())
    myStack.push(thirdVal)
    print(myStack.top())
    print(myStack.isEmpty())

    myStack.pop()
    print(myStack.top())
    myStack.pop()
    print(myStack.top())
    myStack.pop()
    print(myStack.top())
    print(myStack.isEmpty())
    

    

if __name__ == "__main__":
    main()