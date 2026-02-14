import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
from datetime import datetime
from pathlib import Path


# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Portofolio Take Home Test",
    page_icon="✻",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Selamat Datang di Portofolio Saya")

# Projek data
@st.cache_data
def project_data():
    projects = [
        {
            'title': 'Customer Segmentation pada Data Event',
            'category': 'Customer Segmentation',
            'year': 2026,
            'description': '''**Deskripsi:**
Proyek ini akan  menganalisis mengenai  customer segmentation dengan melihat 4 macam segment  yaitu Champions, Loyal, Potential, At Risk.

**Tools:** Python, Power BI''',
            'has_image': r'C:\Users\ThinkPad\Documents\STUDY\DIBIMBING\tht_da\assets\dashboard.png',
            'Link' : 'https://colab.research.google.com/drive/1veP1YEOBTcxfgHJLiHztO9Qx0NDhMukM?usp=sharing'
        }
    ]
    return pd.DataFrame(projects)

# Project
df_projects = project_data()   
st.header("My Projects")

for index, row in df_projects.iterrows():
    with st.container(border=True): 
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(row['title'])
            st.caption(f"{row['category']} | {row['year']}")
            st.markdown(row['description'])
            st.link_button("Lihat di Google Colab", row['Link'])
            
        with col2:
            st.write("📌")
            st.image(row['has_image'], use_container_width=True)

# Cara 1: Mengimpor file yang ada di folder lokal
try:
    df = pd.read_csv(r'C:\Users\ThinkPad\Documents\STUDY\DIBIMBING\tht_da\data\raw\data_event.csv')
    st.success("Data berhasil dimuat!")
    
    # Menampilkan 5 data teratas
    st.subheader("Preview Data:")
    st.dataframe(df.head())
    
except FileNotFoundError:
    st.error("File tidak ditemukan. Pastikan path-nya benar.")

# Visualisasi
# pendapatan perbulannya selama event berlangsung
df['event_time'] = pd.to_datetime(df['event_time'])
df['event_month'] = df['event_time'].dt.to_period('M')
monthly_revenue = df.groupby('event_month')['price'].sum().reset_index()
monthly_revenue['event_month'] = monthly_revenue['event_month'].astype(str)

fig, ax= plt.subplots()
ax.bar(monthly_revenue['event_month'], monthly_revenue['price'], color='skyblue')
ax.set_title("Total Pendapatan Per Bulan")
st.pyplot(fig)
