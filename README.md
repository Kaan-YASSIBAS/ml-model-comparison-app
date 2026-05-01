# ML Model Comparison App

![CI](https://github.com/Kaan-YASSIBAS/ml-model-comparison-app/actions/workflows/ci.yml/badge.svg)

An interactive Machine Learning web application for comparing classical ML algorithms on a spam classification dataset.

The project uses **FastAPI**, **scikit-learn**, **TF-IDF**, Docker, Docker Compose, and a simple HTML/CSS/JavaScript frontend.

## Project Overview

This project compares multiple classical Machine Learning algorithms on the same text classification dataset.

The dataset contains SMS messages labeled as:

- `ham` — normal message
- `spam` — unwanted or suspicious message

The application allows users to:

1. Evaluate a single selected model
2. Compare all available models
3. View Accuracy, Precision, Recall, F1 Score
4. View the Confusion Matrix for a selected model

## Tech Stack

- Python
- FastAPI
- Pydantic
- pandas
- scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Linear SVM
- Naive Bayes
- Pytest
- Docker
- Docker Compose
- Nginx
- HTML / CSS / JavaScript
- GitHub Actions

## Project Structure

```text
ml-model-comparison-app/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── ml/
│   │       ├── __init__.py
│   │       ├── dataset.py
│   │       ├── models.py
│   │       └── evaluator.py
│   │
│   ├── data/
│   │   └── spam.csv
│   │
│   ├── tests/
│   │   └── test_api.py
│   │
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   └── pytest.ini
│
├── frontend/
│   ├── index.html
│   ├── evaluate.html
│   ├── compare.html
│   ├── style.css
│   ├── evaluate.js
│   ├── compare.js
│   ├── Dockerfile
│   └── .dockerignore
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Features

- Interactive frontend with separate pages
- Single model evaluation page
- All-model comparison page
- FastAPI backend
- CORS support
- TF-IDF text vectorization
- Multiple classical ML algorithms
- Accuracy, Precision, Recall, F1 Score
- Confusion Matrix output
- Dockerized backend and frontend
- Docker Compose multi-container setup
- Pytest backend API tests
- GitHub Actions CI
- Docker image build checks in CI

## Dataset

This project uses the **SMS Spam Collection Dataset**.

The dataset file should be located at:

```text
backend/data/spam.csv
```

The original dataset usually contains these columns:

| Column | Description |
| --- | --- |
| `v1` | Label: `ham` or `spam` |
| `v2` | SMS message text |

Inside the application, these columns are renamed to:

| Project Column | Description |
| --- | --- |
| `label` | Message class |
| `message` | SMS text |

## Machine Learning Workflow

The application uses the same dataset and train/test split for all models.

General workflow:

```text
SMS message
↓
TF-IDF Vectorizer
↓
Selected ML algorithm
↓
spam / ham classification
↓
Evaluation metrics
```

## Algorithms Compared

The application compares the following algorithms:

| Model | Description |
| --- | --- |
| Logistic Regression | Linear classification model commonly used as a strong baseline |
| K-Nearest Neighbors | Classifies based on nearest examples |
| Decision Tree | Rule-based tree model |
| Random Forest | Ensemble of multiple decision trees |
| Linear SVM | Linear Support Vector Machine, strong for text classification |
| Naive Bayes | Probabilistic model commonly used for spam filtering |

## Evaluation Metrics

The app reports the following metrics:

| Metric | Meaning |
| --- | --- |
| Accuracy | Overall percentage of correct predictions |
| Precision | When the model predicts spam, how often it is actually spam |
| Recall | How many real spam messages the model successfully detects |
| F1 Score | Balance between Precision and Recall |
| Confusion Matrix | Breakdown of correct and incorrect predictions |

## Confusion Matrix Format

The confusion matrix is displayed as:

```text
                 Predicted Ham   Predicted Spam
Actual Ham            TN               FP
Actual Spam           FN               TP
```

For this project:

- `TN`: Ham message correctly predicted as ham
- `FP`: Ham message incorrectly predicted as spam
- `FN`: Spam message incorrectly predicted as ham
- `TP`: Spam message correctly predicted as spam

## Backend API

The backend is built with FastAPI.

### Health Check

```http
GET /health
```

Example response:

```json
{
  "message": "ML Model Comparison API is running"
}
```

### List Available Models

```http
GET /models
```

Example response:

```json
{
  "available_models": [
    {
      "key": "logistic_regression",
      "name": "Logistic Regression"
    },
    {
      "key": "linear_svm",
      "name": "Linear SVM"
    }
  ]
}
```

### Evaluate Single Model

```http
POST /evaluate
```

Request body:

```json
{
  "model_name": "logistic_regression"
}
```

Example response:

```json
{
  "model_key": "logistic_regression",
  "model_name": "Logistic Regression",
  "accuracy": 0.9704,
  "precision": 1.0,
  "recall": 0.7785,
  "f1_score": 0.8755,
  "confusion_matrix": [[966, 0], [33, 116]]
}
```

### Compare All Models Endpoint

```http
GET /compare-all
```

Example response:

```json
{
  "results": [
    {
      "model_key": "linear_svm",
      "model_name": "Linear SVM",
      "accuracy": 0.9848,
      "precision": 0.9925,
      "recall": 0.8926,
      "f1_score": 0.9399,
      "confusion_matrix": [[965, 1], [16, 133]]
    }
  ]
}
```

## Frontend Pages

The frontend has separate pages for each main function.

### Home Page

```text
http://127.0.0.1:8080
```

Provides navigation to:

- Evaluate Single Model
- Compare All Models

### Evaluate Single Model Page

Allows the user to select one algorithm and view:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Compare All Models Page

Runs all available models and displays their metrics in a comparison table.

## Run Locally

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install backend dependencies:

```powershell
pip install -r backend\requirements.txt
```

Run the backend:

```powershell
cd backend
uvicorn app.main:app --reload
```

Backend URLs:

| Service | URL |
| --- | --- |
| API | `http://127.0.0.1:8000` |
| Swagger UI | `http://127.0.0.1:8000/docs` |
| Health Check | `http://127.0.0.1:8000/health` |

To test the frontend locally without Docker, open:

```text
frontend/index.html
```

or use a local static server / Live Server extension.

## Run with Docker Compose

From the project root:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

Stop containers:

```bash
docker compose down
```

Application URLs:

| Service | URL |
| --- | --- |
| Frontend | `http://127.0.0.1:8080` |
| Backend API | `http://127.0.0.1:8000` |
| Swagger UI | `http://127.0.0.1:8000/docs` |
| Health Check | `http://127.0.0.1:8000/health` |

## Running Tests

Go to the backend folder:

```bash
cd backend
```

Run tests:

```bash
python -m pytest -v
```

The tests cover:

- Health check endpoint
- Model list endpoint
- Single model evaluation endpoint
- Invalid model request
- Compare all models endpoint

## Continuous Integration

This project uses GitHub Actions for CI.

The workflow runs automatically on:

- Pushes to the `main` branch
- Pull requests targeting the `main` branch

The CI workflow includes:

### Backend Tests

This job checks whether the backend works correctly.

It performs the following steps:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs backend dependencies from `backend/requirements.txt`
4. Runs backend API tests with Pytest

### Docker Image Build Checks

This job verifies that both services can be containerized.

It builds:

- Backend Docker image
- Frontend Docker image

These steps check that:

- `backend/Dockerfile` is valid
- `frontend/Dockerfile` is valid
- The backend can be packaged as a Docker image
- The frontend can be packaged as a Docker image
- Docker build errors are caught automatically in CI

The CI does not deploy the application. It only verifies that tests pass and Docker images can be built successfully.

Workflow file:

```text
.github/workflows/ci.yml
```

## Example Usage

### Evaluate Logistic Regression

```bash
curl -X POST "http://127.0.0.1:8000/evaluate" \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "logistic_regression"
  }'
```

### Compare All Models

```bash
curl -X GET "http://127.0.0.1:8000/compare-all"
```

## Notes

This project is built for learning purposes.

The main goal is to understand:

```text
Dataset Loading
↓
TF-IDF Feature Extraction
↓
Classical ML Algorithms
↓
Model Evaluation
↓
API Serving
↓
Frontend Visualization
↓
Dockerization
↓
Testing and CI
```

## Future Improvements

- Cache model evaluation results
- Add charts for metric comparison
- Add ROC-AUC scores
- Add model training time comparison
- Add downloadable CSV results
- Add Kubernetes manifests
- Deploy the application to a cloud platform
