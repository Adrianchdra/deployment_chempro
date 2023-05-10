import streamlit as st

st.title("◼ ANALISIS GRAVIMETRI")

Bobot = st.number_input("Masukan Bobot Sampel, dalam satuan gram")
BK = st.number_input("Masukan Bobot Cawan Kosong, dalam satuan gram")
BT = st.number_input("Masukan Bobot Abu, dalam satuan gram")
FK = st.number_input("Masukan Faktor Kimia Sampel")

Kadar = st.button("KADAR")

if Kadar:
    Kadar = (((BT-BK)*FK)/Bobot)*100
    st.success(f"{Kadar} %")

