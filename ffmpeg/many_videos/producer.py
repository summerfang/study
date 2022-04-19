from producer_layout import producerLayout

if __name__ == "__main__":
    bg = "background.mp4"
    logo = "logo.mp4"
    spk1 = "obama.mp4"
    spk2 = "spk2.mp4"
    spk3 = "spk3.mp4"
    spk4 = "spk4.mp4"

    cmd_line = "ffmpeg -stream_loop -1 -i {0} -stream_loop -1 -i {1} -stream_loop -1 -i {2} -stream_loop -1 -i {3} -stream_loop -1 -i {4} -stream_loop -1 -i {5} ".format(bg, spk1, spk2, spk3, spk4, logo)

    filter_complex_string = "-filter_complex "
    bg_string = "[0]scale=1920:1080[bg0];"

    spks = list()
    spks.append(spk1)
    spks.append(spk2)
    spks.append(spk3)
    spks.append(spk4)

    lo = producerLayout(num_of_videos = 4)

    str_spk = ""
    for i in range(len(spks)):
        str_spk = str_spk + "[{}]crop={}:{}:{}:{}[out{}]".format(i+1, lo.get_rect(i)[0], lo.get_rect(i)[1], 350, 0, i + 1)
        str_spk = str_spk + ";[bg{}][out{}]overlay={}:{}[bg{}]".format(i, i + 1, lo.get_rect(i)[2],lo.get_rect(i)[3], i + 1)
        if i < len(spks) - 1:
            str_spk += ";"

    # print(str_spk)

    str_logo = "{};[{}]scale=180:-1[logo]".format(str_spk, i + 2)

    str_video =  "{};[bg{}][logo]overlay=1920-180-30:14[video]".format(str_logo, i + 1)
    str_audio = ';[1:a]volume=-3dB[audio] '
    str_output2ffplay = '-map "[video]" -map "[audio]" -preset ultrafast -tune zerolatency -crf 28 -g 60 -c:a aac -f matroska - | ffplay -'
    cmd_line = cmd_line + filter_complex_string + '"' + bg_string + str_video + str_audio + '" ' + str_output2ffplay
    print(cmd_line)

# Good work!

# This is line is used to cherry pick!