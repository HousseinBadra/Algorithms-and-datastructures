# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
     x=a[l]
     j=l
     equal=0
     for i in range(l+1,r+1):
       
        if a[i] <x:
         j+=1
         a[i],a[j]=a[j],a[i]
        elif a[i]== x:
          a[i],a[j+1+equal]= a[j+1+equal],a[i]
          equal+=1
     a[l],a[j]=a[j],a[l]
     if equal==0:
      return [j,equal]
     return [j,equal]



def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)[0]
    mega=partition3(a,l,r)[1]
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1+mega, r);
    ##
    
    
def quicksort(arr):
    if len(arr)<=1 :
        return arr
    equal=[]
    more=[]
    less=[]
    pivot=arr[0]
    for i in arr:
        if i>pivot:
            more.append(i)
        elif i<pivot:
            less.append(i)
        else:
            equal.append(i)
    return quicksort(less)+equal+quicksort(more)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a=quicksort(a)
    for x in a:
        print(x, end=' ')
