ch = "You have to be strong"
ch = ch.split(" ")
nch =""
for i in ch:
    nch = nch+""+i[:1]
ch = " ".join(ch)
print(ch)
print(nch)