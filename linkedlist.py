class Node:
    def __init__(self,value):
        self.value=value
        self.next=None




class Linkedlist:
    def __init__(self):
        self.head=None


    def insertend(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            loop=self.head
            while True:
                if loop.next==None:
                    break
                loop=loop.next
            loop.next=newnode



    def insertbegin(self,newnode):
        newnode.next=self.head
        self.head=newnode



    def printlist(self):
       if self.head is None:
           print("empty linked list")
           return
       loop=self.head
       while True:
           if loop is None:
               break
           print(loop.value)
           loop=loop.next



node1=Node(3)
var1=Linkedlist()
var1.insertend(node1)
node2=Node(4)
var1.insertend(node2)
node3=Node(5)
var1.insertbegin(node3)
var1.printlist()
