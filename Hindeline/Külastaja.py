from Raamat import Raamat

class Külastaja:
    def __init__(self, eesnimi, perekonnanimi):
        self.külastajaEesnimi = eesnimi
        self.külastajaPerekonnanimi = perekonnanimi
        self.külastajaLaenatudRaamatud = []


    def laenutaRaamat(self, lisatudRaamat):
        if not lisatudRaamat.laenutatud:
            lisatudRaamat.laenutatud = True
            self.külastajaLaenatudRaamatud.append(lisatudRaamat)
        else:
            print("Raamatut ei saa laenutada, see on juba välja laenatud!", lisatudRaamat.raamatuTiitel)


    def tagastaRaamat(self, lisatudRaamat):
        self.külastajaLaenatudRaamatud.remove(lisatudRaamat)


    def kuvaLaenutatudRaamatud(self):
        for uuritavRaamat in self.külastajaLaenatudRaamatud:
            print("Laenatud raamatu tiitel: ", uuritavRaamat.raamatuTiitel)



külaliseTestimine = Külastaja("Joosep", "Joosepson")

raamatuTest1 = Raamat("Mingi vahva tiitel", "Keegi kaval autor", 305)
raamatuTest2 = Raamat("Parimad koka road", "Kuulus Ekspert", 275)

külaliseTestimine.laenutaRaamat(raamatuTest1)
külaliseTestimine.laenutaRaamat(raamatuTest2)
külaliseTestimine.tagastaRaamat(raamatuTest1)
#print(külaliseTestimine.külastajaLaenatudRaamatud)
külaliseTestimine.laenutaRaamat(raamatuTest2)
#print(külaliseTestimine.külastajaLaenatudRaamatud)

külaliseTestimine.kuvaLaenutatudRaamatud()


