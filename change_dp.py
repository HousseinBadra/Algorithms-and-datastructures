# Uses python3
import sys
import math

i=0
j=0
arr=[0,1,None,1,1]

m=int(input())
           
def get_change(m):
     if m<0:
         return float('inf')
     else:
         return arr[m]
         
while j<=m:
     if j<5:
        j+=1
     else:
         arr.append(None)
         j+=1
         
while i<=m:
        if arr[i] != None:
           pass
           
        else:
           arr[i]=min(get_change(i-1),get_change(i-3),get_change(i-4))+1
        i+=1 
       
print(get_change(m))
    
           

       





