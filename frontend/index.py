import streamlit as st 
import requests

API_URL = 'http://127.0.0.1:8000/predict'

st.title('Laptop Price Predictor API')

st.markdown("Enter Laptop details below")

company = st.selectbox('Brand', options=['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
       'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
       'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'])

typename = st.selectbox('Enter Laptop Type', options=['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible',
       'Workstation'])

inches = st.number_input('Enter Size of Laptop(in)')

ram_gb = st.selectbox("RAM", options=['2GB','4GB', '6GB', '8GB', '12GB', '16GB', '24GB', '32GB', '64GB'])

opsys = st.selectbox('Operating System', options=['macOS', 'Mac OS X', 'Linux', 'Android',
       'Chrome OS', 'Windows 7','Windows 10','Windows 10 S', 'No OS'])

resolution = st.selectbox('Select Laptop Screen Resolution', options=['2560x1600', '1440x900', '1920x1080', '2880x1800', '1366x768',
       '2304x1440', '3200x1800', '1920x1200', '2256x1504', '3840x2160',
       '2160x1440', '2560x1440', '1600x900', '2736x1824', '2400x1600'])

touchscreen = st.selectbox('Touchscreen Enabled', options=[True, False])

memory  = st.selectbox('Memory Type', options=['SSD', 'HDD', 'Flash Drive'])

cpu_brand = st.selectbox('CPU', options=['Intel', 'AMD', 'Samsung'])

gpu_brand = st.selectbox('GPU', options=['Intel', 'AMD', 'Nvidia', 'ARM'])

if st.button("Predict Price"):
    input_data={
        'company' : company,
        'typename': typename,
        'inches' : inches,
        'ram_gb' : ram_gb,
        'opsys' : opsys,
        'resolution' : resolution,
        'touchscreen' : touchscreen,
        'memory' : memory,
        'cpu_brand' : cpu_brand,
        'gpu_brand' : gpu_brand
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price: **{result['prediction']}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI Server. Make sure it's running on port 8000")