# INP104 - Bilgisayar Programlama (Python)

> **AI Asistanlar İçin Rehber Döküman**
> Bu döküman, ders içeriklerinin oluşturulması, bakımı ve geliştirilmesinde AI asistanlara yol göstermek için hazırlanmıştır.

---

## Proje Yapısı ve Amaç

Bu repo, Google Colab ortamında Python programlama dilinin temellerini öğreten 10 haftalık ders içeriğini barındırır. Her hafta için:
- **Jupyter Notebook** (`.ipynb`): Detaylı açıklamalar ve inline yorumlu kod örnekleri
- **README.md**: Konu özeti, öğrenme hedefleri ve referanslar

---

## AI Asistanlar İçin İçerik Oluşturma Rehberi

### Referans Kaynak
Tüm ders içerikleri `/docs/yazbel.md` dosyasındaki Python Referans Belgesi'nden alınmalıdır. Bu dosya Python programlama dilinin Türkçe kapsamlı referansıdır.

### Notebook Formatı (Her Hafta İçin)

Her haftalık notebook şu yapıyı takip etmelidir:

```markdown
# **[Hafta No]. [Konu Başlığı]**

# **[Hafta No].[Alt Konu No] [Alt Başlık]**

[Resmi pedagojik dille yazılmış açıklama paragrafı - yazbel.md'den]

---

### [Detay Başlığı]
[Açıklama metni]
```

### Kod Hücresi Formatı

Her kod hücresinde detaylı inline yorumlar bulunmalıdır:

```python
# [Fonksiyon/konsept açıklaması - ne işe yaradığı]
# [Nasıl kullanıldığının açıklaması]
# [Dikkat edilmesi gereken noktalar]
kod_satırı  # Satır sonu açıklaması
```

### README.md Formatı (Her Hafta İçin)

```markdown
# Hafta [No]: [Konu]

## Konu Özeti
[2-3 cümlelik özet]

## Öğrenme Hedefleri
- [Hedef 1]
- [Hedef 2]

## Konu Başlıkları
### [No] [Başlık]
[Açıklama ve kod örneği]

## Referanslar
- Python Programlama Dili Referans Belgesi
```

---

## Haftalık İçerik Yapısı

| Hafta | Konu | Klasör | Durum |
|-------|------|--------|-------|
| 1 | Python'a Giriş | `week-01-python-giris/` | ✅ Tamamlandı |
| 2 | Gömülü Fonksiyonlar ve Değişkenler | `week-02-fonksiyonlar-degiskenler/` | Bekliyor |
| 3 | Koşullu İfadeler (if-elif-else) | `week-03-kosullu-ifadeler/` | Bekliyor |
| 4 | Döngüler (while, for) | `week-04-donguler/` | Bekliyor |
| 5 | Karakter Dizileri ve Metotları | `week-05-karakter-dizileri/` | Bekliyor |
| 6 | Listeler ve Demetler | `week-06-listeler-demetler/` | Bekliyor |
| 7 | Dosya İşlemleri | `week-07-dosya-islemleri/` | Bekliyor |
| 8 | Fonksiyonlar | `week-08-fonksiyonlar/` | Bekliyor |
| 9 | Modüller ve OOP | `week-09-moduller-oop/` | Bekliyor |
| 10 | Veri Tabanı İşlemleri (SQLite) | `week-10-veritabani/` | Bekliyor |

---

## Klasör Yapısı

```
INP104/
├── README.md                          # Bu dosya (AI rehberi)
├── docs/
│   ├── yazbel.md                      # Ana referans kaynak (Python belgesi)
│   ├── yazbel.pdf                     # Referans PDF
│   └── 2S_task_veri_hazirlama.ipynb   # Örnek format notebook
├── tools/
│   ├── yazbel_web_scraper.py          # Referans içerik çekme scripti
│   └── yazbel_pdf_extractor.py        # PDF dönüştürme scripti
├── week-01-python-giris/
│   ├── README.md
│   └── 01-python-giris.ipynb
├── week-02-fonksiyonlar-degiskenler/
│   ├── README.md
│   └── 02-fonksiyonlar-degiskenler.ipynb
└── ... (diğer haftalar)
```

---

## AI Asistan İçin Görev Talimatları

### Yeni Hafta Oluşturma

1. `docs/yazbel.md` dosyasından ilgili konuyu bul
2. `docs/2S_task_veri_hazirlama.ipynb` örnek formatı incele
3. Notebook oluştur: resmi pedagojik dil + inline yorumlu kodlar
4. README.md oluştur: konu özeti + öğrenme hedefleri

### Görev ve Cevap Anahtarı Ekleme (Her Hafta İçin)

Her haftalık notebook'un **en sonuna** iki adet kod hücresi eklenmelidir:

**1. Hücre – Alıştırma Görevleri (🟩 GÖREV):**
- Notebook'taki **her kod hücresine** karşılık gelen bir görev olmalıdır
- Görevler, orijinal kod örnekleriyle **aynı zorluk seviyesinde** ve **aynı formatta** olmalıdır
- Görevler, orijinal kodlarla **aynı olmamalı**, çok benzer ama farklı değerlerle yazılmalıdır
- Her görev `# 🟩 GÖREV [No]: [Konu Başlığı]` formatında başlamalıdır
- Öğrencinin yapması gereken açıkça yorum satırlarında belirtilmelidir
- Tamamlanacak kod satırları `# ??? ` yer tutucularıyla verilmelidir
- Her görevde ilgili orijinal örneğe `# İpucu:` satırıyla referans verilmelidir

```python
# ============================================================================
# 🟩 GÖREV 1: [Konu Başlığı]
# ============================================================================
# [Öğrencinin ne yapması gerektiğinin açık açıklaması]
#
# İpucu: [orijinal kod örneğine referans]
# ------------------------------------------------------------

# [tamamlanacak_kod = ???]
```

**2. Hücre – Cevap Anahtarı (🟨 CEVAP):**
- Görevlerdeki **her sorunun** tamamlanmış çözümü olmalıdır
- Görevlerle **tam uyumlu** olmalıdır (aynı değişken isimleri, aynı değerler)
- Her cevap `# 🟨 CEVAP [No]: [Konu Başlığı]` formatında başlamalıdır
- Cevaplar arasında `print(f"\n{'-'*82}\n")` ayırıcısı kullanılmalıdır
- Her satırda inline yorum bulunmalıdır

```python
# ============================================================================
# 🟨 CEVAP 1: [Konu Başlığı]
# ============================================================================
tamamlanmis_kod = "değer"  # Satır sonu açıklaması
print(tamamlanmis_kod)  # Beklenen çıktı açıklaması

print(f"\n{'-'*82}\n")
```

**Kontrol Listesi:**
- [ ] Notebook'taki TÜM kod hücreleri için görev var mı?
- [ ] Görevler orijinal kodlarla aynı zorluk seviyesinde mi?
- [ ] Görevler orijinal kodlardan farklı değerler kullanıyor mu?
- [ ] Cevap anahtarı görevlerle tam uyumlu mu?
- [ ] Öğrenci görev açıklamalarını okuyarak ne yapacağını anlayabiliyor mu?

---

### Mevcut İçerik Güncelleme

1. Değiştirilecek dosyayı incele
2. `yazbel.md`'den güncel içeriği al
3. Resmi dil ve inline yorumlarla güncelle

### Kalite Standartları

- **Dil**: Resmi, pedagojik, akademik Türkçe
- **Kod Yorumları**: Her satırda ne yapıldığını açıkla
- **Başlıklar**: Numaralı ve hiyerarşik (1.1, 1.2, vb.)
- **Referans**: Tüm içerik `yazbel.md`'den alınmalı
- **Platform**: Google Colab (kurulum gerektirmez)

---

## Önemli Notlar

- **Kurulum bölümü EKLENMEZ** - Google Colab kullanıldığı için
- **İkonlar kullanılmaz** - Sadece tablo ve başlıklarda
- **Yazbel kelimesi kullanılmaz** - Açıklamalarda "Python Referans Belgesi" ifadesi tercih edilir

---

## Referanslar

- `/docs/yazbel.md` - Ana Python referans kaynağı
- `/docs/2S_task_veri_hazirlama.ipynb` - Örnek notebook formatı
- https://docs.python.org/3/ - Python resmi dokümantasyonu