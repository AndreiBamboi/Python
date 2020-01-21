def arata_nth_radacina(radicand, n):
    radacina = n_radacina(radicand, n)
    mesaj = "The" + ordinal(n) + "roof of" + str(radicand) + "is" + str(radacina)
    print(mesaj)

arata_nth_radacina(64 ,4)