import setuptools

with open("autok.txt") as f:
    adatok = f.read().split("\n")[:-1]

# print(adatok)


# 2. Adja meg, hogy melyik autót vitték el utoljára a parkolóból! Az eredményt a mintának
# megfelelően írja a képernyőre!
# '1 12:23 CEG307 514 26508 0'

print("2. feladat")
auto = ""
nap = 0
for r in adatok:
    if r.split(" ")[-1] == "0":
        auto = r.split(" ")[2]
        nap = r.split(" ")[0]
print(nap + ". nap rendszám:", auto)



# 3. Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat vitték ki és
# hozták vissza az adott napon!


print("3. feladat")
szam = input("Nap: ")
be = ""
print("Forgalom a(z)", szam + ". napon:")
for h in adatok:
    if h.split(" ")[0] == szam:
        if h.split(" ")[5] == "1":
            be = "be"
        else:
            be = "ki"
        print(h.split(" ")[1], h.split(" ")[2], h.split(" ")[3], be)

#4.Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban!


autok = []
for x in adatok:
    if x.split(" ")[2] not in autok:
        autok.append(x.split(" ")[2])

szamlalo = 0
for c in autok:
    kVB = 1
    for t in adatok:
        if t.split(" ")[2] == c:
            kVB = t.split(" ")[5]
    if kVB == "0":
        szamlalo += 1
print("4. feladat")
print("A hónap végén", szamlalo, "autót nem hoztak vissza.")


# 5 Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben a hónapban
# megtett távolságot kilométerben! A hónap végén még kint lévő autók esetén az utolsó
# rögzített kilométerállással számoljon! A kiírásban az autók sorrendje tetszőleges lehet

print("5. feladat")

for j in autok:
    minKm = 999999999999
    maxKm = 0
    for t in adatok:
        if t.split(" ")[2] == j:
            if int(t.split(" ")[4]) < minKm:
                minKm = int(t.split(" ")[4])
            if int(t.split(" ")[4]) > maxKm:
                maxKm = int(t.split(" ")[4])
    print(j, maxKm - minKm, "km")

#6 Határozza meg, melyik személy volt az, aki az autó egy elvitele alatt a leghosszabb
# távolságot tette meg! A személy azonosítóját és a megtett kilométert a minta szerint írja a
# képernyőre! (Több legnagyobb érték esetén bármelyiket kiírhatja.)

szemelyek = []

for o in adatok:
    if o.split(" ")[3] not in szemelyek:
        szemelyek.append(o.split(" ")[3])


illeto = 0
valtozas = 0
for a in szemelyek:
    induloKm = 0
    erkezoKm = 0
    for b in adatok:
        if b.split(" ")[3] == a:
            if b.split(" ")[-1] == "0":
                induloKm = int(b.split(" ")[-2])
            if b.split(" ")[-1] == "1":
                erkezoKm = int(b.split(" ")[-2])
                if erkezoKm - induloKm > valtozas:
                    valtozas = erkezoKm - induloKm
                    illeto = b.split(" ")[3]
print("6. feladat")
print("Leghosszabb út:", valtozas, "km, személy:", illeto)



#7 Az autók esetén egy havi menetlevelet kell készíteni! Kérjen be a felhasználótól egy
# rendszámot! Készítsen egy X_menetlevel.txt állományt, amelybe elkészíti az adott
# rendszámú autó menetlevelét! (Az X helyére az autó rendszáma kerüljön!) A fájlba
# soronként tabulátorral elválasztva a személy azonosítóját, a kivitel időpontját (nap.
# óra:perc), a kilométerszámláló állását, a visszahozatal időpontját (nap. óra:perc), és
# a kilométerszámláló állását írja a minta szerint! (A tabulátor karakter ASCII-kódja: 9.


print("7. feladat")

rendszam = input("Rendszám: ")
print("Menetlevél kész")
file = open(rendszam + "_menetlevél.txt", "w")

for p in adatok:
    azonosito = p.split(" ")[3]
    nap = p.split(" ")[0]
    ido = p.split(" ")[1]
    km = p.split(" ")[-2]
    if p.split(" ")[2] == rendszam:
        if p.split(" ")[-1] == "0":
            file.write(azonosito + "\t" + nap + ".\t" + ido + "\t" + km + "km"+ "\t")
        if p.split(" ")[-1] == "1":
            file.write(nap + ".\t" + ido + "\t" + km + "km" + "\n")

file.close()