class Prodotto():
    def __init__(self, descr_prodotto, tipo, prezzo, costo_materie):
        self._descrizione = descr_prodotto
        self._tipo = tipo
        self._prezzo = prezzo
        self._costo_materie = costo_materie

    def get_prezzo(self):
        return self._prezzo

    def to_string(self):
        return "[" + self._descrizione + "-" + str(self._costo_materie) + "-" + str(self._prezzo) + "]"

    def __str__(self):
        return str(self._descrizione + " " + self._costo_materie + " " + self._prezzo)