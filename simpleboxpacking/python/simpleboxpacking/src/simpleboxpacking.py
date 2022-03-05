from math import sqrt

class SimpleBoxPacking:
    def __init__(self, width = 1, height = 1, n = 1, p = 1) -> None:
        self._W = width
        self._H = height
        self._n = n
        self._p = p

        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)

        # height = round(height/item[0])
        # width = round(width/item[1])

        # w = height * p
        # h = width/p

        # if height <= h:
        #     width = height * p
        # else:
        #     height = width/p

        # self._w = round(width)
        # self._h = round(height)
        # self._row = round(height/self._h)
        # self._col = round(width/self._w)
    
    def set_n(self, n):
        self._n = n
        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)

    def set_p(self, p):
        self._p = p
        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)

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

    @property
    def W(self):
        return self._W

    @property
    def H(self):
        return self._H

    def __box_combination(self, n):
        """
        Return a list of combination of row, column when n boxes

            Parameters: 
                n (int): How many boxes will be put into container

            Returns:
                combinations (list contains row and col pair, eg [[row1,col1],[row2,col2],...,[rown,coln]]): Return a list which contains any possible row and col combination when boxes is n

        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n has to be positive integer.")

        combinations = list()

        for i in range(1, n + 1):
            y = 1

            while i * y < n:
                y = y + 1
            
            item = list()
            item.append(i)
            item.append(y)

            combinations.append(item)

        return combinations

    def __get_row_column_make_area_biggest(self, CW, CH, n, ratio):
        """
        Knowing container's size, box's width vs height and numbers, return row and col

            parameter:

            Returns:

        """
        list_areas = list()

        list_row_col = self.__box_combination(n)
        for item in list_row_col:
            row = item[0]
            col = item[1]

            w = CW/col
            h_by_ratio = w / ratio

            h = CH/row

            if h_by_ratio >= h:
                height = h
            else:
                height = h_by_ratio

            width = height * ratio

            area = width * height * n
            list_areas.append(area)

        max_area = max(list_areas)
        max_index = list_areas.index(max_area)

        row = list_row_col[max_index][0]
        col = list_row_col[max_index][1]
        w = round(CW/col)
        h = round(w/self._p)

        return row, col, w, h