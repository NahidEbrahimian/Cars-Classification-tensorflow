import cv2 
import numpy as np
from config import *
from argparse import ArgumentParser
from keras.models import load_model
from models import *

def get_optimal_font_scale(text, width):

    for scale in reversed(range(0, 60, 1)):
        textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=scale/10, thickness=1)
        new_width = textSize[0][0]
        if (new_width <= width):
            return scale/10
    return 1

parser = ArgumentParser()
parser.add_argument("--input_image", type=str)
parser.add_argument("--model", type=str)
args = parser.parse_args()

model = load_model(args.model)

img = cv2.imread(args.input_image)
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_RGB = cv2.resize(img_RGB, (width, height))
img_np = np.array(img_RGB)
img_np = img_np / 255.0
img_np = img_np.reshape(1, width, height, 3)

y_pred = model.predict(img_np)
prediction = np.argmax(y_pred)

label_map = np.load('label_map.npy',allow_pickle='TRUE').item()
key_list = list(label_map.keys())
val_list = list(label_map.values())

position = val_list.index(prediction)
label = key_list[position]

font_size = get_optimal_font_scale(label, img.shape[1] // 4)
cv2.putText(img, label, (img.shape[0] // 12, img.shape[1] // 12), cv2.FONT_HERSHEY_SIMPLEX, font_size,
            (0, 255, 0), 2,
            cv2.LINE_AA)

cv2.imshow('Iranian Cars Classification', img)
cv2.waitKey()
print('Predicted label:', label)