import streamlit as st

st.title("◼ MOLARITAS")

Bobot = st.number_input("Masukan Bobot Zat, dalam Satuan gram",)
Volume = st.number_input("Masukan Volume Larutan, dalam Satuan Liter",)
Bobot_Molekul = st.number_input("Masukan BM Senyawa",)

HITUNG = st.button("HITUNG")

if HITUNG:
    Molaritas = Bobot/(Bobot_Molekul*Volume)
    st.success(f"{Molaritas} Mol/L")
