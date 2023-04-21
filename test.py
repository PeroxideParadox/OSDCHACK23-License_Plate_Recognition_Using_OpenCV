
import streamlit as st 
import cv2
from PIL import Image,ImageEnhance
import numpy as np 
import os
from streamlit_lottie import st_lottie


face_cascade = cv2.CascadeClassifier('haarcascades.xml')

def detect_faces(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
	# Detect faces

	faces = face_cascade.detectMultiScale(gray, 1.2, 4)
	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	return img,faces 

def main():
	"""Face Detection App"""

	st.title("Hackathon Project")
	st.text("Crafted With Love By Baibhav Singh")

	activities = ["Detection","About"]
	choice = st.sidebar.selectbox("Select Activty",activities)
	
	if choice == 'Detection':
		st.subheader("Face Detection")

		image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)
			st.text("Original Image")
			# st.write(type(our_image))
			st.image(our_image)

		enhance_type = st.sidebar.radio("Enhance Type",["Original","Gray-Scale","Contrast","Brightness","Blurring"])
	



		# Face Detection
		task = ["Faces","Smiles","Eyes","Cannize","Cartonize"]
		feature_choice = st.sidebar.selectbox("Find Features",task)
		if st.button("Process"):

			if feature_choice == 'Faces':
				result_img,result_faces = detect_faces(our_image)
				st.image(result_img)

				st.success("Found {} faces".format(len(result_faces)))
			


			




	elif choice == 'About':
		st.subheader("About Face Detection App")
		st.markdown("Built with Streamlit by [JCharisTech](https://www.jcharistech.com/)")
		st.text("Jesse E.Agbe(JCharis)")
		st.success("Jesus Saves @JCharisTech")



if __name__ == '__main__':
		main()