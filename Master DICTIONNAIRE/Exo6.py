d1 = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}

for key,val in d1.items():
    if type(val) == str:
        d1[key] = "_"+val+"_"

print(d1)