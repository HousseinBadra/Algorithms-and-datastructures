# Uses python3
import sys
import math
def get_optimal_value(capacity, weights, values):
    # write your code 
     ##
     arr=[]
     numberofitems=int(len(values))
     total=0
     length=int(len(values))-1
     while length>=0:    
            arr.append((float(values[length])/int(weights[length]),int(weights[length])))
            length-=1
     arr.sort()   
     while capacity>0 and numberofitems>=1:
        if arr[numberofitems-1][1]>capacity:
          total+=arr[numberofitems-1][0]*capacity
          capacity=0            
        else:
          total+=arr[numberofitems-1][0]*arr[numberofitems-1][1]
          capacity-=arr[numberofitems-1][1]
          numberofitems-=1
         
     return round(total,4)
   


data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value=get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))
