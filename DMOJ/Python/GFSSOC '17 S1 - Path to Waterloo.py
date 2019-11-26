n, t = raw_input().split()
n = int(n)
t = int(t)
locl = ['home']
dis = [0]
bfs = [[]]
for x in range(n):
    dis.append(100000000)
    locl.append(raw_input())
    bfs.append([])
locl.append('Waterloo GO')
dis.append(100000000)
bfs.append([])
for x in range(t):
    a,b = raw_input().split('-')
    bfs[locl.index(a)].append(locl.index(b))
    bfs[locl.index(b)].append(locl.index(a))
q = [0]
while len(q) != 0:
    for x in bfs[q[0]]:
        if dis[q[0]] + 1 < dis[x] or dis[x] == -1:
            dis[x] = dis[q[0]] + 1
            q.append(x)
    del q[0]
if dis[-1] == 100000000:
    print 'RIP ACE'
else:
    print dis[-1]
