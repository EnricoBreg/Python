from Prodotto import Prodotto


class Ristorante():
    def __init__(self, codice, tipo, nome_ristorante):
        self._codice = codice
        self._tipo = tipo
        self._nome_ristorante = nome_ristorante
        self._menu = []

    def get_costo_medio_menu(self):
        tot = 0.0
        for p in self._menu:
            costo = p.get_prezzo()
            tot += costo
        return tot / float(len(self._menu))

    def get_nome_ristorante(self):
        return self._nome_ristorante

    def add_prodotto(self, prod):
        self._menu.append(prod)

    def stampa_menu(self):
        line = self._nome_ristorante + "\n\t["
        for prod in self._menu:
            line += prod.__str__()
        line += "]"
        return line

    def __str__(self):
        return self._nome_ristorante + " " + str(self._codice) + " " + self._tipo
