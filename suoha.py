import random
import os

pc = 0
me = 0

def roll():
    arr = []
    for _ in range(5):
        arr.append(random.randint(1,6))
    return arr


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
    return groups

def judge(arr):
    if len(arr) == 1:
        return 6
    elif len(arr) == 2:
        return findmx(arr)+1
    elif len(arr) == 3:
        return 3 if findmx(arr) == 2 else 2
    elif len(arr) == 4:
        return 1
    else:
        shun = True
        for i in range(5):
            if arr[i][0] - arr[i - 1][0] > 1:
                shun = False
                break
        return (7 if shun else 0)

def findmx(arr):
    maxlen = 0
    for i in arr:
        if len(i) > maxlen:
            maxlen = len(i)
    return maxlen

def compare(arr1, arr2):
    arr1Sum = []
    arr2Sum = []
    for i in range(len(arr1)):
        arr1Sum.append(sum(arr1[i]))
        arr2Sum.append(sum(arr2[i]))
    arr1Sum.sort()
    arr1Sum.reverse()
    arr2Sum.sort()
    arr2Sum.reverse()
    for i in range(len(arr1Sum)):
        if arr1Sum[i] == arr2Sum[i]:
            continue
        else:
            return 1 if arr1Sum[i] > arr2Sum[i] else 0

while 1:
    pcDice = roll()
    pcDice.sort()
    os.system('clear')
    print('pc win : %d' % pc)
    print('you win : %d' % me)
    print('now pc \'s')
    print(pcDice)
    # inp = input()
    # if inp is 'exit':
    #     print('bye')
    #     break
    myDice = roll()
    myDice.sort()
    print('now your \'s')
    print(myDice)
    res = 0
    if myDice == pcDice:
        print('even')
        # input()
        continue
    elif judge(mkGroup(myDice)) == judge(mkGroup(pcDice)):
        res = compare(mkGroup(myDice),mkGroup(pcDice))
    else:
        res = 1 if judge(mkGroup(myDice)) > judge(mkGroup(pcDice)) else 0
    if res:
        print('you win')
        me += 1
    else:
        print('you lose')
        pc += 1
    # input()
