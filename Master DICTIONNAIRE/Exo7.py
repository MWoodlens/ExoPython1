d1 = {"a": "12", "b": "abc", "c": "12r", "d":"90"}
d2 = {}

for key, value in d1.items():
    if value.isdigit() :
        d2[key] = value

print(d1)
print(d2)