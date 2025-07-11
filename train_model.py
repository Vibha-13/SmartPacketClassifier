# train_model.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Dummy training data
data = {
    'Flow Duration': [10000, 50000, 30000, 70000],
    'Total Fwd Packets': [10, 22, 15, 30],
    'Total Backward Packets': [8, 18, 12, 25],
    'Fwd Packet Length Mean': [200, 512.3, 350, 600],
    'Bwd Packet Length Mean': [180, 486.7, 320, 550],
    'Label': ['Normal', 'Video Stream', 'Normal', 'Suspicious']
}

df = pd.DataFrame(data)

X = df.drop('Label', axis=1)
y = df['Label']

model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
with open('packet_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'packet_model.pkl'")
