import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
def generateur_unique(n):
    code = "".join(random.sample(alphabet,n))
    return code
    

print(generateur_unique(20))