import math
class Heap():
    def __init__(self,list):
         self.list=list
         self.length=len(list)
    def dropdown(self,i):
       while i<=math.floor(self.length/2)-1:     
         if i==self.length/2-1:
           childindex=i*2+1
           if prior(self.list[childindex],self.list[i]):
            self.list[i],self.list[childindex]=self.list[childindex],self.list[i]
            i=childindex
           else:
               break
         else:
          left=i*2+1
          right=i*2+2
          if prior(self.list[left],self.list[right]):
           if prior(self.list[left],self.list[i]):
            self.list[i],self.list[left]=self.list[left],self.list[i]
            i=left
           else:
                break
          elif prior(self.list[right],self.list[i]):
           self.list[i],self.list[right]=self.list[right],self.list[i]
           i=right
          else:
              break
       

def prior(a,b):
    if a[1]<b[1]:
        return True
    elif a[1] == b[1] and a[0]< b[0]:
        return True
    return False




def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    bots=[[i,0] for i in range(n_workers)]
    botsheap=Heap(bots)
    i=0
    while i<len(jobs):
      x=jobs[i]
      result.append([botsheap.list[0][0],botsheap.list[0][1]])
      botsheap.list[0][1]+=x
      botsheap.dropdown(0)
      i+=1
    return result



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    assigned_jobs = assign_jobs(n_workers,jobs)
    for k,v in assigned_jobs:
        print(k,v)


main()
