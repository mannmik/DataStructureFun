
from Bag import Bag

def main():
    
    myBag = Bag()
    
    firstVal = 5
    secondVal = 7

    myBag.add(firstVal)
    print(myBag.contains(firstVal))

    myBag.add(secondVal)
    print(myBag.contains(secondVal))

    myBag.remove(firstVal)
    print(myBag.contains(firstVal))
    

    

if __name__ == "__main__":
    main()