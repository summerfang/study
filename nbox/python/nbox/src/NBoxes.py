class NBoxes:
    def __init__(self) -> None:
        pass

    def box_combination(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n has to be positive integer")

        qualified_combination = list()

        for i in range(1, n + 1):
            y = 1

            while i * y < n:
                y = y + 1
            
            item = list()
            item.append(i)
            item.append(y)

            qualified_combination.append(item)

        return qualified_combination

    def get_row_column_make_area_biggest(self, GW, GH, n, ratio):
        list_areas = list()

        list_row_col = self.box_combination(n)
        for item in list_row_col:
            row = item[0]
            col = item[1]

            w = GW/col
            h_by_ratio = w / ratio

            h = GH/row

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
    