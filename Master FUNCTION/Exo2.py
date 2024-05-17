import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
def generateur(n):
    code =""
    for i in range(n):
        code = code +""+ alphabet[random.randint(0,len(alphabet)-1)]
    
    return code

print(generateur(10))

    
    
