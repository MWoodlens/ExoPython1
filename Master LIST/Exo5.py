l1 =[1,2,3,4,5,6,7,8,9]
l2 = []
a = 1
for i in range(0,len(l1),3):
    l2.append(tuple(l1[i:i+3]))

print(l2)


