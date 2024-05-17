lis = ["a","b","c","d","e","f","g","h","i"]

def afiche_vale(i):
    try:
        val = lis[i]
        return f"vale ki nan endeks {i} la se : {val}"
    except IndexError:
        return "Endeks ou antre a depase longè lis la "
    except TypeError:
        return "Endeks ou antre a pa bon"

print(afiche_vale(10))
print(afiche_vale(8))
print(afiche_vale("Bonjour"))