import streamlit as st

st.title("◼ NORMALITAS")

Bobot = st.number_input("Masukan Bobot Zat, dalam Satuan gram",)
Volume = st.number_input("Masukan Volume Larutan, dalam Satuan Liter",)
Bobot_Ekivalen = st.number_input("Masukan BE Senyawa",)

HITUNG = st.button("HITUNG")

if HITUNG:
    Normalitas = Bobot/(Bobot_Ekivalen*Volume)
    st.success(f"{Normalitas} grek/L")
