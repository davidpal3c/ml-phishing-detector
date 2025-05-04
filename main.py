import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, RocCurveDisplay
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from utils import generate_dataset, classify_message

# 1. Generate or load dataset
df = generate_dataset(size=10000)

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, stratify=df['label'], random_state=42)

# 3. Build pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', RandomForestClassifier(n_estimators=100, class_weight='balanced'))
])

# 4. Train model
pipeline.fit(X_train, y_train)

# 5. Evaluate model
y_pred = pipeline.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy Score: {accuracy:.2f}")

# 6. Cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')
print("\nCross-Validation Scores:", cv_scores)
print(f"Mean CV Accuracy: {cv_scores.mean():.2f}")

# 7. ROC Curve
RocCurveDisplay.from_estimator(pipeline, X_test, y_test)
plt.title("ROC Curve")
plt.show()

# 8. Save model
joblib.dump(pipeline, 'phishing_detector_model.pkl')

# 9. Classify test message
test_msg = "Subject: Urgent: Account Verification Required\n\nClick here: http://banck.com/verify"
print(f"\nTest message classification: {classify_message(pipeline, test_msg)}")
