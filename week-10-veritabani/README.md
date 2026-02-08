# Hafta 10: Veri Tabanı İşlemleri (SQLite)

## Konu Özeti

Bu hafta Python ile SQLite veri tabanı işlemleri incelenmektedir. SQLite, sunucu gerektirmeyen, dosya tabanlı hafif bir veri tabanı yönetim sistemidir. Python'un `sqlite3` modülü ile kolayca kullanılabilir ve CRUD (Create, Read, Update, Delete) işlemleri gerçekleştirilebilir.

---

## Neden Önemli

Veri tabanları, uygulamaların kalıcı ve yapılandırılmış veri saklamasını sağlar. Kullanıcı bilgileri, ürün katalogları, işlem kayıtları gibi veriler veri tabanlarında saklanır. SQLite, öğrenme aşamasında ve küçük-orta ölçekli projelerde ideal bir seçenektir.

---

## Öğrenme Hedefleri

Bu bölümü tamamladığınızda aşağıdaki becerileri kazanmış olacaksınız:

- SQLite3 modülünü kullanabilme
- Veri tabanı ve tablo oluşturabilme
- CRUD işlemlerini uygulayabilme
- Parametreli sorgular yazabilme
- `with` ifadesi ile güvenli bağlantı yönetimi

---

## Konu Başlıkları

### 10.1 Veri Tabanı Bağlantısı

SQLite veri tabanına bağlanmak için `sqlite3.connect()` fonksiyonu kullanılır.

```python
import sqlite3                         # sqlite3 modülü import edilir

vt = sqlite3.connect('ornek.db')       # Veri tabanı dosyası oluşturulur/açılır
im = vt.cursor()                       # İmleç (cursor) nesnesi oluşturulur
# Veri tabanı işlemleri burada yapılır
vt.close()                             # Bağlantı kapatılır
```

---

### 10.2 Tablo Oluşturma

`CREATE TABLE` SQL komutu ile tablolar oluşturulur.

```python
import sqlite3                         # sqlite3 modülü import edilir

vt = sqlite3.connect('ornek.db')       # Veri tabanına bağlanılır
im = vt.cursor()                       # İmleç oluşturulur

im.execute('''CREATE TABLE IF NOT EXISTS personel (
    no INTEGER PRIMARY KEY,            -- Birincil anahtar, otomatik artan
    isim TEXT NOT NULL,                -- Zorunlu metin alanı
    statu TEXT,                        -- İsteğe bağlı metin alanı
    yas INTEGER                        -- Tam sayı alanı
)''')                                  # Tablo oluşturma sorgusu çalıştırılır

vt.commit()                            # Değişiklikler kaydedilir
vt.close()                             # Bağlantı kapatılır
```

---

### 10.3 Veri Ekleme (INSERT)

`INSERT INTO` komutu ile tabloya yeni kayıtlar eklenir.

```python
import sqlite3                         # sqlite3 modülü import edilir

vt = sqlite3.connect('ornek.db')       # Veri tabanına bağlanılır
im = vt.cursor()                       # İmleç oluşturulur

# Parametreli sorgu (güvenli yöntem)
veri = (1, "Züber Doğan", "Uzman", 30) # Eklenecek veri tuple olarak hazırlanır
im.execute("INSERT INTO personel VALUES (?, ?, ?, ?)", veri)  # Soru işaretleri değerlerle değiştirilir

vt.commit()                            # Değişiklikler kaydedilir
print(f"{im.rowcount} kayıt eklendi")  # Eklenen kayıt sayısı yazdırılır
vt.close()                             # Bağlantı kapatılır
```

---

### 10.4 Veri Okuma (SELECT)

`SELECT` komutu ile tablodaki veriler okunur.

```python
import sqlite3                         # sqlite3 modülü import edilir

vt = sqlite3.connect('ornek.db')       # Veri tabanına bağlanılır
im = vt.cursor()                       # İmleç oluşturulur

im.execute("SELECT * FROM personel")   # Tüm kayıtları seçen sorgu çalıştırılır
kayitlar = im.fetchall()               # Tüm sonuçlar alınır

for kayit in kayitlar:                 # Her kayıt işlenir
    print(kayit)                       # Kayıt yazdırılır

vt.close()                             # Bağlantı kapatılır
```

**Koşullu Sorgular:**

```python
im.execute("SELECT * FROM personel WHERE yas > 30")  # 30 yaş üstü kayıtlar seçilir
sonuclar = im.fetchall()               # Sonuçlar alınır
```

---

### 10.5 Veri Güncelleme (UPDATE)

`UPDATE` komutu ile mevcut kayıtlar değiştirilir.

```python
import sqlite3                         # sqlite3 modülü import edilir

vt = sqlite3.connect('ornek.db')       # Veri tabanına bağlanılır
im = vt.cursor()                       # İmleç oluşturulur

im.execute("UPDATE personel SET statu = 'Genel Müdür' WHERE no = 1")  # 1 nolu kaydın statüsü güncellenir

vt.commit()                            # Değişiklikler kaydedilir
print(f"{im.rowcount} kayıt güncellendi")  # Güncellenen kayıt sayısı yazdırılır
vt.close()                             # Bağlantı kapatılır
```

---

### 10.6 Veri Silme (DELETE)

`DELETE` komutu ile kayıtlar silinir.

```python
import sqlite3                         # sqlite3 modülü import edilir

vt = sqlite3.connect('ornek.db')       # Veri tabanına bağlanılır
im = vt.cursor()                       # İmleç oluşturulur

im.execute("DELETE FROM personel WHERE no = 4")  # 4 nolu kayıt silinir

vt.commit()                            # Değişiklikler kaydedilir
print(f"{im.rowcount} kayıt silindi")  # Silinen kayıt sayısı yazdırılır
vt.close()                             # Bağlantı kapatılır
```

---

### 10.7 with İfadesi ile Güvenli Yönetim

`with` ifadesi, bağlantının otomatik kapatılmasını sağlar.

```python
import sqlite3                         # sqlite3 modülü import edilir

with sqlite3.connect('ornek.db') as vt:  # Bağlantı with bloğu içinde açılır
    im = vt.cursor()                   # İmleç oluşturulur
    im.execute("SELECT * FROM personel")  # Sorgu çalıştırılır
    for kayit in im.fetchall():        # Sonuçlar işlenir
        print(kayit)                   # Her kayıt yazdırılır
# Blok bitince commit() ve close() otomatik çağrılır
```

---

### 10.8 Pratik Uygulama: Ürün Yönetimi

```python
import sqlite3                         # sqlite3 modülü import edilir

def veritabani_olustur():              # Veri tabanı oluşturma fonksiyonu
    with sqlite3.connect('urunler.db') as vt:  # Bağlantı açılır
        im = vt.cursor()               # İmleç oluşturulur
        im.execute('''CREATE TABLE IF NOT EXISTS urunler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Otomatik artan ID
            ad TEXT NOT NULL,          -- Ürün adı (zorunlu)
            fiyat REAL NOT NULL,       -- Fiyat (ondalıklı)
            stok INTEGER DEFAULT 0     -- Stok (varsayılan 0)
        )''')                          # Tablo oluşturulur

def urun_ekle(ad, fiyat, stok):        # Ürün ekleme fonksiyonu
    with sqlite3.connect('urunler.db') as vt:
        im = vt.cursor()
        im.execute("INSERT INTO urunler (ad, fiyat, stok) VALUES (?, ?, ?)",
                   (ad, fiyat, stok))  # Parametreli sorgu ile ürün eklenir

def urunleri_listele():                # Ürün listeleme fonksiyonu
    with sqlite3.connect('urunler.db') as vt:
        im = vt.cursor()
        im.execute("SELECT * FROM urunler")  # Tüm ürünler seçilir
        return im.fetchall()           # Sonuçlar döndürülür

# Kullanım
veritabani_olustur()                   # Veri tabanı oluşturulur
urun_ekle("Laptop", 15000, 10)         # Ürün eklenir
print(urunleri_listele())              # Ürünler listelenir
```

---

## SQL Komutları Özet Tablosu

| Komut | Açıklama | Örnek |
|-------|----------|-------|
| `CREATE TABLE` | Tablo oluşturma | `CREATE TABLE adi (...)` |
| `INSERT INTO` | Veri ekleme | `INSERT INTO tablo VALUES (...)` |
| `SELECT` | Veri okuma | `SELECT * FROM tablo` |
| `UPDATE` | Veri güncelleme | `UPDATE tablo SET alan=deger` |
| `DELETE` | Veri silme | `DELETE FROM tablo WHERE ...` |

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `10-veritabani.ipynb` | Haftalık ders notebooku |

---

## Alıştırma Soruları

1. Öğrenci bilgilerini saklayan bir veri tabanı ve CRUD fonksiyonları yazınız.
2. Kütüphane sistemi için kitap ve ödünç alma tabloları tasarlayınız.
3. Basit bir not defteri uygulaması geliştirip, notları veri tabanında saklayınız.
4. Ürün envanter sistemi tasarlayarak stok takibi yapan program yazınız.
