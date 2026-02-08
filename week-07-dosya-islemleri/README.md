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

## Alıştırma Görevleri

Notebook'un sonunda görev hücreleri ve bir cevap anahtarı hücresi bulunmaktadır:

### 🟩 Görevler (Cell 30-42)

Her görev ayrı bir kod hücresindedir. Öğrenci `???` işaretlerinin yerine doğru kodları yazar.

| Görev | Konu |
|-------|------|
| Görev 1 | Dosya oluşturma ve yazma – "w" kipi |
| Görev 2 | Dosya ekleme – "a" kipi |
| Görev 3 | read() metodu – Tüm dosyayı okuma |
| Görev 4 | readline() metodu – Satır satır okuma |
| Görev 5 | readlines() metodu – Liste olarak okuma |
| Görev 6 | Dosya üzerinde doğrudan döngü |
| Görev 7 | with ifadesi – Yazma |
| Görev 8 | with ifadesi – Okuma |
| Görev 9 | with ile dosya kopyalama |
| Görev 10 | try-except – FileNotFoundError |
| Görev 11 | seek() ve tell() |
| Görev 12 | writelines() metodu |
| Görev 13 | Pratik Örnek – Kelime sayacı |

### 🟨 Cevap Anahtarı (Cell 43)

Yukarıdaki görevlerin tamamlanmış çözümleri.

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
