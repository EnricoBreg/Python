from Servizio import Servizio


class Cliente():
    def __init__(self, codice, nome):
        self._codice = codice
        self._nome = nome
        self._servizi = []

    def add_servizio(self, servizio):
        self._servizi.append(servizio)

    def get_nome(self):
        return self._nome

    def get_numero_servizi(self):
        return len(self._servizi)

    def get_totale(self):
        totale = 0.0
        for s in self._servizi:
            costo = s.get_costo()
            totale += costo
        return totale

    def __str__(self):
        totale = self.get_totale()
        return str(self._codice) + " " + self._nome + " " + str(totale)
