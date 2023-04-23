import cv2
import streamlit as st
import os
import requests
from streamlit_lottie import st_lottie
import json


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


car_cascade = cv2.CascadeClassifier('cars.xml')
face_data=cv2.CascadeClassifier('haarcascades.xml')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_bniew9j6.json")
lottie_coding1=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ljotbiif.json")
lottie_coding2=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_xeqirqoe.json")




st.title("Hackathon Project")
st.text("Made By Team CTRL ALT DEL")

activities=["CarDetection","Face Detection","About us"]
choice = st.sidebar.selectbox("Select Your Activty",activities)
left_column,right_column=st.columns(2)



if choice=="CarDetection":
    with left_column:
        
       
        st.text("")
        st.text("")


        video_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])

        
        if video_file is not None:
            
            video_bytes = video_file.read()

            # Save the video to a temporary file
            with open("temp_video.mp4", "wb") as f:
                f.write(video_bytes)

            
            video_placeholder = st.empty()

            cap = cv2.VideoCapture("temp_video.mp4")

            
            while True:
                # Read a frame from the video stream
                ret, frame = cap.read()

                # Check if the frame was successfully captured
                if not ret:
                    break

                # Convert the frame from BGR to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Detect cars in the frame
                cars = car_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)

               
                for (x, y, w, h) in cars:
                    cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                
                video_placeholder.image(rgb_frame, channels="RGB")

            
            cap.release()
            os.remove("temp_video.mp4")
    with right_column:
        st_lottie(lottie_coding,height="10",key="coding")
    

elif choice=="Face Detection":
     with left_column:
         
        
        video_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])

        
        if video_file is not None:
            # Read the contents of the video file
            video_bytes = video_file.read()

            # Save the video to a temporary file
            with open("temp_video.mp4", "wb") as f:
                f.write(video_bytes)

            
            video_placeholder = st.empty()

            # Open the video file using VideoCapture
            cap = cv2.VideoCapture("temp_video.mp4")

            # Loop through the frames of the video
            while True:
                # Read a frame from the video stream
                ret, frame = cap.read()

                # Check if the frame was successfully captured
                if not ret:
                    break

                # Convert the frame from BGR to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                
                cars = face_data.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)

                
                for (x, y, w, h) in cars:
                    cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Display the frame in the Streamlit window
                video_placeholder.image(rgb_frame, channels="RGB")

           
            cap.release()
            os.remove("temp_video.mp4")
     with right_column:
         st_lottie(lottie_coding2,height="10",key="coding")
elif choice=="About us":
    #st.subheader("Project Made By Team CTRL ALT DEL")
    st.text("This Project Will Solve the Problem of manual Data Entry & Things Will get better and Fast")
    st.text("")
    
    st.markdown("Built with Streamlit by CTRL ALT DEL   [Github Link](https://github.com/PeroxideParadox/OSDCHACK.git)")
	
    st.success("Project Successful")
    st_lottie(lottie_coding1,height="100",key="coding1")
