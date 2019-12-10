from Ristorante import Ristorante

class Pub(Ristorante):
    def __init__(self, codice, tipo, nome_ristorante, n_dipendenti, n_tavolini):
        super(Pub, self).__init__(codice, tipo, nome_ristorante)
        self._n_dipendenti = n_dipendenti
        self._n_tavolini = n_tavolini

    def __str__(self):
        return super(Pub, self).__str__() + " " + str(self._n_dipendenti) + " " + str(self._n_tavolini) + "\t-\t-\t- "
