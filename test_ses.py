import time
import winsound

# Ses testi başlatılıyor
print("Ses testi başlatılıyor...")

# Bilgisayarın yerleşik winsound kütüphanesi ile ses çalma denemesi
try:
    # Not: ses dosyasının tam yolunu veya test dosyasını burada çağırıyoruz
    winsound.PlaySound("ses.wav", winsound.SND_FILENAME)
    print("Ses başarıyla çalandı!")
except Exception as e:
    print(f"Bir hata yakalandı: {e}")

print("Test tamamlandı.")