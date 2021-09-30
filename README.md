# Iranian Cars Classification using TF

- [x] train.ipynb

- [x] inference.py

- [x] preprocess.py

- [x] models.py

## Dataset:

The data set contains 2100 images of the car in five categories.

        .../IranianCarsDataset/iranKhodro_dena/1.jpg, 2.jpg, ..., n.jpg

                              /kia_cerato/1.jpg, 2.jpg, ..., n.jpg
                   
                             /mazda_3/1.jpg, 2.jpg, ..., n.jpg
                 
                             /peugeot_206/1.jpg, 2.jpg, ..., n.jpg
                 
                             /saipa_saina/1.jpg, 2.jpg, ..., n.jpg

Dataset link: [IranianCarsDataset]( https://drive.google.com/drive/folders/1ymuR1fEXrIjnDA_qxQkL-seBYGSNFG02?usp=sharing)

#

## Training:

| Pre_trained Model | Accuracy | Model |
| :---         |     :---:      |          :---: |
| MobileNetV2  | 0.97     | [mobilenetV2.h5]    |
|ResNet50V2     | 0.86       | [resnet50V2.h5]    |
|inceptionV3    | 0.37       | [inceptionV3.h5]      |

#


## Inference

- Inference on an image:

1- Download trained model from this link: [download model]( https://drive.google.com/drive/folders/1oB-TYojq2VELADOlBaKFIkPtC75aRO66?usp=sharing)

2- Put your input images in `./input` directory.

In root directory of project, run the following command for inference on an image:

```
!python3 inference_a.py --input_image ./input/image.jpg
```

Run the following command for inference on multiple images. by inference using this command, result be saved in `.txt` file:

```
!python3 inference_b.py --input_path ./input --output_file output_file_name.txt
```
