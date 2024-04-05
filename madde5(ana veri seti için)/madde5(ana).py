import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Veri setini yükleme
data = pd.read_csv('diyabetSet.csv')

# Bağımsız değişkenler (X) ve bağımlı değişken (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Veri setini eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Naive Bayes modelini oluşturma ve eğitme
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

# Test verisi üzerinde tahmin yapma
y_pred = naive_bayes.predict(X_test)

# Confusion matrix hesaplama
conf_matrix = confusion_matrix(y_test, y_pred)

# Sensitivity (Duyarlılık) ve Specificity (Özgüllük) hesaplama
tn, fp, fn, tp = conf_matrix.ravel()
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)

# Accuracy hesaplama
accuracy = (tp + tn) / (tp + tn + fp + fn)

# Precision, Recall ve F1 Score hesaplama
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Sonuçları DataFrame'e dönüştürme
results_df = pd.DataFrame({
    'Metric': ['Sensitivity', 'Specificity', 'Accuracy', 'Precision', 'Recall', 'F1 Score'],
    'Score': [sensitivity, specificity, accuracy, precision, recall, f1]
})

# Sonuçları CSV dosyasına kaydetme
results_df.to_csv('naive_bayes_metrics.csv', index=False)
