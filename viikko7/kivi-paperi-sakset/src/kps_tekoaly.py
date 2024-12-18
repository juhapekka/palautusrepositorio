from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _kysy_ekan_siirto(self):
        # pelaajan siirto
        return input("Sinun siirto: ")

    def _kysy_tokan_siirto(self):
        # tekoälyn siirto
        siirto = self.tekoaly.anna_siirto()
        print(f"Tekoäly valitsi: {siirto}")
        return siirto