# Hafta 1: Python'a Giriş

## Konu Özeti

Bu hafta Python programlama diline giriş yapılmaktadır. Python'ın tarihçesi, kullanım alanları, `print()` fonksiyonu, tırnak kullanımı ve temel veri tipleri ele alınmaktadır.

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- Python'ın ne olduğunu ve neden tercih edildiğini açıklayabilecektir
- `print()` fonksiyonunu ve parametrelerini (`sep`, `end`) kullanabilecektir
- Tek tırnak, çift tırnak ve üç tırnak arasındaki farkları kavrayacaktır
- Temel veri tiplerini (`str`, `int`, `float`) tanıyacak ve ayırt edebilecektir
- `type()` ve `len()` gömülü fonksiyonlarını doğru kullanabilecektir
- Kaçış dizilerini (`\n`, `\t`, `\'`, `\"`) uygulayabilecektir

---

## Konu Başlıkları

### 1.0 Python Nedir?

Python, C, C++, Perl ve Ruby gibi dillerle aynı kategoride yer alan bir **programlama dilidir**. Guido Van Rossum tarafından 1990'lı yılların başında geliştirilmeye başlanmıştır.

**Tarihçe:** Dilin ismi, çoğu kişinin düşündüğünün aksine, piton yılanından gelmemektedir. "Monty Python" adlı İngiliz komedi grubunun "Monty Python's Flying Circus" gösterisinden esinlenilerek adlandırılmıştır.

**Neden Python Öğrenmeliyiz?**
- Tekrarlayan işlemleri otomatikleştirmek
- Veri analizi ve görselleştirme yapmak
- Web, oyun ve mobil uygulama geliştirmek
- Yapay zeka ve makine öğrenmesi çalışmaları yürütmek

**Python'ın Avantajları:**
- Kolay öğrenilir (basit ve temiz söz dizimi)
- Derleme gerektirmez (hızlı geliştirme)
- Geniş kabul görmüş (Google, YouTube, Instagram, Dropbox)
- Güçlü topluluk ve kütüphane desteği

**Telaffuz:** [paytın] veya [piton]

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

**Önemli Kural:** Karakter dizisini hangi tırnakla başlatırsak, o tırnakla bitirmeliyiz.

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
print(type(3.14))       # <class 'float'>
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

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `01-python-giris.ipynb` | Haftalık ders notebooku - Detaylı açıklamalar ve inline yorumlar içerir |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Python Resmi Dokümantasyonu: https://docs.python.org/3/

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır. Notebook'u Colab'da açmak için `01-python-giris.ipynb` dosyasına sağ tıklayıp "Open in Colab" seçeneğini kullanabilirsiniz.
