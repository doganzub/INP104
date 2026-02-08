# Hafta 8: Fonksiyonlar

## Konu Özeti

Bu hafta Python'da fonksiyon tanımlama, parametreler ve değer döndürme kavramları incelenmektedir. Fonksiyonlar, kod tekrarını önleyen, programları modüler hale getiren ve bakımı kolaylaştıran yapılardır. Python'da fonksiyonlar `def` anahtar kelimesi ile tanımlanır.

---

## Neden Önemli

Fonksiyonlar, programlamanın temel yapı taşlarından biridir. Kod tekrarını önler, programları daha okunabilir ve bakımı kolay hale getirir. Ayrıca karmaşık problemleri küçük parçalara bölerek çözmeyi sağlar. Modern programlama paradigmalarının çoğu fonksiyon tabanlıdır.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- `def` ile fonksiyon tanımlayabilme
- Parametreler ve argümanları anlama
- `return` ifadesi ile değer döndürebilme
- `*args` ve `**kwargs` kullanabilme
- Varsayılan parametre değerleri tanımlayabilme

---

## Konu Başlıkları

### 8.1 Fonksiyon Tanımlama

Fonksiyonlar `def` anahtar kelimesi ile tanımlanır.

**Temel Sözdizimi:**

```python
def fonksiyon_adi():                   # Fonksiyon tanımı başlar
    # Fonksiyon gövdesi                # Çalıştırılacak kodlar
    pass                               # Yer tutucu ifade
```

**Basit Fonksiyon:**

```python
def selamla():                         # Parametresiz fonksiyon tanımlanır
    print("Merhaba!")                  # Ekrana mesaj yazdırılır

selamla()                              # Fonksiyon çağrılır
```

**Çıktı:**
```
Merhaba!
```

---

### 8.2 Parametreli Fonksiyonlar

Fonksiyonlar parametre alarak dinamik çalışabilir.

**Tek Parametre:**

```python
def selamla(isim):                     # 'isim' parametresi tanımlanır
    print(f"Merhaba, {isim}!")         # Parametre kullanılarak mesaj oluşturulur

selamla("Züber")                       # Fonksiyon argüman ile çağrılır
```

**Birden Fazla Parametre:**

```python
def kayit(isim, soyisim, sehir):       # Üç parametre tanımlanır
    print(f"İsim    : {isim}")         # İlk parametre yazdırılır
    print(f"Soyisim : {soyisim}")      # İkinci parametre yazdırılır
    print(f"Şehir   : {sehir}")        # Üçüncü parametre yazdırılır

kayit("Züber", "Doğan", "İstanbul")    # Fonksiyon çağrılır
```

---

### 8.3 Varsayılan Parametre Değerleri

Parametrelere varsayılan değer atanabilir.

```python
def selamla(isim, mesaj="Hoş geldiniz"):  # 'mesaj' parametresi varsayılan değerli
    print(f"{isim}, {mesaj}!")            # Her iki parametre kullanılır

selamla("Züber")                       # Sadece isim verilir, varsayılan mesaj kullanılır
selamla("Züber", "Günaydın")           # Her iki parametre de verilir
```

**Çıktı:**
```
Züber, Hoş geldiniz!
Züber, Günaydın!
```

---

### 8.4 return İfadesi

`return` ifadesi, fonksiyondan değer döndürür.

**Değer Döndürme:**

```python
def alan_hesapla(uzunluk, genislik):   # İki parametre alan fonksiyon
    alan = uzunluk * genislik          # Alan hesaplanır
    return alan                        # Sonuç döndürülür

sonuc = alan_hesapla(5, 3)             # Dönen değer değişkene atanır
print(f"Alan: {sonuc}")                # Sonuç yazdırılır
```

**Birden Fazla Değer Döndürme:**

```python
def bolme_islemi(bolunen, bolen):      # Bölme işlemi fonksiyonu
    bolum = bolunen // bolen           # Tam bölüm hesaplanır
    kalan = bolunen % bolen            # Kalan hesaplanır
    return bolum, kalan                # İki değer döndürülür

b, k = bolme_islemi(17, 5)             # Dönen değerler ayrı değişkenlere atanır
print(f"Bölüm: {b}, Kalan: {k}")       # Sonuçlar yazdırılır
```

---

### 8.5 *args: Sınırsız Pozisyonel Argüman

`*args`, fonksiyona istenen sayıda argüman geçilmesini sağlar.

```python
def toplam(*args):                     # Sınırsız sayıda argüman kabul edilir
    sonuc = 0                          # Toplam değişkeni başlatılır
    for sayi in args:                  # Her argüman için döngü çalışır
        sonuc += sayi                  # Sayı toplama eklenir
    return sonuc                       # Toplam döndürülür

print(toplam(1, 2, 3))                 # 6
print(toplam(10, 20, 30, 40, 50))      # 150
```

---

### 8.6 **kwargs: Sınırsız İsimli Argüman

`**kwargs`, fonksiyona anahtar-değer çiftleri olarak argüman geçilmesini sağlar.

```python
def kisi_bilgisi(**kwargs):            # Sınırsız isimli argüman kabul edilir
    for anahtar, deger in kwargs.items():  # Her çift için döngü çalışır
        print(f"{anahtar}: {deger}")   # Anahtar ve değer yazdırılır

kisi_bilgisi(isim="Züber", yas=30, sehir="İstanbul")  # Fonksiyon çağrılır
```

**Çıktı:**
```
isim: Züber
yas: 30
sehir: İstanbul
```

---

### 8.7 İsimli Argümanlar (Keyword Arguments)

Fonksiyon çağırılırken parametre isimleri belirtilebilir.

```python
def islem(p1, p2, p3):                 # Üç parametreli fonksiyon
    print(f"p1={p1}, p2={p2}, p3={p3}") # Parametreler yazdırılır

islem(p3="C", p1="A", p2="B")          # Sıra önemli değil, isim belirtildi
```

**Çıktı:**
```
p1=A, p2=B, p3=C
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `08-fonksiyonlar.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. İki sayının en büyük ortak bölenini (EBOB) hesaplayan fonksiyon yazınız.
2. Bir listenin ortalamasını hesaplayan fonksiyon yazınız.
3. Verilen bir sayının asal olup olmadığını kontrol eden fonksiyon yazınız.
4. Faktöriyel hesaplayan özyinelemeli (recursive) fonksiyon yazınız.
