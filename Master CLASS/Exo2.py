class Vivan:
    def __init__(self, pye, men, non, laj):
        self.pye = pye
        self.men = men
        self. non = non
        self.laj = laj

class Moun(Vivan):
    def __init__(self, pye, men, non, laj, ote):
        super().__init__(pye, men, non, laj)
        self.ote = ote

    def __str__(self):
        return("Non     : " + str(self.non) + "\n" +
               "Nb men  : " + str(self.men) + "\n" +
               "Nb pye  : " + str(self.pye) + "\n" +
               "laj     : " + str(self.laj) + "\n" +
               "ote     : " + str(self.ote))

class S:
    def __init__(self, pye, zel):
        self.pye = pye
        self.zel = zel

class Poul(S):
    def __init__(self,pye,zel,koule,pwa):
        super().__init__(pye,zel)
        self.koule = koule
        self.pwa = pwa
    
    def __str__(self):
        return("Nb pye   : " + str(self.pye) + "\n" +
               "Nb zel : " + str(self.zel) + "\n" +
               "koule : " + str(self.koule) + "\n" +
               "pwa     : " + str(self.pwa))




moun1 = Moun(2,2,"Pierre Petit",30,180)
moun2 = Moun(2,2,"Blaise Magloire",29,182)
#--------------------------------------------
poul1 = Poul(2,2,"nwa",20)
poul2 = Poul(2,2,"gri",18)

print(str(moun1))
print("---------------------------------")
print(str(moun2))
print("---------------------------------")
print("---------------------------------")
print(str(poul1))
print("---------------------------------")
print(str(poul2))