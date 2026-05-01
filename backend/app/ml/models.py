from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB


def get_models():
    return {
        "logistic_regression": {
            "display_name": "Logistic Regression",
            "model": LogisticRegression(max_iter=1000)
        },
        "knn": {
            "display_name": "K-Nearest Neighbors",
            "model": KNeighborsClassifier(n_neighbors=5)
        },
        "decision_tree": {
            "display_name": "Decision Tree",
            "model": DecisionTreeClassifier(random_state=42)
        },
        "random_forest": {
            "display_name": "Random Forest",
            "model": RandomForestClassifier(n_estimators=100, random_state=42)
        },
        "linear_svm": {
            "display_name": "Linear SVM",
            "model": LinearSVC(random_state=42)
        },
        "naive_bayes": {
            "display_name": "Naive Bayes",
            "model": MultinomialNB()
        }
    }


def get_model_by_name(model_name: str):
    models = get_models()

    if model_name not in models:
        return None

    return models[model_name]