import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Veri setlerini yükleme
pca_data = pd.read_csv('pca_sonucları.csv', index_col=0)  # İndeks sütunu olduğunu varsayıyorum
data = pd.read_csv('diyabetSet.csv')

# PCA bileşenlerini kullanarak yeni bir veri çerçevesi oluşturma
pca_df = pca_data.iloc[:, :2]  # İlk iki sütunu seçin

# Eğitim ve test veri setlerini oluşturma
X_train, X_test, y_train, y_test = train_test_split(pca_df, data['Outcome'], test_size=0.30, random_state=42)

# Karar ağacı sınıflandırıcı modelini oluşturma ve eğitme
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)

# Test verisi üzerinde tahmin yapma
y_pred = decision_tree.predict(X_test)

# Doğruluk değerini hesaplama
accuracy = accuracy_score(y_test, y_pred)
print("Karar Ağacı Doğruluğu (Test):", accuracy)

# Ağaç yapısını görselleştirme
plt.figure(figsize=(10, 8))
plot_tree(decision_tree, feature_names=pca_df.columns.tolist(), class_names=['No Diabetes', 'Diabetes'], filled=True, fontsize=10) # feature_names parametresi düzeltildi
plt.savefig('decision_tree_structure_pca.png')
plt.show()

# Performans metriklerini bir CSV dosyasına kaydetme
output_df = pd.DataFrame({'Decision_Tree_Accuracy_Test': [accuracy]})
output_df.to_csv('model_performance_decision_tree_pca.csv', index=False)
