with open("kerites.txt") as f:
    adatok = f.read().split("\n")[:-1]

# print(adatok)

# 2. Írja a képernyőre, hogy hány telket adtak el az utcában!

print("2. feladat")
print("Az eladott telkek száma:", len(adatok), "\n")

# 3. Jelenítse meg a képernyőn, hogy az utolsó eladott telek
# a. melyik (páros / páratlan) oldalon talált gazdára!
# b. milyen házszámot kapott!

print("3. feladat")
utolsohaz = adatok[-1]
if utolsohaz.split(" ")[0]:
    print("A páros oldalon adták el az utolsó telket.")
else:
    print("A páratlan oldalon adták el az utolsó telket.")

szamlalo = 0
for t in adatok:
    if t.split(" ")[0] == "0":
        szamlalo += 2

print("Az utolsó telek házszáma:", szamlalo, "\n")

#4 Írjon a képernyőre egy házszámot a páratlan oldalról, amely melletti telken ugyanolyan
# színű a kerítés! (A hiányzó és a festetlen kerítésnek nincs színe.) Feltételezheti, hogy van
# ilyen telek, a több ilyen közül elég az egyik ház számát megjeleníteni.
# 1 10 K
print("4.feladat")
szin = ""
szamlalo = -1
for x in adatok:
    if x.split(" ")[0] == "1":
        if szin == x.split(" ")[-1] and x.split(" ")[-1] != ":" and x.split(" ")[-1] != "#":
            print("A szomszédossal egyezik a kerítés színe: ", szamlalo, "\n")
        szin = x.split(" ")[-1]
        szamlalo += 2


# 5 Kérje be a felhasználótól egy eladott telek házszámát, majd azt felhasználva oldja meg a
# következő feladatokat!
#      a. Írja ki a házszámhoz tartozó kerítés színét, ha már elkészült és befestették,
# egyébként az állapotát a „#” vagy „:” karakter jelöli!
#      b. A házszámhoz tartozó kerítést szeretné tulajdonosa be- vagy átfesteni. Olyan
# színt akar választani, amely különbözik a mellette lévő szomszéd(ok)tól és a
# jelenlegi színtől is. Adjon meg egy lehetséges színt! A színt a teljes palettából
# (A–Z) szabadon választhatja meg.


print("5. feladat")
szam = int(input("Adjon meg egy házszámot! "))

hazSzam = 2
hazSzin = []
noszin = []
if szam % 2 == 0:
    for k in adatok:
        if k.split(" ")[0] == "0":
            hazSzin.append(k.split(" ")[-1])
            if hazSzam == szam:
                print("A kerítés színe / állapota:", k.split(" ")[-1])
            hazSzam += 2

hazSzam2 = 1

if szam % 2 == 1:
    for x in adatok:
        if x.split(" ")[0] == "1":
            hazSzin.append(x.split(" ")[-1])
            if hazSzam2 == szam:
                print("A kerítés színe / állapota:", x.split(" ")[-1])
            hazSzam2 += 2

noszin.append(hazSzin[int(szam / 2 - 1)])
if len(hazSzin) != int(szam / 2 + 1):
    noszin.append(hazSzin[int(szam / 2 + 1)])
noszin.append(hazSzin[int(szam / 2 )])
print(noszin)
szinek = ["A", "B", "C", "D", "E", "F", "G", "J"]
for m in szinek:
    if m not in noszin:
        print("Egy lehetséges festési szín:", m)
        break







# 6. Jelenítse meg az utcakep.txt fájlban a páratlan oldal utcaképét az alábbi mintának
# megfelelően!

file = open("utcakep.txt", "w")

szamlalo = -1
for t in adatok:
    if t.split(" ")[0] == "1":
        file.write(t.split(" ")[-1] * int(t.split(" ")[1]))

file.write("\n")

for x in adatok:
    if x.split(" ")[0] == "1":
        szamlalo += 2
        if szamlalo <= 9:
            file.write(str(szamlalo) + " " * (int(x.split(" ")[1]) -1))
        if szamlalo > 9 and szamlalo <= 99:
            file.write(str(szamlalo) + " " * (int(x.split(" ")[1]) - 2))
        if szamlalo > 99:
            file.write(str(szamlalo) + " " * (int(x.split(" ")[1]) - 3))
file.close()