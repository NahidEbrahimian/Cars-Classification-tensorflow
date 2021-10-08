# Iranian Cars Classification using TF



| ![01](https://user-images.githubusercontent.com/82975802/136616267-19f31a62-958b-441f-a459-cb9891c20090.png)| ![02](https://user-images.githubusercontent.com/82975802/136616818-5ce0c329-0cf4-4109-86eb-843c18873d7f.png)| ![05](https://user-images.githubusercontent.com/82975802/136615270-66586596-4f17-49c2-9b8c-dfcf64e5de48.png)| 
|     :---:      |     :---:      |      :---:      |

|![04](https://user-images.githubusercontent.com/82975802/136615306-569de517-c9bd-4b39-bfb1-f1d6acca1eaf.png)| ![03](https://user-images.githubusercontent.com/82975802/136615737-aaef3e4d-4442-4a61-9754-02dcac0a4753.png) |
|      :---:      |      :---:      |


- [x] train.ipynb

- [x] inference.py

- [x] preprocess.py

- [x] models.py

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
| :---:         |     :---:      |          :---: |
| MobileNetV2  | 0.716| [Download]( https://drive.google.com/file/d/1-9vG-O2_raP1fHnR2hmq1aZPcSUqz5QH/view?usp=sharing)|
|ResNet50V2     |   0.7136     |[Download]( https://drive.google.com/file/d/1Blv-AesEu4RjnD9Yk9OsrjAl-5DoL9MM/view?usp=sharing)    |
|inceptionV3    |  0.7184      | [Download]( https://drive.google.com/file/d/1-6FHKt8wgvvSAEDSlyqNfs4vcAqIRXeq/view?usp=sharing)|     |

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
python3 inference_a.py --input_image input/03-mazda.jpg --mode mobilenetV2.h5
```

- Inference on multiple images:

Run the following command for inference on multiple images. by inference using this command, result be saved in `.txt` file:

```
python3 inference_b.py --input_images input --model mobilenetV2.h5 --output_file test_inferense.txt
```

