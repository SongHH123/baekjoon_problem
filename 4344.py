#평균은 넘겠지
C = int(input())
Rate = []

for i in range(C):
    Rate.append(0)
    NG = input().split(' ')
    NG = list(map(int, NG))
    N = NG[0]
    G = NG[1:]
    Sum = 0
    avg = sum(G)/N
    for j in range(N):
        if(G[j]>avg):
            Rate[i] += 1
    Rate[i] = round((Rate[i]/N)*100, 3)

for i in range(len(Rate)):
    a = Rate[i]
    print(str(format(a, ".3f"))+"%")
