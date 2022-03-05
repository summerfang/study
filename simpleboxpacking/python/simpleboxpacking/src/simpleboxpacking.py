from math import sqrt

class SimpleBoxPacking:
    def __init__(self, width = 1, height = 1, n = 1, p = 1) -> None:
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

    def __box_combination(self, n):
        """
        Return a list of combination of row, column when n boxes

            Parameters: 
                n (int): How many boxes will be put into container

            Returns:
                combinations (list contains row and col pair, eg [[row1,col1],[row2,col2],...,[rown,coln]]): Return a list which contains any possible row and col combination when boxes is n

        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n has to be positive integer")

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

        return list_row_col[max_index]