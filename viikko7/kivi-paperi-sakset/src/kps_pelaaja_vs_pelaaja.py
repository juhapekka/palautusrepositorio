from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def _kysy_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _kysy_tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")
