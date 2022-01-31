# Face-Mask-Detection-using-TF-OD-API

Annotations directory contains all the image annotation.
model directory has custom face mask trained checkpoint.
image directory has the data set that, I used to train.

## All generated files will be in folder "data"
Steps to generate necessary files :
1. xml_to_csv.py file to convert annotations into csv format.
2. split labels.py to split the data to train and test sets.
3. generate_tfrecord.py to convert csv files to .record
4. paths to be configired in pipeline.config
5. load_and_test.py to load the checkpoint after training and you are good to go and test.


