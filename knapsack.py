# Uses python3
import sys

def slicer(array,elem):
  x=array.copy()
  x.remove(elem)
  return x



def optimal_weight(W, w):
           arr=[[0,w.copy()] for i in range(W+1)]
           
           for bar in w:
               if bar<=W:
                arr[bar]=[bar,slicer(w.copy(),bar)]
           
           for i in range(1,W+1):
               for bar in w:
                   if i-bar>=0 and  not i in w:
                       if arr[i-bar][0]+bar>=arr[i][0]  :
                           if  bar in arr[i-bar][1]:
                            arr[i][0]=arr[i-bar][0]+bar
                            arr[i][1]=slicer(arr[i-bar][1],bar)
                            
                                               
                           if not bar in arr[i-bar][1]:
                              if arr[i-bar][0]>arr[i][0]:
                               arr[i][0]=arr[i-bar][0]
                               arr[i][1]=arr[i-bar][1]
                               
                       
           return arr[W][0]
           
##x=optimal_weight(351,[20,2,2,2,248,13, 20,24,3,5,117,150,1,1,1,1,1])
#print('    ',x)
       
           
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
