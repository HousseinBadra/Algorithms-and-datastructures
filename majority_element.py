# Uses python3
import sys
import math
def get_majority_element(a, left, right):
    for i in a :
        if getmajority(a,i)>len(a)/2:
         return 1
    return -1
         
    #write your code here
    
def getmajority(arr,i):
    if len(arr) ==0:
        return 0
    if arr[0]==i and len(arr) == 1:
        return 1
    if arr[0] != i and len(arr) == 1:
        return 0
    x=math.floor((len(arr)-1)/2)
    
    left=arr[:x+1]
    right=arr[x+1:]
    return getmajority(left,i) + getmajority(right,i)
    



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
