# Hafta 1: Python'a Giriş

## Konu Özeti

Bu hafta Python programlama diline giriş yapılmaktadır. Python'ın neden öğrenilmesi gerektiği, dünya genelindeki popülerliği, `print()` fonksiyonu, tırnak kullanımı ve temel veri tipleri ele alınmaktadır.

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- Python'ın neden bu kadar popüler olduğunu ve dünya genelindeki konumunu açıklayabilecektir
- `print()` fonksiyonunu ve parametrelerini (`sep`, `end`) kullanabilecektir
- Tek tırnak, çift tırnak ve üç tırnak arasındaki farkları kavrayacaktır
- Temel veri tiplerini (`str`, `int`, `float`) tanıyacak ve ayırt edebilecektir
- `type()` ve `len()` gömülü fonksiyonlarını doğru kullanabilecektir
- Kaçış dizilerini (`\n`, `\t`, `\'`, `\"`) uygulayabilecektir

---

## Konu Başlıkları

### 1.0 Neden Python? 

Python, 2024-2025 yıllarında **tüm popülerlik endekslerinde 1. sırada** yer almaktadır:

| Kaynak | Python Konumu |
|--------|---------------|
| TIOBE 2024 | **1. sıra** (%23.84) |
| GitHub 2024 | **1. sıra** (JavaScript'i ilk kez geçti) |
| PYPL 2024 | **1. sıra** (%29.71) |

**İstatistikler:**
- 2024 "Yılın Programlama Dili" (TIOBE)
- Geliştiricilerin %86'sının birincil dili
- Spotify backend'inin %80'i Python
- Google, Netflix, Meta, Dropbox tarafından kullanılıyor

> Detaylı araştırma için: [neden_python.md](./neden_python.md)

---

### 1.1 print() Fonksiyonu

`print()` fonksiyonu, Python'da ekrana çıktı vermemizi sağlayan temel fonksiyondur.

```python
# Temel kullanım
print("Merhaba Dünya!")

# Birden fazla parametre
print("Python", "Programlama", "Dili")  # Parametreler boşlukla birleştirilir
```

---

### 1.2 Tırnak Kullanımı

| Tırnak Tipi | Kullanım | Örnek |
|-------------|----------|-------|
| **Tek tırnak** | Basit metinler | `'Merhaba Python'` |
| **Çift tırnak** | İçinde kesme işareti olan metinler | `"İstanbul'un havası"` |
| **Üç tırnak** | Çok satırlı metinler | `"""Uzun metin..."""` |

---

### 1.3 Veri Tipleri

| Veri Tipi | Python Kodu | Örnek | Açıklama |
|-----------|-------------|-------|----------|
| **Karakter Dizisi** | `str` | `"Züber Doğan"` | Metin verileri |
| **Tam Sayı** | `int` | `1978` | Ondalık kısmı olmayan sayılar |
| **Ondalıklı Sayı** | `float` | `73.3` | Kesirli sayılar |

---

### 1.4 type() ve len() Fonksiyonları

**type() Fonksiyonu:** Verinin tipini döndürür.
```python
print(type("Merhaba"))  # <class 'str'>
print(type(42))         # <class 'int'>
```

**len() Fonksiyonu:** Karakter dizisinin uzunluğunu verir.
```python
metin = "Python"
print(len(metin))  # 6
```

---

### 1.5 print() Özel Parametreleri

**sep Parametresi:** Parametreler arası ayırıcı (varsayılan: boşluk)
```python
print("A", "B", "C", sep="-")  # A-B-C
```

**end Parametresi:** Satır sonu karakteri (varsayılan: `\n`)
```python
print("Merhaba", end=" ")
print("Dünya")  # Çıktı: Merhaba Dünya
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

---

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `01-python-giris.ipynb` | Haftalık ders notebooku |
| `neden_python.md` | Python popülerlik araştırması ve istatistikler |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- TIOBE Programming Language Index (tiobe.com)
- Stack Overflow Developer Survey 2024-2025
- GitHub Octoverse Report 2024

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
