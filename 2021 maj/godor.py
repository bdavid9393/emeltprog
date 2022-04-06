

with open('melyseg.txt') as g:
    adatok = g.read().split("\n")[:-1]

#print(adatok)

#1 Olvassa be és tárolja el a melyseg.txt fájl tartalmát! Írja ki a képernyőre, hogy az
# adatforrás hány adatot tartalmaz!

print("1. feladat:")
print("A fájl adatainak száma:", len(adatok))



# 2 Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen van a gödör
# alja azon a helyen! Ezt a távolságértéket használja majd a 6. feladat megoldása során is!

print("2. feladat")
szam = int(input("Adjon meg egy távolságértéket!" + " ")) - 1
melyseg = adatok[szam]

print("Ezen a helyen a felszín", melyseg, "méter mélyen van.")

#3 Határozza meg, hogy a felszín hány százaléka maradt érintetlen és jelenítse meg 2 tizedes
# pontossággal!

print("3. feladat")

szamlalo = 0
for x in adatok:
    if x == "0":
        szamlalo += 1
erintetlen = szamlalo / len(adatok) * 100

print("Az érintetlen terület aránya", "{:.2f}".format(erintetlen) + "%.")

#4 Írja ki a godrok.txt fájlba a gödrök leírását, azaz azokat a számsorokat, amelyek egy-egy
# gödör méterenkénti mélységét adják meg! Minden gödör leírása külön sorba kerüljön! Az
# állomány pontosan a gödrök számával egyező számú sort tartalmazzon!

# file = open("sajat.txt", "w")
# file.write("a macsak egy halatlan allat \n")
# file.write("a macsak egy halatlan allat \n")
# file.close()

#0 0 0 0 0 0 2 3 1 5 0 0 0 4 5 3 0 0 0

# file = open("godrok.txt", "w")
# voltEnter = True
# for t in adatok:
#     if t > "0":
#         voltEnter = False
#         file.write(t + " ")
#     else:
#         if not voltEnter:
#            file.write("\n")
#            voltEnter = True
# file.close()
#
# with open('godrok.txt') as g:
#     godorAdatok = g.read()[:-1]
#
# file = open("godrok.txt", "w")
# file.write(godorAdatok)
# file.close()


#5 Határozza meg a gödrök számát és írja a képernyőre!

print("5. feladat")

voltNulla = True
godrokSzama = 0
for z in adatok:
    if z > "0":
        voltNulla = False
    else:
        if not voltNulla:
            godrokSzama += 1
            voltNulla = True

print("A gödrök száma:", godrokSzama)


#6 Ha a 2. feladatban beolvasott helyen nincs gödör, akkor „Az adott helyen nincs gödör.”
# üzenetet jelenítse meg, ha ott gödör található, akkor határozza meg, hogy

# a) mi a gödör kezdő és végpontja! A meghatározott értékeket írja a képernyőre!
# (Ha nem tudja meghatározni, használja a további részfeladatoknál a 7 és 22
# értéket, mint a kezdő és a végpont helyét)

print("6.feladat")

if adatok[szam] == "0":
    print("Az adott helyen nincs gödör.")

godorEleje = 0
godorVege = 0
for g in range(szam, 2000):
    if adatok[g] == "0":
        godorVege = g
        break
for h in range(szam, 0, -1):
    if adatok[h] == "0":
        godorEleje = h + 2
        break
print("a)")
print("A gödör kezdete:", godorEleje, "méter, a gödör vége:", godorVege, "méter.")

#6b a legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e! Azaz a gödör
# az egyik szélétől monoton mélyül egy pontig, és onnantól monoton emelkedik a
# másik széléig. Az eredménytől függően írja ki a képernyőre a „Nem mélyül
# folyamatosan.” vagy a „Folyamatosan mélyül.” mondatot

# mely = 0
#
# for p in range(godorEleje, godorVege):
#     if adatok[p] > mely:



#6c mekkora a legnagyobb mélysége! A meghatározott értéket írja a képernyőre!

legMely = "0"
for t in range(szam, 2000):
    if adatok[t] == "0":
        break
    else:
        if adatok[t] > legMely:
            legMely = adatok[t]
for p in range(szam, 0, -1):
    if adatok[p] == "0":
        break
    else:
        if adatok[p] > legMely:
            legMely == adatok[t]

print("c)")
print("A legnagyobb mélysége", legMely, "méter.")


#6d mekkora a térfogata, ha szélessége minden helyen 10 méternyi! A meghatározott
# értéket írja a képernyőre!

melysegek = []

for c in range(szam+1, 2000):
    if adatok[c] == "0":
        break
    else:
        melysegek.append(adatok[c])
for v in range(szam, 0, -1):
    if adatok[v] == "0":
        break
    else:
        melysegek.append(adatok[v])

osszmely = 0
for b in melysegek:
    if b > "0":
        osszmely += int(b)
print('d)')
print("A térfogata", osszmely * 10, "m^3.")

#e a félkész csatorna esőben jelentős mennyiségű vizet fogad be. Egy gödör annyi
# vizet képes befogadni anélkül, hogy egy nagyobb szélvihar hatására se öntsön
# ki, amennyi esetén a víz felszíne legalább 1 méter mélyen van a külső felszínhez
# képest. Írja a képernyőre ezt a vízmennyiséget!

adatCS = []

for b in melysegek:
    if b > "0":
        adatCS.append(int(b)-1)

vizTerF = 0
for a in adatCS:
    if a > 0:
        vizTerF += int(a)
print("e)")
print("A vízmennyiség", vizTerF * 10, "m^3.")







