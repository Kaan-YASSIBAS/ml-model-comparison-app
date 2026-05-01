from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from app.ml.dataset import get_train_test_data
from app.ml.models import get_model_by_name, get_models


def build_pipeline(classifier):
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            max_features=5000
        )),
        ("classifier", classifier)
    ])


def evaluate_single_model(model_name: str):
    model_info = get_model_by_name(model_name)

    if model_info is None:
        return None

    X_train, X_test, y_train, y_test = get_train_test_data()

    pipeline = build_pipeline(model_info["model"])
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    cm = confusion_matrix(y_test, predictions, labels=["ham", "spam"])

    return {
        "model_key": model_name,
        "model_name": model_info["display_name"],
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, pos_label="spam", zero_division=0),
        "recall": recall_score(y_test, predictions, pos_label="spam", zero_division=0),
        "f1_score": f1_score(y_test, predictions, pos_label="spam", zero_division=0),
        "confusion_matrix": cm.tolist()
    }


def compare_all_models():
    results = []

    for model_name in get_models().keys():
        result = evaluate_single_model(model_name)

        if result is not None:
            results.append(result)

    results = sorted(
        results,
        key=lambda item: item["f1_score"],
        reverse=True
    )

    return results