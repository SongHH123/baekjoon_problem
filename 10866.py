import sys
Deq=[]
for _ in range(int(sys.stdin.readline())):
    c = sys.stdin.readline().split()
    if(c[0]=='push_front'):
        Deq = c[1:]+Deq
    elif(c[0]=='push_back'):
        Deq.append(c[1])
    elif(c[0]=='pop_front'):
        if(len(Deq) != 0):
            print(Deq.pop(0))
        else:
            print(-1)
    elif(c[0]=='pop_back'):
        if(len(Deq) != 0):
            print(Deq.pop())
        else:
            print(-1)
    elif(c[0]=='size'):
        print(len(Deq))
    elif(c[0]=='empty'):
        if(len(Deq) != 0):
            print(0)
        else:
            print(1)
    elif(c[0]=='front'):
        if(len(Deq) != 0):
            print(Deq[0])
        else:
            print(-1)
    else:
        if(len(Deq) != 0):
            print(Deq[-1])
        else:
            print(-1)