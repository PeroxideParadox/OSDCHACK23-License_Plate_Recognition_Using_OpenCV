import streamlit as st
import cv2
import numpy as np
import easyocr
import pandas as pd
from io import BytesIO
import base64
import requests
from streamlit_lottie import st_lottie
from datetime import datetime

# Load the pre-trained EasyOCR reader
reader = easyocr.Reader(lang_list=['en'])

# Load the Haarcascade XML file for car number plates
plate_cascade = cv2.CascadeClassifier('cars.xml')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_bniew9j6.json")
lottie_coding1 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ljotbiif.json")

def main():
    st.title("License Plate of Cars Recognition App")
    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    left_column, right_column = st.columns([0.6, 0.4])

    if choice == "Detection":
        with left_column:
            st.text(" ")
            st.markdown("Please Make sure that the image is clear and clicked at the right angles so that it can be detected easily")

            uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = read_image(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            if st.button("Detect License Plates"):
                detected_plates = detect_license_plates(image)
                st.write("Detected Plates:")
                st.write(detected_plates)
                
                #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                csv_data = save_to_csv(detected_plates)
                download_link = get_download_link(csv_data)
                st.markdown(download_link, unsafe_allow_html=True)

        with right_column:
            st_lottie(lottie_coding, height="20", key="coding")

    elif choice == "About":
        st.subheader("About the Detection App")
        st.markdown("This app allows users to upload an image containing a vehicle with a visible license plate. The app then detects license plates in the image using OpenCV and EasyOCR, and provides the detected license plate numbers in a CSV format.")
        st.markdown("This can be used practically for automatic registration in societies and other areas/institutions.")
        st.markdown("Connect with me Through [GitHub](https://github.com/PeroxideParadox/OSDCHACK23-License_Plate_Recognition_Using_OpenCV)")
        st.success("Success")
        st_lottie(lottie_coding1, height="10", width="20", key="coding")

def read_image(uploaded_file):
    image = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def detect_license_plates(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15))
    
    detected_plates = []
    for (x, y, w, h) in plates:
        plate_image = gray[y:y+h, x:x+w]
        texts = reader.readtext(plate_image)
        detected_text = " ".join([text[1] for text in texts])
        detected_plates.append(detected_text)
    
    return detected_plates

def save_to_csv(detected_plates):
    data = []
    for i, plate_text in enumerate(detected_plates):
        data.append({"Index No": i + 1, "License Plate Number": plate_text})
    
    df = pd.DataFrame(data)
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()
    return csv_data

def get_download_link(data):
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="detected_plates.csv"><button style="background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 20px; border-radius: 5px; cursor: pointer;">Download CSV</button></a>'
    return href

if __name__ == "__main__":
    main()
