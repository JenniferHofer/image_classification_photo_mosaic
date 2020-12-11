#IMPORTS

import pandas as pd
import streamlit as st
import numpy as np
import tensorflow as tf 
import photomosaic as pm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pickle
import os
import cv2
import keras 

from tensorflow import keras
from PIL import Image
from skimage.io import imread
from skimage.io import imsave
from skimage import data
from skimage import img_as_float
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

IMAGE_SIZE = (250, 250)

model = keras.models.load_model('Notebooks/classification_model')

st.title('Turn your pet photo into a mosaic!')
st.write('''Upload your photo below to see it transform into a mosaic of cats or dogs.''')

st.image('images/key_image/unsplash_1.jpg', caption='Original example ', width=300)
st.image('images/retreiver.jpg', caption='Mosaic example ', width=300) 


uploaded_file = st.file_uploader(
    '''drop your .jpg or .jpeg file below''',
    type = ['jpg', 'jpeg']
)

#FUNCTIONS

def upload():
    try:
        if uploaded_file:
            img = Image.open(uploaded_file)
            img = img.resize(IMAGE_SIZE)
            img = keras.preprocessing.image.img_to_array(img)
            img = np.array([img])
            return img
    except:
        pass
img = upload()
try:
    if img is not None:
        st.write('file uploaded')
        predicted_class = model.predict(img)[0]
        if predicted_class[0] > .5:
            animal = 'cat'
        else:
            animal = 'dog'
except:
    pass
#if img is None:
    #st.write('Upload file here')
        

#dog mosaic
@st.cache
def dog_mosaic(directory):
    #key image
    #d_image = mpimg.imread(directory)
    d_image = img_as_float(img)
    
    #pool of images for mosaic tiles
    d_pool = pm.make_pool('Data/folders/train/dog/*.jpg')
    
    #mosaic of 250x250 tiles
    d_mos = pm.basic_mosaic(d_image, d_pool, (100, 100), depth = 1)
    
    #return mosaic
    return st.image(d_mos)

@st.cache
#cat mosaic
def cat_mosaic(directory):
    #key image
    c_image = mpimg.imread(directory)
    c_image = img_as_float(c_image)
    
    #pool of images for mosaic tiles
    c_pool = pm.make_pool('../Data/folders/train/cat/*.jpg')
    
    #mosaic of 250x250 tiles
    c_mos = pm.basic_mosaic(c_image, c_pool, (100, 100), depth = 1)
    
    #return mosaic
    return st.image(c_mos)

#RUN MODELS
try:
    img = upload()
    predicted_class = model.predict(img)[0]
    st.write(f'What a cute {animal}! Your mosaic is rendering, and will be ready in a few minutes')
    if animal == 'cat':
        cat_mosaic(img)
        st.progress

    if animal == 'dog':
        dog_mosaic(img)
        st.progress

except:
    pass
#mosaic
