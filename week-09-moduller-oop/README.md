# Hafta 9: Modüller ve Nesne Tabanlı Programlama

## Konu Özeti

Bu hafta Python modülleri ve Nesne Tabanlı Programlama (OOP) temelleri incelenmektedir. Modüller, kodun yeniden kullanılabilirliğini sağlayan yapılardır. Nesne Tabanlı Programlama ise gerçek dünya nesnelerini sınıflar ve objeler olarak modellemeyi sağlar.

---

## Neden Önemli

Modüller, Python'un güçlü standart kütüphanesine ve üçüncü parti paketlere erişim sağlar. OOP ise büyük ve karmaşık projelerde kodun organize edilmesini, bakımını ve genişletilmesini kolaylaştırır. Modern yazılım geliştirmenin temel paradigmalarından biridir.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- Modül import etme yöntemlerini kullanabilme
- Standart kütüphaneleri kullanabilme
- Sınıf (class) tanımlayabilme
- `__init__` ve `self` kavramlarını anlayabilme
- Kalıtım (inheritance) uygulayabilme

---

## Konu Başlıkları

### 9.1 Modül Import Etme

Python'da modüller farklı yöntemlerle içe aktarılabilir.

**Tam Modül Import:**

```python
import os                              # os modülü tam olarak import edilir
print(os.getcwd())                     # Modül adı ile fonksiyon çağrılır
```

**Belirli Fonksiyon Import:**

```python
from math import sqrt, pi             # math modülünden sadece sqrt ve pi import edilir
print(sqrt(16))                        # Doğrudan fonksiyon adı ile kullanılır
print(pi)                              # Pi sayısı: 3.141592...
```

**Takma Ad (Alias) ile Import:**

```python
import datetime as dt                  # datetime modülü 'dt' takma adı ile import edilir
bugun = dt.date.today()                # Kısa isimle kullanılır
print(bugun)                           # Bugünün tarihi yazdırılır
```

---

### 9.2 Önemli Standart Kütüphaneler

**os Modülü - İşletim Sistemi İşlemleri:**

```python
import os                              # os modülü import edilir
print(os.getcwd())                     # Çalışma dizini görüntülenir
os.makedirs("yeni_klasor", exist_ok=True)  # Klasör oluşturulur
```

**random Modülü - Rastgele Sayılar:**

```python
import random                          # random modülü import edilir
sayi = random.randint(1, 100)          # 1-100 arası rastgele tam sayı
print(f"Rastgele sayı: {sayi}")        # Sayı yazdırılır
```

---

### 9.3 Sınıf (Class) Tanımlama

Sınıflar, nesnelerin şablonlarıdır. Özellikler (attributes) ve davranışlar (methods) içerir.

**Basit Sınıf:**

```python
class Calisan:                         # Sınıf tanımlanır
    ad = "züber"                       # Sınıf niteliği (attribute)
    soyad = "doğan"                    # Sınıf niteliği

p1 = Calisan()                         # Sınıftan nesne oluşturulur
print(p1.ad)                           # Nesne niteliğine erişilir
```

---

### 9.4 __init__ Metodu ve self

`__init__` metodu, nesne oluşturulduğunda otomatik çalışan yapıcı (constructor) metodudur.

```python
class Personel:                        # Sınıf tanımlanır
    def __init__(self, ad, soyad, yas):  # Yapıcı metot tanımlanır
        self.ad = ad                   # Nesneye ad niteliği atanır
        self.soyad = soyad             # Nesneye soyad niteliği atanır
        self.yas = yas                 # Nesneye yas niteliği atanır
    
    def bilgi_goster(self):            # Örnek metot tanımlanır
        print(f"{self.ad} {self.soyad}, {self.yas} yaşında")  # Bilgiler yazdırılır

p1 = Personel("Züber", "Doğan", 30)    # Nesne parametrelerle oluşturulur
p1.bilgi_goster()                      # Nesne metodu çağrılır
```

**Çıktı:**
```
Züber Doğan, 30 yaşında
```

---

### 9.5 Kalıtım (Inheritance)

Kalıtım, bir sınıfın başka bir sınıftan özellik ve davranış devralmasını sağlar.

```python
class Personel:                        # Temel sınıf (parent class)
    def __init__(self, isim):          # Yapıcı metot
        self.isim = isim               # İsim niteliği

class Detay(Personel):                 # Alt sınıf, Personel'den miras alır
    def __init__(self, isim, bolum, unvan):  # Alt sınıf yapıcısı
        super().__init__(isim)         # Üst sınıfın yapıcısı çağrılır
        self.bolum = bolum             # Ek nitelik: bölüm
        self.unvan = unvan             # Ek nitelik: ünvan
    
    def bilgi(self):                   # Alt sınıfa özgü metot
        print(f"{self.isim} - {self.bolum} - {self.unvan}")

d1 = Detay("Züber", "Bilişim", "Uzman") # Alt sınıftan nesne oluşturulur
d1.bilgi()                             # Alt sınıf metodu çağrılır
```

---

### 9.6 OOP Kavramları Özeti

| Kavram | Açıklama |
|--------|----------|
| `class` | Sınıf tanımlama anahtar kelimesi |
| `object` | Sınıftan oluşturulan örnek |
| `__init__` | Yapıcı (constructor) metot |
| `self` | Nesnenin kendisine referans |
| Inheritance | Kalıtım - özellik devralma |
| `super()` | Üst sınıfa erişim |

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `09-moduller-oop.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. Dikdörtgen sınıfı oluşturunuz. Alan ve çevre hesaplayan metotlar ekleyiniz.
2. Banka hesabı sınıfı oluşturunuz. Para yatırma ve çekme metotları ekleyiniz.
3. Öğrenci sınıfından miras alan LisansOgrencisi ve YuksekLisansOgrencisi sınıfları yazınız.
4. Araç sınıfı oluşturup, Otomobil ve Motosiklet alt sınıfları tanımlayınız.
