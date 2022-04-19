import tensorflow as tf
from tensorflow.keras import models,layers
import matplotlib.pyplot as plt

model = models.load_model('/Users/jianbfan/Desktop/covid-cxr/results/models/model20220322-175005.h5', compile=False)
model.summary()

for layer in model.layers:
    if 'conv' in layer.name:
        filters, bias = layer.get_weights()
        print("{} {} {} {} {}".format(layer.name, filters, filters.shape, bias, bias.shape))

        f_min, f_max = filters.min(), filters.max()
        filters = (filters - f_min) / (filters + f_max)
        print("{}".format(filters))

        filter_cnt = 1
        for i in range(filters.shape[3]):
            filter = filters[:,:,:,i]
            for j in range(filters.shape[0]):
                ax = plt.subplot(filters.shape[3], filters.shape[0], filter_cnt)
                ax.set_xticks([])
                ax.set_yticks([])
                plt.imshow(filter[:,:,j])
                filter_cnt += 1
                plt.show()