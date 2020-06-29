
string = "HELLO WORLD"
cipher = "GDKKN VNQKC"

output = ""

for i in cipher:
    if i != ' ':
        a = (ord(i)-12) % 26 +65
        output += chr(a)
    else:
        output += ' '

print(output)
