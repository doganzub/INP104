# Hafta 9: Modüller ve Nesne Tabanlı Programlama (OOP)

## Konu Özeti

Bu hafta Python'da **modüller** ve **nesne tabanlı programlama (OOP)** kapsamlı şekilde işlenmektedir.

---

## Neden Önemli?

- Modüller kod tekrarını azaltır ve düzen sağlar
- OOP gerçek dünya problemlerini modellemeyi kolaylaştırır
- Büyük projelerde bakım ve genişleme kolaylaşır

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- `import` ile modül kullanabilecektir
- Farklı içe aktarma yöntemlerini (`from`, `as`) uygulayabilecektir
- Standart kütüphane modüllerini (`os`, `random`, `sys`) kullanabilecektir
- `class` ile sınıf tanımlayabilecektir
- `__init__` ve `self` kavramlarını anlayabilecektir
- Kalıtım ve `super()` kullanabilecektir

---

## Konu Başlıkları

### 9.1 Modül Nedir?
- Standart, üçüncü taraf ve kullanıcı tanımlı modüller

---

### 9.2 Modül İçe Aktarma

| Yöntem | Örnek |
|--------|-------|
| `import modul` | `import os` |
| `from modul import oge` | `from math import sqrt` |
| `import modul as isim` | `import datetime as dt` |

---

### 9.3 Standart Modüller
- `os`, `sys`, `math`, `random`, `datetime`

---

### 9.4 Nesne Tabanlı Programlama
- Sınıf (Class) ve Nesne (Object)
- Nitelik ve Metot kavramları

---

### 9.5 Sınıf Tanımlama
- `class` anahtar kelimesi
- `__init__` yapıcı metot

---

### 9.6 self Kavramı
- Nesneye referans
- Örnek niteliği vs sınıf niteliği

---

### 9.7 Kalıtım (Inheritance)
- Taban sınıf ve alt sınıf
- `super()` kullanımı

---

## Alıştırma Görevleri

Notebook'un sonunda görev hücreleri ve bir cevap anahtarı hücresi bulunmaktadır:

### 🟩 Görevler (Cell 31-41)

Her görev ayrı bir kod hücresindedir. Öğrenci `???` işaretlerinin yerine doğru kodları yazar.

| Görev | Konu |
|-------|------|
| Görev 1 | import ile modül kullanımı |
| Görev 2 | from ... import ile belirli öğe alma |
| Görev 3 | Takma ad (alias) ile import |
| Görev 4 | random modülü |
| Görev 5 | dir() ile modül içeriğini görme |
| Görev 6 | Basit sınıf tanımlama – Sınıf nitelikleri |
| Görev 7 | __init__ metodu ve nesne oluşturma |
| Görev 8 | self ile metot tanımlama |
| Görev 9 | Sınıf niteliği vs Örnek niteliği |
| Görev 10 | Kalıtım (Inheritance) |
| Görev 11 | Pratik Örnek – Banka hesabı |

### 🟨 Cevap Anahtarı (Cell 42)

Yukarıdaki görevlerin tamamlanmış çözümleri.

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `09-moduller-oop.ipynb` | Haftalık ders notebooku |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Modüller bölümü (satır 46016+)
- OOP bölümü (satır 48430+)

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
