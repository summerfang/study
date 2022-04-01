import ffmpeg
from videolayer import VideoLayer
from layer import Layer

if __name__ == "__main__":
    vl = VideoLayer(iw = 1280, ih = 720)
    stream = ffmpeg.input('background.mp4')

    layer1 = Layer(stream, width=1280, height=720, layer_type=Layer.BACKGROUND)
    vl.append(layer1)

    s1 = ffmpeg.input("obama.mp4")
    layer1 = Layer(s1, width=360, height=600, x=120)
    vl.append(layer1)

    # s2 = ffmpeg.input("spk2.mp4")
    # layer2 = Layer(s2, width=360, height=600, x=120)
    # vl.append(layer2)
    # s3 = ffmpeg.input("spk3.mp4")
    # layer3 = Layer(s3, width=360,height=600, x=120)
 
    # vl.append(layer3)

    # s4 = ffmpeg.input("spk4.mp4")
    # layer4 = Layer(s4, width=360,height=600, x=120)
    # vl.append(layer4)

    logo = ffmpeg.input("logo.mp4")
    layer_logo = Layer(logo, width=180,height=100, x=120, position_x=1280 - 180 - 10, position_y= 25, layer_type=Layer.LOGO)
    vl.append(layer_logo)

    vl.set_panelist_number(1)
    vl.set_speaker(1)
    vl.playback()