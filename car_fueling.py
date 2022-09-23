# python3
import sys

def compute_min_refills(distance, tank, stops,alr,where):
    # write your code here
    ##print('   ',alr,where,distance,stops)
    if stops ==[] and distance-where>tank:
        return -1
    if stops ==[] and distance-where<=tank:
        return alr
    if stops[0] -where> tank:
        return -1
    if distance-where <= tank :
        return alr
    i=int(len(stops))-1
    while i>=0:
            if stops[i]-where<=tank:
                break
            i-=1
    return compute_min_refills(distance,tank,stops[i+1:],alr+1,stops[i])
                
##print('     ' ,compute_min_refills(1200,300,[100,200,400,500,800,900,1000,1100],0,0))                
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops,0,0))
