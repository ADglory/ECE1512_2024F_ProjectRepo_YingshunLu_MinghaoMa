# -*- coding: utf-8 -*-
"""1512p1t2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BqXlZgeO8gbeB7tJePtzd_wyJFCL6JjA
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/VICO-UoE/DatasetCondensation
# %cd DatasetCondensation

!pip install -r requirements.txt

from torchvision.datasets import MNIST
from torchvision import transforms

# download MNIST dataset
mnist_data = MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())

!python main.py --dataset MNIST --method DM --ipc 10

!ls /content/