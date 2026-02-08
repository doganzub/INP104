# Hafta 4: Döngüler

## Konu Özeti

Bu hafta Python programlama dilinde döngü yapıları incelenmektedir. Döngüler, belirli kod bloklarının tekrar tekrar çalıştırılmasını sağlayan yapılardır. Python'da iki temel döngü türü bulunmaktadır: `while` döngüsü ve `for` döngüsü. Ayrıca döngülerin akışını kontrol eden `break`, `continue` ve `pass` ifadeleri de bu hafta ele alınmaktadır.

---

## Neden Önemli

Programlamada döngüler, tekrarlayan işlemlerin otomatikleştirilmesi için temel yapı taşlarıdır. Veri listelerinin işlenmesi, kullanıcı girişlerinin doğrulanması, dosya işlemleri ve pek çok algoritmik çözüm döngüler sayesinde gerçekleştirilir.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- `while` döngüsü ile koşula bağlı tekrarlama yapabilme
- `for` döngüsü ile iterasyon gerçekleştirebilme
- `range()` fonksiyonu ile sayı dizileri oluşturabilme
- `break`, `continue` ve `pass` ifadelerini etkin kullanabilme
- İç içe döngüler tasarlayabilme

---

## Konu Başlıkları

### 4.1 while Döngüsü

`while` döngüsü, belirtilen koşul doğru olduğu sürece kod bloğunu tekrar eder. Koşul yanlış olduğunda döngüden çıkılır.

**Temel Sözdizimi:**

```python
while kosul:                           # Koşul doğru olduğu sürece döngü çalışır
    # Tekrarlanacak kod bloğu          # Her tekrarda bu blok çalıştırılır
```

**Örnek - Sayaç Döngüsü:**

```python
sayac = 0                              # Sayaç değişkeni başlangıç değeri ile tanımlanır
while sayac < 5:                       # Sayaç 5'ten küçük olduğu sürece döngü devam eder
    print(f"Sayaç: {sayac}")           # Mevcut sayaç değeri ekrana yazdırılır
    sayac += 1                         # Sayaç değeri 1 artırılır (sonsuz döngü önlenir)
```

**Çıktı:**
```
Sayaç: 0
Sayaç: 1
Sayaç: 2
Sayaç: 3
Sayaç: 4
```

---

### 4.2 for Döngüsü

`for` döngüsü, bir dizi veya iterable (yinelenebilir) nesne üzerinde eleman eleman dolaşır. Her turda bir sonraki elemana geçilir.

**Karakter Dizisi Üzerinde Döngü:**

```python
isim = "Python"                        # İşlenecek karakter dizisi tanımlanır
for harf in isim:                      # Her turda bir karakter 'harf' değişkenine atanır
    print(harf)                        # Mevcut karakter ekrana yazdırılır
```

**Çıktı:**
```
P
y
t
h
o
n
```

**range() Fonksiyonu ile Döngü:**

`range()` fonksiyonu, belirtilen aralıkta sayı dizisi oluşturur.

```python
for i in range(5):                     # 0'dan 4'e kadar (5 dahil değil) sayı üretir
    print(i)                           # Üretilen sayı ekrana yazdırılır
```

**Çıktı:**
```
0
1
2
3
4
```

**range() Fonksiyonunun Farklı Kullanımları:**

```python
for i in range(1, 6):                  # 1'den 5'e kadar sayı üretir (6 dahil değil)
    print(i)                           # Çıktı: 1, 2, 3, 4, 5

for i in range(0, 10, 2):              # 0'dan 10'a kadar 2'şer artarak sayı üretir
    print(i)                           # Çıktı: 0, 2, 4, 6, 8
```

---

### 4.3 Döngü Kontrol İfadeleri

Döngülerin akışını kontrol etmek için üç önemli ifade kullanılır:

**break - Döngüyü Sonlandırma:**

```python
for i in range(10):                    # 0'dan 9'a kadar döngü başlatılır
    if i == 5:                         # Eğer i değeri 5'e eşit ise
        break                          # Döngü tamamen sonlandırılır
    print(i)                           # Sadece 0, 1, 2, 3, 4 yazdırılır
```

**continue - Adımı Atlama:**

```python
for i in range(10):                    # 0'dan 9'a kadar döngü başlatılır
    if i % 2 == 0:                     # Eğer i değeri çift sayı ise
        continue                       # Bu tur atlanır, sonraki tura geçilir
    print(i)                           # Sadece tek sayılar yazdırılır: 1, 3, 5, 7, 9
```

**pass - Boş İşlem (Yer Tutucu):**

```python
for i in range(5):                     # Döngü başlatılır
    if i == 3:                         # Koşul kontrolü yapılır
        pass                           # Hiçbir işlem yapılmaz (yer tutucu)
    print(i)                           # Tüm sayılar yazdırılır: 0, 1, 2, 3, 4
```

---

### 4.4 İç İçe Döngüler

Bir döngü içinde başka bir döngü kullanılabilir. Bu yapı özellikle çok boyutlu veri yapılarında ve matris işlemlerinde kullanılır.

**Örnek - Çarpım Tablosu:**

```python
for i in range(1, 4):                  # Dış döngü: 1, 2, 3 değerlerini alır
    for j in range(1, 4):              # İç döngü: Her dış döngü turu için 1, 2, 3 değerlerini alır
        print(f"{i} x {j} = {i*j}")    # Çarpım sonucu formatlanarak yazdırılır
    print("---")                       # Her dış döngü turu sonunda ayraç yazdırılır
```

---

### 4.5 Pratik Uygulama: Parola Doğrulama

```python
dogru_parola = "python123"             # Sistem tarafından kabul edilecek parola tanımlanır
deneme_hakki = 3                       # Kullanıcıya verilen deneme hakkı sayısı

while deneme_hakki > 0:                # Deneme hakkı kaldığı sürece döngü devam eder
    girilen = input("Parola: ")        # Kullanıcıdan parola girişi alınır
    
    if girilen == dogru_parola:        # Girilen parola doğru ise
        print("Giriş başarılı!")       # Başarı mesajı gösterilir
        break                          # Döngüden çıkılır
    else:                              # Parola yanlış ise
        deneme_hakki -= 1              # Kalan deneme hakkı azaltılır
        print(f"Hatalı! Kalan hak: {deneme_hakki}")  # Uyarı mesajı gösterilir

if deneme_hakki == 0:                  # Tüm haklar tükendiyse
    print("Hesap kilitlendi!")         # Kilitleme mesajı gösterilir
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `04-donguler.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. 1'den 100'e kadar olan sayıların toplamını hesaplayan bir program yazınız.
2. Kullanıcıdan alınan bir sayının faktöriyelini hesaplayınız.
3. Fibonacci dizisinin ilk 20 terimini ekrana yazdırınız.
4. 1-100 arasındaki asal sayıları bulan bir program yazınız.
