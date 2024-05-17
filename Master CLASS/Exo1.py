import os
class File1:
    def __init__(self,link):
        self.link = link
    
    def read(self):
        try:
            with open(self.link,"r") as f1:
                lines = f1.readlines()
                return lines
        except FileNotFoundError:
           return "Le fichier est introuvable"
    
    def add(self,contenu):
        try:
            with open(self.link,"a") as f2:
                f2.write(contenu)
                return "contenu enregistrer"
        except FileNotFoundError:
            return "Fichier introuvable"
    
    def delete_contents(self):
        try:
            with open(self.link,"w") as f3:
                ...
            return "Le fichier est vide maintenant"
        except FileNotFoundError:
            return "Fichier introuvable"
    def remove(self, permission = False):
        if permission:
            try:
                os.remove(self.link)
                return "le fichier est supprimé avec succès"
            except FileNotFoundError:
                return "Fichier introuvable"
            except Exception as e:
                return f"une erreur de suppression :{e}"
        else:
            return "Vous n'avez pas le droit de faire la suppression"
        
#-----------------------------
link = "./Master CLASS/TestP.txt"
file1 = File1(link)

#add
a = file1.add("Blaise Gabriel")
print(a)

#read
r = file1.read()
print(r)

#delete_contents
dc = file1.delete_contents()
print(dc)

#remove
rmf = file1.remove(True)
print(rmf)


