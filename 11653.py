import sys
import math
N = int(sys.stdin.readline())
n = []
while(int(math.sqrt(N))>=1):
    for i in range(2, int(math.sqrt(N))+2):
        if(N%i==0):
            n.append(i)
            N//=i
            break
        elif(i == int(math.sqrt(N))+1):
            n.append(N)
            N=0
            
if(len(n)==0):
    print(N)
elif(n[-1]==1):
    for i in n[:-1]:
        print(i)
else:
    for i in n:
        print(i)