from Dipendente import Dipendente


class Nutrizionista(Dipendente):
    def __init__(self, codice, tipo, nome, telefono, medico, appuntamenti_settimanali, costo_orario):
        super(Nutrizionista, self).__init__(codice, tipo, nome, costo_orario)
        self._telefono = telefono
        self._medico = medico
        self._appuntamenti = appuntamenti_settimanali

    def __str__(self):
        return super(Nutrizionista, self).__str__() + "\t-\t- " + str(self._telefono) + " " + str(self._medico) + \
            str(self._appuntamenti) + " " + str(super().get_costo())
