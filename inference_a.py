import cv2 
import numpy as np
import os
from config import *
from argparse import ArgumentParser
from keras.models import load_model
from MyModel import Model
from google.colab.patches import cv2_imshow

parser = ArgumentParser()
parser.add_argument("--input_image", type=str)
args = parser.parse_args()

path = options['path']

# model = Model(options)
# model.load_weights(os.path.join(path, 'Train/weight/Weights.hdf5'))
model = load_model(os.path.join(path, "Train/model/model.h5"))

width = options['input_width_size']
height = options['input_height_size']


img = cv2.imread(args.input_image)
img = cv2.resize(img, (width, height))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_np = np.array(img1)
img_np = img_np / 255.0
img_np = img_np.reshape(1, width, height, 3)

y_pred = model.predict(img_np)
prediction = np.argmax(y_pred)

label_map = np.load('label_map.npy',allow_pickle='TRUE').item()
key_list = list(label_map.keys())
val_list = list(label_map.values())

position = val_list.index(prediction)
label = key_list[position]

cv2_imshow(img1)
print('Predicted label:', label)