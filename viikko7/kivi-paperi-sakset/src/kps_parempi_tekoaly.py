from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _kysy_ekan_siirto(self):
        # pelaajan siirto
        return input("Sinun siirto: ")

    def _kysy_tokan_siirto(self):
        # tekoälyn siirto
        siirto = self.tekoaly.anna_siirto()
        print(f"Parannettu tekoäly valitsi: {siirto}")
        return siirto

    def kirjaa_siirrot(self, ekan_siirto, tokan_siirto):
        # tallennetaan pelaajan siirto
        self.tekoaly.aseta_siirto(ekan_siirto)