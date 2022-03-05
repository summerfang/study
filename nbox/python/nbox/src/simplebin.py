from math import sqrt

class SimpleBin:
    def __init__(self, width = 0, height = 0, n = 1, p = 1) -> None:
        self._w = round(sqrt(width*height/(n*p)))
        self._h = round(self._w*p)
        self._row = round(height/self._h)
        self._col = round(width/self._w)

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

        