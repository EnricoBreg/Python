class Partecipante():
    def __init__(self, codice, tipo, nome, cognome):
        self._codice = codice
        self._tipo = tipo
        self._nome = nome
        self._cognome = cognome

    def get_cognome(self):
        return self._cognome

    def get_tipo(self):
        return self._tipo

    def __str__(self):
        return self._tipo + ' ' + str(self._codice) + ' ' + self._nome + ' ' + self._cognome + ' '
