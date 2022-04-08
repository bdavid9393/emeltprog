

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
        adatSor.append(adat[0] + "*" + adat[1] + "*" + adat[2] + "*" + adat[3] + "*" + adat[4])
        adat = []

# print(adatSor)

# szamlalo = 0
# for x in adatSor:
#     if x.split("*")[0] != "NI":
#         szamlalo += 1
# print("2. feladat")
# print("A listában", szamlalo, "db vetítési dátummal rendelkező epizód van.")

# 3. Határozza meg, hogy a fájlban lévő epizódok hány százalékát látta már a listát rögzítő
# személy! A százalékértéket a minta szerint, két tizedesjeggyel jelenítse meg a képernyőn!
# 2017.07.16 Games 7x01 60 1
# szamlalo = 0
# #
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



# print("5.feladat")
# # datum = input("Adjon meg egy dátumot! Dátum= ")
# datum = "2017.10.18"
# for g in adatSor:
#     if g[-1] == "0":
#         if g.split("*")[0] <= datum:
#             print(g.split("*")[2] + "\t" + g.split("*")[1])


# 6. Készítse el az alábbi algoritmus alapján a hét napját meghatározó függvényt! A függvény
# neve Hetnapja legyen! A függvény az év, hónap és nap megadása után szöveges
# eredményként visszaadja, hogy az adott nap a hét melyik napja volt. (Az a és b egész
# számok maradékos osztása esetén az a div b kifejezés adja meg a hányadost,
# az a mod b pedig a maradékot, például 17 div 7 = 2 és 17 mod 7 = 3.)

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]


# 7. Kérjen be a felhasználótól egy napot az előző feladatban látható rövidített alakban!
# A napokat egy (h, k, p, v), kettő (cs), vagy három (sze, szo) karakterrel adja meg! Határozza
# meg, hogy a fájlban lévő sorozatok közül melyike(ke)t vetítik az adott napon! A sorozatok
# nevét a minta szerint jelenítse meg a képernyőn! Ha az adott napon egy sorozatot sem adtak
# adásba, akkor „Az adott napon nem kerül adásba sorozat.” üzenetet jelenítse meg!


# print("7. feladat")
# nap = input("Adja meg a hét egy napját (például cs)! Nap= ")
#
# sorozatNev = []
# for e in adatSor:
#     if e.split("*")[0] != "NI":
#         datum = e.split("*")[0]
#         if hetnapja(int(datum.split(".")[0]), int(datum.split(".")[1]), int(datum.split(".")[2])) == nap:
#             if e.split("*")[1] not in sorozatNev:
#                 sorozatNev.append(e.split("*")[1])
#
# if len(sorozatNev) == 0:
#     print("Az adott napon nem kerül adásba sorozat.")
#
# for p in sorozatNev:
#     print(p)

# 8. Határozza meg sorozatonként az epizódok összesített vetítési idejét és az epizódok számát!
# A számításnál vegye figyelembe a vetítési dátummal nem rendelkező epizódokat is!
# A megoldás során felhasználhatja, hogy egy sorozat epizódjainak adatai egymást követik
# a forrásállományban. A listát írja ki a summa.txt fájlba! A fájl egy sorában a sorozat címe,
# az adott sorozatra vonatkozó összesített vetítési idő percben és az epizódok száma
# szerepeljen szóközzel elválasztva!
#2017.07.16*Games*7x01*60*1

# sorozatok = []
# for p in adatSor:
#     if p.split("*")[1] not in sorozatok:
#         sorozatok.append(p.split("*")[1])
#
# file = open("summa.txt", "w")
#
# for r in sorozatok:
#     ido = 0
#     osszEp = 0
#     for t in adatSor:
#         if t.split("*")[1] == r:
#             ido += int(t.split("*")[3])
#             osszEp += 1
#     file.write(r + " " + str(ido) + " " + str(osszEp) + "\n")
# file.close()
# with open("summa.txt") as l:
#     jav = l.read()[:-1]
# file = open("summa.txt", "w")
# file.write(jav)
# file.close()



