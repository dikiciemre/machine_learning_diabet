# Diabetes Veri Seti Normalizasyonu

Bu proje, bir diyabet veri setinin min-max normalizasyonu işlemini gerçekleştiren bir Python betiğini içermektedir. Min-max normalizasyonu, veri setindeki değerleri belirli bir aralığa ölçeklendirir ve veri setinin tüm özniteliklerinin aynı ölçekte olmasını sağlar.

## Kullanım

1. Öncelikle, pandas kütüphanesini yükleyin. Eğer bilgisayarınızda pandas yüklü değilse aşağıdaki komutu kullanabilirsiniz:

2. Projenin ana dizininde `diyabetSet.csv` adında bir veri seti dosyası olmalıdır. Bu dosya, diyabet hastalarının özelliklerini ve sonuçlarını içermelidir.

3. Ardından, `diabetes_normalization.py` dosyasını çalıştırın. Bu dosya, veri setini yükleyecek, min-max normalizasyonunu uygulayacak ve sonuçları `normalized_diabetes.csv` adında yeni bir CSV dosyasına kaydedecektir.

## İçeriğin Açıklaması

- `diabetes_normalization.py`: Ana betik dosyasıdır. Bu dosya, veri setini yükler, min-max normalizasyonunu uygular ve sonuçları kaydeder.

- `diyabetSet.csv`: Kullanılacak diyabet veri seti.

- `normalized_diabetes.csv`: Normalizasyon işlemi sonucunda oluşturulan yeni CSV dosyası.

## Min-Max Normalizasyonu

Min-max normalizasyonu, veri setinin değerlerini belirli bir aralığa (genellikle [0, 1] veya [-1, 1]) dönüştürmek için kullanılan bir ölçekleme yöntemidir. Bu yöntemde, her bir değer, o sütundaki minimum ve maksimum değerlere göre yeniden ölçeklendirilir.

Formül:

Burada:
- `X_normalized`: Normalize edilmiş değer
- `X`: Orijinal değer
- `X_min`: Sütundaki minimum değer
- `X_max`: Sütundaki maksimum değer

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.
