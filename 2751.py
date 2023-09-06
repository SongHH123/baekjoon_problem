import sys
n = int(sys.stdin.readline())
L= []
for i in range(n):
    L.append(int(sys.stdin.readline()))

L.sort()
for i in range(n):
    print(L[i])