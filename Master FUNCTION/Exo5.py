import random

def generate_slug(l1):
    sl = ""
    for c in l1:
        c = str(c)
        while True:
            a = random.randint(0,len(c)-1)
            if c[a].isalnum() or c[a] == "-":
                sl += c[a]
                break
    
    return sl

l1 = ["Bonjour","Pierre-Jacques","petit@gmail.com",123456789]
print(generate_slug(l1))
            
