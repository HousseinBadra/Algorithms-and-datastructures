# Uses python3
import sys
import itertools

def dicttoarray(nnn):
    result=[]
    for key in nnn.keys():
        while nnn[key]>0:
            result.append(key)
            nnn[key]-=1
    return result

def slicer(array,elem):
  x=array.copy()
  x.remove(elem)
  return x


def adder(array,elem):
    x=array.copy()
    x.append(elem)
    return x

def copy(xxx):
    new={}
    for key in xxx.keys():
        new[key]=xxx[key]
    return new
    
    
    
    
def create(w):
            dictio={}
            for bar in w:
               dictio[bar]=dictio.get(bar,0)+1
            return dictio
               
def all_weight(W, w):
           dict=create(w)
           
               
           arr=[[] for i in range(W+1)]
           
           for bar in w:
            if W-bar>=0: 
                 dico={}
                 for key in dict.keys():
                     dico[key]=0
                 dico[bar]+=1
                 arr[bar]=[dico]
           
                
                      
           for i in range(W+1):
                 for bar in w:
                         if i-bar>=0:
                             for way in arr[i-bar]:
                                 if way[bar]<dict[bar]:
                                     
                                        newdict=copy(way)
                                                                        
                                        newdict[bar]+=1    
                                        if not newdict in arr[i]:                
                                         arr[i].append(newdict)
                                        
                                            
           return arr[W]
           



def partition3(list):
    if len(list) <3:
        return 0
    x=sum(list)
    if x%3 !=0:
        return 0
    finder=(2*x)//3
    poss=all_weight(finder,list)
    for z in poss:
        x= all_weight(finder//2,dicttoarray(z))
        if len(x)>0:
            return 1
        
         
            
     
         
    return 0
        

##print('    ',all_weight(2,[1,1,2,5]))
##x=partition3([101,100,99,1,2])
##print('   ',x)
##print('     ',x)
##for i in x:
 ## print(all_weight(118,i) !=[] , i)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

