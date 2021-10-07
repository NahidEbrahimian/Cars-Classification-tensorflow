# Iranian Cars Classification using TF

- [ ] train.ipynb

- [ ] inference.py

- [ ] preprocess.py

- [ ] models.py

## Dataset:

Dataset contains 2100 images of the cars in five categories.

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
| MobileNetV2  | 0.71| [Download]( https://drive.google.com/file/d/1-9vG-O2_raP1fHnR2hmq1aZPcSUqz5QH/view?usp=sharing)|
|ResNet50V2     |        |    |
|inceptionV3    |  0.71      | ][Download]( https://drive.google.com/file/d/1-6FHKt8wgvvSAEDSlyqNfs4vcAqIRXeq/view?usp=sharing)|     |

#


## Inference:

1- For inference, first clone this repository using the following command:

```
git clone https://github.com/NahidEbrahimian/Iranian-Cars-Classification-tensorflow

```

2- Then, download pre-trained model from the table and put in `./Iranian-Cars-Classification-tensorflow` directory.


- Inference on an image:

Put your input images in `./input` directory.

In root directory of project, run the following command for inference on an image:

```
!python3 inference_a.py --input_image ./input/image.jpg
```

- Inference on multiple images:

Run the following command for inference on multiple images. by inference using this command, result be saved in `.txt` file:

```
!python3 inference_b.py --input_path ./input --output_file output_file_name.txt
```

