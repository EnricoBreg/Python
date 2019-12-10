class Voto():
    def __init__(self, codice_corso, nome_corso, valutazione):
        self._codice_corso = codice_corso
        self._nome_corso = nome_corso
        self._valutazione = valutazione

    def get_voto(self):
        if self._valutazione == "30L":
            return 31
        else:
            return int(self._valutazione)

    def get_corso(self):
        return self._nome_corso

    def toString(self):
        voto = self.get_voto()
        corso = self._codice_corso
        res=""
        res = "(" + str(voto) + "," + str(corso) + ")"
        return res

    def __str__(self):
        return "(", + str(self._codice_corso) + "," + " " + str(self._valutazione) + ")"
