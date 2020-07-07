
christian = [True] * 30

count,idx,number = 0,0,0

while count < 15:
    if christian[idx]:
        number += 1
        if number == 9:
            christian[idx] = False
            count += 1
            number = 0
    idx += 1
    idx %= 30

print(christian)