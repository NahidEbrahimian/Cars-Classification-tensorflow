from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ----->train
def train_DataGenerator(options):

    dir = options['train_folder']

    width = options['input_width_size']
    height = options['input_height_size']
    input_image_size = (width, height)

    data_generator = ImageDataGenerator(
        rotation_range = 10,
        # horizontal_flip = True,
        vertical_flip = True,
        zoom_range = 0.1,
        height_shift_range = 0.1,
        rescale = 1 / 255
    )

    train_data = data_generator.flow_from_directory(
        dir,
        target_size = input_image_size,
        batch_size = 8,
        class_mode = 'categorical',
        subset = 'training'
    )

    label_map = (train_data.class_indices)
    return train_data, label_map


# ---->validation
def test_DataGenerator(options):

    dir = options['test_folder']

    width = options['input_width_size']
    height = options['input_height_size']
    input_image_size = (width, height)

    data_generator = ImageDataGenerator(rescale = 1 / 255)


    validation_data = data_generator.flow_from_directory(
        dir,
        target_size = input_image_size,
        batch_size = 8,
        class_mode = 'categorical',
        subset = 'training'
    )
    return validation_data