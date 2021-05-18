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
        for uuritavRaamat in self.külastajaLaenatudRaamatud:
            if uuritavRaamat.raamatuTiitel == True:
                print("Laenatud raamatu tiitel: ", uuritavRaamat.raamatuTiitel)



külaliseTestimine = Külastaja("Joosep", "Joosepson")

raamatuTest1 = Raamat("Mingi vahva tiitel", "Keegi kaval autor", 305)
raamatuTest2 = Raamat("Parimad koka road", "Kuulus Ekspert", 275)

külaliseTestimine.laenutaRaamat(raamatuTest1)
külaliseTestimine.laenutaRaamat(raamatuTest2)

külaliseTestimine.kuvaLaenutatudRaamatud()














