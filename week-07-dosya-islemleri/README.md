# Hafta 7: Dosya İşlemleri (File Operations)

## Konu Özeti

Bu hafta Python'da **dosya işlemleri** kapsamlı şekilde işlenmektedir. Dosyalar, verilerin kalıcı olarak saklanmasını ve programlar arası veri paylaşımını sağlar.

---

## Neden Önemli?

- Kullanıcı verilerinin kalıcı olarak saklanması
- Konfigürasyon dosyalarının okunması
- Log (günlük) dosyalarının oluşturulması
- Veri aktarımı ve yedekleme

---

## Öğrenme Hedefleri

Bu dersin sonunda öğrenci:

- `open()` fonksiyonu ile dosya açabilecektir
- Dosya kiplerini (`r`, `w`, `a`) anlayabilecektir
- `read()`, `readline()`, `readlines()` metotlarını kullanabilecektir
- `with` ifadesinin avantajlarını kavrayacaktır
- Dosya hatalarını `try-except` ile yönetebilecektir
- `seek()` ve `tell()` ile imleç yönetimi yapabilecektir

---

## Konu Başlıkları

### 7.1 Dosya İşlemlerine Giriş
- Dosya işlemlerinin önemi
- Temel işlem adımları: Aç → İşle → Kapat

---

### 7.2 Dosya Açma Kipleri

| Kip | Açıklama |
|-----|----------|
| `"r"` | Okuma (varsayılan) |
| `"w"` | Yazma (mevcut içeriği siler!) |
| `"a"` | Ekleme (sona ekler) |

---

### 7.3 Dosya Okuma

| Metot | Dönen Değer |
|-------|-------------|
| `read()` | Karakter dizisi (tümü) |
| `readline()` | Karakter dizisi (tek satır) |
| `readlines()` | Liste (tüm satırlar) |

---

### 7.4 with İfadesi
- Otomatik dosya kapatma
- Hata durumunda bile güvenli

---

### 7.5 Hata Yönetimi
- `FileNotFoundError`
- `PermissionError`
- `try-except` kullanımı

---

### 7.6 Dosya Metot ve Nitelikleri
- `seek()`, `tell()`
- `writelines()`
- `name`, `mode`, `closed`

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `07-dosya-islemleri.ipynb` | Haftalık ders notebooku |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Dosya İşlemleri bölümü (satır 28600+)

---

## Colab Ortamı

Bu ders Google Colab üzerinde çalışılmaktadır.
