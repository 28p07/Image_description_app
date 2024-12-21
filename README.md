# Image Description App

# Image Description App

This is a web application built with Flask and TensorFlow that allows users to upload an image and get a description of the image based on the predictions of a pre-trained InceptionV3 model from TensorFlow Hub.

## Features
- Upload an image to the app.
- Get a description of the image based on its content (e.g., dog, cat, car).
- Built using Flask for the backend and TensorFlow for image classification.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow, TensorFlow Hub
- **Image Processing**: Pillow (PIL)
- **Model**: Pre-trained InceptionV3 model from TensorFlow Hub
- **Hosting**: Local server (development)

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.10
- pip (Python package manager)

## Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/28p07/Image_description_app
    cd image-description-app
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the `imagenet-classes.txt` file that contains the class labels for InceptionV3. You can find it here: [imagenet-classes.txt](https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json). Save it in the project directory.

4. Set up your environment (optional but recommended):
  
Start the Flask server:
  ```Bash
    python app.py
  ```
- The application will be running locally at http://127.0.0.1:5000/.

## App Usage
- Visit http://127.0.0.1:5000/ in your browser.
- Upload an image using the "Upload an Image" button.
- The app will process the image and display a description of the image (e.g., "A dog", "A cat").


File Structure
```
/image-description-app
│
├── app.py                 
├──.gitignore
├── README.md            
├── imagenet-classes.txt    
├── requirements.txt       
└── /templates              
    └── /index.html
```

## Dependencies
#### The app requires the following Python libraries:
- Flask
- TensorFlow
- Pillow (PIL)
- TensorFlow Hub
- NumPy

To install all dependencies, use the following command:
- pip install -r requirements.txt

### Error: Failed to process the image

-Check if the image is in a valid format (JPEG, PNG, etc.) and has dimensions that are compatible with the model (299x299 pixels).

### Model Prediction Error

-If there is an issue with TensorFlow or the model, ensure that your environment has the required dependencies and TensorFlow is properly installed.


### Instructions for Running the App
1. Clone the repository and install dependencies using `pip install -r requirements.txt`.
2. Download the `imagenet-classes.txt` file and save it in the project directory.
3. Run the Flask app using `python app.py`.
4. Open a web browser and go to `http://127.0.0.1:5000/`.
5. Upload an image to get a description.






