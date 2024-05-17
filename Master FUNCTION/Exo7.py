alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
def kripte(mot):
    kriptaj =""
    for i in mot.upper():
        kriptaj += str(alphabet.index(i))+"-"  

    return kriptaj[:-1]

print(kripte("Bonjour"))
