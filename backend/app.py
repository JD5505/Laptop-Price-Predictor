from fastapi import FastAPI
from Schema.user_input import UserInput
from Model.predict import user_input, MODEL_VERSION, model
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/')
def landing():
    return {
        'message': 'Hello, Welcome to Laptop Price Predictor API'
    }


@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'Port': 'http://127.0.0.1:8000',
        'model loaded': model is not None
    }


@app.post('/predict')
def predict_output(data: UserInput):

    input_df = {
        'Company': data.company,
        'Product': data.product,
        'TypeName': data.typename,
        'Inches': data.inches,
        'Ram': data.ram_gb,
        'OpSys': data.opsys,

        'ssd_gb': data.ssd_gb,
        'hdd_gb': data.hdd_gb,
        'flash_gb': data.flash_gb,
        'hybrid_gb': data.hybrid_gb,

        'cpu_speed_ghz': data.cpu_speed_ghz,
        'cpu_family': data.cpu_family,
        'cpu_brand': data.cpu_brand,

        'gpu_brand': data.gpu_brand,

        'res_width': data.res_width,
        'res_height': data.res_height,
        'is_touchscreen': data.is_touchscreen
    }

    prediction = user_input(input_df)

    return JSONResponse(
        status_code=200,
        content={
            'prediction': float(prediction)
        }
    )

