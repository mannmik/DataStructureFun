from LinkedList import LinkedList

def main():
    myList = LinkedList()

    node_data_one = 5
    node_data_two = 7
    node_data_three = 9

    print(myList.isEmpty())
    myList.addFront(node_data_one)
    print(myList.front())
    myList.addFront(node_data_two)
    myList.addFront(node_data_three)

    myList.printList()
    print(myList.isEmpty())

    myList.removeFront()
    myList.printList()

    myList.removeFront()
    myList.removeFront()
    myList.printList()
    print(myList.isEmpty())


main()