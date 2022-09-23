import math
import sys
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    k=math.floor(len(data)/2-1)
    while k>=0:
       
       i=k+0
       
       while i<=math.floor(len(data)/2)-1:
         
         if i==len(data)/2-1:
           childindex=i*2+1
           if data[childindex]<data[i]:
            data[i],data[childindex]=data[childindex],data[i]
            swaps.append([i,childindex])
            i=childindex
           else:
               break
         else:
          left=i*2+1
          right=i*2+2
          if data[left]<data[right]:
           if data[left]<data[i]:
            data[i],data[left]=data[left],data[i]
            swaps.append([i,left])
            i=left
           else:
                break
          elif data[right]<data[i]:
           data[i],data[right]=data[right],data[i]
           swaps.append([i,right])
           i=right
          else:
              break
       k-=1   
## k     
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
