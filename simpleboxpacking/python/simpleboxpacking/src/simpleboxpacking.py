from math import floor, sqrt

class SimpleBoxPacking:
    def __init__(self, width = 1, height = 1, n = 1, p = 1) -> None:
        self._W = width
        self._H = height
        self._n = n
        self._p = p

        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)
   
    def set_n(self, n):
        self._n = n
        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)

    def set_p(self, p):
        self._p = p
        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)

    def set_np(self, n, p):
        self._n = n
        self._p = p
        self._row, self._col, self._w, self._h = self.__get_row_column_make_area_biggest(self._W, self._H, self._n, self._p)

    def set_WH(self, new_W, new_H):
        self._W = new_W
        self._H = new_H
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

    def get_integer_pairs_which_product_is_no_more_than_n(self, n):
        """
        Return a list of postive integer pair (x, y) which x * y >= n and (x + 1) * y or x * (y + 1) < n. n is another positive integer.
            Parameters: 
                n (int): For example 5.
            Returns:
                combinations, for example, [(1,5), (5,1), (2,3), (3,2)].
        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n has to be positive integer.")

        combinations = list()

        for i in range(1, n + 1):
            y = 1

            while i * y < n:
                y = y + 1
            
            combinations.append((i, y))

        return combinations

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
            
            combinations.append((i, y))

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
                width = height * ratio
            else:
                width = w
                height = h_by_ratio

            area = width * height * n
            list_areas.append(area)


        max_area = max(list_areas)
        max_index = list_areas.index(max_area)

        row = list_row_col[max_index][0]
        col = list_row_col[max_index][1]
        
        w = CW/col
        h_by_ratio = w / ratio

        h = CH/row

        if h_by_ratio >= h:
            height = h
            width = height * ratio
        else:
            width = w
            height = h_by_ratio

        w = floor(width)
        h = floor(height)

        return row, col, w, h