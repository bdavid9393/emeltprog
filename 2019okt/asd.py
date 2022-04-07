with open('utasadat.txt') as f:
    adatok = f.read().split("\n")[:-1]

# print("2. feladat")
# print("A buszra", len(adatok), "utas akart fellszálni")


print(adatok)
# import datetime
#
# nszalfel = 0
#
# for x in adatok:
#     if x[1] == " ":
#         if x[24:27] == "JGY":
#             if x[28:] == "0":
#                 nszalfel += 1
#         else:
#             # if x[2:10] > x[-8:]:
#             d1 = datetime.datetime(int(x[2:6]), int(x[6:8]), int(x[8:10]))
#             d2 = datetime.datetime(int(x[-8:-4]), int(x[-4:-2]), int(x[-2:]))
#             if d1 > d2:
#                 nszalfel += 1
#     if x[2] == " ":
#         if x[25:28] == "JGY":
#             if x[29] == "0":
#                 nszalfel += 1
#         else:
#             # if x[3:11] > x[-8:]:
#             d3 = datetime.datetime(int(x[3:7]), int(x[7:9]), int(x[9:11]))
#             d4 = datetime.datetime(int(x[-8:-4]), int(x[-4:-2]), int(x[-2:]))
#             if d3 > d4:
#                 nszalfel += 1
# print("3. feladat")
# print("A buszra", nszalfel, "utas nem szálhatottt fel.")


#4 Adja meg, hogy melyik megállóban próbált meg felszállni a legtöbb utas! (Több azonos
# érték esetén a legkisebb sorszámút adja meg!)

#
# megAllokSorszama = []
#
# for t in adatok:
#     if t[1] == " ":
#         if t[0] not in megAllokSorszama:
#             megAllokSorszama.append(t[0])
#     else:
#         if t[0:2] not in megAllokSorszama:
#             megAllokSorszama.append(t[0:2])
# # print(megAllokSorszama)
#
# tomb = []
#
# for z in megAllokSorszama:
#     szerep = 0
#     for u in adatok:
#         if u[1] == " ":
#             if z == u[0]:
#                 szerep += 1
#         else:
#             if z == u[0:2]:
#                 szerep += 1
#     tomb.append(z + "  " + str(szerep))
#
# legTobb = 0
# megallo = 0
# for p in tomb:
#     if int(p[-3:]) > legTobb:
#         legTobb = int(p[-3:])
#         megallo = int(p[:2])
# print("4. feladat")
# print("A legtöbb utas (" + str(legTobb), "fő) a", str(megallo) + ". megállóban próbált felszállni.")



#5 A közlekedési társaságnak kimutatást kell készítenie, hogy hányszor utaztak valamilyen
# kedvezménnyel a járművön. Határozza meg, hogy hány kedvezményes és hány ingyenes
# utazó szállt fel a buszra! (Csak az érvényes bérlettel rendelkező szállhatott fel a buszra!)
# 0 20190326-0700 9031038 JGY 3
# 0 20190326-0700 2810806 FEB 20190331
# 13 20190326-0717 4828987 NYB 20190404
# 13 20190326-0717 9123243 JGY 10

# ingyen = ["NYP", "RVS", "GYK"]
# kedv = ["TAB", "NYB"]
#
# ingyenOssz = 0
#
# for q in ingyen:
#     for k in adatok:
#         if k[1] == " ":
#             if q == k[24:27]:
#                 if k[2:10] <= k[-8:]:
#                     ingyenOssz += 1
#         if k[2] == " ":
#             if q == k[25:28]:
#                 if k[3:11] <= k[-8:]:
#                     ingyenOssz += 1
#
# kedvOssz = 0
#
# for a in kedv:
#     for k in adatok:
#         if k[1] == " ":
#             if a == k[24:27]:
#                 if k[2:10] <= k[-8:]:
#                     kedvOssz += 1
#         if k[2] == " ":
#             if a == k[25:28]:
#                 if k[3:11] <= k[-8:]:
#                     kedvOssz += 1
# print("5. feladat")
# print("Ingyenesen utazók száma:", ingyenOssz, "fő")
# print("A kedvezményesen utazók száma:", kedvOssz, "fő")


#6 Készítsen függvényt napokszama néven az alábbi algoritmus alapján. Az algoritmus
# a paraméterként megadott két dátumhoz (év, hónap, nap) megadja a közöttük eltelt napok
# számát! (A MOD a maradékos osztást, a DIV az egészrészes osztást jelöli.) Az algoritmust
# a fuggveny.txt fájlban is megtalálja. A függvényt a következő feladat megoldásához
# # felhasználhatja.

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2-d1


# def napokszama(e1, h1, n1, e2, h2, n2):
#     h1 = (h1+9) % 12
#     e1 = - e1 - h1 // 10
#     d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
#     h2 = (h2+9) % 12
#     e2 = e2 - h2 // 10
#     d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
#     return d2 -d1



#7 A közlekedési társaság azoknak az utasoknak, akiknek még érvényes, de 3 napon belül lejár
# a bérlete, figyelmeztetést szeretne küldeni e-mailben. (Például, ha a felszállás időpontja
# 2019. február 5., és a bérlet érvényessége 2019. február 8., akkor már kap az utas levelet,
# ha 2019. február 9. az érvényessége, akkor még nem kap levelet.) Válogassa ki és írja a
# figyelmeztetes.txt állományba ezen utasok kártyaazonosítóját és a bérlet
# érvényességi idejét (éééé-hh-nn formátumban) szóközzel elválasztva!

# 0 20190326-0700 9031038 JGY 3
# 0 20190326-0700 2810806 FEB 20190331
# 13 20190326-0717 4828987 NYB 20190404
# 13 20190326-0717 9123243 JGY 10

file = open("figyelmeztetes.txt", "w")

# for l in adatok:
#     if l.split(" ")[3] != "JGY":
#         if l[1] == " ":
#           print(napokszama(int(l[2:6]), int(l[6:8]), int(l[8:10]), int(l[-8:-4]), int(l[-4:-2]), int(l[-2:])))

for m in adatok:
    if m.split(" ")[3] != "JGY":
        if m[1] == " ":
            if napokszama(int(m[2:6]), int(m[6:8]), int(m[8:10]), int(m[-8:-4]), int(m[-4:-2]), int(m[-2:])) <= 3 and napokszama(int(m[2:6]), int(m[6:8]), int(m[8:10]), int(m[-8:-4]), int(m[-4:-2]), int(m[-2:])) >= 0:
                file.write(m.split(" ")[2] + " " + m[-8:-4] + "-" + m[-4:-2] + "-" + m[-2:] + "\n")
        if m[2] == " ":
            if napokszama(int(m[3:7]), int(m[7:9]), int(m[9:11]), int(m[-8:-4]), int(m[-4:-2]), int(m[-2:])) <= 3 and napokszama(int(m[3:7]), int(m[7:9]), int(m[9:11]), int(m[-8:-4]), int(m[-4:-2]), int(m[-2:])) >= 0:
                file.write(m.split(" ")[2] + " " + m[-8:-4] + "-" + m[-4:-2] + "-" + m[-2:] + "\n")

file.close()

# for m in adatok:
#     if m.split(" ")[3] != "JGY":
#         felszallasIdopontja = m.split(" ")[1]
#         ervenyessegDatum = m.split(" ")[4]
#         kulombsegNapokban = napokszama(int(felszallasIdopontja[0:4]),int(felszallasIdopontja[4:6]),int(felszallasIdopontja[6:8]), int(ervenyessegDatum[0:4]),int(ervenyessegDatum[4:6]),int(ervenyessegDatum[6:8]))
#
#         if kulombsegNapokban <= 3 and kulombsegNapokban >= 0:
#             print(m.split(" ")[2] + " " + m[-8:-4] + "-" + m[-4:-2] + "-" + m[-2:] + "\n") #ezt nem piszkáltam












