# streamlit_app.py

import streamlit as st
from PIL import Image
from rembg import remove

# Set title for the web app
st.title("Background Removal App")

# Upload the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    input_img = Image.open(uploaded_file)
    
    # Display the input image
    st.image(input_img, caption="Uploaded Image", use_column_width=True)
    st.write("Removing background...")

    # Remove background
    output_img = remove(input_img)

    # Display the output image
    st.image(output_img, caption="Image without Background", use_column_width=True)

    # Download the output image
    st.download_button(
        label="Download Image without Background",
        data=output_img.tobytes(),
        file_name="output.png",
        mime="image/png"
    )
else:
    st.write("Please upload an image to process.")
