
# 1 Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)!
# A későbbi feladatokat ezen értékek felhasználásával kell megoldania!

# print("1. feledat")
# nev = input("Adja meg a bemeneti fájl nevét! ")
# sorSzam = int(input("Adja meg egy sor számát! "))
# oszlopSzam = int(input("Adja meg egy oszlop számát! "))


#2 Az előző feladatban beolvasott névnek megfelelő fájl tartalmát olvassa be, és tárolja el a
# táblázat adatait!
import math

nev = "konnyu.txt"
sorSzam = 3
oszlopSzam = 3     #TODO törölni


with open(nev) as f:
    adatok = f.read().split("\n")[:-1]
# print(adatok)

# 3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely...
# a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott
# helyet még nem töltötték ki.” szöveget jelenítse meg!
# b. melyik résztáblázathoz tartozik!

# print("3. feladat")
# if adatok[sorSzam - 1].split(" ")[oszlopSzam - 1] == "0":
#     print("Az adott helyet még nem töltötték ki.")
# else:
#     print("Az adott helyen szereplő szám:", adatok[sorSzam - 1].split(" ")[oszlopSzam - 1])
#
#
#
# if sorSzam == 1 or sorSzam == 2 or sorSzam == 3:
#     if oszlopSzam == 1 or oszlopSzam == 2 or oszlopSzam == 3:
#         print("A hely a(z) 1 résztáblázathoz tartozik.")
#     if oszlopSzam == 4 or oszlopSzam == 5 or oszlopSzam == 6:
#         print("A hely a(z) 2 résztáblázathoz tartozik.")
#     if oszlopSzam == 7 or oszlopSzam == 8 or oszlopSzam == 9:
#         print("A hely a(z) 3 résztáblázathoz tartozik.")
#
# if sorSzam == 4 or sorSzam == 5 or sorSzam == 6:
#     if oszlopSzam == 1 or oszlopSzam == 2 or oszlopSzam == 3:
#         print("A hely a(z) 4 résztáblázathoz tartozik.")
#     if oszlopSzam == 4 or oszlopSzam == 5 or oszlopSzam == 6:
#         print("A hely a(z) 5 résztáblázathoz tartozik.")
#     if oszlopSzam == 7 or oszlopSzam == 8 or oszlopSzam == 9:
#         print("A hely a(z) 6 résztáblázathoz tartozik.")
#
# if sorSzam == 7 or sorSzam == 8 or sorSzam == 9:
#     if oszlopSzam == 1 or oszlopSzam == 2 or oszlopSzam == 3:
#         print("A hely a(z) 7 résztáblázathoz tartozik.")
#     if oszlopSzam == 4 or oszlopSzam == 5 or oszlopSzam == 6:
#         print("A hely a(z) 8 résztáblázathoz tartozik.")
#     if oszlopSzam == 7 or oszlopSzam == 8 or oszlopSzam == 9:
#         print("A hely a(z) 9 résztáblázathoz tartozik.")













# #4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy
# pontossággal jelenítse meg a képernyőn!

# nullak = 0
# for q in adatok:
#     for t in q.split(" "):
#         if t == "0":
#             nullak += 1
#
# print("4. feladat")
# print("Az üres helyek aránya: " + str(round(nullak / 81 * 100, 1)) + "%")


#
# Vizsgálja meg, hogy a fájlban szereplő lépések lehetségesek-e a beolvasott táblázaton!
# Tekintse mindegyiket úgy, mintha az lenne az egyetlen lépés az eredeti táblázaton, de ne
# hajtsa azt végre! Állapítsa meg, hogy okoz-e valamilyen ellentmondást a lépés végrehajtása!
# Írja ki a lépéshez tartozó három értéket, majd a következő sorba írja az alábbi
# megállapítások egyikét! Ha több megállapítás is igaz, elegendő csak egyet megjelenítenie.
# • „A helyet már kitöltötték”
# • „Az adott sorban már szerepel a szám”
# • „Az adott oszlopban már szerepel a szám”
# • „Az adott résztáblázatban már szerepel a szám”
# • „A lépés megtehető”

# ertek  sor   oszlop
# 9       2      4
ertek = 4
sor = 7
oszlop = 4

igaz = True

if igaz == True:
    if adatok[sor-1].split(" ")[oszlop-1] > "0":
      print("A helyet már kitöltötték")
      igaz = False

if igaz == True:
    for m in adatok[sor-1].split(" "):
         if int(m) == ertek:
             print("Az adott sorban már szerepel a szám")
             igaz = False

if igaz == True:
    for p in adatok[:9]:
         if int(p.split(" ")[oszlop - 1]) == ertek:
             print("Az adott oszlopban már szerepel a szám")
             igaz = False

if igaz == True:
    for z in adatok[(math.ceil(sor/3) - 1) * 3:math.ceil(sor/3) * 3]:
         for q in range((math.ceil(oszlop/3) - 1) * 3, math.ceil(oszlop/3) * 3):
              if int(z.split(" ")[q]) == ertek:
                   print("Az adott résztáblázatban már szerepel a szám")
                   igaz = True

if igaz == True:
    print("A lépés megtehető")






