
import ffmpeg
import subprocess

from layer import Layer


class VideoLayer:
    def __init__(self, iw = 1920, ih = 1080, margin_left = 10, martin_right = 10, martin_top = 10, martin_bottom = 400, border = 4, spacing = 4, color = 'white'):
        self.__layers = list()
        self.__stream = None
        self.__init_layout(iw, ih, margin_left, martin_right, martin_top, martin_bottom, border, spacing, color)

    def __init_layout(self,  iw = 1920, ih = 1080, margin_left = 10, martin_right = 10, martin_top = 10, martin_bottom = 400, border = 4, spacing = 4, color = 'white'):
        self.__iw = iw # The canvas width
        self.__ih = ih # The canvas height
        self.__margin_left = margin_left # The margin between left side of canvas and left side of the first rectangles
        self.__margin_right = martin_right # The margin between the right side of the canvas and right side of the most right rectangle.
        self.__margin_top = martin_top
        self.__margin_bottom = martin_bottom
        self.__boader = border
        self.__spacing = spacing
        self.__color = color

    def append(self, layer):
        if not isinstance(layer, Layer):
            raise Exception("Sorry, layer must be an object of class Layer")

        self.__layers.append(layer)

    def __transcode(self):
        if len(self.__layers) == 0:
            raise Exception("Sorry, you must need at least one layer of video")

        bg_layer = self.get_background_layer()
        if bg_layer == None:
            raise Exception("Sorry, you must have background layer")
        
        self.__stream = bg_layer.get_stream().filter('scale', self.__iw, self.__ih)

        for layer in self.__layers:
            if layer.get_layer_type() == Layer.SPEAKER:
                _stream = layer.get_stream().crop(layer.get_x(), layer.get_y(), layer.get_width(), layer.get_height())
                self.__stream = self.__stream.drawbox(
                                                        x = layer.get_position_x() - self.__boader, 
                                                        y = layer.get_position_y() - self.__boader, 
                                                        width = layer.get_width() + 2*self.__boader,
                                                        height = layer.get_height() + 2*self.__boader,
                                                        thickness = self.__boader, 
                                                        color = self.__color)

                self.__stream = self.__stream.overlay(_stream, x=layer.get_position_x(), y=layer.get_position_y())

        logo_layer = self.get_logo_layer()
        if logo_layer != None:
            _stream = logo_layer.get_stream().filter('scale', logo_layer.get_width(), logo_layer.get_height())
            self.__stream = self.__stream.overlay(_stream, x=layer.get_position_x(), y=layer.get_position_y())

    def playback(self):
        self.__transcode()
        process1 = (
            self.__stream
            .output('pipe:', format='rawvideo', pix_fmt='rgb24')
            .run_async(pipe_stdout=True)
        )
        process2 = subprocess.Popen(
            [
                'ffplay',
                '-f', 'rawvideo',
                '-pix_fmt', 'rgb24',
                '-s', '{}x{}'.format(self.__iw, self.__ih),
                '-i', 'pipe:',
            ],
            stdin=process1.stdout,
        )
        process1.wait()
        process2.wait()

    def set_4panelist(self, num_of_panelists = 4):
        number_of_speakers = 0
        for layer in self.__layers:
            if layer.get_layer_type() == Layer.SPEAKER:
                number_of_speakers += 1

        if number_of_speakers != num_of_panelists:
            print("set_4panelist() need {} speakers!".format(num_of_panelists))
            return False
        
        speaker_order = 0
        x_pos = self.__margin_left + self.__boader
        _width = (self.__iw - self.__margin_left - self.__margin_right - self.__boader * 4 * 2 - self.__spacing*3)/4
        for layer in self.__layers:
            if layer.get_layer_type() == Layer.SPEAKER:
                speaker_order += 1
                layer.set_position_x(x_pos)
                layer.set_position_y(self.__margin_top + self.__boader)
                layer.set_width(_width)
                x_pos += layer.get_width() + 2*self.__boader + self.__spacing

        return True
        

    def get_background_layer(self):
        for layer in self.__layers:
            if layer.get_layer_type() == Layer.BACKGROUND:
                return layer;

        return None

    def get_logo_layer(self):
        for layer in self.__layers:
            if layer.get_layer_type() == Layer.LOGO:
                return layer
        
        return None