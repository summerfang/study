from cgitb import enable


class producerLayout:
    def __init__(self, iw = 1920, ih = 1080, margin_left = 30, martin_right = 30, martin_top = 30, martin_bottom = 330, border = 4, spacing = 2, num_of_videos = 0, color = 'white') -> None:
        self.__init_rects(iw, ih, margin_left, martin_right, martin_top, martin_bottom, border, spacing, num_of_videos)

    def __init_rects(self,  iw = 1920, ih = 1080, margin_left = 10, martin_right = 10, martin_top = 10, martin_bottom = 400, border = 4, spacing = 4, num_of_videos = 0, color = 'white'):
        self.__rects = list()
        self.__iw = iw # The canvas width
        self.__ih = ih # The canvas height
        self.__margin_left = margin_left # The margin between left side of canvas and left side of the first rectangles
        self.__margin_right = martin_right # The margin between the right side of the canvas and right side of the most right rectangle.
        self.__margin_top = martin_top
        self.__margin_bottom = martin_bottom
        self.__boader = border
        self.__spacing = spacing
        self.__color = color

        self.__num_of_videos = num_of_videos

        for i in range(self.__num_of_videos):
            rect = list()
            rect.append((self.__iw - self.__margin_left - self.__margin_right - self.__spacing * (self.__num_of_videos - 1) - self.__boader * self.__num_of_videos * 2)/self.__num_of_videos) # The width of inner rectangle
            rect.append(self.__ih - self.__margin_top - self.__margin_bottom - 2 * border) # The height of the inner rectangle
            rect.append(self.__margin_left + self.__boader + self.__boader * i * 2 + self.__spacing * i + rect[0] * i) # x position of the ith rectangle
            rect.append(self.__margin_top + self.__boader) # y position of the ith rectangle 

            self.__rects.append(rect)

    def __str__(self) -> str:
        pass

    def set_number_of_videos(self, num_of_vidoes):
        self.__init_rects(num_of_videos = num_of_vidoes)
    
    def get_filter_string(self):
        str_filter = 'drawbox='
        for i in range(self.__num_of_videos):
            str_filter = str_filter + "x=" + str(self.__rects[i][2]) + ":y=" + str(self.__rects[i][3]) + ":w=" + str(self.__rects[i][0]) + ":h=" + str(self.__rects[i][1]) + ":color=" + self.__color + ":t=" + str(self.__boader) + ":enable='between(t,0,10)'"
            if i < self.__num_of_videos - 1:
                str_filter = str_filter + ",drawbox="
        return str_filter

    def get_rect(self, i):
        return self.__rects[i]