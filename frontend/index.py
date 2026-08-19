import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/predict'

st.title('Laptop Price Predictor')
st.markdown("Enter the laptop specifications below.")

company = st.selectbox(
    'Brand',
    options=[
        'Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo',
        'Chuwi', 'MSI', 'Microsoft', 'Toshiba', 'Huawei',
        'Xiaomi', 'Vero', 'Razer', 'Mediacom', 'Samsung',
        'Google', 'Fujitsu', 'LG'
    ]
)

product = st.text_input(
    'Laptop Model',
    placeholder='e.g. MacBook Pro, Inspiron, ThinkPad'
)

typename = st.selectbox(
    'Laptop Type',
    options=[
        'Ultrabook',
        'Notebook',
        'Netbook',
        'Gaming',
        '2 in 1 Convertible',
        'Workstation'
    ]
)

inches = st.number_input(
    'Screen Size (inches)',
    min_value=10.0,
    max_value=20.0,
    value=15.6,
    step=0.1
)

ram_gb = st.selectbox(
    'RAM (GB)',
    options=[2, 4, 6, 8, 12, 16, 24, 32, 64]
)

opsys = st.selectbox(
    'Operating System',
    options=[
        'macOS',
        'Mac OS X',
        'Linux',
        'Android',
        'Chrome OS',
        'Windows 7',
        'Windows 10',
        'Windows 10 S',
        'No OS'
    ]
)


st.subheader("Storage")

ssd_gb = st.number_input(
    'SSD Storage (GB)',
    min_value=0,
    max_value=4096,
    value=256,
    step=1
)

hdd_gb = st.number_input(
    'HDD Storage (GB)',
    min_value=0,
    max_value=4096,
    value=0,
    step=1
)

flash_gb = st.number_input(
    'Flash Storage (GB)',
    min_value=0,
    max_value=1024,
    value=0,
    step=1
)

hybrid_gb = st.number_input(
    'Hybrid Storage (GB)',
    min_value=0,
    max_value=2048,
    value=0,
    step=1
)


st.subheader("CPU")

cpu_brand = st.selectbox(
    'CPU Brand',
    options=[
        'Intel',
        'AMD',
        'Samsung'
    ]
)

cpu_family = st.selectbox(
    'CPU Family',
    options=[
        'Core i3',
        'Core i5',
        'Core i7',
        'Core i9',
        'Core M',
        'Celeron',
        'Pentium',
        'Atom',
        'A-Series',
        'A9-Series',
        'E-Series',
        'Ryzen',
        'Cortex'
    ]
)

cpu_speed_ghz = st.number_input(
    'CPU Speed (GHz)',
    min_value=0.5,
    max_value=5.0,
    value=2.5,
    step=0.1
)

gpu_brand = st.selectbox(
    'GPU Brand',
    options=[
        'Intel',
        'AMD',
        'Nvidia',
        'ARM'
    ]
)


st.subheader("Display")

resolution = st.selectbox(
    'Screen Resolution',
    options=[
        '2560x1600',
        '1440x900',
        '1920x1080',
        '2880x1800',
        '1366x768',
        '2304x1440',
        '3200x1800',
        '1920x1200',
        '2256x1504',
        '3840x2160',
        '2160x1440',
        '2560x1440',
        '1600x900',
        '2736x1824',
        '2400x1600'
    ]
)

touchscreen = st.checkbox(
    'Touchscreen'
)

if st.button("Predict Price"):

    input_data = {
    'company': company,
    'product': product,
    'typename': typename,
    'inches': inches,
    'ram_gb': ram_gb,
    'opsys': opsys,

    'ssd_gb': ssd_gb,
    'hdd_gb': hdd_gb,
    'flash_gb': flash_gb,
    'hybrid_gb': hybrid_gb,

    'cpu_speed_ghz': cpu_speed_ghz,
    'cpu_family': cpu_family,
    'cpu_brand': cpu_brand,
    'gpu_brand': gpu_brand,

    'resolution': resolution,
    'touchscreen': touchscreen
    }

    try:
        response = requests.post(
            API_URL,
            json=input_data
        )

        if response.status_code == 200:

            result = response.json()

            st.success(
                f"Predicted Price: **€{result['prediction']:.2f}**"
            )

        else:
            st.error(
                f"API Error: {response.status_code} - {response.text}"
            )

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to FastAPI Server. "
            "Make sure it's running on port 8000."
        )

        