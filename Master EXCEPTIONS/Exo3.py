d1 = {"Nom" : "BLAISE","Prenom":"Amboise","Numero":19}

def find_by_key(k):
    try:
        return f"Vale ki afekte a kle : '{k}' se : {d1[k]}"
    except KeyError :
        d1[k] = None
        return f"Kle '{k}' pat egziste nan diksyone a men li ajoute kounya men se vale None ki afekte ak li"
    
print(find_by_key("Nom"))
print(d1)
print(find_by_key("Adresse"))
print(d1)

