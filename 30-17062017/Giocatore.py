class Giocatore():
    def __init__(self, codice, nome_squadra, cognome, nome, titolare, eta, numero_maglia, ruolo):
        self._codice = codice
        self._nome_squadra = nome_squadra
        self._cognome = cognome
        self._nome = nome
        self._titolare = titolare
        self._eta = eta
        self._numero_maglia = numero_maglia
        self._ruolo = ruolo

    def __str__(self):
        return self._nome + " " + self._cognome + " " + str(self._eta) + " " + str(self._numero_maglia) + " " + \
            self._ruolo + " " + self._nome_squadra
