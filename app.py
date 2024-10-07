import streamlit as st
from PIL import Image
import random
import os

# Load funny comments from a hardcoded list
funny_comments = [
    "Nobody puts Baby in a corner.",
    "Just keep swimming!",
    "I’m not superstitious, but I am a little stitious.",
    "Why so serious?",
    "I'm gonna make him an offer he can't refuse.",
    # Add the rest of your funny comments here...
]

# Define a function to display the feed of images with funny comments
def show_feed():
    st.title("Welcome to the Funny Picture Feed!")
    st.write("Enjoy the photos and laugh out loud with random funny comments!")

    # Fetch images from the uploaded folder
    image_folder = 'uploaded_images'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    images = [img for img in os.listdir(image_folder) if img.endswith(('png', 'jpg', 'jpeg'))]

    # Display images with comments
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = Image.open(img_path)
        st.image(img, caption=image, use_column_width=True)

        # Randomly assign a funny comment to the image
        comment = random.choice(funny_comments)
        st.write(f"**Funny Comment:** {comment}")
        st.write("---")  # Separator for UI

# Define the function to allow users to upload their photos
def upload_image(username):
    st.subheader(f"Hello, {username}! Upload your picture below:")
    uploaded_file = st.file_uploader("Choose a picture...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image_folder = 'uploaded_images'
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        # Save uploaded image to the folder
        img_path = os.path.join(image_folder, uploaded_file.name)
        with open(img_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Your image has been uploaded!")
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Main Streamlit app
def main():
    st.set_page_config(page_title="Funny Picture Feed", layout="centered")

    # Add header and footer for a consistent UI
    st.markdown("<h1 style='text-align: center; color: #ff6347;'>Funny Picture Feed</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)

    # Ask the user to input their username
    username = st.text_input("Enter your username", max_chars=20)
    if username:
        # Create tabs for uploading images and viewing the feed
        tab1, tab2 = st.tabs(["Upload Photo", "View Feed"])

        with tab1:
            upload_image(username)

        with tab2:
            show_feed()

    st.write("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Developed with 💻 using Streamlit</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
