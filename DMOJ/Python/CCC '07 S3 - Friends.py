N = input()
l = []
for x in range(10000):
    l.append(0)
for x in range(1,N+1):
    a,b = raw_input().split()
    a = int(a)
    b = int(b)
    l[a] = b
while 1:
    start,end = raw_input().split()
    start = int(start)
    end = int(end)
    if start == 0 and end == 0:
        break
    q = []
    q.append(l[start])
    v = [l[start]]
    c = 0
    t = False
    while 1:
        for x in v:
            if l[q[0]] == x:
                t = True
        if t == True:
            check = False
            break
        if l[q[0]] == 0:
            check = False
            break
        if q[0] == end:
            check = True
            print 'Yes',c
            break
        q.append(l[q[0]])
        c+=1
        del q[0]
    if check == False:
        print 'No'
