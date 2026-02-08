# Python Programlama Dili Temel Kavramlari Referans Belgesi

Bu belge, INP104 dersinin haftalik konularina ait temel Python kavramlarini icerir. Her bolum, resmi akademik dil ile yazilmis ve kod ornekleri aciklayici yorumlar ile desteklenmistir.

---

## 1. Python'a Giris

Python, okunabilir soz dizimi ve guclu standart kutuphanesi ile taninan yuksek seviyeli bir programlama dilidir. Bu bolumde temel konsol ciktisi ve veri kavrami tanitilar.

### print() Fonksiyonu

`print()` fonksiyonu, konsola metin veya deger yazdirmak icin kullanilir.

```python
print("Merhaba Dunya!")           # Basit metin ciktisi
print("Python", "Dersi")          # Birden fazla deger
print("A", "B", sep="-")          # Ozel ayirici karakter
print("Sayi:", 42, end=".\n")     # Ozel satir sonu karakteri
```

### Tirnak Kullanimi

Python'da metinler tek, cift veya uc tirnak ile tanimlanabilir.

```python
'Tek tirnak'                      # Tek tirnak kullanimi
"Cift tirnak"                     # Cift tirnak kullanimi
"""Cok satirli
metin ornegi"""                   # Uc tirnak ile cok satirli metin
```

### Temel Veri Tipleri

```python
isim = "Zuber"                    # str: karakter dizisi
yas = 46                          # int: tam sayi
kilo = 73.5                       # float: ondalikli sayi
```

### type() ve len() Fonksiyonlari

```python
type("Merhaba")                   # <class 'str'> dondurur
type(42)                          # <class 'int'> dondurur
len("Python")                     # 6 (karakter sayisi)
```

---

## 2. Gomulu Fonksiyonlar ve Degiskenler

### Tip Donusum Fonksiyonlari

```python
int("23")                         # String'i tam sayiya cevirir
float("23.5")                     # String'i ondalik sayiya cevirir
str(2024)                         # Sayiyi karakter dizisine cevirir
```

### input() Fonksiyonu

```python
isim = input("Adinizi girin: ")   # Kullanicidan metin alir (str dondurur)
yas = int(input("Yasiniz: "))     # Sayi icin tip donusumu gerekir
```

### Degisken Tanimlama

```python
isim = "Zuber"                    # Temel atama
a = b = c = 10                    # Coklu atama
x, y = y, x                       # Deger takasi
```

### format() ve f-string

```python
"{} yasinda".format(25)           # format metodu ile
f"{isim} {yas} yasinda"           # f-string ile (onerilen)
```

---

## 3. Kosullu Ifadeler

### if-elif-else Yapisi

```python
if kosul:                         # Kosul dogru ise calisir
    # islem
elif baska_kosul:                 # Ilk kosul yanlis, bu dogru ise
    # islem
else:                             # Hic bir kosul dogru degilse
    # islem
```

### Karsilastirma Operatorleri

```python
a == b    # Esit mi
a != b    # Esit degil mi
a > b     # Buyuk mu
a < b     # Kucuk mu
a >= b    # Buyuk esit mi
a <= b    # Kucuk esit mi
```

### Mantiksal Operatorler

```python
and       # Her iki kosul da dogru olmali
or        # En az bir kosul dogru olmali
not       # Kosulu tersine cevirir
```

---

## 4. Donguler

### while Dongusu

```python
sayac = 0
while sayac < 5:                  # Kosul dogru oldukca tekrarlar
    print(sayac)
    sayac += 1                    # Sayaci artir
```

### for Dongusu

```python
for harf in "Python":             # Her karakter uzerinde doner
    print(harf)

for i in range(5):                # 0'dan 4'e kadar
    print(i)
```

### range() Fonksiyonu

```python
range(5)                          # 0, 1, 2, 3, 4
range(1, 6)                       # 1, 2, 3, 4, 5
range(0, 10, 2)                   # 0, 2, 4, 6, 8
```

### Dongu Kontrol Ifadeleri

```python
break                             # Donguyu sonlandirir
continue                          # Sonraki adima gecer
pass                              # Hicbir sey yapmaz (yer tutucu)
```

---

## 5. Karakter Dizileri

### Indeksleme

```python
metin = "Python"
metin[0]                          # 'P' (ilk karakter)
metin[-1]                         # 'n' (son karakter)
```

### Dilimleme (Slicing)

```python
metin[0:3]                        # 'Pyt' (0-2 arasi)
metin[:3]                         # 'Pyt' (bastan 3'e kadar)
metin[3:]                         # 'hon' (3'ten sona kadar)
metin[::-1]                       # 'nohtyP' (ters cevirme)
```

### String Metotlari

```python
metin.lower()                     # Kucuk harfe cevirir
metin.upper()                     # Buyuk harfe cevirir
metin.replace("a", "b")           # Karakter degistirir
metin.split()                     # Listeye boler
" ".join(liste)                   # Listeyi birlestir
metin.count("a")                  # Karakter sayisini verir
metin.find("a")                   # Indeksini bulur
```

---

## 6. Listeler ve Demetler

### Liste Olusturma

```python
liste = []                        # Bos liste
liste = [1, 2, 3]                # Degerli liste
liste = list("abc")              # String'den liste
liste = list(range(5))           # range'den liste
```

### Liste Metotlari

```python
liste.append(x)                   # Sona ekle
liste.insert(i, x)                # Belirli konuma ekle
liste.remove(x)                   # Degeri sil
liste.pop()                       # Son ogesi sil ve dondur
liste.sort()                      # Sirala
liste.reverse()                   # Ters cevir
liste.copy()                      # Bagimsiz kopya olustur
```

### Demetler (Tuple)

```python
demet = (1, 2, 3)                # Demet tanimlama
demet = (1,)                     # Tek ogeli demet (virgul zorunlu)
# Demetler degistirilemez (immutable)
```

---

## 7. Dosya Islemleri

### Dosya Acma Modlari

```python
"r"   # Okuma (read)
"w"   # Yazma (write) - dosyayi sifirlar
"a"   # Ekleme (append) - sona ekler
```

### Temel Islemler

```python
# Yazma
dosya = open("dosya.txt", "w")
dosya.write("Merhaba")
dosya.close()

# Okuma
dosya = open("dosya.txt", "r")
icerik = dosya.read()             # Tum icerigi oku
satirlar = dosya.readlines()      # Satirlari liste olarak oku
dosya.close()
```

### with Ifadesi (Onerilen)

```python
with open("dosya.txt", "w") as dosya:
    dosya.write("Merhaba")
# Dosya otomatik kapanir
```

---

## 8. Fonksiyonlar

### Fonksiyon Tanimlama

```python
def fonksiyon_adi(parametre1, parametre2):
    """Fonksiyon aciklamasi"""
    # islemler
    return sonuc
```

### Varsayilan Parametre Degerleri

```python
def selamla(isim, mesaj="Hosgeldiniz"):
    print(f"{isim}, {mesaj}!")
```

### args ve kwargs

```python
def toplam(*args):                # Sinirsiz pozisyonel arguman
    return sum(args)

def bilgi(**kwargs):              # Sinirsiz isimli arguman
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

---

## 9. Moduller ve OOP

### Modul Import Etme

```python
import os                         # Tum modulu import et
from math import sqrt, pi         # Belirli fonksiyonlari import et
import datetime as dt             # Takma ad ile import et
```

### Sinif Tanimlama

```python
class Personel:
    def __init__(self, ad, yas):  # Yapici metot
        self.ad = ad              # Ornek niteli
        self.yas = yas

    def bilgi_goster(self):       # Ornek metodu
        print(f"{self.ad}, {self.yas} yasinda")
```

### Kalitim

```python
class Mudur(Personel):            # Personel'den kalitim
    def __init__(self, ad, yas, bolum):
        super().__init__(ad, yas) # Ust sinif yapicisini cagir
        self.bolum = bolum
```

---

## 10. Veri Tabani Islemleri (SQLite)

### Baglanti ve Imlem

```python
import sqlite3

vt = sqlite3.connect('db.sqlite')  # Baglanti ac
im = vt.cursor()                   # Imlec olustur
```

### Temel SQL Islemleri

```python
# Tablo olustur
im.execute("CREATE TABLE IF NOT EXISTS tablo (id INTEGER PRIMARY KEY, isim TEXT)")

# Veri ekle
im.execute("INSERT INTO tablo VALUES (?, ?)", (1, "Zuber"))

# Veri oku
im.execute("SELECT * FROM tablo")
veriler = im.fetchall()

# Veri guncelle
im.execute("UPDATE tablo SET isim = ? WHERE id = ?", ("Yeni", 1))

# Veri sil
im.execute("DELETE FROM tablo WHERE id = ?", (1,))

vt.commit()                        # Degisiklikleri kaydet
vt.close()                         # Baglantiyi kapat
```

### with ile Guvenli Kullanim

```python
with sqlite3.connect('db.sqlite') as vt:
    im = vt.cursor()
    im.execute("SELECT * FROM tablo")
    veriler = im.fetchall()
# Baglanti otomatik kapanir
```
