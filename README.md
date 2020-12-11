# Turn your pet photo into a personalized mosaic!

___

This project's goal was to create a photo mosaic of a user's pet. I would use image recognition to classify the animal in the photo, and then select only tiles of that same animal type to make up the mosaic. 

This process had to include training a model to distinguish cat and dog images, creating the mosaic, and then deploying through Streamlit for user access.

### Data
All images were gathered from a [Kaggle dataset](https://www.kaggle.com/c/dogs-vs-cats) which includes 25,000 training images. These images were also used for the tiles in the mosaic.

### CNN Model
Machine learning was applied through a Convolutional Neural Network(CNN) as well as Keras Image Data Generator for image augmentation. The final model concluded with 81.2% training accuracy, and 85% testing accuracy, visualized in the graph below.

![](https://github.com/JenniferHofer/image_classification_photo_mosaic/images/classification_model.png)

### Model Application and testing
The final step for classification was to build a function that could take in an unseen image, and make a prediction on whether it was a cat or a dog. Below is a random sample of images that were ran through this function. Following closely to the 85% testing accuracy, we can see that 8/9 of these images were classified correctly.
![](https://github.com/JenniferHofer/image_classification_photo_mosaic/images/unseen_data.png)

### Mosaic build
The [Photomosaic Library](http://danielballan.github.io/photomosaic/docs/index.html) allowed me to easily define the key image (the image that would be recreated) as well as the tiles. The entire process was written into two functions, one with cats tiles and one with dog tiles, so that either could be ran based on the class prediction results. 
![](https://github.com/JenniferHofer/image_classification_photo_mosaic/images/key_image/retriever.jpeg)
![](https://github.com/JenniferHofer/image_classification_photo_mosaic/images/retriever.png)
The tiles were sized 250x250 for the final image in order to showcase a clear final image.

### Streamlit deployment

The final step is deploying this project through Streamlit, and is still a work in progress. This will allow users to upload photos on their own terms, and get their image back in a mosaic. Below is an example of how the initial site is looking
![](https://github.com/JenniferHofer/image_classification_photo_mosaic/images/streamlit_1)
![](https://github.com/JenniferHofer/image_classification_photo_mosaic/images/streamlit_2)
A link to the application will shared upon completion. Until then if you have any questions, feel free to reach out to me at hofer.jenn@gmail.com.