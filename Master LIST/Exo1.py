n = int(input("Antre vale n :"))
l = []
for i in range(n+1):
    if i % 2 == 0:
        l.append(i)

print(f"Men eleman ki divizib pa 2 nan enteval [0,{n}] : {l}")