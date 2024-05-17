def add5(dijit):
    try:
        val = float(dijit) + 5
        return f"rezilta {dijit} + 5 = {val}"
    except ValueError as e:
        return f"Ou pa tape yon dijit :{e}"
    
dijit = input("Antre yon dijit : ")
print(add5(dijit))