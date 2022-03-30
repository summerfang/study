import tensorflow as tf
import tensorflow.keras as keras

import numpy as np
import matplotlib.pyplot as plt

print('tensorflow {}'.format(tf.__version__))
print("keras {}".format(keras.__version__))

model = keras.applications.VGG16(weights='imagenet')
model.summary()

_img = keras.preprocessing.image.load_img('cat_front.jpeg',target_size=(224,224))
plt.imshow(_img)
plt.show()