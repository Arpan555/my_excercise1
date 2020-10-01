string=[]
while True:
    line=input()
    if line:
        string.append(line.upper())
    else:
        break;
for line in string:
    print(line)
