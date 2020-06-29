import random

pc = []
mine = []

for _ in range(5):
    pc.append(random.randint(1,6))
    mine.append(random.randint(1,6))

pc.sort()
mine.sort()

def mkGroup(arr):
    groups = []
    for x in arr:
        pushed = False
        for y in groups:
            if x == y[0]:
                y.append(x)
                pushed = True
        if not pushed:
            groups.append([x])
    return judge(groups)

def judge(arr):
    if len(arr) == 1:
        return 6
    elif len(arr) == 2:
        return findmx(arr)+1
    elif len(arr) == 3:
        return 3
    elif len(arr) == 4:
        return 2
    else:
        shun = True
        for i in range(5):
            if arr[i][0] - arr[i - 1][0] > 1:
                shun = False
                break
        return (7 if shun else 1)


        
def findmx(arr):
    maxlen = 0
    for i in arr:
        if len(i) > maxlen:
            maxlen = len(i)
    return maxlen
    

print(pc,mine)
print("me" if mkGroup(mine) > mkGroup(pc) else "me" if sum(mine) > sum(pc) else "pc")