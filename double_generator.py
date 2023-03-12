#import random
#import os
#insert a prime number, the prime number + 1 is the amount of icons you get
def kartenlistenersteller(icons):
    zeilenzuweisung = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-.+*ç%&/"
    kartennummer = 1
    kartenliste = []

    #generating the cards

    for steigung in range(icons):

        for starting_point in range(1,icons+1):
            karte = ["karte" + str(kartennummer)]
            laufvariable = starting_point

            for y in zeilenzuweisung[:icons]:
                if laufvariable > icons:
                    laufvariable -= icons
                karte.append(y+str(laufvariable))
                laufvariable += steigung
            karte.append(zeilenzuweisung[icons]+str(steigung+1))
            kartenliste.append(karte)
            #wegnehmen um die einzelnen karten zu printen, bis da sollte alles funktionieren
            #print(karte)
            kartennummer+=1

    #print(kartenliste)
    zahlenlist = []
    for count, x in enumerate(kartenliste):
        zahlenlist = [x[0]]
        for y in range(len(x)-1):
            zahlenlist.append((y) * icons + int(x[y+1][1:]))
        kartenliste[count] = zahlenlist
        #print(zahlenlist)

    for x in range(icons):
        zusatzkarte = ["weitere_Karte"+ str(x + 1)]
        for y in range(1,icons+1):
            zusatzkarte.append(x*icons+y)
        zusatzkarte.append(icons ** 2 + icons +1)
        kartenliste.append(zusatzkarte)
        #print(zusatzkarte)

    # theoretisch auch noch mögliche Karte
    fancyzuesatzkarte = ["zfancyzuesatzkarte"]
    for x in range(1+ icons):
        fancyzuesatzkarte.append(icons ** 2 + x + 1)
    #print(fancyzuesatzkarte)

    kartenliste.append(fancyzuesatzkarte)
    return kartenliste

#testen
def uberpruefe(liste):

    for index_x, x in enumerate(liste):
        for y in liste[index_x + 1:]:
            counter = 0
            for z in x:
                for i in y:
                    if i == z:
                        counter += 1
            if counter != 1:
                print("erste Karte die den Fehler hervorruft: "+ str(x))
                print("zweite Karte die den Fehler hervorruft: "+ str(y))
                print(f"Es gibt {counter} Icons auf diesen Karten doppelt")
                raise Warning("Es klappt nöd... Buhuhuhu")

def uberpruefe_2(liste):
    for index_karte_1, karte_1 in enumerate(liste):
        for karte_2 in liste[index_karte_1+1:]:
            matching_number = set(karte_1) & set(karte_2)
            if len(matching_number) != 1:
                print("erste Karte die den Fehler hervorruft: " + str(karte_1))
                print("zweite Karte die den Fehler hervorruft: " + str(karte_2))
                print(f"Es gibt {len(matching_number)} Icons auf diesen Karten doppelt")
                raise Warning("Die zweiti Überprüefig het fehlgschlage")



if __name__ == "__main__":
    grossi = 31 #muess e Primzahl si
    liste = kartenlistenersteller(grossi)
    #uberpruefe(liste)
    #uberpruefe_2(liste)
    print(len(liste))
    for x in liste:
        print(x)


