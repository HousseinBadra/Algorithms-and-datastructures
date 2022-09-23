#        7
#   2          9
#4    5    6   10

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
node1=Node(7)       
node2=Node(2)
node3=Node(9)
node4=Node(1)
node5=Node(5)
node6=Node(6)
node7=Node(10)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7

#### depth search

def depth_search(head):
    list=[head]
    while len(list)>0:
        x=list.pop()
        if x.right != None:
         list.append(x.right)
        if x.left!=None:
            list.append(x.left)
        print(x.value)
        
   
#depth_search(node1)

def traversal_search(head):
    list=[head]
    while len(list)>0:
        x=list[0]
        list=list[1:]
        if x.left !=None:
         list.append(x.left)
        if x.right !=None:
         list.append(x.right)
        print(x.value)
        
        
#traversal_search(node1)


def isbt(head):
    
    if head==None:
        return True
          
    if head.left==None and head.right == None :
        return isbt(head.left)  and isbt(head.right) 
        
    if head.left==None :
        return isbt(head.left)  and isbt(head.right)  and head.value<head.right.value
     
    if head.right==None :
        return isbt(head.left)  and isbt(head.right) and head.value > head.left.value 
    
    return isbt(head.left)  and isbt(head.right) and head.value > head.left.value and head.value<head.right.value
    
    
#print(isbt(node1))


def isbst(head):
    lowest=head.right
    highest=head.left
    if head == None:
        return True
    while lowest.left != None:
     lowest=lowest.left
    while highest.right != None:
        highest=highest.right
    print('    ',highest.value,lowest.value)
  
isbst(node1)
        