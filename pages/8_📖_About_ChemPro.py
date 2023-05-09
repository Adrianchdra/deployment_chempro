import streamlit as st
from PIL import Image

st.title("Welcome to ChemPro")
st.text("Your Chemical Support")

img = Image.open("ChemPro.jpg")

st.image(img)

st.write("ChemPro adalah aplikasi berbasis web yang dirancang untuk membantu anda dalam bidang analisis kimia. ChemPro menyediakan berbagai fitur yang utama dalam bidang analisis kimia. ChemPro dapat anda akses dimanapun dan kapanpun melalui gadget anda. ChemPro hadir untuk membantu. ChemPro, your chemical support")
st.text("Akses ChemPro secara gratis sekarang !")
