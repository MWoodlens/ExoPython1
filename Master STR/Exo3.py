ch = "you can do it"
ch = ch.split(" ")
for i in range(len(ch)):
    ch[i] = ch[i].capitalize()

ch = " ".join(ch)
print(ch)
