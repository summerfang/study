from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras import regularizers
from keras.layers import BatchNormalization
from tensorflow.keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

# load and prepate cifar images
(xtrain, ytrain), (xtest, ytest) = cifar10.load_data()
x_train = xtrain.astype('float32')
x_test = xtest.astype('float32')
x_train  /= 255
x_test /= 255
nb_classes = 10
y_train = np_utils.to_categorical(ytrain, nb_classes)
y_test = np_utils.to_categorical(ytest, nb_classes)

# augment images with a generator
cifar_gen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    )
cifar_gen.fit(x_train)

# create convolutional neural network (CNN)
def create_cnn(input_shape=x_train.shape[1:], nb_classes=nb_classes, 
               nb_blocks=3, nb_filters=32, filter_size=(3,3), 
               pool_size=(2,2), weight_decay=1e-4, padding='same', 
               dropout=.2, output_activation='softmax'):

    model = Sequential()

    for i in range(nb_blocks):
        if i==0:
            model.add(Conv2D(nb_filters, filter_size, activation='relu', 
                             padding=padding, kernel_regularizer=regularizers.l2(weight_decay), 
                             input_shape=input_shape))
        else:
            model.add(Conv2D(nb_filters, filter_size, activation='relu', 
                             padding=padding, kernel_regularizer=regularizers.l2(weight_decay)))        
        model.add(BatchNormalization())
        model.add(Conv2D(nb_filters, filter_size, activation='relu', 
                  padding=padding, kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=pool_size))
        model.add(Dropout(dropout))

    model.add(Flatten())
    model.add(Dense(nb_classes, activation=output_activation))

    return model
       
cnn = create_cnn(nb_filters=32)

# compile CNN
opt_rms = RMSprop(lr=0.001, decay=1e-6)
cnn.compile(loss='categorical_crossentropy', optimizer=opt_rms, metrics=['accuracy'])

# train CNN
batch_size = 64
epochs = 100
steps = x_train.shape[0]

cnn_history = cnn.fit_generator(cifar_gen.flow(x_train, y_train, batch_size=batch_size),
                                  steps_per_epoch=steps, 
                                  epochs=epochs,
                                  verbose=1,
                                  validation_data=(x_test,y_test))

from random import randint
import matplotlib.pylab as plt 
import numpy as np

def get_feature_maps(model, layer_id, input_image):
    model_ = Model(inputs=[model.input], 
                   outputs=[model.layers[layer_id].output])
    return model_.predict(np.expand_dims(input_image, 
                                         axis=0))[0,:,:,:].transpose((2,0,1))

def plot_features_map(img_idx=None, layer_idx=[0, 2, 4, 6, 8, 10, 12, 16], 
                      x_test=x_test, ytest=ytest, cnn=cnn):
    if img_idx == None:
        img_idx = randint(0, ytest.shape[0])
    input_image = x_test[img_idx]
    fig, ax = plt.subplots(3,3,figsize=(10,10))
    ax[0][0].imshow(input_image)
    ax[0][0].set_title('original img id {} - {}'.format(img_idx, 
                                                        labels[ytest[img_idx][0]]))
    for i, l in enumerate(layer_idx):
        feature_map = get_feature_maps(cnn, l, input_image)
        ax[(i+1)//3][(i+1)%3].imshow(feature_map[:,:,0])
        ax[(i+1)//3][(i+1)%3].set_title('layer {} - {}'.format(l, 
                                                               cnn.layers[l].get_config()['name']))
    return img_idx

labels =  ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

img_idx = plot_features_map()