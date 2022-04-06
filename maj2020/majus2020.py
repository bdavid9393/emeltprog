

#BP 2330 08004 19



with open('tavirathu13.txt') as f:
    adatok = f.read().split("\n")[:-1]


#2 Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikor érkezett
# az utolsó mérési adat! A kiírásban az időpontot óó:pp formátumban jelenítse meg
# print("2. feladat")
# varosKod = input("Adja meg egy település kódját! Település:")
# varosKodTomb = []
# for x in adatok:
#     if x[:2] == varosKod:
#         varosKodTomb.append(x)
#
# szepenIrjukKi = varosKodTomb[-1]                                           #vagy varosKodTomb[len(varosKodTomb)-1]
# idoPerc = szepenIrjukKi[3:7]
#
# print("Az utolsó mérési adat a megadott településről", idoPerc[0:2] + ":" + idoPerc[2:4] + "-kor érkezett.")                # veszző = space

#3 Határozza meg, hogy a nap során mikor mérték a legalacsonyabb és a legmagasabb
# hőmérsékletet! Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és
# a hőmérsékletet! Amennyiben több legnagyobb vagy legkisebb érték van, akkor elég
# az egyiket kiírnia.
#SM 0015 01013 21

# legalacsonyabbHomersekletAdatSor = ""
# legalacsonyabbHomerseklet = 100
# for x in adatok:
#     if legalacsonyabbHomerseklet > int(x[-3:]):
#         legalacsonyabbHomersekletAdatSor = x
#         legalacsonyabbHomerseklet = int(x[-3:])
#
#
# legmagasabbHomersekletAdatsor = ""
# legmagasabbHomerseklet = 0
# for x in adatok:
#     if legmagasabbHomerseklet < int(x[-3:]):
#         legmagasabbHomersekletAdatsor = x
#         legmagasabbHomerseklet = int(x[-3:])
#
# print("3. feladat")
# print("A legalacsonyabb hőmérséklet:", legalacsonyabbHomersekletAdatSor[0:2], legalacsonyabbHomersekletAdatSor[3:5] + ":" + legalacsonyabbHomersekletAdatSor[5:7], legalacsonyabbHomersekletAdatSor[-2:], "fok.")
# print("A legmagasabb hőmérséklet:", legmagasabbHomersekletAdatsor[0:2], legmagasabbHomersekletAdatsor[3:5] + ":" + legmagasabbHomersekletAdatsor[5:7], legmagasabbHomersekletAdatsor[-2:], "fok.")

#4 Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején
# szélcsend volt! (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor
# a „Nem volt szélcsend a mérések idején.” szöveget írja ki! A kiírásnál a település kódját és
# az időpontot jelenítse meg.
#SM 0015 01013 21


# szelcsendTomb = []
# print("4. feladat:")
# for x in adatok:
#     if x[8:13] == "00000":
#         szelcsendTomb.append(x)
# if len(szelcsendTomb) == 0:
#     print("Nem volt szélcsend a mérések idején.")
# for y in szelcsendTomb:
#     print(y[0:3], y[3:5] + ":" + y[5:7])

#5 Határozza meg a települések napi középhőmérsékleti adatát és a hőmérséklet-ingadozását!
# A kiírásnál a település kódja szerepeljen a sor elején a minta szerint! A kiírásnál csak
# a megoldott feladatrészre vonatkozó szöveget és értékeket írja ki!

# a. A középhőmérséklet azon hőmérsékleti adatok átlaga, amikor a méréshez tartozó óra
# értéke 1., 7., 13., 19. Ha egy településen a felsorolt órák valamelyikén nem volt mérés,
# akkor a kiírásnál az „NA” szót jelenítse meg! Az adott órákhoz tartozó összes adat
# átlagaként határozza meg a középhőmérsékletet, azaz minden értéket azonos súllyal
# vegyen figyelembe! A középhőmérsékletet egészre kerekítve jelenítse meg!

# b. A hőmérséklet-ingadozás számításhoz az adott településen a napi legmagasabb és
# legalacsonyabb hőmérséklet különbségét kell kiszámítania! (Feltételezheti, hogy
# minden település esetén volt legalább két mérési adat.
#SM 0015 01013 21


# idoAdatSorBP = []

# for x in adatok:
#     if x[3:5] == "01" and x[0:2] == "BP":
#         idoAdatSorBP.append(x)
# for x in adatok:
#     if x[3:5] == "07" and x[0:2] == "BP":
#         idoAdatSorBP.append(x)
# for x in adatok:
#     if x[3:5] == "13" and x[0:2] == "BP":
#         idoAdatSorBP.append(x)
# for x in adatok:
#     if x[3:5] == "19" and x[0:2] == "BP":
#         idoAdatSorBP.append(x)
# kozepHom = 0
# for y in idoAdatSorBP:
#     if int(y[14:]) > 0:
#         kozepHom += int(y[14:])
# atlag = kozepHom / len(idoAdatSorBP)
#
# homIngadozas = 0
#
# for x in idoAdatSorBP:
#
# print(kozepHom)
# #print("{:.0f}".format(atlag))
# print(int(atlag))
# print("BP", "Középhőmérséklet:", int(atlag))

varosok = []


ido =["01", "07", "13", "19"]

for x in adatok:
    if x[0:2] not in varosok:
        varosok.append(x[0:2])

legKisHom = 999
legMaghom = 0


# if 1 and 2 and 4 and "asdf" and True and ["dfadsf"]:
#     print("ez mind igaz")
# if 0 or "" or []:
#     print("ezek hamisak")

for x in varosok:
    idoAdat = []
    mertOrak = []
    legKisHom = 999
    legMaghom = 0
    for y in adatok:
        if x == y[0:2]:
            if y[3:5] == "01" or y[3:5] == "07" or y[3:5] == "13" or y[3:5] == "19":
                idoAdat.append(y)
                if y[3:5] not in mertOrak:
                    mertOrak.append(y[3:5])
            if int(y[-2:]) < legKisHom:
                legKisHom = int(y[-2:])
            if int(y[-2:]) > legMaghom:
                legMaghom = int(y[-2:])
    hom = 0
    for z in idoAdat:
        if int(z[-2:]) > 0:
            hom += int(z[-2:])
    if len(mertOrak) == 4:
        print(x, "Középhömérséklet:", "{:.0f}".format(hom / len(idoAdat)), "Hőmérséklet-ingadozás:", legMaghom - legKisHom)
    else:
        print(x, "NA", "Hőmérséklet-ingadozás:", legMaghom - legKisHom)



# #6 Hozzon létre településenként egy szöveges állományt, amely első sorában a település kódját
# tartalmazza! A további sorokban a mérési időpontok és a hozzá tartozó szélerősségek
# jelenjenek meg! A szélerősséget a minta szerint a számértéknek megfelelő számú
# kettőskereszttel (#) adja meg! A fájlban az időpontokat és a szélerősséget megjelenítő
# kettőskereszteket szóközzel válassza el egymástól! A fájl neve X.txt legyen, ahol
# az X helyére a település kódja kerüljön!

file = open("sajat.txt", "w")
file.write("a macsak egy halatlan allat \n")
file.write("a macsak egy halatlan allat \n")
file.close()

#SM 0015 01013 21

for e in varosok:
    file = open(e + ".txt", "w")
    file.write(e + "\n")

    for k in adatok:
        if k[:2] == e:
            file.write(k[3:5] + ":" + k[5:7] + " " + int(k[11:13]) * "#" + "\n")
    file.close()

















