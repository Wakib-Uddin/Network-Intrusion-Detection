# 🛡️ Network Intrusion Detection

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

A reproducible machine-learning pipeline for detecting potentially malicious network activity from structured traffic data.

## 🎯 Problem
Network intrusion detection is a classification problem where traffic records are analyzed to distinguish normal activity from suspicious or malicious behavior. This project emphasizes a clean, reproducible workflow rather than a dataset-specific demo.

## 🔬 Pipeline
```text
CSV → Validation → Cleaning → Train/Test Split → Imputation
    → Encoding/Scaling → Random Forest → Precision/Recall/F1
    → Confusion Matrix
```

## ✨ Engineering Features
- Automatic numeric/categorical feature detection
- Missing-value imputation
- One-hot encoding and feature scaling
- Balanced Random Forest classifier
- Reproducible train/test split
- Standard classification metrics
- Dataset files excluded when redistribution is inappropriate

## 🚀 Run Locally
```bash
git clone https://github.com/Wakib-Uddin/Network-Intrusion-Detection.git
cd Network-Intrusion-Detection
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python train.py --data data/network_traffic.csv --target label
```

Your CSV should contain a target column named `label` plus network traffic features.

## 📊 Evaluation
The training script reports precision, recall, F1-score, and a confusion matrix. For security applications, recall and false-negative behavior deserve special attention because missed attacks can be costly.

## 🧰 Stack
Python · Pandas · NumPy · Scikit-learn · Matplotlib

## 🔐 Data & Ethics
No third-party dataset is redistributed by this repository. Use datasets according to their licenses and analyze only traffic you are authorized to inspect.

## 👨‍💻 Author
**A.M. Wakib Uddin** — CSE Engineer | Python | Machine Learning | Backend

[GitHub](https://github.com/Wakib-Uddin)
