# Uses python3
import sys
def best(a,b,c):
    if len(a)<=len(b) and len(a)<=len(c):
        return a
    if len(b)<=len(a) and  len(b)<=len(c):
        return b
    if len(c)<=len(a) and len(c)<=len(b):
        return c
    
    
    
def optimal_sequence(n):
    if n==1 :
        return [1]
    if n==2 or n==3:
        return [1 , n]
    sequence = [[]]*(n+1)
    sequence[1]=[1]
    sequence[2]=[1,2]
    sequence[3]=[1,3]
    
        
    for i in range(1,n+1):
        
        if i%3==0 and i%2 ==0:
            sequence[i]=best(sequence[i//3],sequence[i//2],sequence[i-1])+[i]
        elif i%3==0:
            sequence[i]=best(sequence[i//3],sequence[i-1],sequence[i-1])+[i]
        elif i%2 ==0:
             sequence[i]=best(sequence[i//2],sequence[i-1],sequence[i-1])+[i]
        else:
            sequence[i]=sequence[i-1]+[i]
    return sequence[n]



n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for i in sequence:
    print(i)

    
