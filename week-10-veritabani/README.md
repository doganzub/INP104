# Hafta 10: Veri Tabanı İşlemleri (SQLite)

## Konu Özeti

Bu hafta, Python ile SQLite veri tabanı işlemleri öğrenilir.

---

## Öğrenme Hedefleri

- SQLite3 modülünü kullanmak
- Veri tabanı ve tablo oluşturmak
- CRUD işlemlerini uygulamak (Create, Read, Update, Delete)
- Parametreli sorgular yazmak

---

## Konu Başlıkları

### 10.1 Veri Tabanı Bağlantısı
```python
import sqlite3
vt = sqlite3.connect('veritabani.db')
im = vt.cursor()
```

### 10.2 SQL Komutları
| Komut | Açıklama |
|-------|----------|
| `CREATE TABLE` | Tablo oluştur |
| `INSERT INTO` | Veri ekle |
| `SELECT` | Veri oku |
| `UPDATE` | Veri güncelle |
| `DELETE` | Veri sil |

### 10.3 with İfadesi
```python
with sqlite3.connect('vt.db') as vt:
    im = vt.cursor()
    # işlemler
# Otomatik kapanır
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `10-veritabani.ipynb` | Haftalık ders notebooku |
