import streamlit as st

st.title("◼ ANALISIS GRAVIMETRI")

Bobot = st.number_input("Masukan Bobot Sampel, dalam satuan gram")
BK = st.number_input("Masukan Bobot Cawan Kosong, dalam satuan gram")
BT = st.number_input("Masukan Bobot Total, dalam satuan gram")
FK = st.number_input("Masukan Faktor Kimia Sampel")
KS = st.number_input("Masukan Kadar Sebenarnya")

Kadar = st.button("KADAR")
Kesalahan = st.button("KESALAHAN")

if Kadar:
    Kadar = (((BT-BK)*FK)/Bobot)*100
    st.success(f"{Kadar} %")

if Kesalahan:
    Kesalahan = ((KS-Kadar)/KS)*100
    st.success(f"{Kesalahan} %")
