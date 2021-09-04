# ImageClassification-using-TF-TransferLearnin

- Training data demo, Path and Classes:


Each class of training images are inside a seperate folder that name of folder is class name of images, and all folders placed in dataset folder as below:

        .../dataset/iranKhodro_dena/1.jpg, 2.jpg, ..., n.jpg

                   /kia_cerato/1.jpg, 2.jpg, ..., n.jpg
                   
                   /mazda_3/1.jpg, 2.jpg, ..., n.jpg
                 
                   /peugeot_206/1.jpg, 2.jpg, ..., n.jpg
                 
                   /saipa_saina/1.jpg, 2.jpg, ..., n.jpg
                 

#

- In **CreateModel.py** you can select pretraned model. already `MobileNet` selected as pretrained model.

#

- After model training, you can inference model using **inference_a.py** and **inference_b.py** files and folowing commands:



Run the following command for inference on an image:

```
!python3 inference_a.py --input_image ./image.jpg
```


Run the following command for inference on multiple images. by inference using this command, result be saved in .txt file:

```

!python3 inference_b.py --input_folder ./folder_name --output_file output_file_name.txt

```
