from Kodutöö import Kodutöö

class Õpilane:
    def __init__(self, nimi, kursuseNimetus):
        self.õpilaseNimi = nimi
        self.õpilaseKursuseNimetus = kursuseNimetus
        self.õpilaseTegemataKodutööd = []
        self.õpilaseTehtudKodutööd = []

    def lisaKodutöö(self, lisatudKodutöö):
        self.õpilaseTegemataKodutööd.append(lisatudKodutöö)

    def tagastaTegemataKodutööd(self):
        #tagastatudTööd = uuritavKodutöö.õpilaseTegemataKodutööd , uuritavKodutöö.kodutööPealkiri
        for uuritavKodutöö in self.õpilaseTegemataKodutööd:
            print("Tegemata on: ", uuritavKodutöö.kodutööPealkiri)


    def märgiKodutööTehtud(self, lisatavKodutöö):
        self.õpilaseTegemataKodutööd.remove(lisatavKodutöö)
        self.õpilaseTehtudKodutööd.append(lisatavKodutöö)
        lisatavKodutöö.kodutööTehtud = True


    def tagastaTehtudKodutööd(self):
        #tagastatudTegemataTööd = uuritavKodutöö.õpilaseTehtudKodutööd , uuritavKodutöö.kodutööPealkiri
        #return  tagastatudTegemataTööd
        for uuritavKodutöö in self.õpilaseTehtudKodutööd:
            print("Tehtud on: ", uuritavKodutöö.kodutööPealkiri)


    def tagastaHindelisedKodutööd(self):
        #tagastatudHindelisedTööd = uuritavKodutöö.õpilaseTegemataKodutööd , uuritavKodutöö.kodutööHindeline
         #   if uuritavKodutöö.kodutööHindeline = 0:
          #      print(tagastatudHindelisedTööd.kodutööPealkiri)
        for uuritavKodutöö in self.õpilaseTegemataKodutööd:
            if uuritavKodutöö.kodutööHindeline == True:
                print("Hindeline kodutöö on: ", uuritavKodutöö.kodutööPealkiri)


õpilaseTestimine = Õpilane("Joosep Joosepson", "ABC21")

kodutööTest1 = Kodutöö("Esse mingil teemal", False)
kodutööTest2 = Kodutöö("Kirjand mingil teemal", True)

õpilaseTestimine.lisaKodutöö(kodutööTest1)
õpilaseTestimine.lisaKodutöö(kodutööTest2)

õpilaseTestimine.tagastaTegemataKodutööd()

õpilaseTestimine.tagastaHindelisedKodutööd()
õpilaseTestimine.märgiKodutööTehtud(kodutööTest2)
õpilaseTestimine.tagastaTehtudKodutööd()

