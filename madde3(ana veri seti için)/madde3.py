import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Veri setini yükleme
data = pd.read_csv('diyabetSet.csv')

# Bağımsız değişkenler (X) ve bağımlı değişken (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Veri setini eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Çoklu Doğrusal Regresyon modelini eğitme
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# Multinominal Lojistik Regresyon modelini eğitme
logistic_reg = LogisticRegression(max_iter=1000)
logistic_reg.fit(X_train, y_train)

# Test kümesi için performans metriklerini hesaplama
linear_reg_predictions = linear_reg.predict(X_test)
linear_reg_rmse = mean_squared_error(y_test, linear_reg_predictions, squared=False)

logistic_reg_predictions = logistic_reg.predict(X_test)
logistic_reg_accuracy = accuracy_score(y_test, logistic_reg_predictions)

# Konfüzyon matrisi hesaplama
conf_matrix = confusion_matrix(y_test, logistic_reg_predictions)

# Hassasiyet, özgüllük ve F1 skoru hesaplama
precision = precision_score(y_test, logistic_reg_predictions)
recall = recall_score(y_test, logistic_reg_predictions)
f1 = f1_score(y_test, logistic_reg_predictions)

# Sonuçları bir DataFrame'e dönüştürme
results = pd.DataFrame({
    'Model': ['Çoklu Doğrusal Regresyon', 'Multinominal Lojistik Regresyon'],
    'Test Kümesi Performans Metrikleri': [linear_reg_rmse, logistic_reg_accuracy],
    'Konfüzyon Matrisi': [conf_matrix, ''],
    'Hassasiyet (Precision)': [precision, ''],
    'Özgüllük (Recall)': [recall, ''],
    'F1 Skoru': [f1, '']
})

# Sonuçları CSV dosyasına yazma
results.to_csv('classification_results.csv', index=False)

print("Sonuçlar başarıyla 'classification_results.csv' dosyasına kaydedildi.")
