import cv2 
import numpy as np
import os
from config import *
from argparse import ArgumentParser
from keras.models import load_model
from models import *

parser = ArgumentParser()
parser.add_argument("--input_images", type=str)
parser.add_argument("--output_file", type=str)
parser.add_argument("--model", type=str)
args = parser.parse_args()

model = load_model(args.model)

test_data_dir = args.input_images


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