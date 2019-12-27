from Impegno import Impegno

class Ricercatore():
    def __init__(self, nome, cognome):
        self._nome, self._cognome = nome, cognome
        self._lista_impegni = []

    def add_impegno(self, codice, titolo_progetto, ore):
        i = Impegno(codice, titolo_progetto, ore)
        self._lista_impegni.append(i)

    def get_cognome(self):
        return self._cognome

    def get_nome(self):
        return self._nome

    def get_max_impegno(self):
        max = 0.0
        max_i = ""
        for i in self._lista_impegni:
            ore = i._ore
            if max < ore:
                max = ore
                max_i = i._titolo
        return self._nome + " " + self._cognome + " " + str(max) + " " + str(max_i)

    def __str__(self):
        res = "["
        for i in self._lista_impegni:
            res = res + i.__str__() + ","

        res += "]"
        return self._nome + " " + self._cognome + " " + res


