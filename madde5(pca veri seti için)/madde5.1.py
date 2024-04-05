import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Veri setini yükleme
data = pd.read_csv('diyabetSet.csv')

# Bağımsız değişkenler (X) ve bağımlı değişken (y) olarak veriyi ayırma
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Eğitim ve test veri setlerini oluşturma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Naive Bayes sınıflandırıcısını oluşturma ve eğitme
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

# Test verisi üzerinde tahmin yapma
y_pred = naive_bayes.predict(X_test)

# Performans metriklerini hesaplama
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Sonuçları DataFrame'e dönüştürme
results_df = pd.DataFrame({
    'Accuracy': [accuracy],
    'Precision': [precision],
    'Recall': [recall],
    'F1 Score': [f1]
})

# Sonuçları CSV dosyasına kaydetme
results_df.to_csv('naive_bayes_results.csv', index=False)

# Confusion Matrix'i CSV dosyasına kaydetme
conf_matrix_df = pd.DataFrame(conf_matrix, columns=['Predicted Negative', 'Predicted Positive'], index=['Actual Negative', 'Actual Positive'])
conf_matrix_df.to_csv('confusion_matrix.csv')
