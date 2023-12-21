# -*- coding: utf-8 -*-
"""kain defect-upload gambar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18g-8q2TNJ6b-M1uaSXb-uKXBELNsY0zO
"""

from google.colab import drive
drive.mount('/content/drive')

!nvidia-smi

import os
HOME = os.getcwd()
print(HOME)

!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

# Commented out IPython magic to ensure Python compatibility.
!mkdir {HOME}/datasets
# %cd {HOME}/datasets

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="tk7TheArOGljnx3N8JjB")
project = rf.workspace("anik-oktavia-1dhcj").project("kain-defect")
dataset = project.version(1).download("yolov8")

!yolo detect train data='/content/drive/MyDrive/FP ORBIT/data.yaml' epochs=10

!ls {HOME}/runs/detect/train/

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
Image(filename=f'/content/runs/detect/train2/confusion_matrix.png', width=600)

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
Image(filename=f'/content/runs/detect/train2/results.png', width=600)

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
Image(filename=f'/content/runs/detect/train2/val_batch0_pred.jpg', width=600)

!yolo detect predict model='/content/runs/detect/train2/weights/best.pt' source='/content/drive/MyDrive/FP ORBIT/valid/images/1022_jpg.rf.9608c3e1094c27e04101a4f5ed77d99d.jpg' save=true

!yolo detect predict model='/content/runs/detect/train2/weights/best.pt' source='https://i.ytimg.com/vi/tXltrSSZJj4/sddefault.jpg' save=true