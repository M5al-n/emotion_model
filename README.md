# Facial Emotion Recognition

## About the Project

For this project, I have built a neural network to predict emotions based on the facial expressions found in pictures. The data used is FER2013 dataset containing seven emotions: angry, disgust, fear, happy, neutral, sad, and surprised.

In addition, I developed a small application with the help of Streamlit that allows users to make predictions by taking a picture with the use of their webcams or uploading an image.

## Dataset

I used the FER2013 dataset containing:

- 28,709 images for training
- 7,178 images for testing
- Seven classes of emotions

All the pictures were rescaled to 48 × 48 pixels and made black and white. Moreover, I normalized the values of pixels and split the train set into training and validation sets.

## Model Training

I created my neural network with the use of Keras using Flatten and Dense layers.

I started with three layers with 100 neurons. I used the ReLU function for the hidden layers and Softmax for the output one.

I trained several models to check whether it will be possible to improve my predictions. In addition, I used EarlyStopping since the model began overfitting when I was training it for too many epochs.

## Results

The most accurate model obtained accuracy of **37.59%** on test data.

The results were evaluated by means of accuracy, precision, recall, F1-score, and a confusion matrix.

The model performed well in classifying happy and surprised emotions but had difficulties classifying other emotions.

## Streamlit Application

In order to create an application I used Streamlit. Users can:

- Take a picture using their web camera;
- Upload an image;
- Get a prediction of the emotion;
- Get probabilities of each emotion.

## Results

The most accurate model obtained accuracy of 37.59% on test data.

The results were evaluated by means of accuracy, precision, recall, F1-score, and a confusion matrix.

The model performed well in classifying happy and surprised emotions but had difficulties classifying other emotions.

## Streamlit Application

In order to create an application I used Streamlit. Users can:

- Take a picture using their web camera;
- Upload an image;
- Get a prediction of the emotion;
- Get probabilities of each emotion.

## To Run the Model

Install necessary libraries:

`pip install streamlit tensorflow numpy pandas pillow`

Place `emotion_model.keras` and `appp.py` in the same folder.

To run the application use:

streamlit run appp.py`

## Limitations

As of now, the model isn't quite accurate. Lighting, the quality of the images, and facial angle can influence the predictions.

Also, certain emotions are difficult to distinguish. Besides, facial expression doesn't always represent emotion.

## Conclusion

Thus, this project gave me an experience in data preparation, construction and training of neural networks, analysis of the results, and implementation in Streamlit application.

Besides, I found out that just by adding layers or epochs one doesn't get better results.
