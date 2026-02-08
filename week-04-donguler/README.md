# Hafta 4: Döngüler (Loops)

## Konu Özeti

Bu hafta Python programlama dilinde **döngü yapıları** kapsamlı şekilde işlenmektedir. Döngüler, belirli kod bloklarının tekrar tekrar çalıştırılmasını sağlayan yapılardır. Python'da iki temel döngü türü bulunur: `while` ve `for`. Ayrıca döngülerin akışını kontrol eden `break`, `continue` ve `pass` deyimleri de bu hafta ele alınmaktadır.

---

## Neden Önemli?

Programlamada döngüler, tekrarlayan işlemlerin otomatikleştirilmesi için temel yapı taşlarıdır:
- Program sürekli çalışır, tek seferlik değil
- Kullanıcı istediği kadar işlem yapabilir
- Program ancak biz istediğimizde kapanır

**Kullanım Alanları:** Veri işleme, kullanıcı girişi doğrulama, dosya işlemleri, algoritmik çözümler

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- `while` döngüsü ile koşula bağlı tekrarlama yapabilecektir
- Sonsuz döngüden kaçınma yöntemlerini bilecektir
- `while True` ve `break` kombinasyonunu kullanabilecektir
- `for` döngüsü ile koleksiyonlar üzerinde dolaşabilecektir
- `range()` fonksiyonunun tüm parametrelerini uygulayabilecektir
- `break`, `continue`, `pass` deyimlerini doğru kullanabilecektir
- `döngü + else` yapısını anlayabilecektir
- İç içe döngüler tasarlayabilecektir

---

## Konu Başlıkları

### 4.1 Döngü Kavramı ve Önemi

Döngüler programların tekrar tekrar çalışmasını sağlar. İngilizce'de "loop" olarak adlandırılır.

---

### 4.2 while Döngüsü

`while` = "... olduğu sürece"

```python
while koşul:
    # koşul True olduğu sürece bu blok tekrarlanır
```

**Sonsuz Döngü Riski:** Koşulu değiştiren bir kod olmazsa döngü sonsuza kadar çalışır!

---

### 4.3 while True ve break

```python
while True:  # Aksi belirtilmediği sürece çalış
    if çıkış_koşulu:
        break  # Döngüyü kır ve çık
```

---

### 4.4 for Döngüsü

Koleksiyon üzerinde eleman eleman dolaşır.

```python
for değişken in koleksiyon:
    # her eleman için bu blok çalışır
```

**Not:** Sayılar (int, float) üzerinde döngü kurulamaz! (not iterable)

---

### 4.5 range() Fonksiyonu

| Söz Dizimi | Açıklama |
|------------|----------|
| `range(stop)` | 0'dan stop-1'e kadar |
| `range(start, stop)` | start'tan stop-1'e kadar |
| `range(start, stop, step)` | step kadar atlayarak |

**Önemli:** `stop` değeri sonuca dahil değildir!

---

### 4.6 Döngü Kontrol Deyimleri

| Deyim | İşlevi |
|-------|--------|
| `break` | Döngüyü tamamen sonlandır |
| `continue` | Mevcut adımı atla, sonrakine geç |
| `pass` | Hiçbir şey yapma (yer tutucu) |

---

### 4.7 Döngü ile else Kullanımı

- `break` çalışmadıysa → `else` bloğu **çalışır**
- `break` çalıştıysa → `else` bloğu **çalışmaz**

---

### 4.8 İç İçe Döngüler

Dış döngünün **her bir turu** için iç döngü **tamamen** çalışır.

```python
for i in range(3):      # Dış: 3 tur
    for j in range(2):  # İç: her dış turda 2 tur
        print(i, j)     # Toplam: 3 x 2 = 6 yazdırma
```

---

### 4.9 while vs for Karşılaştırması

| while | for |
|-------|-----|
| Koşul True iken çalışır | Koleksiyon bitene kadar çalışır |
| Sayaç elle yönetilir | Sayaç otomatik ilerler |
| Belirsiz tekrar sayısı | Belirli tekrar sayısı |

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `04-donguler.ipynb` | Haftalık ders notebooku - Detaylı açıklamalar ve inline yorumlar içerir |

---

## Alıştırma Soruları

1. 1'den 100'e kadar olan sayıların toplamını hesaplayan bir program yazınız.
2. Kullanıcıdan alınan bir sayının faktöriyelini hesaplayınız.
3. Fibonacci dizisinin ilk 20 terimini ekrana yazdırınız.
4. 1-100 arasındaki asal sayıları bulan bir program yazınız.
5. Kullanıcıdan parola alıp, 3 deneme hakkı ile doğrulama yapan program yazınız.

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Döngüler bölümü (satır 12669+)

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
