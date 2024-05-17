l1 = ["Matthieu","Marc","Luc","Jean","Actes","Romain","1 Corinthiens","2 Corinthiens","Galates","Ephesiens"]
l2 =[]
for i, el in enumerate(l1):
    if i % 3 ==0:
        l2.append(el)

print(l1)
print(l2)