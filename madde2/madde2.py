from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd

# Veri setini yükleme
data = pd.read_csv('diyabetSet.csv')

# Özellikler ve etiketler
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Hedef dizisini düzeltme
y = y.values.ravel()  # Tek boyutlu bir diziye dönüştürme

# PCA modelini oluşturma ve uygulama
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# LDA modelini oluşturma ve uygulama
lda = LinearDiscriminantAnalysis(n_components=min(X.shape[1], len(set(y)) - 1))
X_lda = lda.fit_transform(X, y)

# Ana veri setine PCA ve LDA uygulanması
# Ana veri seti üzerine PCA uygulanmış öznitelik matrisi
X_pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])

# Ana veri seti üzerine LDA uygulanmış öznitelik matrisi
X_lda_df = pd.DataFrame(X_lda, columns=['LD1'])

# PCA ve LDA sonuçlarını birleştirme
result_df = pd.concat([X_pca_df, X_lda_df], axis=1)

# CSV dosyasına yazma
result_df.to_csv('pca_lda_results.csv', index=False)

# Veriyi gösterme
print("PCA ve LDA sonuçları başarıyla 'pca_lda_results.csv' dosyasına kaydedildi.")
