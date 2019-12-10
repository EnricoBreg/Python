from Corso import Corso

class Laboratorio(Corso):
    def __init__(self, codice, tipo, nome, docente, nome_laboratorio, assistente, postazioni):
        super(Laboratorio, self).__init__(codice, tipo, nome, docente)
        self._nome_laboratorio = nome_laboratorio
        self._assistente = assistente
        self._postazioni = postazioni

    def __str__(self):
        return super().__str__() + "\t-\t-\t- " + self._nome_laboratorio + " " + self._assistente + \
            " " + str(self._postazioni)