from config import *
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.models import Model


def Model(options):

    width = options['input_width_size']
    height = options['input_height_size']
    InputShape = (width, height, 3)

    base_model = tf.keras.applications.MobileNet(
                      alpha=1.0,
                      depth_multiplier=1,
                      dropout=0.001,
                      include_top=False,
                      weights="imagenet",
                      input_shape = InputShape,
                      pooling=None,
                      # classes=1000,
                      classifier_activation="softmax")


    for layer in base_model.layers:
      layer.trainable = False
    base_model.get_layer('conv_pw_13').trainable = True
    base_model.get_layer('conv_pw_12').trainable = True
    base_model.get_layer('conv_pw_11').trainable = True
    base_model.get_layer('conv_pw_10').trainable = True

    model = tf.keras.models.Sequential([
                                base_model,
                                Flatten(),
                                Dense(512, activation='relu'),
                                # Dropout(0.2),
                                Dense(64, activation='relu'),
                                Dense(5, activation='softmax')])

    return model