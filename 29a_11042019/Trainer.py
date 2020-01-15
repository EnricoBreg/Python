from Dipendente import Dipendente


class Trainer(Dipendente):
    def __init__(self, codice, tipo, nome, ore_settimana, costo_orario, specialita):
        super(Trainer, self).__init__(codice, tipo, nome, costo_orario)
        self._ore_settimana = ore_settimana
        self._specialita = specialita

    def __str__(self):
        return super(Trainer, self).__str__() + " "  + str(self._ore_settimana) + " " + self._specialita + "\t-\t-\t- "\
            + str(super().get_costo())
