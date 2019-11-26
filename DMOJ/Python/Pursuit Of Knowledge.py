n,m,t = raw_input().split()
n = int(n)
m = int(m)
t = int(t)
bfs = []
ndis = []
dp = []
for x in range(n):
    bfs.append([])
    ndis.append(-1)
    dp.append([])
for x in range(m):
    a,b = raw_input().split()
    bfs[int(a)-1].append(int(b)-1)
for x in range(input()):
    a,b = raw_input().split()
    a = int(a) - 1
    b = int(b) - 1
    if dp[a] != []:
        if dp[a][b] == -1:
            print 'Not enough hallways!'
        else:
            print dp[a][b]
    else:
        dis = ndis[:]
        dis[a] = 0
        q = [a]
        while len(q) != 0:
            for x in bfs[q[0]]:
                if dis[q[0]] + t < dis[x] or dis[x] == -1:
                    dis[x] = dis[q[0]] + t
                    q.append(x)
            del q[0]
        dp[a] = dis
        if dis[b] == -1:
            print 'Not enough hallways!'
        else:
            print dis[b]
