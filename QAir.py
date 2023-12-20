import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv"
df = pd.read_csv(url)

# Sidebar untuk memilih stasiun dan tahun
st.sidebar.title("Filter Data")
selected_station = st.sidebar.selectbox("Pilih Station:", df['station'].unique())
selected_year = st.sidebar.selectbox("Pilih Tahun:", df['year'].unique())

# Filter data berdasarkan stasiun dan tahun yang dipilih
filtered_df = df[(df['station'] == selected_station) & (df['year'] == selected_year)]

# Judul dashboard
st.title("Dashboard Analisis Data Cuaca / Kualitas Udara")

# Visualisasi tingkat polusi udara berkaitan dengan faktor-faktor cuaca
st.header("1. Hubungan Tingkat Polusi Udara dengan Faktor-faktor Cuaca")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x='TEMP', y='PM2.5', hue='RAIN', ax=ax)
ax.set_title(f"Hubungan PM2.5 dengan Suhu dan Hujan ({selected_station}, {selected_year})")
st.pyplot(fig)

# Visualisasi pola perubahan polusi udara seiring waktu
st.header("2. Pola Perubahan Polusi Udara Seiring Waktu")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='hour', y='PM2.5', ax=ax)
ax.set_title(f"Pola Perubahan PM2.5 Seiring Waktu ({selected_station}, {selected_year})")
st.pyplot(fig)

# Tampilkan tabel data
st.header("Tabel Data")
st.dataframe(filtered_df)
