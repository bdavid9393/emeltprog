

with open("lista.txt") as f:
    adatok = f.read().split("\n")

# print(adatok)

# 2. Írassa ki a képernyőre, hogy hány olyan epizód adatait tartalmazza a fájl, amelynek ismert
# az adásba kerülési dátuma!

adat = []
adatSor = []
for t in adatok:
    adat.append(t)
    if len(adat) == 5:
        adatSor.append(adat[0] + " " + adat[1] + " " + adat[2] + " " + adat[3] + " " + adat[4])
        adat = []

# print(adatSor)

# szamlalo = 0
# for x in adatSor:
#     if x.split(" ")[0] != "NI":
#         szamlalo += 1
# print("2. feladat")
# print("A listában", szamlalo, "db vetítési dátummal rendelkező epizód van.")

# 3. Határozza meg, hogy a fájlban lévő epizódok hány százalékát látta már a listát rögzítő
# személy! A százalékértéket a minta szerint, két tizedesjeggyel jelenítse meg a képernyőn!
# 2017.07.16 Games 7x01 60 1
# szamlalo = 0
#
# for x in adatSor:
#     if x[-1] == "1":
#         szamlalo += 1
# szazalek = szamlalo / len(adatSor) * 100
# print("3. feladat")
# print("A listában lévő epizódok", "{:.2f}".format(szazalek) + "%-át látta.")


# 4. Számítsa ki, hogy összesen mennyi időt töltött a személy az epizódok megnézésével!
# Az eredményt a minta szerint nap, óra, perc formában adja meg!

# percOssz = 0
# for t in adatSor:
#     if t[-1] == "1":
#          percOssz += int(t[-4:-2])
#
# nap = int(percOssz / 60 // 24)
# ora = int(percOssz / 60 - nap * 24)
# perc = int(percOssz - nap * 24 * 60 - ora * 60)
# print("4. feladat")
# print("Sorozatnézéssel", nap, "napot", ora, "órát és", perc, "percet töltött.")


# 5. Kérjen be a felhasználótól egy dátumot „éééé.hh.nn” formában! Határozza meg, hogy
# az adott dátumig megjelent epizódokból melyeket nem látta még! Az aznapi epizódokat is
# számolja bele! A feltételnek megfelelő epizódok esetén írja a képernyőre tabulátorral
# elválasztva az évad- és az epizódszámot, valamint a sorozat címét a minta szerint!
# 2017.07.16 Games 7x01 60 1
# 2017.11.27 Spectacular Power 6x08 42 0

# print("5.feladat")
# datum = input("Adjon meg egy dátumot! Dátum= ")
# datum = "2017.10.18"
# for g in adatSor:
#     if g[-1] == "0":
#         if g.split(" ")[0] <= datum:
#             print(g[-9:-5] + "\t" + g.split(" ")[1])
# ez nincs kész






