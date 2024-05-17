class Liv:
    def __init__(self,isbn,tit,nb_paj) :
        self.isbn = isbn
        self.tit = tit
        self.nb_paj= nb_paj
    
   
liv1 = Liv(1234,"Code with fun",300)
try:
    print(liv1.ote)
except AttributeError as e:
    e = str(e).split(" ")
    liv1.__setattr__(e[-1][1:-1],"inconnu")
    print(f"Atribi ou tap eseye aksede avel la pat egziste men nou kreyel pou ou kounya")
    print(liv1.ote)

