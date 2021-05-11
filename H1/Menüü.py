from Toit import Toit

class Menüü:
    def __init__(self, pealkiri):
        self.menüüPealkiri = pealkiri
        self.menüüToidud = []

    def lisaToit(self, lisatudToit):
        self.menüüToidud.append(lisatudToit)

    def kuvaToidudJaHinnad(self, uuritavToit):
        kuvatudToitJaHind = uuritavToit.toiduNimetus , uuritavToit.toiduHind
        return kuvatudToitJaHind

    def kuvaPäevaEri(self):
        for toit in self.menüüToidud:
            if toit.toiduPäevaEri == True:
                print(self.kuvaToidudJaHinnad(toit))
            else:
                print(self.kuvaToidudJaHinnad(toit), "Ei ole eri pakkumine")

    def leiaKallimToit(self):
        maxHind = 0
        for toit in self.menüüToidud:
            if toit.toiduHind > maxHind:
                maxHind = toit.toiduHind
                kallimToit = toit

        print(kallimToit.toiduNimetus, kallimToit.toiduHind)

menüüTestimine = Menüü("Lõuna Menüü")

toiduTest1 = Toit("Ühepaja toit", 3.75, False)

toiduTest2 = Toit("Sealiha guljašš", 4.25, False)

toiduTest3 = Toit("Pasta bolognese", 3.00, True)


menüüTestimine.lisaToit(toiduTest1)
menüüTestimine.lisaToit(toiduTest2)
menüüTestimine.lisaToit(toiduTest3)
menüüTestimine.kuvaPäevaEri()
menüüTestimine.leiaKallimToit()

