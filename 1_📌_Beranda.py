import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ChemPro",
    page_icon="house"
)

st.title("Welcome to ChemPro")
st.write("ChemPro merupakan aplikasi yang ditujukan sebagai alat bantu dalam melakukan analisis kimia")

import streamlit as st

from PIL import Image

img = Image.open("D:\ProjectLPK\Aplikasi\pages\ChemPro.jpg")

st.image(img, width=200)


st.text("Perhatian! : Aplikasi ini digunakan sebagai alat bantu")
st.sidebar.success("Select a Page Above")