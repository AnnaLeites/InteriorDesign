import streamlit as st 

st.header("Please choose one of the options to generate design of your room")

col1, col2 = st.columns(2)

with col1:
   st.header("Text to Room generator")
   col11, col12 = st.columns(2)
   with col11:
       st.text_input("Input detailed description of the room") 
   with col12:
       st.button("OK", type="primary")

with col2:
   st.header("Room to Room generator")
   #st.write("Upload a photo of your room")
   upload_file = st.file_uploader(label="Choose a image file ")    
   if upload_file:

        img = upload_file.read()
        content_img=  upload_file.name
        #content_img= image_to_data_url(content_img, img)
        st.info("Uploaded Image")
        st.image(img, width=300)
    
    
    
   
