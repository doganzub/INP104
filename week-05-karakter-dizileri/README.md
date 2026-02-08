# Hafta 5: Karakter Dizileri ve Metotları (Strings)

## Konu Özeti

Bu hafta Python programlama dilinde **karakter dizileri (strings)** kapsamlı şekilde işlenmektedir. Karakter dizileri, metin verilerinin saklandığı ve işlendiği temel veri tiplerinden biridir. Python'da karakter dizileri **değiştirilemez (immutable)** nesnelerdir.

---

## Neden Önemli?

Karakter dizileri programlamada en sık kullanılan veri tiplerinden biridir:
- Kullanıcı girişleri `input()` ile karakter dizisi olarak gelir
- Dosya içerikleri karakter dizisi olarak okunur
- Web verileri genellikle metin formatındadır
- Veritabanı kayıtlarının çoğu metin içerir

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- Karakter dizilerinin temel özelliklerini açıklayabilecektir
- Pozitif ve negatif indeksleme yapabilecektir
- Dilimleme (slicing) işlemlerini uygulayabilecektir
- Karakter dizilerinin değiştirilemezliğini (immutability) anlayacaktır
- Temel string metotlarını kullanabilecektir
- `enumerate()` fonksiyonu ile indeksli döngü kurabilecektir

---

## Konu Başlıkları

### 5.1 Karakter Dizisi Nedir?

`type()` fonksiyonu `<class 'str'>` döndüren nesnelerdir. Tek, çift veya üç tırnak ile tanımlanır.

---

### 5.2 İndeksleme (Indexing)

Her karakterin bir indeks numarası vardır. Python'da indeksler **0'dan başlar**.

```
P  y  t  h  o  n
0  1  2  3  4  5   ← Pozitif indeks
-6 -5 -4 -3 -2 -1  ← Negatif indeks
```

---

### 5.3 Dilimleme (Slicing)

```python
karakter_dizisi[başlangıç:bitiş:adım]
```

- `başlangıç` dahil, `bitiş` dahil değil
- `[::-1]` ile ters çevirme

---

### 5.4 Immutability (Değiştirilemezlik)

Karakter dizileri bir kez oluşturulduktan sonra doğrudan değiştirilemez. Değişiklik için yeniden atama gerekir.

---

### 5.5 String Metotları

| Metot | Açıklama |
|-------|----------|
| `replace()` | Karakter/metin değiştirme |
| `split()` | Metni bölme |
| `join()` | Liste birleştirme |
| `lower()` / `upper()` | Harf dönüşümü |
| `count()` | Karakter sayma |
| `find()` | Konum bulma |
| `strip()` | Boşluk temizleme |
| `startswith()` / `endswith()` | Başlangıç/bitiş kontrolü |
| `isdigit()` / `isalpha()` | Karakter tipi kontrolü |

---

### 5.6 enumerate() Fonksiyonu

Döngüde hem indeks hem değere aynı anda erişim sağlar.

```python
for indeks, harf in enumerate("Python"):
    print(f"{indeks}: {harf}")
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `05-karakter-dizileri.ipynb` | Haftalık ders notebooku - Detaylı açıklamalar ve inline yorumlar içerir |

---

## Alıştırma Soruları

1. Kullanıcıdan alınan bir cümledeki sesli harf sayısını hesaplayınız.
2. Bir metnin palindrom olup olmadığını kontrol ediniz.
3. Verilen bir e-posta adresinden kullanıcı adı ve domain kısmını ayırınız.
4. Bir cümledeki her kelimenin ilk harfini büyük yapan program yazınız.
5. İki metin arasındaki ortak karakterleri bulan program yazınız.

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Karakter Dizileri bölümü (satır 15978+)
- Karakter Dizilerinin Metotları bölümü (satır 17806+)

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
