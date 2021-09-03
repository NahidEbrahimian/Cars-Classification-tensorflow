import cv2 
import numpy as np
import os
from config import *
from argparse import ArgumentParser
from keras.models import load_model
from MyModel import Model

parser = ArgumentParser()
parser.add_argument("--input_folder", type=str)
parser.add_argument("--output_file", type=str)
args = parser.parse_args()

path = options['path']

# model = Model(options)
# model.load_weights(os.path.join(path, 'Train/weight/Weights.hdf5'))
model = load_model(os.path.join(path, "Train/model/model.h5"))

test_data_dir = args.input_folder


width = options['input_width_size']
height = options['input_height_size']


with open(args.output_file, "w") as f:

    for _, _, imgs in os.walk(test_data_dir):
        for im in imgs:

            f.write(im + "\n")
            img = cv2.imread(test_data_dir + '/' + im)
            img = cv2.resize(img, (width, height))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = np.array(img)
            img = img / 255.0
            img = img.reshape(1, width, height, 3)

            y_pred = model.predict(img)
            prediction = np.argmax(y_pred)

            label_map = np.load('label_map.npy',allow_pickle='TRUE').item()
            key_list = list(label_map.keys())
            val_list = list(label_map.values())

            position = val_list.index(prediction)
            label = key_list[position]

            print(label)
            f.write(str(label)+ "\n")