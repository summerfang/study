import ffmpeg

class Layer:
    SPEAKER = 0
    BACKGROUND = 1
    LOGO = 2

    def __init__(self, video_input, x = 0, y = 0, width = 0, height = 0, position_x = 0, position_y = 0, layer_type = SPEAKER) -> None:
        # if not isinstance(video_input, ffmpeg.input):
        #     raise Exception("Sorry, video_input must to be ffmpeg.input type.")

        self.__input = video_input
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__position_x = position_x
        self.__position_y = position_y
        self.__layer_type = layer_type # 0 - speaker; 1 - backgroup; 2 - logo

    def get_layer_type(self):
        return self.__layer_type

    def set_position_x(self, position_x):
        self.__position_x = position_x

    def get_position_x(self):
        return self.__position_x

    def set_position_y(self, position_y):
        self.__position_y = position_y

    def get_position_y(self):
        return self.__position_y

    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_stream(self):
        return self.__input