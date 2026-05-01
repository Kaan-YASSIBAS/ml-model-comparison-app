from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.ml.evaluator import evaluate_single_model, compare_all_models
from app.ml.models import get_models


app = FastAPI(title="ML Model Comparison API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ModelEvaluationRequest(BaseModel):
    model_name: str = Field(
        ...,
        description="Model key to evaluate. Example: logistic_regression, knn, decision_tree, random_forest, linear_svm, naive_bayes"
    )


@app.get("/health")
def health_check():
    return {
        "message": "ML Model Comparison API is running"
    }


@app.get("/models")
def list_models():
    models = get_models()

    return {
        "available_models": [
            {
                "key": key,
                "name": value["display_name"]
            }
            for key, value in models.items()
        ]
    }


@app.post("/evaluate")
def evaluate_model(request: ModelEvaluationRequest):
    result = evaluate_single_model(request.model_name)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    return result


@app.get("/compare-all")
def compare_models():
    return {
        "results": compare_all_models()
    }