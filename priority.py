processes=[['p1',0,3,3],
          ['p2',1,6,4],
          ['p3',3,1,9],
          ['p4',2,2,7],
          ['p5',4,4,8]]
m=len(processes)
ct = [0]*m

processes.sort(key=lambda a:a[1])
# print(processes)

for i in range(m):
    if processes[i][1]==0:
        ct1 = processes[i][2]+ct[i-1]
        ct[i]=ct1
        break
    for j in range(0,ct[i]):
        mini = min(processes[][3])
        index = processes.index(mini)
        ct2 = processes[mini][2]+ct[i-1]
        ct[i]=ct2
        print(ct2)
        break

    print(ct1)
 