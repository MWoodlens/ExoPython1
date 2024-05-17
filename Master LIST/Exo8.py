l1 = ["chemiz","sandal","chapo","linet","mont"]
l2 = ["soulye","chemiz","sentiwon","pantalon","chapo"]
l3 = list(set(l1).symmetric_difference(set(l2)))
#l3 = list(set(l1)-set(l2)) + list(set(l2)-set(l1))

print(l1)
print(l2)
print(l3)