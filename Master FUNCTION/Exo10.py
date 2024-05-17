def initial(nom):
    v = nom.split(" ")
    inisyal = ""
    for i in v:
        if i.find("-") == -1 or i.find("-") ==len(i)-1:
            inisyal += i[0].upper()
            
        else:
            a = i.split("-")
            for el in a:
                inisyal += el[0].upper()
            

    return inisyal

print(initial("Jean-Baptiste Jean"))
