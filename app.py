import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

# Commpany Name
company = st.selectbox("Laptop Brand",df['Company'].unique())

#Type
type = st.selectbox("Laptop Type",df['TypeName'].unique())

#Ram
ram = st.selectbox("Ram",[2,4,6,8,12,16,32,64])

# weight
weight = st.number_input("Weight of laptop in KGs")

# touchscreen
touchscreen = st.selectbox("TouchScreen",['No','Yes'])

#IPS
ips = st.selectbox("IPS",['No','Yes'])

#ScreenResolution
screen_reso = st.selectbox("Screen Resolution",['1920x1080','1366x768', '1600x900','3840x2160','3200x1800','2560x1600','2560x1440','2304x1440'])

#screen size
screen_size = st.number_input("Screen Size (in cm)")

# cpu brand
cpu = st.selectbox("Processor",df['cpu_brand'].unique())

#HDD
hdd= st.selectbox("HDD (in GB)",[0,128,256,512,1024,2048])

#SSD
ssd= st.selectbox("SSD (in GB)",[0,128,256,512,1024,2048])

#GPU
gpu = st.selectbox("GPU",df['Gpu_brand'].unique())

#OS
os = st.selectbox("Operating System",df['os'].unique())

if st.button('Predict Price'):
    # pass
    if touchscreen == 'Yes':
        touchscreen =1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips =1
    else:
        ips = 0

    x_res = int(screen_reso.split('x')[0])
    y_res = int(screen_reso.split('x')[1])

    ppi = ((x_res**2) + (y_res**2))**0.5/screen_size

    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title('Price Of laptop is Rs '+str(int(np.exp(pipe.predict(query)[0]))))
