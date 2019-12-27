from Progetto import Progetto


class Innovazione(Progetto):
    def __init__(self, codice, tipo, titolo_progetto, coordinatore, organizzazione, az_coinv, importo_totale):
        super(Innovazione, self).__init__(codice, tipo, titolo_progetto, coordinatore, organizzazione)
        self._az_coiv, self._importo_totale = az_coinv, importo_totale

    def __str__(self):
        return super(Innovazione, self).__str__() + "\t-\t- " + str(self._az_coiv) + " " + str(self._importo_totale)
