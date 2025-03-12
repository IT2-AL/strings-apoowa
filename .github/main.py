#1. Přepsání stringu na velká písmena
'slovo'.upper()
#2. Přepsání stringu na malá písmena
'slovo'.lower()
#3. Počet výskytů p, k, y ve slově Program, Python
'slovo'.count("s")
#4. Vypište 3. písmeno ze slova Python
'python'[:4]
#5. Vypište prostřední 3 písmena slova Program
'program'[2:5]
#6. Spojte string "Ahoj" a "Slunce"
"ahoj" + "slunce"
#7. Napiš program, který se zeptá na jméno, pak na příjmení a pak vypíše iniciály – první písmena zadaných jmen.
jmeno = input("zadejte jmeno: ")
prijmeni = input("zadejte prijmeni: ")

inicialy = jmeno[0].upper() + prijmeni[0].upper()
print("inicialy jsou:", inicialy)

#Výsledný commit - String_done
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#1. Vytvořte pole stringů, které bude obsahovat pět vašich oblíbených měst.
pole = ["praha", "brno", "ostrava", "plzen", "lednice"]

#2. Vypište toto pole
print(pole)

#3. Vypište čtvrté město z tohoto pole.
print(pole[3])

#4. Pomocí cyklu for vypište všechna města pole.
for mesto in pole:
    print(mesto)

#5. Vypište na obrazovku všechna města v seznamu, a před každé město vypište jeho pořadové číslo.
for i, mesto in enumerate(pole, start=1):
    print(f"{i}. {mesto}")

#6. Přidejte do pole další město.
pole.append("karlovy vary")
print(pole) 

#7. Odstraňte z pole druhé město.
del pole[1]

#8. Vypište upravené pole na obrazovku.
print("upravene pole:", pole)

#9. Seřaďte pole měst abecedně.
pole.sort
print("serazene pole:", pole)

#10. Napište funkci, která zkontroluje, zda se v poli měst nachází zadané město.
def najdi_mesto(seznam, hledane_mesto):
    return hledane_mesto in seznam

#11. Vytvořte nové pole, který bude obsahovat pouze řetězce, které začínají na písmeno „a“.
pole_s_a = [mesto for mesto in pole if mesto.startswith("a")]
print("mesta zacinajici na 'a':", pole_s_a)

#12. Vypište na obrazovku všechna slova, která mají více než 5 písmen.
delsi_slova = [mesto for mesto in pole if len(mesto) > 5]
print("mesta vice nez 5 pismen:", delsi_slova)

#Výsledný commit - String_Pole
