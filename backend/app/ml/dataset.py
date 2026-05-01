from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parents[2]  # Adjust this if your directory structure is different
DATA_PATH = BASE_DIR / "data" / "spam.csv"


def load_spam_dataset():
    df = pd.read_csv(DATA_PATH, encoding="latin-1")

    df = df[["v1", "v2"]]
    df.columns = ["label", "message"]

    return df


def get_train_test_data():
    df = load_spam_dataset()

    X = df["message"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y  # Ensure the split maintains the same proportion of classes in both sets
    )

    return X_train, X_test, y_train, y_test