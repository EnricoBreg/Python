from Progetto import Progetto


class Ricerca(Progetto):
    def __init__(self, codice, tipo, titolo_progetto, coordinatore, organizzazione, cod_arg, num_partner,
                 importo_totale):
        super(Ricerca, self).__init__(codice, tipo, titolo_progetto, coordinatore, organizzazione,)
        self._cod_arg, self._num_partner, self._importo_totale = cod_arg, num_partner, importo_totale

    def __str__(self):
        return super(Ricerca, self).__str__() + " " + self._cod_arg + " " + str(self._num_partner) + "\t- "\
               + str(self._importo_totale)
