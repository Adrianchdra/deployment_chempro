import streamlit as st

st.title("◼ MORALITAS")

Bobot = st.number_input("Masukan Bobot Zat, dalam Satuan gram",)
Volume = st.number_input("Masukan Volume Larutan, dalam Satuan Liter",)
Bobot_Molekul = st.number_input("Masukan BM Senyawa",)

HITUNG = st.button("HITUNG")

if HITUNG:
    Moralitas = Bobot/(Bobot_Molekul*Volume)
    st.success(f"{Moralitas} Mol/L")
