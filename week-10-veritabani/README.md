# Hafta 10: Veri Tabanı İşlemleri (SQLite)

## Konu Özeti

Bu hafta Python ile **SQLite veri tabanı işlemleri** kapsamlı şekilde işlenmektedir. `sqlite3` modülü ile veri tabanı bağlantısı, SQL sorguları ve CRUD işlemleri öğrenilir.

---

## Neden Önemli?

- Verilerin kalıcı olarak saklanmasını sağlar
- Yapılandırılmış veri depolama
- Gerçek dünya uygulamalarının temelini oluşturur

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- `sqlite3` ile veri tabanı bağlantısı kurabilecektir
- `CREATE TABLE` ile tablo oluşturabilecektir
- `INSERT` ile veri ekleyebilecektir
- `SELECT` ile veri sorgulayabilecektir
- `UPDATE` ile veri güncelleyebilecektir
- `DELETE` ile veri silebilecektir
- Parametreli sorgular kullanabilecektir

---

## Konu Başlıkları

### 10.1 SQLite Nedir?
- Dosya tabanlı veri tabanı
- Veri tipleri (INTEGER, TEXT, REAL, BLOB)

---

### 10.2 Veri Tabanı Bağlantısı
- `connect()`, `cursor()`, `commit()`, `close()`

---

### 10.3 Tablo Oluşturma
- `CREATE TABLE IF NOT EXISTS`
- PRIMARY KEY, NOT NULL

---

### 10.4 Veri Ekleme (INSERT)
- Tek kayıt: `execute()`
- Çoklu kayıt: `executemany()`
- Parametreli sorgular (? placeholder)

---

### 10.5 Veri Okuma (SELECT)
- `fetchone()`, `fetchall()`, `fetchmany()`
- WHERE koşulu
- ORDER BY, LIMIT
- COUNT, AVG, SUM, MIN, MAX

---

### 10.6 Veri Güncelleme (UPDATE)
- `UPDATE SET WHERE`
- `rowcount` ile etkilenen satırlar

---

### 10.7 Veri Silme (DELETE)
- `DELETE FROM WHERE`

---

### 10.8 with İfadesi
- Güvenli bağlantı yönetimi
- Otomatik commit ve close

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `10-veritabani.ipynb` | Haftalık ders notebooku |

---

## SQL Komutları Özeti

| Komut | Açıklama |
|-------|----------|
| `CREATE TABLE` | Tablo oluştur |
| `INSERT INTO` | Veri ekle |
| `SELECT` | Veri oku |
| `UPDATE` | Veri güncelle |
| `DELETE FROM` | Veri sil |

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
