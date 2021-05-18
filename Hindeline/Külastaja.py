from Raamat import Raamat

class Külastaja:
    def __init__(self, eesnimi, perekonnanimi):
        self.külastajaEesnimi = eesnimi
        self.külastajaPerekonnanimi = perekonnanimi
        self.külastajaLaenatudRaamatud = []

    def laenutaRaamat(self, lisatudRaamat):
        self.külastajaLaenatudRaamatud.append(lisatudRaamat)


    def tagastaRaamat(self, lisatudRaamat):
        self.külastajaLaenatudRaamatud.append(lisatudRaamat)
        self.külastajaLaenatudRaamatud.remove(lisatudRaamat)


    def kuvaLaenutatudRaamatud(self):


















