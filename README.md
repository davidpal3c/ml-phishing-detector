# Phishing Email Detector 

Machine learning project for detecting phishing emails using text classification. This version is complete with modular code, realistic evaluation metrics, and ready-to-deploy model pipeline.

---

## 📌 Features

- Dataset generation (phishing and legitimate emails)
- Text vectorization with TF-IDF
- Classification with Random Forest
- Evaluation: Accuracy, Confusion Matrix, ROC Curve
- Stratified cross-validation
- Modular code (`main.py`, `utils.py`)
- Prediction function for new messages
- Saved model (`.pkl`)

---

## 🚀 How to Run

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the main script**:
```bash
python main.py
```

## Future Improvements
-- Replace synthetic data with real phishing corpora
-- Deploy using Flask/FastAPI + React frontend
-- Add adversarial robustness checks
-- Compare with deep learning models (BERT, LSTM)