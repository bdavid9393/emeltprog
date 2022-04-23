
with open("valaszok.txt") as p:
    adatok = p.read().split("\n")[:-1]

print("1. feladat: Az adatok beolvasása")
print()

# 2. Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett részt
# a tesztversenyen!

print("2. feladat: A vetélkedőn", len(adatok[1:]), "versenyző indult.")
print()

# 3. Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a hozzá
# eltárolt válaszokat! Feltételezheti, hogy a fájlban létező azonosítót adnak meg

szam = input("3. feladat: A versenyző azonosítója = ")

for t in adatok[1:]:
    if t.split(" ")[0] == szam:
        print(t.split(" ")[1] + "\t" + "(a versenyző válasza)")
print()

# 4. Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba „+” jelet tegyen,
# ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy
# szóközt! A kiírást a mintának megfelelő módon alakítsa ki!

joEredmeny = adatok[0]
valasz = ""
for t in adatok[1:]:
    if t.split(" ")[0] == szam:
        valasz += t.split(" ")[1]


print("4. feladat:")
print(joEredmeny + "\t" + "(a helyes megoldás)")

for v in range(0, 14):
    if valasz[v] == joEredmeny[v]:
        print("+", end="")
    else:
        print(" ", end="")
print("\t(a versenyző helyes válaszai)")
print()

# 5. Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra
# helyes megoldást, és ez a versenyzők hány százaléka! A százalékos eredményt a mintának
# megfelelően, két tizedesjeggyel írassa ki!

sorSzam = int(input("5. feladat: A feladat sorszáma = "))
szamlalo = 0
for l in adatok[1:]:
    feladatok = l.split(" ")[1]
    if feladatok[sorSzam - 1] == joEredmeny[sorSzam - 1]:
        szamlalo += 1
szazalek = szamlalo / len(adatok[1:]) * 100
print("A feladatra", szamlalo, "fő, a versenyzők", str("{:.2f}".format(szazalek)) + "%-a adott helyes választ.")
print()


# 6. A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat
# 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér. Határozza meg az egyes
# versenyzők pontszámát, és a listát írassa ki a pontok.txt nevű állományba! Az állomány
# minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot
# tartalmazza!
print("6. feladat: A versenyzők pontszámának meghatározása")
file = open("pontok.txt", "w")
for k in adatok[1:]:
    feladatok = k.split(" ")[1]
    szamlalo = 0
    for t in range(0, 5):
        if feladatok[t] == joEredmeny[t]:
            szamlalo += 3
    for t in range(5, 10):
        if feladatok[t] == joEredmeny[t]:
            szamlalo += 4
    for t in range(10, 13):
        if feladatok[t] == joEredmeny[t]:
            szamlalo += 5
    if feladatok[13] == joEredmeny[13]:
            szamlalo += 6
    if k != adatok[len(adatok[1:])]:
        file.write(k.split(" ")[0] + " " + str(szamlalo) + "\n")
    else:
        file.write(k.split(" ")[0] + " " + str(szamlalo))
file.close()
print()

# 7. A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5
# indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki. Így megtörténhet az is,
# hogy nem kerül sor mindegyik díj kiadására. Írassa ki a mintának megfelelően a képernyőre
# a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben!

print("7. feladat: A verseny legjobbjai:")

with open("pontok.txt") as t:
    pontszamok = t.read().split("\n")

pontok = []
for o in pontszamok:
    if int(o.split(" ")[1]) not in pontok:
        pontok.append(int(o.split(" ")[1]))
pontok.sort(reverse=True)


for z in pontok[:3]:
    for i in pontszamok:
        if str(z) == i.split(" ")[1]:
            print(pontok.index(z)+1, ". díj (", z, " pont): ", i.split(" ")[0], sep="")
# 1. díj (56 pont): JO001




