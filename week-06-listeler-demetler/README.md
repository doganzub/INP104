# Hafta 6: Listeler ve Demetler (Lists & Tuples)

## Konu Özeti

Bu hafta Python'da **listeler** ve **demetler** (tuples) kapsamlı şekilde işlenmektedir. Her iki veri tipi de birden fazla öğeyi bir arada tutar, ancak önemli farkları vardır.

---

## Neden Önemli?

- Listeler, birçok veriyi organize etmek için kullanılır
- Kullanıcıdan gelen verilerin toplanması
- Dosyadan okunan satırların saklanması
- Veritabanı sorgu sonuçlarının işlenmesi

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- Liste ve demet tanımlayabilecektir
- Liste öğelerine indeks ve dilimleme ile erişebilecektir
- Listelerin **mutable** (değiştirilebilir) özelliğini anlayacaktır
- Temel liste metotlarını (`append`, `extend`, `insert`, `remove`, `pop`, `sort`) kullanabilecektir
- Liste kopyalama yöntemlerini bilecektir
- Demetlerin **immutable** özelliğini kavrayacaktır

---

## Konu Başlıkları

### 6.1 Liste Tanımlama
- Köşeli parantez `[]` ile tanımlama
- `list()` fonksiyonu ile dönüşüm
- Farklı veri tiplerini içeren listeler

---

### 6.2 Liste Öğelerine Erişim
- Pozitif ve negatif indeksleme
- Dilimleme (slicing)
- İç içe listelere erişim

---

### 6.3 Listeler Mutable (Değiştirilebilir)
- Öğe değiştirme
- Toplu değişiklik (dilimleme ile)

---

### 6.4 Liste Birleştirme ve Öğe Ekleme
- `+` işleci ile birleştirme
- `del` ile öğe silme

---

### 6.5 Liste Metotları

| Metot | Açıklama |
|-------|----------|
| `append()` | Sona tek öğe ekle |
| `extend()` | Birden fazla öğe ekle |
| `insert()` | Belirli konuma ekle |
| `remove()` | Değere göre sil |
| `pop()` | İndekse göre sil ve döndür |
| `sort()` | Sırala |
| `reverse()` | Ters çevir |
| `count()` | Öğe say |
| `index()` | İndeks bul |

---

### 6.6 Liste Kopyalama
- Referans vs bağımsız kopya
- `copy()`, `list()`, `[:]` yöntemleri

---

### 6.7 Demetler (Tuple)
- `()` ile tanımlama
- Tek öğeli demet: `(öğe,)` - virgül zorunlu!
- Immutable (değiştirilemez)
- `count()` ve `index()` metotları

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `06-listeler-demetler.ipynb` | Haftalık ders notebooku |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Listeler bölümü (satır 23586+)
- Liste metotları bölümü (satır 26468+)

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
