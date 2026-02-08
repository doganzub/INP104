# Hafta 3: Koşullu İfadeler

## Konu Özeti

Bu hafta Python'da koşullu durumlar ele alınmaktadır. Programların belirli koşullara göre farklı davranışlar sergilemesini sağlayan `if`, `elif`, `else` deyimleri, karşılaştırma ve mantıksal operatörler kapsamlı şekilde işlenmektedir.

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- `if`, `elif`, `else` deyimlerini doğru söz dizimiyle kullanabilecektir
- Karşılaştırma operatörlerini (`==`, `!=`, `<`, `>`, `<=`, `>=`) uygulayabilecektir
- Mantıksal operatörleri (`and`, `or`, `not`) kullanarak karmaşık koşullar oluşturabilecektir
- `if` ve `elif` arasındaki kritik farkı anlayabilecektir
- İç içe koşullu yapılar tasarlayabilecektir

---

## Konu Başlıkları

### 3.1 Koşullu Durumlar ve if Deyimi

Koşullu durumlar, programın belirli koşullara göre farklı kod bloklarını çalıştırmasını sağlar.

```python
if koşul:
    # koşul doğruysa bu blok çalışır
```

**Önemli:** `if` satırının sonunda `:` olmalı ve blok 4 boşluk girintili yazılmalıdır.

---

### 3.2 Karşılaştırma Operatörleri

| Operatör | Anlamı | Örnek |
|----------|--------|-------|
| `==` | Eşit | `a == b` |
| `!=` | Eşit değil | `a != b` |
| `>` | Büyük | `a > b` |
| `<` | Küçük | `a < b` |
| `>=` | Büyük eşit | `a >= b` |
| `<=` | Küçük eşit | `a <= b` |

**Dikkat:** `=` (atama) ve `==` (karşılaştırma) farklıdır!

---

### 3.3 if-else Yapısı

```python
if koşul:
    # koşul True ise
else:
    # koşul False ise
```

---

### 3.4 if-elif-else Yapısı

```python
if koşul_1:
    # ilk koşul doğruysa
elif koşul_2:
    # ilk yanlış, ikinci doğruysa
else:
    # hiçbiri doğru değilse
```

**Kritik Fark:**
- Art arda `if` → Tüm doğru koşullar çalışır
- `if-elif` → Sadece ilk doğru koşul çalışır

---

### 3.5 Mantıksal Operatörler

| Operatör | Anlamı | Açıklama |
|----------|--------|----------|
| `and` | Ve | Her iki koşul True olmalı |
| `or` | Veya | En az bir koşul True olmalı |
| `not` | Değil | Koşulun tersini alır |

---

### 3.6 İç İçe Koşullar

Bir koşul bloğunun içinde başka koşul blokları tanımlanabilir.

```python
if dış_koşul:
    if iç_koşul:
        # her iki koşul da True
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `03-kosullu-ifadeler.ipynb` | Haftalık ders notebooku - Detaylı açıklamalar ve inline yorumlar içerir |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Koşullu Durumlar bölümü (satır 8787+)

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
