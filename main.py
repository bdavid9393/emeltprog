# 2.  Írj programot, beolvassa a felhasználó nevét, majd köszön neki!
# print("Szia! mi a neved?")
# nev = input()
# print("Szerbusz " + nev)


# 3. Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét
# print("Szia adj meg egy számot")
# szam = input()
# szamKetszerese = int(szam) * 2
# print(szamKetszerese)

# 4. Írj programot, ami beolvas két számot, majd kiírja:
# a. az összegüket;
# b. különbségüket;
# c. szorzatukat;
# d. hányadosukat, ha lehet!l
# print("Szia adj meg egy számot")
# szam1 = input()
# print("kérek még egy számot")
# szam2 = input()
# print("az összegük")
# print(int(szam1) + int(szam2))
# print("kül")
# print(int(szam1) - int(szam2))
# print("a hányadosuk")
# if szam2 == "0":
#     print("Nullával nem lehet osztani")
# else:
#     print(int(szam1) / int(szam2))

#5 írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!
# print("kérem az első egész számot")
# szam1 = int(input())
# print("kérem a második egész számot")
# szam2 = int(input())
# if szam1 == szam2:
#     print("egyenlő a két szám")
# if szam1 < szam2:
#     print("a nagyobb szám:")
#     print(szam2)
# if szam1 > szam2:
#     print("a nagyobb szám")
#     print(szam1)

#abc rend, egész számok, float= nem egész számok pl.:1.1

#6. Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!
# print("kérem az első számot")
# szam1 = int(input())
# print("kérem a második számot")
# szam2 = int(input())
# print("kérem a harmadik számot")
# szam3 = int(input())
# if szam1 < szam2:
#     if szam1 < szam3:
#         print("a legkisebb szám:")
#         print(szam1)
# if szam2 < szam1:
#     if szam2 < szam3:
#         print("a legkisebb szám:")
#         print(szam2)
# if szam3 < szam2:
#     if szam3 < szam1:
#         print("a legkisebb szám:")
#         print(szam3)
# if szam1 == szam2:
#    if szam1 == szam3:
#        print("egyenlők")
#
# print("kérem az első számot")
# szam1 = int(input())
# print("kérem a második számot")
# szam2 = int(input())
# print("kérem a harmadik számot")
# szam3 = int(input())
#
# if szam1 < szam2 and szam1 < szam3:
#     print("A legkisebb ")
#     print(szam1)
# if szam2 < szam1 and szam2 < szam3:
#     print("A legkisebb ")
#     print(szam2)
# if szam3 < szam2 and szam3 < szam1:
#     print("A legkisebb ")
#     print(szam3)
# if szam3 == szam2 and szam3 == szam1:
#     print("Egyenlőek")

#és kapu vagy and
# aKonyhabaEgAVillany = True
# aFurdobeEgAVillany = False
#
# if not(aKonyhabaEgAVillany or  aFurdobeEgAVillany):
#     print("A feleség mérges mert miért a villany két helyen milkor nem vagyunk ott!")
# else:
#     print("nem biztos hogy mérges")


#7 Írj programot, ami beolvassa a háromszög oldalainak hosszát, és megmondja, hogy ilyen oldalakkal szerkeszthető-e háromszög

# print("kérem a egyik oldal hossza")
# szam1 = int(input())
# print("kérem a második oldal hosszát")
# szam2 = int(input())
# print("kérem a harmadik oldal hosszát ")
# szam3 = int(input())
# if szam1 < szam2 + szam3 and szam2 < szam1 + szam3 and szam3 < szam1 + szam2:
#     print("megszerkeszthető")
# else:print ("nem szerk")

#8 Írj programot, mely beolvas két pozitív egész számot, és kiírja a számtani és mértani közepüket! A gyökvonáshoz használd a Math.Sqrt() függvényt!
# import math
#
# print("irj egy pozitiv egész számot be te p..")
# szam1 = int(input())
# print("irj egy pozitiv egész számot be te p..")
# szam2 = int(input())
# print("számtani közepuk" + str((szam1 + szam2) / 2))
# print("mértani közepuk" + str(math.sqrt(szam1 * szam2)))

#9írj programot, mely beolvassa a másodfokú egyenlet együtthatóit, és kiírja, hogy az egyenletnek van-e megoldása






#11 Írj programot, mely beolvassa egy derékszögű háromszög két befogóját, és megadja az átfogójának a hosszát! Az átfogót 2 tizedesjeggyel add meg!
# import math
# print("derékszögű hsz egyik befogoja")
# szam1 = int(input())
# print("derékszögű hsz másik befogoja")
# szam2 = int(input())
# print("átfogó hossza:")
# szam3 = (math.sqrt((szam1 * szam1) + (szam2 * szam2)))
# print("{:.2f}".format(szam3))



#12 Írj programot, mely beolvassa a téglatest három élének hosszát, és kiírja a felszínének és térfogatának mérőszámát!
# print("téglatestalap éle")
# szam1 = int(input())
# print("téglatesalap másik éle")
# szam2 = int(input())
# print("téglatest magassága")
# szam3 = int(input())
# print("térfogata:")
# print(szam1 * szam2 * szam3)
# print("felszíne:")
# print((szam1 * szam2) * 2 + (szam1 * szam3 * 2) + (szam2 * szam3 * 2))

#13 Írj programot, mely beolvassa egy kör átmérőjét, és kiírja a kör kerületét és területét! A pi értékének meghatározásához használd a Math.PI értéket!
# import math
# print("kör átmérője")
# szam1 = int(input())
# print("kör kerülete:")
# print(szam1 * math.pi)
# print("kör területe:")
# print(math.pi * (szam1 * szam1) / 4)





# 15.Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a
# képernyőre eddig a számig, egymástól szóközzel elválasztva!

# print("irgyá egy pozitiv egész számot")
# szam1 = int(input())
# szokozesKiiras = ""
# for x in range(1, szam1 + 1, 1): #[1,2,3,4,5,6,7]
#    szokozesKiiras = szokozesKiiras + str(x) + " "
#    print(szokozesKiiras)
# print("Eredmény: " + szokozesKiiras)

#17.Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit!
# print("irgyá egy pozitiv egész számot")
# szam1 = int(input())
# for x in range(1, szam1 +1):
#    if szam1 % x == 0:
#        print(x)

#18 Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az összegét!

# print("irgyá egy pozitiv egész számot")
# szam1 = int(input())
# db = 0
# osszeg= 0
# for x in range(1, szam1 +1):
#    if szam1 % x == 0:
#        db += 1
#        osszeg += x
#        print(x)
# print("ennyi darab:", db)
# print("összegük", osszeg)


#19 Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy
#tökéletes szám-e! (A tökéletes számok azok, melyek osztóinak összege egyenlő a
#szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)

# szam = int(input("kérem as számot:"))
# osztokÖsszege = 0
# for x in range(1, szam + 1):
#     if szam % x == 0:
#         osztokÖsszege += x
# if osztokÖsszege == szam * 2:
#     print("tökéletes szám")
# else:
#     print("nem tökéletes szám")


#20 Írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a
# hatványértéket!

# hartványAlap = int(input("hatványalap:"))
# hatványKitevő = int(input("hatványkitevő:"))
# hatványErtek = hartványAlap
# for x in range(1, hatványKitevő):
#     if x > 0:
#         hatványErtek *= hartványAlap
#
# print(hatványErtek)

#21 Írj programot, ami csak pozitív számot hajlandó beolvasni.

# print("pozitív szám:")
# szam = int(input())
# while szam < 1:
#     print("ez nem poztiv szám, kérlek adj meg egy pozitiv számot:")
#     szam = int(input())

#print("köszönöm")

#22 Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok
# kisebbek, mint tíz. Írja ki ezek után a beolvasott számok összegét!


# print("számok:")
# szamok = int(input())
# szamokÖsszege = szamok
# while szamok < 10:
#     szamok = int(input())
#     szamokÖsszege += szamok
# print(szamokÖsszege, "összegük")


#23 Írj programot, amely beolvas egy egész számot, majd elosztja 2-vel annyiszor,
# ahányszor lehet és közben felírja a számot a kettes számok szorzataként
# megszorozva egy olyan számmal, amely már nem osztható 2-vel.
# Kérek egy egész számot: 120
# 120 = 2*2*2*15

# szam = int(input("Kérek egy egész számot:"))
# eredetiSzam = szam
# tomb = []
# if szam % 2 == 0:
#
#     while szam % 2 == 0:
#         szam /= 2
#         tomb.append(2)
#     else:
#         tomb.append(int(szam))
#
#
# else:
#     print(eredetiSzam, "=", szam)
#
# eredmenySzepen = str(tomb[0])
# for szamATomben in tomb[1:]:
#     eredmenySzepen += " * " + str(szamATomben)
# print(int(eredetiSzam), "=", eredmenySzepen)

#Tomb müveletek/lehetőségek
# numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
#
# print(numbers_list)
# print(numbers_list[3])
# print(numbers_list[2:5])
# print(numbers_list[:-5])
# print(numbers_list[5:])
# print(numbers_list[:])

# szovegelek = "A macska egeret fog"
# print(szovegelek)
# print(szovegelek[5:])
# print(szovegelek[:-4])
# print(szovegelek[-4:])
# print(szovegelek[2:4])

#valatozo = ""
# valatozo = "4"
# valatozo = []
# valatozo = ["macska", "egér", "kutya"]
#
# print(valatozo[:])


#split (vágás)

# szoveg = "Dávid 28 200 100"
# darabolas = szoveg.split(" ")
# print(szoveg)
# print(darabolas)
# print(darabolas[3])

# lista = [1,2]
# lista.append(3)
# print(lista)
# lista2 = lista[:]
# print(lista2)
# lista.append(4)
#
# print(lista)
# print(lista2)
#
# szoveg1 = "Kecske"
# szoveg2 = szoveg1
# szoveg1 = "sjatos csiga"
# print(szoveg1)
# print(szoveg2)



#24 Írj programot, ami csak az "alma" szót hajlandó beolvasni, ha ez sikerült, akkor
# kiírja, hogy az "Az alma gyümölcs!"

# szam = input("ird be, hogy alma:")
#
# while szam != "alma":
#     szam = input()
# else:
#     print("Az alma gyümölcs")


#25



#26 Írj programot, mely eldönti egy számról, hogy prímszám-e.

# szam = int(input("kérek egy számot:"))
#
# for x in range(1, szam +1 ):
#     szam % x == 0












#42. Olvass be pár számot (a darabszámot is kérje be a program), majd írd ki a páratlanok darabszámát.

# print("kérem a db számot:")
# dbSzam = int(input())
# print("kérem a számokat")
# szamok = []
# for x in range(0, dbSzam):
#     bevittSzam = int(input())
#     szamok.append(bevittSzam)
#
# paratlanSzamok = 0
# for szam in szamok:
#     if szam % 2 == 1:
#         paratlanSzamok +=1
#
# print("A páratlan számok száma: ", (paratlanSzamok))

# 44. Olvass be egy pár számot (a darabszámot is kérje be a program), majd írd ki a
# párosokat a képernyőre, a sorszámukkal együtt, vagyis hogy hányadiknak olvastad
# be őket.

# print("kérem a db számot:")
# dbSzam = int(input())
# print("kérem a számokat")
# szamok = []
# for x in range(0, dbSzam):
#      bevittSzam = int(input())
#      szamok.append(bevittSzam)
# parosSzamok = 0
# for szam in szamok:
#     if szam % 2 == 0:
#         print(szam, "sorszáma:", (szamok.index(szam) + 1))    #szoveg.index("egy")

# 46. Olvassunk be egész számokat egy tömbbe (a darabszámot is kérje be a program),
# majd kérjünk be egy egész számot, és mondjuk meg, hogy hányszor szerepel a
# tömbben.

# print("kérem a db számot:")
# dbSzam = int(input())
# print("kérem a számokat")
# szamok = []
# for x in range(0, dbSzam):
#     bevittSzam = int(input())
#     szamok.append(bevittSzam)
#
# print("kérek egy számot:")
# keresettSzam = int(input())
# darab = 0
# for x in szamok:
#     if x == keresettSzam:
#         darab += 1
# print("ennyiszer szerepel:", darab, "db")


# 48. Olvassunk be egész számokat egy tömbbe (a darabszámot is kérje be a program),
# majd adjuk meg a legkisebb és a legnagyobb szám különbségét!

# print("kérem a db számot:")
# dbSzam = int(input())
# print("kérem a számokat")
# szamok = []
# for x in range(0, dbSzam):
#     bevittSzam = int(input())
#     szamok.append(bevittSzam)
#                                                # [5, 6, 7, 8]
# legkisebbSzam = 9999
#
# for szam in szamok:
#     if szam < legkisebbSzam:
#         legkisebbSzam = szam
#
# print("legkisebb szam:", legkisebbSzam)
#
#
# legnagyobbSzam = 0
#
# for szam in szamok:
#     if szam > legnagyobbSzam:
#         legnagyobbSzam = szam
#
# print("legnagyobbSzam szam:", legnagyobbSzam)
# print("különbségük:", legnagyobbSzam - legkisebbSzam)


#Tömb index példa
# nevSor = ["David", "Virág", "Adri", "Gyurka", "David"]
# davidIndexe = nevSor.index("David")
# print("Dávid sorszáma a tömbe:", davidIndexe)
# viragIndexe = nevSor.index("Virág")
# print("Virág sorszáma a tömbe:", viragIndexe)
# gyulaIndexe = nevSor.index("Gyula")
# print("Gyula sorszáma a tömbe:", gyulaIndexe)
# szamok = [1,2,3,4,5]
#
# szöveg = "sajtos csiga"
# szövegTömb  = ["s", "a","j","t","o","s", " " , "c"]

# szoveg= "Ez egy mondat!"
# indexEgy = szoveg.index("egy")
# print(indexEgy)
# print(szoveg[5])
# print(szoveg[10:12])

#dávid feladata: menj végig a névsoron és írd ki hogy fiu vagy lány e az illető, David és Gyurka fiu, Virág és Adri pedig lány
# nevSor = ["David", "Virág", "Adri", "Gyurka"]
# for nev in nevSor:
#     if nev == "David" or nev == "Gyurka":
#         print(nev + " egy fiu")
#     else:
#         print(nev + " egy lány")
#
# szamSor = []
# szamSor.append(int(input()))
# szamSor.append(int(input()))
# szamSor.append(int(input()))
# for szam in szamSor:
#     if szam % 2 == 0:
#         print(str(szam) + " páros szám")
#     else:
#         print(str(szam) + " páratlan szám")






#While ciklus példa
# szamLista = [5, 6, 7, 8, 9]
# szovegLista = ["David","David2" ,"David3" ,"David4"]
#
# fussonE = "igen"
#
# while fussonE == "igen":
#     print("Adjal meg egy nevet: ")
#     nev = input()
#     szovegLista.append(nev)
#     print("Fussunk?")
#     fussonE = input()
#
#
# # print(szamLista)
# print(szovegLista)
# # print(szovegLista[0])
# print(len(szovegLista))


#Átlag számítás

# szamLista = [1, 2, 3, 4, 5]
#
# osszeg = 0
# for szam in szamLista:
#     print("A szám:")
#     print(szam)
#     osszeg = osszeg + szam
#     print("Az osszeg:")
#     print(osszeg)
#
# print("Az átlag:")
# print(osszeg / len(szamLista))
#
#
# for x in range(2, 6):
#   print(x)






#2.6Írjunk programot, amely kiszámítja és kiírja a téglalap területét és kerületét!
# print("kérem a rövidebb oldal hosszát")
# szam1 = int(input())
# print("kérem a hosszabb oldal hosszát")
# szam2 = int(input())
# if szam1 == szam2:
#         print("ez négyzet te paraszt")
# else:
#     print("kerülete:")
#     print((szam1 + szam2) * 2)
#     print("területe.")
#     print(szam1 * szam2)


#Hogyan számítható ki a kör területe, kerülete az  átmérőjéből vagy a sugarából?

# print("kör átmérője")
# szam1 = int(input())
# print("a kör területe")
# print((szam1 / 2) * (szam1 / 2) * 3.14)
# print("a kör kerülete")
# print((2 * (szam1 / 2) * 3.14))

# import math
# def udvozolj(nev, kor, nem):
#     print("Szia", nev)
#     print("a te korod", kor, "nemed:",nem)
#
# def addOssze(szam1,szam2):
#     print("Az egyik szám:", szam1)
#     print("Az egyik szám:", szam2)
#     print("Összeadom")
#     print(szam1 + szam2)
#     osszegeAKetSzamnak = szam1 + szam2
#     return osszegeAKetSzamnak


# udvozolj("David", 15, "fiu")
# udvozolj("Gyurka", 15, "fiu")
# udvozolj("Virág", 15, "lány")

# osszeg = addOssze(5,4)
# negyzet = math.cos(5)
# print(negyzet)
# print(osszeg)

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1//400 + (h1*306 + 5) // 10 + n1 -1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 -1
    return d2 - d1

print("napok", napokszama(1990,5,12,2023,3,31))

# print(7/4)
# print(7//4)
# print(int(7/4))
# print(round(7/4,1))

# (A MOD a maradékos osztást, a DIV az egészrészes osztást jelöli.)
# Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész,
# h2: egész, n2: egész): egész
# h1 = (h1 + 9) MOD 12
# e1 = e1 - h1 DIV 10
# d1 = 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 +
# (h1*306 + 5) DIV 10 + n1 - 1
# h2 = (h2 + 9) MOD 12
# e2 = e2 - h2 DIV 10
# d2 = 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 +
# (h2*306 + 5) DIV 10 + n2 - 1
# napokszama:= d2-d1
# Függvény vége



# Készítse el az alábbi algoritmus alapján a hét napját meghatározó függvényt! A függvény
# neve Hetnapja legyen! A függvény az év, hónap és nap megadása után szöveges
# eredményként visszaadja, hogy az adott nap a hét melyik napja volt. (Az a és b egész
# számok maradékos osztása esetén az a div b kifejezés adja meg a hányadost,
# az a mod b pedig a maradékot, például 17 div 7 = 2 és 17 mod 7 = 3.)

# Függvény hetnapja(ev, ho, nap : Egész) : Szöveg
# napok: Tömb(0..6: Szöveg)= (′′v′′, ′′h′′, ′′k′′, ′′sze′′,
# ′′cs′′, ′′p′′, ′′szo′′)
# honapok: Tömb(0..11: Egész)= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
# Ha ho < 3 akkor ev := ev -1
# hetnapja := napok[(ev + ev div 4 – ev div 100 +
# ev div 400 + honapok[ho-1] + nap) mod 7]
# Függvény vége

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1

    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]



print(hetnapja(2022,11,31))


# Készítsen függvényt hetnapja néven, amely a paraméterként megadott dátumhoz (hónap,
# nap) megadja, hogy az a hét melyik napjára esik (hétfő, kedd...). Tudjuk, hogy az adott év
# nem volt szökőév, továbbá azt is, hogy január elseje hétfőre esett. Használhatja az alábbi
# algoritmust is, ahol a tömbök indexelése 0-val kezdődik, de ettől eltérő megoldású
# függvényt is készíthet.
# Függvény hetnapja(honap:egesz, nap:egesz): szöveg
# napnev[]:= ("vasarnap", "hetfo", "kedd", "szerda", "csutortok",
# "pentek", "szombat")
# napszam[]:= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
# napsorszam:= (napszam[honap-1]+nap) MOD 7
# hetnapja:= napnev[napsorszam]
# Függvény vége

def hetnapja2(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1] + nap) % 7
    return napnev[napsorszam]


print(hetnapja2(2,10))

























