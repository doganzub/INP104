# Hafta 1: Python'a Giriş

## Konu Özeti

Bu hafta Python programlama diline giriş yapılmaktadır. `print()` fonksiyonu, tırnak kullanımı, temel veri tipleri ve gömülü fonksiyonlar ele alınmaktadır. Tüm açıklamalar Python Referans Belgesi kaynak alınarak hazırlanmıştır.

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- `print()` fonksiyonunu ve parametrelerini (`sep`, `end`) kullanabilecektir
- Tek tırnak, çift tırnak ve üç tırnak arasındaki farkları kavrayacaktır
- Temel veri tiplerini (`str`, `int`, `float`) tanıyacak ve ayırt edebilecektir
- `type()` ve `len()` gömülü fonksiyonlarını doğru kullanabilecektir
- Kaçış dizilerini (`\n`, `\t`, `\'`, `\"`) uygulayabilecektir

---

## Konu Başlıkları

### 1.1 print() Fonksiyonu

`print()` fonksiyonu, Python'da ekrana çıktı vermemizi sağlayan temel fonksiyondur. Etkileşimli kabukta doğrudan yazdığımız ifadeler görünse de, program dosyalarında `print()` olmadan çıktı alınamaz.

```python
# Temel kullanım
print("Merhaba Dünya!")

# Birden fazla parametre
print("Python", "Programlama", "Dili")  # Parametreler boşlukla birleştirilir
```

---

### 1.2 Tırnak Kullanımı

Python'da karakter dizisi tanımlamak için üç farklı tırnak seçeneği sunulur:

| Tırnak Tipi | Kullanım | Örnek |
|-------------|----------|-------|
| **Tek tırnak** | Basit metinler | `'Merhaba Python'` |
| **Çift tırnak** | İçinde kesme işareti olan metinler | `"İstanbul'un havası"` |
| **Üç tırnak** | Çok satırlı metinler | `"""Uzun metin..."""` |

**Önemli Kural:** Karakter dizisini hangi tırnakla başlatırsak, o tırnakla bitirmeliyiz.

---

### 1.3 Veri Tipleri

| Veri Tipi | Python Kodu | Örnek | Açıklama |
|-----------|-------------|-------|----------|
| **Karakter Dizisi** | `str` | `"Züber Doğan"` | Metin verileri |
| **Tam Sayı** | `int` | `1978` | Ondalık kısmı olmayan sayılar |
| **Ondalıklı Sayı** | `float` | `73.3` | Kesirli sayılar |

```python
isim = "Züber Doğan"  # str
yil = 1978            # int
kilo = 73.3           # float
```

---

### 1.4 type() ve len() Fonksiyonları

**type() Fonksiyonu:** Verinin tipini döndürür.
```python
print(type("Merhaba"))  # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
```

**len() Fonksiyonu:** Karakter dizisinin uzunluğunu verir.
```python
metin = "Python"
print(len(metin))  # 6

# Sayının basamak sayısı
sayi = 12345
print(len(str(sayi)))  # 5 (önce str'e çevrilmeli)
```

---

### 1.5 print() Özel Parametreleri

**sep Parametresi:** Parametreler arası ayırıcı (varsayılan: boşluk)
```python
print("A", "B", "C", sep="-")  # A-B-C
print("A", "B", "C", sep="")   # ABC (boşluksuz)
```

**end Parametresi:** Satır sonu karakteri (varsayılan: `\n`)
```python
print("Merhaba", end=" ")
print("Dünya")  # Çıktı: Merhaba Dünya (aynı satırda)
```

---

### 1.6 Kaçış Dizileri

| Kaçış Dizisi | Anlamı |
|--------------|--------|
| `\n` | Yeni satır |
| `\t` | Sekme (tab) |
| `\\` | Ters eğik çizgi |
| `\'` | Tek tırnak |
| `\"` | Çift tırnak |

```python
print("Satır 1\nSatır 2")  # İki satır
print("İsim\tYaş")         # Sekmeli
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `01-python-giris.ipynb` | Haftalık ders notebooku - Detaylı açıklamalar ve inline yorumlar içerir |

---

## Referanslar

- Python Programlama Dili Referans Belgesi
- Python Resmi Dokümantasyonu: https://docs.python.org/3/

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılacaktır. Notebook'u Colab'da açmak için `01-python-giris.ipynb` dosyasına sağ tıklayıp "Open in Colab" seçeneğini kullanabilirsiniz.
