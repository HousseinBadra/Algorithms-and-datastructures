# python3
import math
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
    
def hash(string):
    result=0
    for i in string:
        result+=ord(i)
    return result
    
def get_occurrences(pattern, text):
    result=[]
    hashedpattern=math.floor(hash(pattern))
    hasher=math.floor(hash(text[0:len(pattern)]))
    for i in range(len(text)-len(pattern)+1):
        if i ==0:
            if hasher==hashedpattern:
                result.append(0)
        else:
           hasher=hasher-ord(text[i-1])+ord(text[i+len(pattern)-1])
           if hasher==hashedpattern:
              if pattern == text[i:i+len(pattern)] :
               result.append(i)
    return result

##print('     ',get_occurrences('nn','alnnkolnn'))

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

