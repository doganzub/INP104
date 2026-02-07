# Hafta 9: Modüller ve Nesne Tabanlı Programlama

## Konu Özeti

Bu hafta, Python modülleri ve nesne tabanlı programlama (OOP) temellerini öğrenilir.

---

## Öğrenme Hedefleri

- Modül import etme
- Standart kütüphaneleri kullanma
- Sınıf (class) tanımlama
- `__init__` ve `self` kavramları
- Kalıtım (inheritance)

---

## Konu Başlıkları

### 9.1 Modüller
```python
import os
from math import sqrt
import datetime as dt
```

### 9.2 Sınıf Tanımlama
```python
class Personel:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
```

### 9.3 Kalıtım
```python
class Detay(Personel):
    def __init__(self, isim, yas, bolum):
        super().__init__(isim, yas)
        self.bolum = bolum
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `09-moduller-oop.ipynb` | Haftalık ders notebooku |
