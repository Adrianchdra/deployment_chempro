import streamlit as st

st.title("◼ ANALISIS TITRIMETRI")
st.write("Perhatian : Gunakan konsentrasi titran dalam grek/L")

Bobot = st.number_input("Masukan Bobot Sampel, dalam satuan gram")
Volume = st.number_input("Masukan Volume Titran, dalam satuan mililiter")
Konsentrasi = st.number_input("Masukan Konsentrasi Titran")
BEBM = st.number_input("Masukan BE atau BM,")
FP = st.number_input("Masukan Faktor Pengali atau Pengenceran")
KS = st.number_input("Masukan Kadar Sebenarnya")

Kadar = st.button("KADAR")
Kesalahan = st.button("KESALAHAN")

if Kadar:
    Kadar = ((Volume*Konsentrasi*BEBM*FP)/1000*100)/Bobot
    st.success(f"{Kadar} %")

if Kesalahan:
    Kesalahan = ((KS-Kadar)/KS)*100
    st.success(f"{Kesalahan} %")
