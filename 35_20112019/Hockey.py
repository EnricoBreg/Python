from Squadra import Squadra


class Hockey(Squadra):
    def __init__(self, codice, sport, nome_squadra, n_vittorie, n_sconfitte, media_goal, media_falli):
        super(Hockey, self).__init__(codice, sport, nome_squadra)
        self._n_vittorie = n_vittorie
        self._n_sconfitte = n_sconfitte
        self._media_goal = media_goal
        self._media_falli = media_falli

    def get_vittorie(self):
        return self._n_vittorie

    def __str__(self):
        return super(Hockey, self).__str__() + " " + str(self._n_vittorie) + " " + str(self._n_sconfitte) + " " + \
            str(self._media_goal) + " " + str(self._media_falli) + " " + super(Hockey, self).get_sport()
