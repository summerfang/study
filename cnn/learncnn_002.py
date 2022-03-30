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