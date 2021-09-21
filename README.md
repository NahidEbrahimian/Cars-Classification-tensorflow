# Image Classification using TF and Transfer Learning

## Dataset:

        .../IranianCarsDataset/iranKhodro_dena/1.jpg, 2.jpg, ..., n.jpg

                              /kia_cerato/1.jpg, 2.jpg, ..., n.jpg
                   
                             /mazda_3/1.jpg, 2.jpg, ..., n.jpg
                 
                             /peugeot_206/1.jpg, 2.jpg, ..., n.jpg
                 
                             /saipa_saina/1.jpg, 2.jpg, ..., n.jpg

Dataset link: [IranianCarsDataset]( https://drive.google.com/drive/folders/1C4RZ59f7sDTr9nKs42LAydMNtwFRw_dh?usp=sharing)

#

## Training

- In `model.py` you can select pretraned model. already `MobileNet` selected as pretrained model.

#


## Inference

- After model training, you can inference model using `inference_a.py` and `inference_b.py` and folowing commands.

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
