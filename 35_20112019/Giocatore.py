class Giocatore():
    def __init__(self, nome_squadra, cognome, nome, eta, numero_maglia, ruolo, titolare):
        self._nome_squadra, self._cognome, self._nome, self._numero_maglia, self._ruolo, self._titolare, self._eta = \
            nome_squadra, cognome, nome, numero_maglia, ruolo, titolare, eta

    def __str__(self):
        return self._nome + " " + self._cognome + " " + str(self._eta) + " " + str(self._numero_maglia) + \
               " " + self._ruolo + " " + str(self._titolare) + " " + self._nome_squadra
