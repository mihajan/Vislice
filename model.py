import random
# to datoteko ustvarjam po navodilih iz spletne učilnice

# najprej nastavimo konstante

#konstante za rezultate ugibanj
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

#konstante za zmago in poraz
ZMAGA = 'w'
PORAZ = 'x'

bazen_besed = []
with open('besede.txt', encoding='UTF-8') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())


class Igra:
    '''V tem razredu bomo definirali več metod koristih za izdelavo igre.'''
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()   #beseda, ki jo igralec poskuša uganiti
        if crke is None:
            self.crke = []
        else:   
            self.crke = crke.lower()    #dosedanji poskusi igralca 


    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True
        
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def pravilni_del_gesla(self):
        trenutno = ""
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += "_"
        return trenutno


    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        
        self.crke.append(ugibana_crka)
        
        if ugibana_crka in self.geslo:
            #uganil je
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        

def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)

        
    



        