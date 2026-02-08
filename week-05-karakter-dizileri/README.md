# Hafta 5: Karakter Dizileri ve Metotları

## Konu Özeti

Bu hafta Python'da karakter dizileri (string) ve bunlarla yapılabilecek işlemler incelenmektedir. Karakter dizileri, metin verilerinin saklandığı ve işlendiği temel veri yapılarıdır. Python'da karakter dizileri değiştirilemez (immutable) nesnelerdir, yani bir kez oluşturulduktan sonra içerikleri doğrudan değiştirilemez.

---

## Neden Önemli

Karakter dizileri, programlamada en sık kullanılan veri tiplerinden biridir. Kullanıcı girişleri, dosya içerikleri, veritabanı kayıtları ve web verileri genellikle karakter dizisi formatındadır. Bu nedenle string işleme becerileri her programcı için temel bir gerekliliktir.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- Karakter dizilerinde indeksleme yapabilme
- Dilimleme (slicing) işlemlerini gerçekleştirebilme
- String metotlarını etkin kullanabilme
- `enumerate()` fonksiyonu ile indeksli döngü yapabilme

---

## Konu Başlıkları

### 5.1 String İndeksleme

Karakter dizilerindeki her karaktere bir indeks numarası ile erişilebilir. Python'da indeksler 0'dan başlar.

```python
isim = "Python"                        # Karakter dizisi tanımlanır
print(isim[0])                         # İlk karakter: P (indeks 0)
print(isim[1])                         # İkinci karakter: y (indeks 1)
print(isim[-1])                        # Son karakter: n (negatif indeks)
print(isim[-2])                        # Sondan ikinci karakter: o
```

**İndeks Tablosu:**

| Karakter | P | y | t | h | o | n |
|----------|---|---|---|---|---|---|
| Pozitif  | 0 | 1 | 2 | 3 | 4 | 5 |
| Negatif  | -6| -5| -4| -3| -2| -1|

---

### 5.2 String Dilimleme (Slicing)

Dilimleme, bir karakter dizisinden belirli bir bölümü ayırmak için kullanılır.

**Sözdizimi:** `karakter_dizisi[başlangıç:bitiş:adım]`

```python
metin = "Python Programlama"           # İşlenecek karakter dizisi

print(metin[0:6])                      # "Python" - 0'dan 6'ya kadar (6 dahil değil)
print(metin[7:])                       # "Programlama" - 7'den sona kadar
print(metin[:6])                       # "Python" - baştan 6'ya kadar
print(metin[::2])                      # "Pto rgaaa" - 2'şer atlayarak
print(metin[::-1])                     # Ters çevirme işlemi
```

**Pratik Örnekler:**

```python
parola = "gizli12345"                  # Parola karakter dizisi
print(parola[0:5])                     # "gizli" - İlk 5 karakter
print(parola[5:])                      # "12345" - 5. karakterden sonrası
print(parola[-5:])                     # "12345" - Son 5 karakter
```

---

### 5.3 String Metotları

Python'da karakter dizileri üzerinde çalışan çok sayıda yerleşik metot bulunmaktadır.

**replace() - Değiştirme:**

```python
metin = "Merhaba Dünya"                # Orijinal metin
yeni = metin.replace("Dünya", "Python")# "Dünya" ifadesi "Python" ile değiştirilir
print(yeni)                            # Çıktı: "Merhaba Python"

# Belirli sayıda değiştirme
kelime = "aaa bbb aaa"                 # Tekrarlı karakter içeren metin
print(kelime.replace("a", "x", 2))     # Sadece ilk 2 "a" değiştirilir: "xxa bbb aaa"
```

**lower() ve upper() - Harf Dönüşümü:**

```python
metin = "Python Programlama"           # Karışık harfli metin

print(metin.lower())                   # Tamamı küçük harfe: "python programlama"
print(metin.upper())                   # Tamamı büyük harfe: "PYTHON PROGRAMLAMA"
```

**split() - Bölme:**

```python
cumle = "Python,Java,C++,JavaScript"   # Virgülle ayrılmış metin
diller = cumle.split(",")              # Virgülden bölerek liste oluşturur
print(diller)                          # ['Python', 'Java', 'C++', 'JavaScript']

isim = "Züber Doğan"                   # Boşlukla ayrılmış metin
parcalar = isim.split()                # Varsayılan olarak boşluktan böler
print(parcalar)                        # ['Züber', 'Doğan']
```

**join() - Birleştirme:**

```python
liste = ["Python", "öğreniyorum"]      # Birleştirilecek liste
sonuc = " ".join(liste)                # Liste elemanları boşlukla birleştirilir
print(sonuc)                           # Çıktı: "Python öğreniyorum"

harfler = ["P", "y", "t", "h", "o", "n"]
kelime = "".join(harfler)              # Boşluksuz birleştirme
print(kelime)                          # Çıktı: "Python"
```

**count() - Sayma:**

```python
metin = "Python programlama dili"      # Aranacak metin
print(metin.count("a"))                # "a" harfi 4 kez geçiyor
print(metin.count("pro"))              # "pro" ifadesi 1 kez geçiyor
```

**find() - Bulma:**

```python
metin = "Python programlama"           # Aranacak metin
print(metin.find("prog"))              # 7 - "prog" ifadesinin başlangıç indeksi
print(metin.find("Java"))              # -1 - Bulunamadı
```

---

### 5.4 enumerate() Fonksiyonu

`enumerate()` fonksiyonu, bir iterable üzerinde dönerken hem indeks hem de değere erişim sağlar.

```python
isim = "Python"                        # İşlenecek karakter dizisi
for indeks, harf in enumerate(isim):   # Her turda indeks ve karakter alınır
    print(f"{indeks}: {harf}")         # İndeks ve karakter yazdırılır
```

**Çıktı:**
```
0: P
1: y
2: t
3: h
4: o
5: n
```

**Başlangıç Değeri Belirleme:**

```python
meyveler = ["elma", "armut", "muz"]    # İşlenecek liste
for no, meyve in enumerate(meyveler, start=1):  # Numaralandırma 1'den başlar
    print(f"{no}. {meyve}")            # Numaralı liste oluşturulur
```

---

### 5.5 String Metotları Özet Tablosu

| Metot | Açıklama | Örnek |
|-------|----------|-------|
| `replace()` | Metin değiştirme | `"abc".replace("a", "x")` → `"xbc"` |
| `lower()` | Küçük harfe çevirme | `"ABC".lower()` → `"abc"` |
| `upper()` | Büyük harfe çevirme | `"abc".upper()` → `"ABC"` |
| `split()` | Metni bölme | `"a,b".split(",")` → `["a","b"]` |
| `join()` | Liste birleştirme | `"-".join(["a","b"])` → `"a-b"` |
| `count()` | Karakter sayma | `"aab".count("a")` → `2` |
| `find()` | Konum bulma | `"abc".find("b")` → `1` |
| `strip()` | Boşluk temizleme | `" ab ".strip()` → `"ab"` |

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `05-karakter-dizileri.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. Kullanıcıdan alınan bir cümledeki sesli harf sayısını hesaplayınız.
2. Bir metnin palindrom (tersten okunuşu aynı) olup olmadığını kontrol ediniz.
3. Verilen bir e-posta adresinden kullanıcı adı ve domain kısmını ayırınız.
4. Bir cümledeki her kelimenin ilk harfini büyük yapan program yazınız.
