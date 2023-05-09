import streamlit as st

st.title("◼ ANALISIS TITRIMETRI")
st.write("Perhatian : Gunakan konsentrasi titran dalam grek/L")

VolumSampel = st.number_input("Masukan Volume atau Bobot Sampel, dalam satuan mL atau gram")
Volume = st.number_input("Masukan Volume Titran, dalam satuan mililiter")
Konsentrasi = st.number_input("Masukan Konsentrasi Titran")
BEBM = st.number_input("Masukan BE atau BM")
FP = st.number_input("Masukan Faktor Pengali atau Pengenceran")
KS = st.number_input("Masukan Kadar Sebenarnya")

Kadar = st.button("KADAR")

if Kadar:
    Kadar = ((Volume*Konsentrasi*BEBM*FP)/1000*100)/VolumSampel
    st.success(f"{Kadar} %")
