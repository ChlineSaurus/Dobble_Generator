from double_generator import kartenlistenersteller, uberpruefe, uberpruefe_2
import os, shutil


def anordner(lischte):
    #s'grööste Element us de Liste finde (göngt au eifacher)
    maximum = 1
    for x in lischte:
        maximum = max(maximum, max(x[1:]))
    #überprüefe öb all fotis existiered
    for x in range(1,maximum+1):
        path_from = f"/Users/marvin/Documents/Sonstiges/Spiele/TribbleTroubleDouble/Symbolordner/{x}.png"
        if not os.path.exists(path_from):
            raise Warning(f"S'Program chan leider nöd ablaufe, da mindestens eis Symbol fehlt: Symbol {x}")
    #überprüefe vo de Ordner (öb scho eine existiert)
    for x in lischte:
        path_to = f"/Users/marvin/Documents/Sonstiges/Spiele/TribbleTroubleDouble/Kartenordner/{x[0]}"
        if os.path.exists(path_to):
            raise Warning("En Ordner existiert bereits i de destination")

    for karte in lischte:
        path_to = f"/Users/marvin/Documents/Sonstiges/Spiele/TribbleTroubleDouble/Kartenordner/{karte[0]}"
        os.mkdir(path_to)
        for icon in karte[1:]:
            path_from = f"/Users/marvin/Documents/Sonstiges/Spiele/TribbleTroubleDouble/Symbolordner/{icon}.png"
            shutil.copy(path_from, path_to)


double_liste = kartenlistenersteller(13)
uberpruefe(double_liste)
uberpruefe_2(double_liste)
anordner(double_liste)