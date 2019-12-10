class Conferenza():
    def __init__(self, nome, luogo):
        self._nome = nome
        self._luogo = luogo
        self._partecipazioni = [] #lista partecipazioni

    def add_partecipazione(self, part):
        self._partecipazioni.append(part)

    def get_totale(self):
        costo = 0
        for part in self._partecipazioni:
            costo = costo + part.get_costo()
        return costo

    def partecipazioni_to_string(self):
        string = ""
        for p in self._partecipazioni:
            string += p.to_string()
        return string

    def __str__(self):
        partecipazioni = self.partecipazioni_to_string()
        return self._nome + '\n' + self._luogo + '\n' + str(self.get_totale()) + ' ' \
               + str(len(self._partecipazioni)) + "\n" + "[" + partecipazioni + "]"
