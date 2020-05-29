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



    def insertpos(self,newnode,pos):
       temp,index=self.head,0
       while pos!=index:
            prevnode=temp
            temp=temp.next
            index=index+1
       prevnode.next=newnode
       newnode.next=temp


    def deleteend(self):

       temp=self.head
       if temp==None:
           print("cannot deleteend")
           return
       if temp.next==None:
          self.head=None
          return
       while True:
           prevnode=temp
           temp=temp.next
           if temp.next==None:
               prevnode.next=None
               return



    def deletehead(self):
           temp=self.head
           self.head=self.head.next
           temp.next=None


    def deletepos(self,position):
       temp,count=self.head,0
       if position==0:
           self.deletehead()
           return
       while position!=count:
           prevnode=temp
           temp=temp.next
           count=count+1
       prevnode.next=temp.next
       temp.next=None









    def printlist(self):
       if self.head is None:
           print("empty linked list")
           return
       loop=self.head
       while True:
           if loop.next==None:
               print(loop.value)
               return
           print(loop.value)
           loop=loop.next



    def length(self):
      count,temp=0,self.head
      if self.head==None:
          return 0
      else:
          while True:
              count=count+1
              if temp.next==None:
                  return count
              temp=temp.next


node1=Node(3)
var1=Linkedlist()
var1.insertend(node1)
node2=Node(4)
var1.insertend(node2)
node3=Node(6)
node4=Node(8)
var1.insertend(node4)
var1.insertpos(node3,2)
var1.deletepos(2)
var1.deleteend()
var1.deletehead()



var1.printlist()
print("The length is ",var1.length())
