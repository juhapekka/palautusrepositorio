KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")  # heitin vaan jotain :D

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        return numero in self.ljono
    
    def varmista_kapasiteetti(self):
        if self.alkioiden_lkm == len(self.ljono):
            uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
            uusi_ljono = self._luo_lista(uusi_koko)
            uusi_ljono[:self.alkioiden_lkm] = self.ljono[:self.alkioiden_lkm]
            self.ljono = uusi_ljono

    def lisaa(self, numero):
        if self.kuuluu(numero):
            return False

        self.varmista_kapasiteetti()

        self.ljono[self.alkioiden_lkm] = numero
        self.alkioiden_lkm += 1
        return True

    def poista(self, numero):
        try:
            self.ljono.remove(numero)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            return True
        except:
            return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        vastaus = IntJoukko()
        for numero in a.to_int_list():
            vastaus.lisaa(numero)

        for numero in b.to_int_list():
            vastaus.lisaa(numero)

        return vastaus

    @staticmethod
    def leikkaus(a, b):
        vastaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for numero in a_taulu:
            if numero in b_taulu:
                vastaus.lisaa(numero)

        return vastaus

    @staticmethod
    def erotus(a, b):
        vastaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for numero in a_taulu:
            if numero not in b_taulu:
                vastaus.lisaa(numero)

        return vastaus

    def __str__(self):
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
