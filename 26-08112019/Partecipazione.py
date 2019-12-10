from Partecipante import Partecipante

class Partecipazione():
    def __init__(self, part, costo):
        self._part = part
        self._costo = costo

    def get_costo(self):
        return self._costo

    def to_string(self):
        nome = self._part.get_cognome()
        costo = str(self._costo)
        return nome + "-" + costo + " "

    def __str__(self):
        return self._part.get_cognome() + " " + str(self._costo)
