"""Train and evaluate an intrusion-detection classifier.

Expected CSV columns: numeric network features + a target column named `label`.
The script automatically encodes non-numeric features and reports standard metrics.
"""
from pathlib import Path
import argparse
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier


def build_pipeline(X: pd.DataFrame) -> Pipeline:
    numeric = X.select_dtypes(include="number").columns
    categorical = X.select_dtypes(exclude="number").columns
    preprocessor = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]), numeric),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]), categorical),
    ])
    return Pipeline([
        ("preprocess", preprocessor),
        ("model", RandomForestClassifier(n_estimators=250, random_state=42, class_weight="balanced")),
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Train an intrusion detection model")
    parser.add_argument("--data", default="data/network_traffic.csv")
    parser.add_argument("--target", default="label")
    args = parser.parse_args()

    path = Path(args.data)
    if not path.exists():
        raise SystemExit(f"Dataset not found: {path}. Add a licensed CSV to data/ first.")

    df = pd.read_csv(path).dropna(axis=1, how="all")
    if args.target not in df.columns:
        raise SystemExit(f"Target column '{args.target}' not found. Available: {list(df.columns)}")

    X = df.drop(columns=[args.target])
    y = df[args.target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y if y.nunique() > 1 else None
    )

    pipeline = build_pipeline(X)
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))


if __name__ == "__main__":
    main()
