import streamlit as st 

st.title("◼ PPM")

Bobot = st.number_input("Masukan Bobot Zat, dalam Satuan gram",)
Volume = st.number_input("Masukan Volume Larutan, dalam Satuan Liter",)

HITUNG = st.button("HITUNG")

if HITUNG:
    ppm = (Bobot*1000)/Volume
    st.success(f"{ppm} mg/L")