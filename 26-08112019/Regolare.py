from Partecipante import Partecipante


class Regolare(Partecipante):
    def __init__(self, codice, tipo, nome, cognome, ente, num_dip, accademico):
        super(Regolare, self).__init__(codice, tipo, nome, cognome)
        self._ente = ente
        self._num_dip = num_dip
        self._accademico = accademico

    def get_ente(self):
        return self._ente

    def __str__(self):
        return super().__str__() + "\t-\t-\t-" + self._ente + " " + str(self._num_dip) + " "  + str(self._accademico)
