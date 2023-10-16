import sys
L = []
N = int(sys.stdin.readline())
for i in range(N):
    C = sys.stdin.readline().split()
    if(C[0]=='push'):
        L.append(C[1])
    elif(C[0]=='pop'):
        if(len(L)==0):
            print(-1)
        else:
            print(L[0])
            L = L[1:]
    elif(C[0]=='size'):
        print(len(L))
    elif(C[0]=='empty'):
        if(len(L)==0):
            print(1)
        else:
            print(0)
    elif(C[0]=='front'):
        if(len(L)==0):
            print(-1)
        else:
            print(L[0])
    elif(C[0]=='back'):
        if(len(L)==0):
            print(-1)
        else:
            print(L[-1])