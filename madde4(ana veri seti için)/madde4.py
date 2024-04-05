import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt

# Veri setini yükleme
data = pd.read_csv('diyabetSet.csv')

# Bağımsız değişkenler (X) ve bağımlı değişken (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Veri setini eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Karar ağacı sınıflandırma modelini oluşturma ve eğitme
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)

# Test verisi üzerinde tahmin yapma
y_pred = decision_tree.predict(X_test)

# Performans metriklerini hesaplama
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Performans metriklerini bir veri çerçevesine kaydetme
performance_metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score'],
    'Score': [accuracy, precision, recall, f1]
})

# Performans metriklerini bir CSV dosyasına kaydetme
performance_metrics.to_csv('performance_metrics_decision_tree.csv', index=False)

# Confusion matrix'i de bir CSV dosyasına kaydetme
confusion_matrix_df = pd.DataFrame(conf_matrix, columns=['Predicted Negative', 'Predicted Positive'], index=['Actual Negative', 'Actual Positive'])
confusion_matrix_df.to_csv('confusion_matrix_decision_tree.csv')

# Karar ağacı modelini görselleştirme (daha büyük boyutta)
plt.figure(figsize=(30,20))  
plot_tree(decision_tree, feature_names=list(X.columns), class_names=['No Diabetes', 'Diabetes'], filled=True,fontsize=7)
plt.savefig('decision_tree_structure.png')
plt.show()

print("Performans metrikleri, confusion matrix ve karar ağacı yapısı başarıyla CSV dosyalarına ve bir PNG dosyasına kaydedildi.")
