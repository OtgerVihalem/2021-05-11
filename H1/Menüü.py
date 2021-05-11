from Toit import Toit

class Menüü:
    def __init__(self, pealkiri):
        self.menüüPealkiri = pealkiri
        self.menüüToidud = []

    def lisaToit(self, lisatudToit):
        self.toiduNimetus.append(lisatudToit)

    def kuvaToidudJaHinnad(self):
        kuvatudToitJaHind = self.toiduNimetus + " " + self.toiduHind
        return kuvatudToitJaHind

    def kuvaPäevaEri(self):
        if self.toiduPäevaEri = True:
            print(self.kuvaToidudJaHinnad())
        else:
            print("Ei ole eri pakkumine")

    def leiaKallimToit(self):
        if self.toiduHind > 5:
            return True
        else:
            return False

menüüTestimine = Menüü()

toiduTest1 = Toit("Ühepaja toit", 3.75, False)

toiduTest2 = Toit("Sealiha guljašš", 4.25, False)

toiduTest3 = Toit("Pasta bolognese", 3.00, False)



