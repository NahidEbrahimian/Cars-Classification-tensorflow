from tensorflow.keras.preprocessing.image import ImageDataGenerator
from config import *

def DataGenerator():

    data_generator = ImageDataGenerator(
        rescale = 1./255,
        horizontal_flip =True,
        rotation_range=20,
        zoom_range=0.1,
        validation_split=0.2
    )

    train_data = data_generator.flow_from_directory(
        data_path,
        target_size=(width, height),
        batch_size = batch_size,
        class_mode='categorical',
        shuffle=True,
        subset='training'
)


    validation_data = data_generator.flow_from_directory(
        data_path,
        target_size=(width, height),
        batch_size = batch_size,
        class_mode='categorical',
        shuffle=True,
        subset='validation'
    )

    label_map = (train_data.class_indices)
    
    return train_data, validation_data, label_map

