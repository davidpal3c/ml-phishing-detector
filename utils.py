# phishing_detector_portfolio/utils.py

import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Generate synthetic phishing and legitimate emails
def generate_dataset(size=10000):
    texts = []
    labels = []

    phishing_keywords = [
        "verify", "account", "bank", "urgent", "click", "password", "login", "suspicious",
        "update", "security", "confirm", "immediately", "action required", "unauthorized access",
        "limited time", "win", "prize", "free", "offer", "expire"
    ]

    legitimate_themes = [
        "newsletter", "order confirmation", "social media notification", "promotion",
        "account summary", "shipping update", "event invitation", "software update"
    ]

    for _ in range(size):
        is_phishing = random.choice([0, 1])

        if is_phishing:
            subject = random.choice([
                "Urgent: Account Verification Required",
                "Immediate Action Required: Unauthorized Login Attempt",
                "Your Account Has Been Compromised",
                "Limited Time Offer: Claim Your Prize Now!",
                "Security Alert: Update Your Password Immediately"
            ])
            body = f"Click here: http://{random.choice(['secure', 'login', 'update'])}-{random.choice(['bank', 'paypal', 'amazon'])}.com?id={random.randint(1000,9999)}"
            email = f"Subject: {subject}\n\n{body}"
            labels.append(1)
        else:
            theme = random.choice(legitimate_themes)
            subject = f"{theme.title()} Notification"
            body = f"Check out our update at http://{theme.replace(' ', '')}.company.com"
            email = f"Subject: {subject}\n\n{body}"
            labels.append(0)

        texts.append(email)

    return pd.DataFrame({'text': texts, 'label': labels})

# Message classification

def classify_message(model, message):
    vec_layer = model.named_steps['tfidf']
    clf = model.named_steps['clf']
    message_vec = vec_layer.transform([message])
    prediction = clf.predict(message_vec)
    return "Phishing" if prediction[0] == 1 else "Not Phishing"
