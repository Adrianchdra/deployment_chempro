import streamlit as st 

st.title("◼ Persentase")

Bobot_Zat = st.number_input("Masukan Bobot Zat, dalam Satuan gram",)
Bobot_Larutan = st.number_input("Masukan Bobot Larutan, dalam Satuan gram *untuk B/B",)
Volume = st.number_input("Masukan Volume Larutan, dalam Satuan mililiter *untuk B/V",)

Volume = st.button("B/V")
Bobot = st.button("B/B")

if Volume:
    Persentase = (Bobot_Zat/Volume)*100
    st.success(f"{Persentase} g/mL")
elif Bobot:
    Persentase = (Bobot_Zat/Bobot_Larutan)*100
    st.success(f"{Persentase} g/g")




