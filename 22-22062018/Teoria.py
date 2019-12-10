from Corso import Corso

class Teoria(Corso):
    def __init__(self, codice, tipo, nome, docente, cod_aula, ore_settimanali, ore_lezione):
        super(Teoria, self).__init__(codice, tipo, nome, docente)
        self._cod_aula = cod_aula
        self._ore_settimanali = ore_settimanali
        self._ore_lezione = ore_lezione

    def __str__(self):
        return super().__str__() + " " + str(self._cod_aula) + " " + str(self._ore_settimanali) + " " + \
               str(self._ore_lezione) + " \t-\t-\t-"
