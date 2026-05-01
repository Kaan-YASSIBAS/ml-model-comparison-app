from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "message": "ML Model Comparison API is running"
    }


def test_list_models():
    response = client.get("/models")

    assert response.status_code == 200

    data = response.json()

    assert "available_models" in data
    assert isinstance(data["available_models"], list)
    assert len(data["available_models"]) > 0

    model_keys = [model["key"] for model in data["available_models"]]

    assert "logistic_regression" in model_keys
    assert "knn" in model_keys
    assert "decision_tree" in model_keys
    assert "random_forest" in model_keys
    assert "linear_svm" in model_keys
    assert "naive_bayes" in model_keys


def test_evaluate_logistic_regression():
    payload = {
        "model_name": "logistic_regression"
    }

    response = client.post("/evaluate", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["model_key"] == "logistic_regression"
    assert data["model_name"] == "Logistic Regression"

    assert "accuracy" in data
    assert "precision" in data
    assert "recall" in data
    assert "f1_score" in data
    assert "confusion_matrix" in data

    assert 0 <= data["accuracy"] <= 1
    assert 0 <= data["precision"] <= 1
    assert 0 <= data["recall"] <= 1
    assert 0 <= data["f1_score"] <= 1

    assert isinstance(data["confusion_matrix"], list)
    assert len(data["confusion_matrix"]) == 2
    assert len(data["confusion_matrix"][0]) == 2
    assert len(data["confusion_matrix"][1]) == 2


def test_evaluate_invalid_model():
    payload = {
        "model_name": "invalid_model"
    }

    response = client.post("/evaluate", json=payload)

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Model not found"
    }


def test_compare_all_models():
    response = client.get("/compare-all")

    assert response.status_code == 200

    data = response.json()

    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) > 0

    first_result = data["results"][0]

    assert "model_key" in first_result
    assert "model_name" in first_result
    assert "accuracy" in first_result
    assert "precision" in first_result
    assert "recall" in first_result
    assert "f1_score" in first_result
    assert "confusion_matrix" in first_result