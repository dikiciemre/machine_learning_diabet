import pandas as pd  # Pandas kütüphanesini içe aktar

# Veri setini yükleyelim
data = pd.read_csv('diyabetSet.csv')

# Min-Max normalizasyonu fonksiyonu
def min_max_normalization(column):
    # Sütunun minimum ve maksimum değerlerini bul
    min_val = column.min()
    max_val = column.max()
    # Normalizasyon formülünü uygula ve normalize edilmiş sütunu döndür
    normalized_column = (column - min_val) / (max_val - min_val)
    return normalized_column

# 'Outcome' sütununu ayrı bir değişkende saklayalım
outcome_column = data['Outcome']

# 'Outcome' sütununu veri setinden çıkaralım
data.drop(columns=['Outcome'], inplace=True)

# Tüm sütunları normalize edelim
normalized_data = data.apply(min_max_normalization, axis=0)

# 'Outcome' sütununu normalize edilmiş veri setine geri ekleyelim
normalized_data['Outcome'] = outcome_column

# Normalize edilmiş veriyi yeni bir CSV dosyası olarak kaydetme
normalized_data.to_csv('normalized_diabetes.csv', index=False)
