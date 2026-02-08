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

## Alıştırma Görevleri

Notebook'un sonunda görev hücreleri ve bir cevap anahtarı hücresi bulunmaktadır:

### 🟩 Görevler (Cell 55-76)

Her görev ayrı bir kod hücresindedir. Öğrenci `???` işaretlerinin yerine doğru kodları yazar.

| Görev | Konu |
|-------|------|
| Görev 1 | Karakter dizisi tanımlama |
| Görev 2 | İndeksleme – Pozitif ve negatif |
| Görev 3 | İndeksleme – len() ile son karakter |
| Görev 4 | İndeksleme – Döngü ile erişim |
| Görev 5 | Dilimleme – Temel |
| Görev 6 | Dilimleme – Kısa yazım |
| Görev 7 | Dilimleme – Negatif indekslerle |
| Görev 8 | Dilimleme – Adım değeri ve ters çevirme |
| Görev 9 | Karakter dizisi değiştirme (immutable) |
| Görev 10 | replace() metodu |
| Görev 11 | split() metodu |
| Görev 12 | split() ile kısaltma çıkarma |
| Görev 13 | join() metodu |
| Görev 14 | lower() ve upper() metotları |
| Görev 15 | capitalize(), title(), swapcase() |
| Görev 16 | count() metodu |
| Görev 17 | find() metodu |
| Görev 18 | strip() metotları |
| Görev 19 | startswith() ve endswith() |
| Görev 20 | isXXX() metotları |
| Görev 21 | enumerate() fonksiyonu |
| Görev 22 | Pratik Örnek – Palindrom kontrolü |

### 🟨 Cevap Anahtarı (Cell 77)

Yukarıdaki görevlerin tamamlanmış çözümleri.

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
