from config import *
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.models import Model


class Models():

  def __init__(self):
    self.input_shape = (width, height, 3)


  def mobilenetV2(self):
      base_model = tf.keras.applications.MobileNetV2(
          input_shape=self.input_shape ,
          alpha=1.0,
          include_top=False,
          weights="imagenet",
          input_tensor=None,
          pooling=None,
          classes=5,
          classifier_activation="softmax",
          # **kwargs
      )

      for layer in base_model.layers:
        layer.trainable = False

      model = tf.keras.Sequential([
                  base_model,
                  Dense(128, activation='softmax'),
                  Dropout(0.2),
                  Flatten(),
                  Dense(5, activation='softmax')])

      return model


  def resnet50V2(self):
      base_model = tf.keras.applications.ResNet50V2(
          include_top=False,
          weights="imagenet",
          input_tensor=None,
          input_shape=self.input_shape ,
          pooling='max',
          classes=5,
          classifier_activation="softmax",)

      for layer in base_model.layers:
        layer.trainable = False

      model = tf.keras.models.Sequential([
                                  base_model,
                                  Flatten(),
                                  Dense(128, activation='relu'),
                                  Dense(5, activation='softmax')])

      return model


  def inceptionV3(self):
      base_model = tf.keras.applications.InceptionV3(
          include_top=False,
          weights="imagenet",
          input_tensor=None,
          input_shape=self.input_shape,
          pooling='max',
          classes=5,
          classifier_activation="softmax",
      )


      for layer in base_model.layers:
        layer.trainable = False

      model = tf.keras.models.Sequential([
                                  base_model,
                                  Flatten(),
                                  Dense(128, activation='relu'),
                                  Dense(5, activation='softmax')])

      return model