from Prodotto import Prodotto

class Ristorante():
    def __init__(self, codice, tipo, nome_ristorante):
        self._codice = codice
        self._tipo = tipo
        self._nome_ristorante = nome_ristorante
        self._menu = []

    def add_prodotto(self, prodotto):
        self._menu.append(prodotto)

    def get_nome(self):
        return self._nome_ristorante

    def menu_to_string(self):
        string = ""
        for prod in self._menu:
            string += string + " " + prod.to_string()
        return string

    def get_prezzo_medio(self):
        tot = 0.0
        for prod in self._menu:
            tot += prod.get_prezzo()
        return tot / len(self._menu)

    def __str__(self):
        return self._nome_ristorante + " " + str(self._codice) + " " + self._tipo
