from Partecipante import Partecipante


class Studente(Partecipante):
    def __init__(self, codice, tipo, nome, cognome, corso, uni, anno):
        super(Studente, self).__init__(codice, tipo, nome, cognome)
        self._corso = corso
        self._uni = uni
        self._anno = anno

    def get_uni(self):
        return self._uni

    def __str__(self):
        return super().__str__() + self._corso + '\t' + self._uni + ' ' + str(self._anno) + "\t-\t-\t-"
