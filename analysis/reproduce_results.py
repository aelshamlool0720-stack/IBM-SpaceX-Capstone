"""Reproduce the four-model Falcon 9 landing comparison from IBM course datasets.
Requires pandas, scikit-learn, numpy and an internet connection.
Execute: python analysis/reproduce_results.py
The 90-row modeling dataset is distinct from the 56-row Dash and 101-row SQL samples.
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, balanced_accuracy_score

ROOT = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/"
features = pd.read_csv(ROOT + "dataset_part_3.csv")
targets = pd.read_csv(ROOT + "dataset_part_2.csv")["Class"].astype(int)
assert len(features) == len(targets) == 90
X_train, X_test, y_train, y_test = train_test_split(
    features, targets, test_size=0.2, random_state=2
)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
candidates = {
    "Logistic regression": (LogisticRegression(max_iter=2000, random_state=2), {"model__C": [0.01, 0.1, 1, 10]}),
    "SVM": (SVC(), {"model__kernel": ["linear", "rbf"], "model__C": [0.1, 1, 10], "model__gamma": ["scale", 0.01]}),
    "Decision tree": (DecisionTreeClassifier(random_state=2), {"model__max_depth": [2, 4, 6, None], "model__min_samples_leaf": [1, 2, 4]}),
    "KNN": (KNeighborsClassifier(), {"model__n_neighbors": [3, 5, 7, 9], "model__weights": ["uniform", "distance"]})
}
results = {}
for name, (model, grid) in candidates.items():
    pipe = Pipeline([("scaler", StandardScaler()), ("model", model)])
    fit = GridSearchCV(pipe, grid, cv=cv, scoring="accuracy", n_jobs=1)
    fit.fit(X_train, y_train)
    predicted = fit.predict(X_test)
    results[name] = {
        "cross_validation_accuracy": float(fit.best_score_),
        "test_accuracy": float(accuracy_score(y_test, predicted)),
        "test_balanced_accuracy": float(balanced_accuracy_score(y_test, predicted)),
        "confusion_matrix": confusion_matrix(y_test, predicted, labels=[0, 1]).tolist(),
        "best_parameters": fit.best_params_
    }
    print(f"{name}: held-out={results[name]['test_accuracy']:.1%}; CV={fit.best_score_:.1%}")
Path("analysis").mkdir(exist_ok=True)
Path("analysis/model_results.json").write_text(json.dumps(results, indent=2))
print("Saved analysis/model_results.json")
