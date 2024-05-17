alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
def dekripte(kriptaj):
    mot=kriptaj.split("-")
    for i in range(len(mot)):
        mot[i] = alphabet[int(mot[i])]
    
    return "".join(mot)

print(dekripte("0-11-14"))
    