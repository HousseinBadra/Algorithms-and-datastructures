# Uses python3
def edit_distance(s, t):
    #write your code here
    matrix=[[0]*len(s+' ') for i in range(len(t+' '))]
    for i in range(len(s)+1):
        matrix[len(t)][i]=len(s)-i
    
    for i in range(len(t)+1):
        matrix[i][len(s)]=len(t)-i
     
        
    for i in reversed(range(len(t))):
           for j in reversed(range(len(s))):
                if s[j]==t[i]:
                 matrix[i][j]=matrix[i+1][j+1]
                else:
                   matrix[i][j]=min(matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1])+1
    return matrix[0][0]
    
    
 
if __name__ == "__main__":
    print(edit_distance(input(), input()))
