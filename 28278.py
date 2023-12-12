import sys
S=[]
for _ in range(int(sys.stdin.readline())):
    i = sys.stdin.readline().split()
    if(i[0]=='1'):
        S.append(i[1])
    elif(i[0]=='2'):
        if(len(S)==0):
            print(-1)
        else:
            print(S.pop())
    elif(i[0]=='3'):
        print(len(S))
    elif(i[0]=='4'):
        if(len(S)==0):
            print(1)
        else:
            print(0)
    elif(i[0]=='5'):
        if(len(S)==0):
            print(-1)
        else:
            print(S[-1])