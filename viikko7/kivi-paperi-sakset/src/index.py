from peli_factory import luo_peli, vaihtoehdot


def main():
    ohje = "\n".join([f" ({avain}) {kuvaus}" for avain, kuvaus in vaihtoehdot().items()])

    while True:
        print(f"Valitse pelataanko:\n{ohje}\nMuilla valinnoilla lopetetaan")
        vastaus = input().strip()

        peli = luo_peli(vastaus)
        if peli:
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
