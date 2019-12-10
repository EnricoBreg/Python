
class Corso():
    def __init__(self, codice, tipo, nome, docente):
        self._codice = codice
        self._tipo = tipo
        self._nome = nome
        self._docente = docente

    def __str__(self):
        return self._nome + " " + str(self._codice) + " " + self._docente + " " + self._tipo