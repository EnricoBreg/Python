from Voto import Voto

class Studente():
    def __init__(self, matricola, nominativo):
        self._matricola = matricola
        self._nominativo = nominativo
        self._libretto = []

    def get_nominativo(self):
        return self._nominativo

    def add_voto(self, codice_corso, nome_corso, valutazione):
        voto = Voto(codice_corso, nome_corso, valutazione)
        self._libretto.append(voto)

    def get_media(self):
        tot = 0
        for v in self._libretto:
            tot += v.get_voto()
        return tot / len(self._libretto)

    def get_libretto(self):
        return self._libretto

    def get_max(self):
        max = 0
        for v in self._libretto:
            if v.get_voto() > max:
                max = v.get_voto()
        return max

    def librString(self):
        res = "["
        for v in self._libretto:
            res = res + v.toString()
        res = res + "]"
        return res

    def __str__(self):
        libretto = self.librString()
        return self._nominativo + " " + str(self.get_media()) + " " + str(libretto)
