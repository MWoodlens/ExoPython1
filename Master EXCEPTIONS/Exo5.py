from typing import Any


class Liv:
    def __init__(self,isbn,tit,nb_paj) :
        self.isbn = isbn
        self.tit = tit
        self.nb_paj= nb_paj
    


liv1 = Liv(1234,"Code with fun",300)
try:
    print(liv1.isbn())
except Exception as e:
    print (f"wap eseye rele yon atribi tankoui yon fonksyon : {e}")
