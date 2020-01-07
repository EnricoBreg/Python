class Squadra():
    def __init__(self, codice, sport, nome_squadra):
        self._codice = codice
        self._sport = sport
        self._nome_squadra = nome_squadra

    def get_sport(self):
        return str(self._sport)

    def __str__(self):
        return self._nome_squadra + " " + str(self._codice)
