class Impegno():
    def __init__(self, codice, titolo, ore):
        self._codice, self._titolo, self._ore = codice, titolo, ore

    def get_ore(self):
        ore = self._ore
        return ore

    def get_titolo(self):
        titolo = self._titolo
        return titolo

    def __str__(self):
        return "(" + str(self._codice) + "," + str(self._ore) + ")"
