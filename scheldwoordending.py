scheldwoorden = ["fuck", "kut", "jk :))"]
def startding():
    keuze = str(input('kies tussen a en b \n a is de array en b is toevoegen aan de array\n'))
    if keuze == 'a':
        alles()
    elif keuze == 'b':
        toevoegen()
    else:
        print('jij idoot kan echt niks lmao')
startding()
def alles():
    print(scheldwoorden)
    startding()

def toevoegen():
    scheldwoorden.append(str(input("geef scheldwoorden nu")))
    startding()

