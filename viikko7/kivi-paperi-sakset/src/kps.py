from tuomari import Tuomari

class KPS:
    SIIRROT = {"k", "p", "s"}

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._kysy_ekan_siirto()
        tokan_siirto = self._kysy_tokan_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._kysy_ekan_siirto()
            tokan_siirto = self._kysy_tokan_siirto()

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in self.SIIRROT

    # Oletustoteutukset..
    def _kysy_ekan_siirto(self):
        raise NotImplementedError("_kysy_ekan_siirto puuttuu")

    def _kysy_tokan_siirto(self):
        raise NotImplementedError("_kysy_tokan_siirto puuttuu")