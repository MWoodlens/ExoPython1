
def verifye_chenn(ch,ref):
    for l in ch:
        if l.upper() not in ref:
            return False

        return True


ref = "IVXLCDM"
ch = input(f"Antre yon chenn ki gen let sa yo selman {ref} : ")
vef = verifye_chenn(ch,ref)
if vef == False:
    raise ValueError(f"let chenn nan dwe fe pati : {ref}")
else:
    print("Byen jwe!")

    