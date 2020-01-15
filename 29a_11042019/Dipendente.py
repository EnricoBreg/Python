class Dipendente():
    def __init__(self, codice, tipo, nome, costo_orario):
        self._codice = codice
        self._tipo = tipo
        self._nome = nome
        self._costo_orario = costo_orario

    def get_costo(self):
        return self._costo_orario

    def __str__(self):
        return self._nome + " " + str(self._codice) + " " + self._tipo
