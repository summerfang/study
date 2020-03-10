    def read_audio(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate,
                         input=True,                                  frames_per_buffer=self.num_samples)

        save_count = 0
        save_buffer = []
        time_count = self.time_count

        while True:
            time_count -= 1

            # 读入num_samples个取样
            string_audio_data = stream.read(self.num_samples)
            # 将读入的数据转换为数组
            audio_data = np.fromstring(
                string_audio_data, dtype=np.short)
            # 计算大于 level 的取样的个数
            large_sample_count = np.sum(audio_data > self.level)

            print(np.max(audio_data)
                  ), "large_sample_count=>", large_sample_count

            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                    save_count = self.save_length
            else:
                 
                    save_count -= 1
            if save_count < 0:
                    save_count = 0
         
            if save_count > 0:
                    save_buffer.append(string_audio_data)
            else:
                     if len(save_buffer) > 0:
                            self.voice_string = save_buffer
                            save_buffer = [] 
                            print("Recode a piece of  voice successfully!")
                            return True
         
            if time_count == 0:
                 
                    if len(save_buffer) > 0:
                            self.voice_string = save_buffer
                            save_buffer = []
                            print("Recode a piece of  voice successfully!")
                             return True
                    else:
                             return False
        return True