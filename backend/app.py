from fastapi import FastAPI
from Schema.user_input import UserInput
from Model.predict import user_input, MODEL_VERSION, model
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get('/')
def landing():
    return {'message' : 'Hello, Welcome to Laptop Price Predictor API'}

@app.get('/health')
def health_check():
    return {
        'status' : 'OK',
        'version': MODEL_VERSION,
        'Port': 'http://127.0.0.1:8000',
        'model loaded' : model is not None
    }
@app.post('/predict')
def predict_output(data: UserInput):
    input_df = {
        'Company' : data.company,
        'TypeName' : data.typename,
        'Inches' : data.inches,
        'Ram' : data.ram,
        'OpSys' : data.opsys,
        'res_width' : data.res_width,
        'res_height' : data.res_height,
        'is_touchscreen' : data.is_touchscreen, 
        'has_ssd' : data.has_ssd,	
        'has_hdd' : data.has_hdd,
        'has_flash' : data.has_flash,
        'cpu_brand': data.cpu_brand,
        'gpu_brand' : data.gpu_brand
    }

    prediction = user_input(input_df)
    
    return JSONResponse(status_code=200, content={'prediction': float(prediction)})

