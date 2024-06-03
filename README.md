# License Plate Recognition App

This app allows users to upload an image containing a vehicle with a visible license plate. The app then detects license plates in the image using OpenCV and EasyOCR, and provides the detected license plate numbers in a CSV format which can be copied or downloaded in your machine 

## Demo

Check out the live demo of the application here:  [Click Here](https://spotmycar.streamlit.app/)


## Installation
To run the app locally, follow these steps:

1. **Clone the repository**:
    ```bash
    https://github.com/PeroxideParadox/OSDCHACK23-License_Plate_Recognition_Using_OpenCV.git
    cd OSDCHACK23-License_Plate_Recognition_Using_OpenCV
    ```

2. **Install the required dependencies**:
    Make sure you have Python installed on your machine. Then, install the required packages using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run main.py
    ```

## Features

- Upload images in JPG, JPEG, or PNG format.
- Detect license plates in uploaded images.
- Display detected license plate numbers.
- Download the detected license plate numbers in CSV format.
- Suitable for various applications such as automatic registration in societies, malls, and other institutions.

## How It Works

1. **Image Upload**: Users upload an image containing a car license plate.
2. **Detection**: The app uses OpenCV's Haarcascade algorithm to detect potential regions of license plates in the image.
3. **Recognition**: EasyOCR reads the text on the detected license plates.
4. **Results**: Detected license plate numbers are displayed and can be downloaded in CSV format.





