# 💻 Laptop Price Predictor

A machine learning web application that predicts laptop prices based on hardware specifications and configuration. Built with a **FastAPI** backend and a **Streamlit** frontend.

The model uses engineered hardware features such as CPU characteristics, GPU brand, RAM, storage configuration, screen resolution, and touchscreen support to estimate the laptop's price in **euros (€)**.

---

## 🗂️ Project Structure
```text
Laptop-Price-Predictor/
├── backend/
│   ├── Model/
│   │   ├── laptop_price.csv        # Training dataset
│   │   ├── model.pkl               # Trained ML model
│   │   ├── model_training.ipynb    # Model training notebook
│   │   └── predict.py              # Prediction logic
│   ├── Schema/
│   │   └── user_input.py           # Pydantic input validation schema
│   └── app.py                      # FastAPI application
├── frontend/
│   └── index.py                    # Streamlit UI
└── requirements.txt                # Python dependencies
```
---

## ⚙️ Features

- Predicts laptop prices in euros (€)
- Uses hardware and configuration-based features
- CPU family and clock speed extraction
- GPU and CPU brand extraction
- Separate SSD, HDD, Flash, and Hybrid storage features
- Screen resolution converted into width and height
- Touchscreen detection
- Input validation using Pydantic v2
- REST API built with FastAPI
- Interactive prediction interface built with Streamlit
- Health check endpoint for API and model status

---

## 🧠 Model Features

The model uses the following input features:

| Feature | Description |
|---|---|
| `Company` | Laptop manufacturer |
| `TypeName` | Laptop category such as Notebook, Gaming, Ultrabook, etc. |
| `Inches` | Screen size |
| `Ram` | RAM capacity in GB |
| `OpSys` | Operating system |
| `ssd_gb` | SSD capacity in GB |
| `hdd_gb` | HDD capacity in GB |
| `flash_gb` | Flash storage capacity in GB |
| `hybrid_gb` | Hybrid storage capacity in GB |
| `cpu_speed_ghz` | CPU clock speed |
| `cpu_family` | CPU family such as Core i5, Core i7, Ryzen, etc. |
| `cpu_brand` | CPU manufacturer |
| `gpu_brand` | GPU manufacturer |
| `res_width` | Screen resolution width |
| `res_height` | Screen resolution height |
| `is_touchscreen` | Whether the laptop has a touchscreen |

### Target

`Price_euros`

The model predicts the laptop's estimated price in euros.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `pip` or `conda`

### 1. Clone the repository

```bash
git clone https://github.com/JD5505/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI backend

Open a terminal in the project directory:

```bash
cd backend
uvicorn app:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

FastAPI's interactive API documentation will be available at:

`http://127.0.0.1:8000/docs`

### 4. Start the Streamlit frontend

Open a **new terminal** and return to the project directory:

```bash
cd frontend
streamlit run index.py
```

The Streamlit application will open in your browser.

> ⚠️ Make sure the FastAPI backend is running before using the Streamlit frontend. The frontend sends prediction requests to the backend at `http://127.0.0.1:8000/predict`.

---

## 🔌 API Endpoints

### `GET /`

Returns a welcome message.

### `GET /health`

Returns the API status and model information.

Example response:

```json
{
  "status": "OK",
  "version": "1.0.0",
  "Port": "http://127.0.0.1:8000",
  "model loaded": true
}
```

### `POST /predict`

Accepts laptop specifications and returns the predicted price.

**Request body:**

```json
{
  "company": "Dell",
  "typename": "Notebook",
  "inches": 15.6,
  "ram_gb": 16,
  "opsys": "Windows 10",
  "ssd_gb": 512,
  "hdd_gb": 0,
  "flash_gb": 0,
  "hybrid_gb": 0,
  "cpu_speed_ghz": 2.5,
  "cpu_family": "Core i5",
  "cpu_brand": "Intel",
  "gpu_brand": "Nvidia",
  "resolution": "1920x1080",
  "touchscreen": false
}
```

**Response:**

```json
{
  "prediction": 1249.99
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Machine Learning | scikit-learn / XGBoost |
| Hyperparameter Optimization | Optuna |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Validation | Pydantic v2 |
| Data Processing | Pandas / NumPy |

---

## 📊 Model Evaluation

The model is evaluated using standard regression metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**
- **Cross-validation**

The primary evaluation metric is **Mean Absolute Error (MAE)**, which represents the average absolute difference between predicted and actual laptop prices in euros.

---

## 📌 Known Limitations

- The model was trained on a historical laptop-price dataset, so predictions may not reflect current market prices.
- Predictions for laptop configurations significantly different from the training data may be less reliable.
- CPU and GPU information is represented using engineered features rather than complete hardware model specifications.
- Supported laptop brands, operating systems, CPU families, and GPU brands are limited to categories represented in the training dataset.
- The model does not account for factors such as laptop condition, retailer, discounts, availability, or regional pricing.
- Predicted prices should be treated as estimates rather than exact market prices.

---

## 📄 License

This project is for educational purposes. No license applied.