import time 
#niet meer nodig, ooit gebruikt voor sleep ding
scheldwoorden = ["fuck", "kut", "jk :))"]
# dit was de array van scheldwoorden 
#keuzeding functie begint hier
def startding():
    keuze = str(input('kies tussen a en b \n a is de array en b is toevoegen aan de array\n en typ c voor verwijderen laatste scheldwoord'))
    if keuze == 'a':
        alles()
    elif keuze == 'b':
        toevoegen()
    elif keuze == 'c':
        verwijderen()	
					
		#alles anders dan a,b en c	
    else:
        print('jij idoot kan echt niks lmao')
        startding()
#keuze ding eindigt hier
#geeft de volledige array aan
def alles():
    print(scheldwoorden)
    startding()
#toevoegen in de scheldwoorden array, automatisch naar str
def toevoegen():
    scheldwoorden.append(str(input("geef scheldwoorden nu:\n")))
    startding()
#functie van verwijderen scheldwoord, moet antwoord geven in nummer
def verwijderen():	
    scheldwoorden.pop(int(input('welke moet weg, kies nummer:\n')))
    startding() 
 

		
		
#eerste message voor keuze	
keuze = str(input('kies tussen a en b \n a is de array en b is toevoegen aan de array\n en c + nummer is verwijderen'))
if keuze == 'a':
    alles()
elif keuze == 'b':
    toevoegen()
elif keuze == 'c':
    verwijderen()
else:
    print('jij idoot kan echt niks lmao')
    startding()
