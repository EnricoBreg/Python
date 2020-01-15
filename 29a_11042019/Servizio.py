class Servizio():
    def __init__(self, codice_dip, ore_servizio, costo_orario):
        self._codice_dip = codice_dip
        self._ore_servizio = ore_servizio
        self._costo_orario = costo_orario

    def get_costo(self):
        costo = self._costo_orario * self._ore_servizio
        return costo
