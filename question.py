string=[]
while True:
    words=input("")
    if words:
        string.append(words.upper())
    else:
        break;

for words in string:
    print(words)
