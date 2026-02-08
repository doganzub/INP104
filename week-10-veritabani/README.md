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

## Alıştırma Görevleri

Notebook'un sonunda görev hücreleri ve bir cevap anahtarı hücresi bulunmaktadır:

### 🟩 Görevler (Cell 35-46)

Her görev ayrı bir kod hücresindedir. Öğrenci `???` işaretlerinin yerine doğru kodları yazar.

| Görev | Konu |
|-------|------|
| Görev 1 | Veri tabanı bağlantısı ve imleç oluşturma |
| Görev 2 | Tablo oluşturma (CREATE TABLE) |
| Görev 3 | Tek kayıt ekleme (INSERT) |
| Görev 4 | Çoklu kayıt ekleme (executemany) |
| Görev 5 | Tüm verileri seçme (SELECT *) |
| Görev 6 | Koşullu seçim (WHERE) |
| Görev 7 | Sıralama ve limit (ORDER BY, LIMIT) |
| Görev 8 | SQL fonksiyonları (COUNT, AVG, MIN, MAX) |
| Görev 9 | Veri güncelleme (UPDATE) |
| Görev 10 | Veri silme (DELETE) |
| Görev 11 | with ifadesi ile güvenli kullanım |
| Görev 12 | Pratik Örnek – Basit kayıt sistemi |

### 🟨 Cevap Anahtarı (Cell 47)

Yukarıdaki görevlerin tamamlanmış çözümleri.

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
