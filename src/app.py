# app.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data from a CSV file
csv_path = './data/data.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_path)

# Assume the CSV file has a 'target' column and the rest are features
features = df.drop('target', axis=1)
target = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a random forest classifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Print accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"len: {len(df)}")