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
