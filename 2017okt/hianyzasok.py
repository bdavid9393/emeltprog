#1.
adatok = []
with open("naplo.txt") as f:
    for sor in f:
        sor = sor.strip().split(" ")
        if sor[0] == "#":
            honapSzam = sor[1]
            napSzam = sor [2]
        else:
            vezNev = sor[0]
            kerNev = sor[1]
            hiany = sor[2]
            adatok.append(honapSzam + " " + napSzam + " " + vezNev + " " + kerNev + " " + hiany)

#2.
print("2. feladat")
print("A naplóban", len(adatok), "bejegyzés van.")


#3.
igazolt = 0
igazolatlan = 0

for t in adatok:
    hianyzas = t.split(" ")[-1]
    for z in range(0, len(hianyzas)):
        if hianyzas[z] == "X":
            igazolt += 1
        if hianyzas[z] == "I":
            igazolatlan += 1
print("3. feladat")
print("Az igazolt hiányzások száma ", igazolt, ", az igazolatlanoké ", igazolatlan, " óra.", sep="" )


#4.

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap -1] + nap) % 7
    return napnev[napsorszam]

#5.
print("5. feladat")
honapSzam = int(input("A hónap sorszáma="))
napSzam = int(input("A nap sorszáma="))
print("Azon a napon", hetnapja(honapSzam, napSzam), "volt.")


#6.

print("6. feladat")
napNev = input("A nap neve=")
oraSorSzam = int(input("Az óra sorszáma="))


szamlalo = 0
for p in adatok:
    orak = p.split(" ")[-1]
    honap = int(p.split(" ")[0])
    nap = int(p.split(" ")[1])
    if hetnapja(honap, nap) == napNev:
        if orak[oraSorSzam - 1] == "X":
            szamlalo += 1
        if orak[oraSorSzam - 1] == "I":
            szamlalo += 1

print("Ekkor összesen", szamlalo, "óra hiányzás történt")

#7.

tanulok = []
for p in adatok:
    if p.split(" ")[2] + " " + p.split(" ")[3] not in tanulok:
        tanulok.append(p.split(" ")[2] + " " + p.split(" ")[3])

tanulokHianyzasa = []
for k in tanulok:
    szamolo = 0
    for r in adatok:
        hiany = r.split(" ")[-1]
        if k == r.split(" ")[2] + " " + r.split(" ")[3]:
            for t in range(0, len(hiany)):
                if hiany[t] == "X":
                    szamolo += 1
                if hiany[t] == "I":
                    szamolo += 1
    tanulokHianyzasa.append(str(szamolo) + " " + k)

hianyzasokSzama = []
for p in tanulokHianyzasa:
    if int(p.split(" ")[0]) not in hianyzasokSzama:
        hianyzasokSzama.append(int(p.split(" ")[0]))
hianyzasokSzama.sort(reverse=True)

print("7. feladat")
print("A legtöbbet hiányzó tanulók: ", end="")
for v in tanulokHianyzasa:
    if str(hianyzasokSzama[0]) == v.split(" ")[0]:
        print(v.split(" ")[-2], " ", v.split(" ")[-1], " ", sep = "", end="")


# 01 15 Galagonya Alfonz OXXXXXX




