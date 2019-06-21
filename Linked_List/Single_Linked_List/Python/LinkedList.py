from Node import Node

class LinkedList:
    # constructor creates new node to be head of the list
    def __init__(self):

        self.head = Node()
        self.head.next = None

    # add a value to the front or top of the list
    def addFront(self, data_to_add):

        # if the list is not empty 
        # create a new node to placed in head node
        if self.head.data is not None:
            new_node = Node(data_to_add)
            temp = self.head
            self.head = new_node
            self.head.next = temp

        # if head is emtpy then store data in head
        else:
            self.head.data = data_to_add


    # return the data value of the head node
    def front(self):
        
        # if the list is not empty return the first value
        if not self.isEmpty():
            return self.head.data

    # remove the head node
    def removeFront(self):

        # if the list is not empty then remove the head node 
        if not self.isEmpty():
            trashNode = self.head
            self.head = self.head.next
            del(trashNode)

    # check that there is at least head data to determine if the list is empty or not
    def isEmpty(self):
        if self.head is not None:
            if self.head.data is not None:
                return False
        
        return True


    # prints all the data in the list
    def printList(self):

        # check that the list is not empty before printing
        if not self.isEmpty():
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data)
                currentNode = currentNode.next

