# Hafta 6: Listeler ve Demetler

## Konu Özeti

Bu hafta Python'da en sık kullanılan veri yapılarından olan listeler ve demetler incelenmektedir. Listeler değiştirilebilir (mutable) veri yapılarıdır ve eleman ekleme, silme, değiştirme işlemlerine izin verir. Demetler ise değiştirilemez (immutable) yapılardır ve oluşturulduktan sonra içerikleri değiştirilemez.

---

## Neden Önemli

Listeler ve demetler, birden fazla veriyi tek bir değişkende saklamak için kullanılır. Öğrenci listeleri, ürün katalogları, koordinat bilgileri gibi pek çok farklı senaryoda bu veri yapıları kullanılmaktadır. Listelerin değiştirilebilir olması dinamik veri yönetimi sağlarken, demetlerin değiştirilemez olması veri güvenliği sağlar.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- Liste oluşturma ve elemanlara erişebilme
- Liste metotlarını etkin kullanabilme
- Demet yapısını anlama ve kullanabilme
- Liste ve demet arasındaki farkları kavrama

---

## Konu Başlıkları

### 6.1 Liste Oluşturma ve Erişim

Listeler köşeli parantez `[]` ile tanımlanır ve farklı veri tiplerini barındırabilir.

```python
# Liste oluşturma yöntemleri
bos_liste = []                         # Boş liste oluşturulur
sayilar = [1, 2, 3, 4, 5]              # Sayı listesi tanımlanır
karisik = ["Python", 42, 3.14, True]   # Farklı tipler bir arada olabilir
ic_ice = ["Minas", "ganimet", ["züber", "idil", "uygar"]]  # İç içe liste
```

**Elemanlara Erişim:**

```python
meyveler = ["elma", "armut", "muz", "çilek"]  # Meyve listesi

print(meyveler[0])                     # İlk eleman: "elma"
print(meyveler[2])                     # Üçüncü eleman: "muz"
print(meyveler[-1])                    # Son eleman: "çilek"
print(meyveler[-2])                    # Sondan ikinci: "muz"
```

**Eleman Değiştirme:**

```python
liste = ["Minas", "ganimet", "züber"]  # Orijinal liste
liste[0] = "Minas Doğan"               # İlk eleman değiştirilir
print(liste)                           # ['Minas Doğan', 'ganimet', 'züber']
```

---

### 6.2 Liste Metotları

**append() - Sona Eleman Ekleme:**

```python
liste = ["elma", "armut"]              # Başlangıç listesi
liste.append("muz")                    # Listenin sonuna "muz" eklenir
print(liste)                           # ['elma', 'armut', 'muz']
```

**insert() - Belirli Konuma Ekleme:**

```python
liste = ["elma", "muz", "çilek"]       # Başlangıç listesi
liste.insert(1, "armut")               # 1. indekse "armut" eklenir
print(liste)                           # ['elma', 'armut', 'muz', 'çilek']
```

**remove() - Değere Göre Silme:**

```python
liste = ["elma", "armut", "muz"]       # Başlangıç listesi
liste.remove("armut")                  # "armut" değeri listeden silinir
print(liste)                           # ['elma', 'muz']
```

**sort() - Sıralama:**

```python
sayilar = [3, 1, 4, 1, 5, 9, 2]        # Sırasız sayı listesi
sayilar.sort()                         # Küçükten büyüğe sıralama
print(sayilar)                         # [1, 1, 2, 3, 4, 5, 9]

sayilar.sort(reverse=True)             # Büyükten küçüğe sıralama
print(sayilar)                         # [9, 5, 4, 3, 2, 1, 1]
```

**reverse() - Ters Çevirme:**

```python
liste = ["a", "b", "c", "d"]           # Orijinal liste
liste.reverse()                        # Liste ters çevrilir
print(liste)                           # ['d', 'c', 'b', 'a']
```

---

### 6.3 Liste Kopyalama

Python'da listeler referans olarak atanır. Gerçek kopya oluşturmak için özel yöntemler kullanılmalıdır.

```python
# Yanlış kopylama (referans)
liste1 = [1, 2, 3]                     # Orijinal liste
liste2 = liste1                        # Aynı listeye referans verir
liste2[0] = 99                         # Her iki listeyi de etkiler
print(liste1)                          # [99, 2, 3]

# Doğru kopyalama (bağımsız kopya)
liste1 = [1, 2, 3]                     # Orijinal liste
liste2 = list(liste1)                  # Bağımsız kopya oluşturulur
liste2[0] = 99                         # Sadece liste2'yi etkiler
print(liste1)                          # [1, 2, 3] - Değişmedi
print(liste2)                          # [99, 2, 3]
```

---

### 6.4 Demetler (Tuple)

Demetler parantez `()` ile tanımlanır ve oluşturulduktan sonra değiştirilemez.

```python
# Demet oluşturma
koordinat = (10, 20)                   # Koordinat demeti
renkler = ("kırmızı", "yeşil", "mavi") # Renk demeti
tek_eleman = ("Python",)               # Tek elemanlı demet (virgül gerekli)
```

**Demet Erişimi:**

```python
demet = ("can", "murat", "aslı")       # İsim demeti
print(demet[0])                        # İlk eleman: "can"
print(demet[-1])                       # Son eleman: "aslı"
```

**Demet Değiştirilemez:**

```python
demet = ("elma", "armut")              # Demet tanımlanır
# demet[0] = "muz"                     # HATA! Demetler değiştirilemez
```

---

### 6.5 Liste ve Demet Karşılaştırması

| Özellik | Liste | Demet |
|---------|-------|-------|
| Tanımlama | `[1, 2, 3]` | `(1, 2, 3)` |
| Değiştirilebilir | Evet | Hayır |
| Eleman ekleme | `append()`, `insert()` | Yapılamaz |
| Eleman silme | `remove()`, `pop()` | Yapılamaz |
| Performans | Daha yavaş | Daha hızlı |
| Kullanım | Dinamik veriler | Sabit veriler |

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `06-listeler-demetler.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. Kullanıcıdan 5 sayı alarak bunları bir listede saklayınız ve toplamını hesaplayınız.
2. Bir listedeki en büyük ve en küçük elemanı bulan program yazınız.
3. İki listenin ortak elemanlarını bulan program yazınız.
4. Bir listedeki tekrar eden elemanları kaldıran program yazınız.
