from Ristorante import Ristorante


class Osteria(Ristorante):
    def __init__(self, codice, tipo, nome_ristorante, n_posti_a_sedere, superficie, bagno_disabili):
        super(Osteria, self).__init__(codice, tipo, nome_ristorante)
        self._n_posti = n_posti_a_sedere
        self._superficie = superficie
        self._bagno_disabili = bagno_disabili

    def __str__(self):
        return super(Osteria, self).__str__() + "\t-\t- " + str(self._n_posti) + " " + str(self._superficie) + " " + \
            str(self._bagno_disabili)