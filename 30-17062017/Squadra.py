class Squadra():
    def __init__(self, codice, sport, nome_squadra):
        self._codice = codice
        self._sport = sport
        self._nome_squadra = nome_squadra
        self._elenco_giocatori = []

    def add_giocatore(self, giocatore):
        self._elenco_giocatori.append(giocatore)

    def get_nome(self):
        return self._nome_squadra

    def get_num_giocatori(self):
        return str(len(self._elenco_giocatori))

    def get_sport(self):
        return self._sport

    def __str__(self):
        return self._nome_squadra + " " + str(self._codice)
