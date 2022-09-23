import math
def binary_search(keys, query,l,r):
    # write your code here
    # write your code here.
    
    median =math.floor(l+(r-l)/2)
    
    if keys[l] ==query :
        return l
        
    if l==r:
        return -1
    
    median =math.floor(l+(r-l)/2)
    
    if query > keys[median]:
        return binary_search(keys,query,median+1,r)
    if query <=keys[median]:
        return binary_search(keys,query,l,median)
    
   



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q,0,len(input_keys)-1), end=' ')
