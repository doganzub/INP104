# Hafta 7: Dosya İşlemleri

## Konu Özeti

Bu hafta Python'da dosya oluşturma, yazma ve okuma işlemleri incelenmektedir. Dosya işlemleri, programların kalıcı veri saklama ihtiyacını karşılar. Python'da dosya işlemleri `open()` fonksiyonu ve `with` bağlam yöneticisi ile gerçekleştirilir.

---

## Neden Önemli

Programlar çoğunlukla verileri kalıcı olarak saklamak zorundadır. Kullanıcı ayarları, log kayıtları, konfigürasyon dosyaları ve veri dosyaları, dosya işlemleri sayesinde yönetilir. Ayrıca dosya okuma becerisi, mevcut verilerin programa aktarılması için temel bir gerekliliktir.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- Dosya oluşturma ve yazma işlemlerini gerçekleştirebilme
- Dosya okuma yöntemlerini kullanabilme
- `with` ifadesi ile güvenli dosya yönetimi yapabilme
- Farklı dosya modlarını anlama ve kullanabilme
- Temel hata yönetimi uygulayabilme

---

## Konu Başlıkları

### 7.1 Dosya Açma Modları

Python'da dosyalar farklı modlarla açılabilir. Her mod belirli bir işlem için kullanılır.

| Mod | Açıklama | Dosya Yoksa |
|-----|----------|-------------|
| `"r"` | Okuma (varsayılan) | Hata verir |
| `"w"` | Yazma (üzerine yazar) | Oluşturur |
| `"a"` | Ekleme (sona ekler) | Oluşturur |
| `"x"` | Oluşturma (dosya varsa hata) | Oluşturur |

---

### 7.2 Dosya Yazma

**Temel Yazma İşlemi:**

```python
dosya = open("ornek.txt", "w")         # Dosya yazma modunda açılır
dosya.write("Merhaba Dünya!\n")        # Metin dosyaya yazılır
dosya.write("Python öğreniyorum\n")    # İkinci satır yazılır
dosya.close()                          # Dosya kapatılır (önemli!)
```

**Birden Fazla Satır Yazma:**

```python
satirlar = ["Satır 1\n", "Satır 2\n", "Satır 3\n"]  # Yazılacak satırlar
dosya = open("coklu.txt", "w")         # Dosya açılır
dosya.writelines(satirlar)             # Tüm satırlar yazılır
dosya.close()                          # Dosya kapatılır
```

---

### 7.3 Dosya Okuma

**Tüm İçeriği Okuma:**

```python
dosya = open("ornek.txt", "r")         # Dosya okuma modunda açılır
icerik = dosya.read()                  # Tüm içerik okunur
print(icerik)                          # İçerik ekrana yazdırılır
dosya.close()                          # Dosya kapatılır
```

**Satır Satır Okuma:**

```python
dosya = open("ornek.txt", "r")         # Dosya açılır
satir = dosya.readline()               # Tek satır okunur
print(satir)                           # Satır yazdırılır
dosya.close()                          # Dosya kapatılır
```

**Tüm Satırları Liste Olarak Okuma:**

```python
dosya = open("ornek.txt", "r")         # Dosya açılır
satirlar = dosya.readlines()           # Tüm satırlar liste olarak alınır
for satir in satirlar:                 # Her satır işlenir
    print(satir.strip())               # Satır sonu karakteri temizlenerek yazdırılır
dosya.close()                          # Dosya kapatılır
```

---

### 7.4 with İfadesi (Önerilen Yöntem)

`with` ifadesi, dosya işlemlerinde en güvenli yöntemdir. Dosya otomatik olarak kapatılır ve hata durumlarında bile kaynaklar temizlenir.

**Yazma İşlemi:**

```python
with open("notlar.txt", "w") as dosya:  # Dosya with bloğu ile açılır
    dosya.write("Python öğreniyorum\n") # Metin yazılır
    dosya.write("Dosya işlemleri\n")    # İkinci satır yazılır
# Blok bitince dosya otomatik kapatılır
```

**Okuma İşlemi:**

```python
with open("notlar.txt", "r") as dosya:  # Dosya okuma modunda açılır
    icerik = dosya.read()               # Tüm içerik okunur
    print(icerik)                       # İçerik yazdırılır
# Dosya otomatik kapatılır
```

**Ekleme Modu:**

```python
with open("kisiler.txt", "a") as dosya:  # Dosya ekleme modunda açılır
    dosya.write("Yeni kullanıcı\n")      # Dosya sonuna eklenir
# Mevcut içerik korunur, yeni satır eklenir
```

---

### 7.5 Hata Yönetimi

Dosya işlemlerinde `FileNotFoundError` hatası sık karşılaşılan bir durumdur.

```python
try:                                    # Hata yakalama bloğu başlatılır
    with open("olmayan_dosya.txt", "r") as dosya:  # Var olmayan dosya açılmaya çalışılır
        icerik = dosya.read()           # Dosya okunmaya çalışılır
except FileNotFoundError:               # Dosya bulunamazsa bu blok çalışır
    print("Dosya bulunamadı!")          # Kullanıcıya bilgi verilir
```

---

### 7.6 Pratik Uygulama: Not Defteri

```python
def not_ekle(dosya_adi, not_metni):    # Not ekleme fonksiyonu tanımlanır
    with open(dosya_adi, "a") as dosya: # Dosya ekleme modunda açılır
        dosya.write(not_metni + "\n")   # Not dosyaya eklenir

def notlari_oku(dosya_adi):            # Notları okuma fonksiyonu tanımlanır
    try:                                # Hata yakalama bloğu
        with open(dosya_adi, "r") as dosya:  # Dosya okuma modunda açılır
            return dosya.read()         # İçerik döndürülür
    except FileNotFoundError:           # Dosya yoksa
        return "Henüz not yok."         # Bilgi mesajı döndürülür

# Kullanım
not_ekle("notlarim.txt", "Python öğreniyorum")  # Not eklenir
print(notlari_oku("notlarim.txt"))      # Notlar ekrana yazdırılır
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `07-dosya-islemleri.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. Kullanıcıdan alınan metinleri bir dosyaya kaydeden program yazınız.
2. Bir metin dosyasındaki satır sayısını bulan program yazınız.
3. İki farklı dosyanın içeriğini birleştiren program yazınız.
4. Dosyadaki belirli bir kelimeyi başka bir kelime ile değiştiren program yazınız.
