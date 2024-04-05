import pandas as pd
from sklearn.decomposition import PCA

# Veri setini yükleme
data = pd.read_csv('diyabetSet.csv')

# PCA modelini oluşturma
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data)

# PCA sonuçlarını bir veri çerçevesine dönüştürme
pca_result = pd.DataFrame(data=data_pca, columns=['Bileşen 1', 'Bileşen 2'])

# Öz değerleri alma
oz_degerler = pca.explained_variance_ratio_

# Sonuç sütununu tekrar ekleyerek tam bir veri çerçevesi oluşturma
# Diyabet veri setindeki hedef değişkenin adını doğru şekilde belirtin
pca_result['Outcome'] = data['Outcome']

# Veri çerçevesini CSV dosyasına kaydetme
pca_result.to_csv('pca_sonucları.csv', index=False)

# Oluşturulan dosyanın yolu
print("PCA sonuçları başarıyla 'pca_sonucları.csv' dosyasına kaydedildi.")
