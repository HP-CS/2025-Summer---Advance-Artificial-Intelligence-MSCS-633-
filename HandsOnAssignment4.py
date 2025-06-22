import pandas as pd
from pyod.models.auto_encoder import AutoEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score

df = pd.read_csv("creditcard.csv")
df.drop(['Time'], axis=1, inplace=True)

scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])

X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = AutoEncoder(hidden_neurons=[32, 16, 32], epochs=30, batch_size=32, contamination=0.001)
clf.fit(X_train)

y_test_scores = clf.decision_function(X_test)
y_test_pred = clf.predict(X_test)

print("ROC AUC:", roc_auc_score(y_test, y_test_scores))
print(classification_report(y_test, y_test_pred))
