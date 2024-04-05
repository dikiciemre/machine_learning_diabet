import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Veri setini yükleme
data = pd.read_csv('pca_sonucları.csv')

# Özellikler ve etiketler
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Veriyi rastgele olarak %70 eğitim ve %30 test olacak şekilde ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Multinominal Lojistik Regresyon modelini oluşturma ve eğitme
logistic_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs')
logistic_reg.fit(X_train, y_train)

# Test kümesi için tahminler
logistic_reg_predictions = logistic_reg.predict(X_test)

# Confusion matrix
conf_matrix = confusion_matrix(y_test, logistic_reg_predictions)
conf_matrix_df = pd.DataFrame(conf_matrix, columns=['Predicted Negative', 'Predicted Positive'], index=['Actual Negative', 'Actual Positive'])
conf_matrix_df.to_csv('confusion_matrix.csv')

# Sınıflandırma raporu
class_report = classification_report(y_test, logistic_reg_predictions, output_dict=True)
class_report_df = pd.DataFrame(class_report).transpose()
class_report_df.to_csv('classification_report.csv')

# Sensitivity, specificity, accuracy ve F1-score hesaplama
tn, fp, fn, tp = conf_matrix.ravel()
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
accuracy = (tp + tn) / (tp + tn + fp + fn)
f1_score = 2 * (sensitivity * (1 - specificity)) / (sensitivity + (1 - specificity))

metrics_data = {'Metric': ['Sensitivity', 'Specificity', 'Accuracy', 'F1-Score'],
                'Value': [sensitivity, specificity, accuracy, f1_score]}
metrics_df = pd.DataFrame(metrics_data)
metrics_df.to_csv('performance_metrics.csv', index=False)

print("Confusion matrix, classification report ve performance metrics başarıyla CSV dosyalarına kaydedildi.")
