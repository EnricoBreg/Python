class Progetto():
    def __init__(self, codice, tipo,titolo_progetto, coordinatore, organizzazione):
        self._codice, self._tipo, self._titolo_progetto, self._coordinatore, self._organizzazione = codice,  tipo, titolo_progetto, coordinatore, organizzazione

    def __str__(self):
        return self._tipo + " " + self._titolo_progetto + " " + str(self._codice) + " " + self._coordinatore + " " \
            + self._organizzazione
