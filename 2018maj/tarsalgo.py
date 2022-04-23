with open("ajto.txt") as f:
    adatok = f.read().split("\n")[:-1]

# print(adatok)

# 2. Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon belül először
# lépett be az ajtón, és azét, aki utoljára távozott a megfigyelési időszakban!

print("2. feladat")
utolso = 0
for t in adatok:
    if t.split(" ")[-1] == "be":
        print("Az első belépő:", t.split(" ")[2])
        break
for k in adatok:
    if k.split(" ")[-1] == "ki":
        utolso = k.split(" ")[2]
print("Az utolsó kilépő:", utolso)
print()

# 3. Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a társalgó ajtaján!
# A meghatározott értékeket azonosító szerint növekvő sorrendben írja az athaladas.txt
# fájlba! Soronként egy személy azonosítója, és tőle egy szóközzel elválasztva az áthaladások
# száma szerepeljen!

file = open("athaladas.txt", "w")

szemelyek = []
for p in adatok:
    if p.split(" ")[2] not in szemelyek:
        szemelyek.append(p.split(" ")[2])


for l in range(1, len(szemelyek) + 1):
    athaladas = 0
    for i in adatok:
        if i.split(" ")[2] == str(l):
            athaladas += 1
    if athaladas != 0:
        file.write(str(l) + " " + str(athaladas) + "\n")
file.close()

# 4. Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén a társalgóban
# tartózkodtak!

print("4.feladat")
print("A végén a társalgóban voltak: ",end="")

for x in range(0, 101):
    beKi = ""
    for y in adatok:
        if y.split(" ")[2] == str(x):
            beKi = y.split(" ")[-1]
    if beKi == "be":
        print(str(x) + " ", end="")

print("\n")

# 5. Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot
# (óra:perc), amikor a legtöbben voltak bent!

print("5.feladat")

letSzam = []
szamlalo = 0
for t in adatok:
    if t.split(" ")[-1] == "be":
        szamlalo += 1
        letSzam.append(szamlalo)
    if t.split(" ")[-1] == "ki":
        szamlalo -= 1
        letSzam.append(szamlalo)
ora = adatok[letSzam.index(max(letSzam))].split(" ")[0]
perc = adatok[letSzam.index(max(letSzam))].split(" ")[1]

print("Például", ora + ":" + perc + "-kor voltak a legtöbben a társalgóban.\n")

# 6. Kérje be a felhasználótól egy személy azonosítóját! A további feladatok megoldásánál ezt
# használja fel!

print("6. feladat")

azonosito = input("Adja meg a személy azonosítóját! ")

print()
#
# 7. Írja a képernyőre, hogy a beolvasott azonosítóhoz tartozó személy mettől meddig
# tartózkodott a társalgóban!
print("7. feladat")
for u in adatok:
    if u.split(" ")[2] == str(azonosito):
        if u.split(" ")[-1] == "be":
            print(u.split(" ")[0] + ":" + u.split(" ")[1] + "-", end="")
        if u.split(" ")[-1] == "ki":
            print(u.split(" ")[0] + ":" + u.split(" ")[1])
print()


# 8. Határozza meg, hogy a megfigyelt időszakban a beolvasott azonosítójú személy összesen
# hány percet töltött a társalgóban! Az előző feladatban példaként szereplő 22-es személy
# 5 alkalommal járt bent, a megfigyelés végén még bent volt. Róla azt tudjuk, hogy 18 percet
# töltött bent a megfigyelés végéig.

print("8. feladat")


diff = 0
bePerc = 0
kiPerc = 0
vIVBVE = 0
for q in adatok:

    if q.split(" ")[2] == str(azonosito):
        if q.split(" ")[-1] == "be":
            vIVBVE += 1
            bePerc = int(q.split(" ")[0]) * 60 + int(q.split(" ")[1])

        if q.split(" ")[-1] == "ki":
            vIVBVE += 1
            kiPerc = int(q.split(" ")[0]) * 60 + int(q.split(" ")[1])
            diff += kiPerc - bePerc


if vIVBVE % 2 == 1:
    diff = 900-bePerc + diff
    print("A(z)", str(azonosito) + ". személy összesen", diff, "percet volt bent, a megfigyelés végén a társalgóban volt.")
else:
    print("A(z)", str(azonosito) + ". személy összesen", diff, "percet volt bent, a megfigyelés végén nem tartozkodott a társalgóban.")


