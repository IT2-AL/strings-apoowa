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
#7. Napiš program, který se zeptá na jméno, pak na příjmení a pak vypíše iniciály – první písmena zadaných jmeno
jmeno = input("zadejjmeno: ")
prijmeni = input("zadej prijmeni: ")

inicialy = jmeno[0].upper() + prijmeni[0].upper()
print("inicialy jsou:", inicialy)
#Výsledný commit - String_done