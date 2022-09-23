# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i  in range(len(text)):
        x=text[i]
        if x in '({[':
         opening_brackets_stack.append([x,i])
        if x in ')}]':
             if opening_brackets_stack==[]:
                 return i+1
             else:  
              l= opening_brackets_stack[len(opening_brackets_stack)-1][0]    
              if are_matching(l,x):
                 opening_brackets_stack.pop()
              else:
                  return i+1
    if opening_brackets_stack ==[]:
             return 'Success'
    return opening_brackets_stack[0][1]+1


def main():
     text = input()
     mismatch = find_mismatch(text)
    # Printing answer, write your code here
     print(mismatch)
  
   
main()       
if __name__ == "__main__":
    main()
