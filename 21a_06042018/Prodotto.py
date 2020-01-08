class Prodotto():
    def __init__(self, descrizione, tipo, prezzo, costo_produzione):
        self._descrizione = descrizione
        self._tipo = tipo
        self._prezzo = prezzo
        self._costo_produzione = costo_produzione

    def get_prezzo(self):
        return self._prezzo

    def __str__(self):
        line = self._descrizione + ": " + str(self._prezzo) + "-" + str(self._costo_produzione) + ", "
        return line
