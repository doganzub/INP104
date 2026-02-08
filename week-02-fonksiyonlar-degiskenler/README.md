# Hafta 2: Gömülü Fonksiyonlar ve Değişkenler

## Konu Özeti

Bu hafta Python'un gömülü fonksiyonları ve değişken kavramı ele alınmaktadır. Değişken tanımlama, kullanıcıdan veri alma, tip dönüşümleri ve metin biçimlendirme konuları işlenmektedir.

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- Değişken kavramını anlayacak ve doğru isimlendirme kurallarını uygulayabilecektir
- `input()` fonksiyonu ile kullanıcıdan veri alabilecektir
- Tip dönüşüm fonksiyonlarını (`int()`, `float()`, `str()`) kullanabilecektir
- `format()` ve f-string ile metin biçimlendirme yapabilecektir
- `round()` ve `bool()` fonksiyonlarını kullanabilecektir

---

## Konu Başlıkları

### 2.1 Değişkenler

Python'da bir program içinde değerlere verilen isimlere **değişken** denir. Değişkenler, verileri geçici olarak bellekte saklar.

```python
# Değişken tanımlama
isim = "Züber"
yas = 46
```

**İsimlendirme Kuralları:**
- Sayı ile başlayamaz (`1isim` ❌)
- Boşluk içeremez (`kullanici adi` ❌)
- Özel karakterler kullanılamaz (`toplam-fiyat` ❌)

---

### 2.2 input() Fonksiyonu

Kullanıcıdan veri almak için kullanılır. **Her zaman string döndürür!**

```python
isim = input("Adınızı girin: ")
print("Merhaba", isim)
```

---

### 2.3 Tip Dönüşümleri

`input()` string döndürdüğü için matematiksel işlemler için tip dönüşümü gerekir.

| Fonksiyon | İşlev | Örnek |
|-----------|-------|-------|
| `int()` | Tam sayıya çevirir | `int("23")` → `23` |
| `float()` | Ondalıklı sayıya çevirir | `float("23.5")` → `23.5` |
| `str()` | Karakter dizisine çevirir | `str(2024)` → `"2024"` |

```python
# input ile matematik
sayi = input("Sayı girin: ")
sonuc = int(sayi) * 2  # Tip dönüşümü gerekli!
```

---

### 2.4 format() ve f-string

**format() Metodu:**
```python
print("{} yaşında".format(46))  # 46 yaşında
```

**f-string (Önerilen):**
```python
yas = 46
print(f"{yas} yaşında")  # 46 yaşında
```

---

### 2.5 round() ve bool() Fonksiyonları

**round():** Ondalıklı sayıları yuvarlar
```python
pi = 22/7
print(round(pi, 2))  # 3.14
```

**bool():** Boolean değere dönüştürür
```python
print(bool(0))   # False
print(bool(1))   # True
print(bool(""))  # False (boş string)
```

---

## Alıştırma Görevleri

Notebook'un sonunda iki ek kod hücresi bulunmaktadır:

### 🟩 Görevler (Cell 33)

Derste işlenen tüm konuların benzeri alıştırmalar. Öğrenci `???` işaretlerinin yerine doğru kodları yazar.

| Görev | Konu |
|-------|------|
| Görev 1 | Değişken tanımlama ve işlem yapma |
| Görev 2 | Birden fazla değişken tanımlama |
| Görev 3 | Çoklu değer atama |
| Görev 4 | Değişken değerlerini takas etme (swap) |
| Görev 5 | input() fonksiyonu – Temel kullanım |
| Görev 6 | input() fonksiyonu – String döndürme kontrolü |
| Görev 7 | input() ile hesaplama yapma |
| Görev 8 | int() – String'i tam sayıya çevirme |
| Görev 9 | float() – String'i ondalıklı sayıya çevirme |
| Görev 10 | str() – Sayıyı karakter dizisine çevirme |
| Görev 11 | Tip dönüşümü ile doğru işlem yapma |
| Görev 12 | format() metodu |
| Görev 13 | format() ile indeks kullanımı |
| Görev 14 | f-string kullanımı |
| Görev 15 | f-string içinde ifade kullanımı |
| Görev 16 | round() fonksiyonu |
| Görev 17 | bool() fonksiyonu |
| Görev 18 | Pratik Örnek – Elektrik faturası hesaplama |
| Görev 19 | Pratik Örnek – Dikdörtgen alan hesaplama (input ile) |

### 🟨 Cevap Anahtarı (Cell 34)

Yukarıdaki görevlerin tamamlanmış çözümleri.

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `02-fonksiyonlar-degiskenler.ipynb` | Haftalık ders notebooku - Detaylı açıklamalar ve inline yorumlar içerir |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Python Resmi Dokümantasyonu: https://docs.python.org/3/

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
