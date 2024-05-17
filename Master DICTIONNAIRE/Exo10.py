d1 = {"Nom":"ANTOINE","Prenom":"Paul","Age" : 30, "assets": ["laptop", "phone"], "price":(200,110), "numero":12.0}
d2 = {"Nom":"SIMON","Prenom":"Magloire","Age" : 35, "assets": ["watch", "earphone"], "price":(80,45), "numero": 11, "moyenne":90.89}
d3 = {}

for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        if k1 == k2:
            #tes antye
            if type(v1) == int :
                if type(v2) == int:
                    d3[k1] = v1 + v2
                    break
                else:
                    d3[k1] = v1
                    break
            else:
                if type(v2) == int:
                    d3[k1] = v2
                    break
            #tes chenn
            if  type(v1) == str :
                if type(v2) == str:
                    d3[k1] = v1 +""+ v2
                    break
                else:
                    d3[k1] = v1
                    break
            else:
                if type(v2) == str:
                    d3[k1] = v2
                    break
            
            #tes lis 
            if  type(v1) == list :
                if type(v2) == list:
                    d3[k1] = v1 + v2
                    break
                else:
                    d3[k1] = v1
                    break
            else:
                if type(v2) == list:
                    d3[k1] = v2
                    break
            
            #tes tuple
            if  type(v1) == tuple :
                if type(v2) == tuple:
                    d3[k1] = v1 + v2
                    break
                else:
                    d3[k1] = v1
                    break
            else:
                if type(v2) == tuple:
                    d3[k1] = v2
                    break
            
for k1,v1 in d1.items():
    if k1 not in d3:
        if type(v1) == int or type(v1) == str or type(v1) == list or type(v1) == tuple:
            d3[k1] = v1


for k2,v2 in d2.items():
    if k2 not in d3:
        if type(v2) == int or type(v2) == str or type(v2) == list or type(v2) == tuple:
            d3[k2] = v2

print(d1)
print(d2)
print(d3)
        


             