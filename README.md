# 💻 Laptop Price Predictor

A machine learning web application that predicts laptop prices based on hardware specifications and configuration. Built with a **FastAPI** backend and a **Streamlit** frontend.

---

## 🗂️ Project Structure

```
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

- Predicts laptop price based on brand, specs, and configuration
- Input validation using Pydantic schemas
- REST API built with FastAPI
- Interactive UI built with Streamlit
- Health check endpoint for monitoring

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

```bash
cd backend
uvicorn app:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### 4. Start the Streamlit frontend

Open a **new terminal**, then:

```bash
cd frontend
streamlit run index.py
```

> ⚠️ The backend **must be running** before you launch the frontend. The UI calls the API on port `8000`.

---

## 🔌 API Endpoints

### `GET /`
Returns a welcome message.

### `GET /health`
Returns the API status and model info.

```json
{
  "status": "OK",
  "version": "1.0.0",
  "Port": "http://127.0.0.1:8000",
  "model loaded": true
}
```

### `POST /predict`
Accepts laptop specs and returns a predicted price.

**Request body example:**
```json
{
  "company": "Dell",
  "typename": "Ultrabook",
  "inches": 14.0,
  "ram_gb": "16GB",
  "opsys": "Windows 10",
  "resolution": "1920x1080",
  "touchscreen": false,
  "memory": "SSD",
  "cpu_brand": "Intel",
  "gpu_brand": "Nvidia"
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
| ML Model | scikit-learn / XGBoost |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Validation | Pydantic v2 |
| Data | Pandas |

---

## 📌 Known Limitations

- The model was trained on a dataset with limited laptop brands and configurations — predictions outside the training distribution may be unreliable.
- Memory type is simplified to SSD, HDD, or Flash Drive only (no hybrid support).
- GPU/CPU options are limited to brands present in the training data.

---

## 📄 License

This project is for educational purposes. No license applied.
