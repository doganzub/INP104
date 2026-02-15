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

---
---

# INP104 - GENEL DERS CERCEVESI VE ANALITIK BUYUK RESIM

> **Bu bolum, tum 10 haftalik ders iceriginin analitik bir cercevesini cizip buyuk resmi ortaya koyan, AI dostu referans dokumanidir.**

---

## 1. DERSIN VIZYONU VE AMACI

**Ders Kodu:** INP104 - Bilgisayar Programlama (Python)
**Platform:** Google Colab (kurulum gereksiz, tarayici tabanli)
**Referans Kaynak:** `/docs/yazbel.md` (Python Referans Belgesi)
**Hedef Kitle:** Programlamaya ilk kez baslayan universite ogrencileri
**Donem Suresi:** 10 hafta (1 donem)

**Temel Vizyon:** Programlama bilgisi sifir olan bir ogrenciyi, donem sonunda Python ile dosya islemleri, veritabani yonetimi ve nesne tabanli programlama yapabilecek seviyeye tasimak.

**Pedagojik Yaklasim:** Her hafta, bir onceki haftanin kazanimlarinin uzerine insa edilir (spiral ogrenme modeli). Teori-pratik dengesi her hafta Jupyter Notebook uzerinde korunur.

---

## 2. HAFTA HAFTA ANALITIK YAPILANDIRMA

### FAZI 1: TEMELLER (Hafta 1-3) — Programlamanin Alfabesi

#### Hafta 1: Python'a Giris
| Bilesen | Detay |
|---------|-------|
| **Konular** | `print()`, tirnak kullanimeri, veri tipleri (`str`, `int`, `float`), `type()`, `len()`, kacis dizileri, `sep`/`end` parametreleri |
| **Kazanimlar** | Ekrana cikti verebilir, veri tiplerini tanimlayabilir, temel gomulu fonksiyonlari kullanabilir |
| **Zorluk Seviyesi** | Dusuk (giris seviyesi) |
| **Kritik Nokta** | Ogrencinin Python'a motivasyonu burada belirlenir. "Neden Python?" sorusunun ikna edici cevaplanmasi gerekir |
| **Onkosul** | Yok |
| **Gorev Sayisi** | Notebook icerisinde inline |

#### Hafta 2: Gomulu Fonksiyonlar ve Degiskenler
| Bilesen | Detay |
|---------|-------|
| **Konular** | Degisken tanimlama, isimlendirme kurallari, `input()`, tip donusumu (`int()`, `float()`, `str()`), `format()`, f-string, `round()`, `bool()` |
| **Kazanimlar** | Kullanicidan veri alabilir, tip donusumu yapabilir, metin bicimlendirme uygulayabilir |
| **Zorluk Seviyesi** | Dusuk-Orta |
| **Kritik Nokta** | `input()` fonksiyonunun **daima string dondurdugu** kavranmalidir. Tip donusumu yapilmadan matematiksel islem yapilamaz |
| **Onkosul** | Hafta 1 |
| **Gorev Sayisi** | 19 gorev + cevap anahtari |

#### Hafta 3: Kosullu Ifadeler
| Bilesen | Detay |
|---------|-------|
| **Konular** | `if`, `elif`, `else`, karsilastirma operatorleri (`==`, `!=`, `<`, `>`, `<=`, `>=`), mantiksal operatorler (`and`, `or`, `not`), ic ice kosullar |
| **Kazanimlar** | Programlarin kosula gore davranis sergilemesini saglayabilir, karmasik karar yapilari tasarlayabilir |
| **Zorluk Seviyesi** | Orta |
| **Kritik Nokta** | `=` (atama) ile `==` (karsilastirma) farki. `if` ile `elif` arasindaki mantiksal fark (tumu calisir vs. ilk dogru calisir) |
| **Onkosul** | Hafta 1-2 |
| **Gorev Sayisi** | 16 gorev + cevap anahtari |

---

### FAZ 2: DONGULER VE VERI YAPILARI (Hafta 4-6) — Programlamanin Iskelet Sistemi

#### Hafta 4: Donguler (while, for)
| Bilesen | Detay |
|---------|-------|
| **Konular** | `while`, `while True` + `break`, `for`, `range()` (3 parametre), `break`/`continue`/`pass`, dongu + `else`, ic ice donguler, while vs for karsilastirmasi |
| **Kazanimlar** | Tekrarlayan islemleri otomtiklestirebilir, dongu kontrol deyimlerini dogru kullanabilir, ic ice dongulerle karmasik yapilar tasarlayabilir |
| **Zorluk Seviyesi** | Orta-Yuksek |
| **Kritik Nokta** | **Sonsuz dongu riski** en buyuk tuzaktir. `while` dongusunde kosulu degistiren kodun unutulmasi. `range()` fonksiyonunda `stop` degerinin dahil olmadiginin kavranmasi |
| **Onkosul** | Hafta 1-3 |
| **Gorev Sayisi** | 21 gorev + cevap anahtari |

#### Hafta 5: Karakter Dizileri ve Metotlari
| Bilesen | Detay |
|---------|-------|
| **Konular** | Indeksleme (pozitif/negatif), dilimleme (slicing), immutability, string metotlari (`replace`, `split`, `join`, `lower`, `upper`, `count`, `find`, `strip`, `startswith`, `endswith`, `isdigit`, `isalpha`), `enumerate()` |
| **Kazanimlar** | Metin verilerini indeksleyebilir, dilimleyebilir, degistiremezlik kavramini anlayabilir, string metotlarini etkin kullanabilir |
| **Zorluk Seviyesi** | Orta |
| **Kritik Nokta** | **Immutability (degistirilemezlik)** kavrami. `metin[0] = "X"` yapilamaz; yeniden atama gerekir. Dilimleme soz diziminde `baslangic` dahil, `bitis` dahil degil kurali |
| **Onkosul** | Hafta 1-4 |
| **Gorev Sayisi** | 22 gorev + cevap anahtari |

#### Hafta 6: Listeler ve Demetler
| Bilesen | Detay |
|---------|-------|
| **Konular** | Liste tanimlama, indeksleme/dilimleme, mutable ozellik, liste metotlari (`append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`, `count`, `index`), liste kopyalama (referans vs kopya), demetler (tuple), immutable |
| **Kazanimlar** | Birden fazla veriyi organize edebilir, liste metotlariyla veri manipulasyonu yapabilir, mutable/immutable farkini kavrayabilir |
| **Zorluk Seviyesi** | Orta-Yuksek |
| **Kritik Nokta** | **Referans vs kopya** meselesi. `liste2 = liste1` atamasinin bagimsiz kopya olusturMAdiginin kavranmasi. `copy()`, `list()`, `[:]` yontemleri. Tek ogeli demette virgulun (`(oge,)`) zorunlulugu |
| **Onkosul** | Hafta 1-5 |
| **Gorev Sayisi** | 17 gorev + cevap anahtari |

---

### FAZ 3: ILERI KONULAR (Hafta 7-10) — Gercek Dunya Becerileri

#### Hafta 7: Dosya Islemleri
| Bilesen | Detay |
|---------|-------|
| **Konular** | `open()`, dosya kipleri (`r`, `w`, `a`), `read()`, `readline()`, `readlines()`, `with` ifadesi, hata yonetimi (`try-except`, `FileNotFoundError`, `PermissionError`), `seek()`, `tell()`, `writelines()` |
| **Kazanimlar** | Dosyadan veri okuyabilir ve dosyaya yazabilir, `with` ile guvenli dosya yonetimi yapabilir, hataları yakalayabilir |
| **Zorluk Seviyesi** | Orta-Yuksek |
| **Kritik Nokta** | `"w"` kipinin mevcut icerigi **tamamen silmesi**. Dosya kapatmayi unutmanin veri kaybina yol acmasi. `with` ifadesinin neden tercih edilmesi gerektigi |
| **Onkosul** | Hafta 1-6 |
| **Gorev Sayisi** | 13 gorev + cevap anahtari |

#### Hafta 8: Fonksiyonlar
| Bilesen | Detay |
|---------|-------|
| **Konular** | `def`, parametreli fonksiyonlar, pozisyonel/isimli argumanlar, varsayilan degerler, `return`, `print()` vs `return` farki, coklu deger dondurme, `*args`, `**kwargs`, docstring, `__doc__` |
| **Kazanimlar** | Tekrar kullanilabilir kod bloklari olusturabilir, moduler programlama yapabilir, esnek parametre yapilari kullanabilir |
| **Zorluk Seviyesi** | Yuksek |
| **Kritik Nokta** | `print()` ile `return` arasindaki fark en cok karistirilan konudur. `*args` ve `**kwargs` soyut kavramlardir. Fonksiyon TANIMLAMAK ile CAGIRMAK arasindaki fark |
| **Onkosul** | Hafta 1-7 |
| **Gorev Sayisi** | 15 gorev + cevap anahtari |

#### Hafta 9: Moduller ve OOP (Nesne Tabanli Programlama)
| Bilesen | Detay |
|---------|-------|
| **Konular** | `import`, `from ... import`, `as` takma ad, standart kutuphane modulleri (`os`, `random`, `sys`, `math`, `datetime`), `class` ile sinif tanimlama, `__init__`, `self`, nitelik/metot, kalitim (inheritance), `super()` |
| **Kazanimlar** | Modulleri ice aktarabilir, sinif ve nesne olusturabilir, kalitim ile kod genisletebilir |
| **Zorluk Seviyesi** | Yuksek |
| **Kritik Nokta** | OOP, tum donem boyunca islenen prosedural mantiktan **paradigma degisikligi** gerektirir. `self` kavraminin anlasilmasi en buyuk zorluktur. Sinif niteligi vs ornek niteligi farki |
| **Onkosul** | Hafta 1-8 (ozellikle Hafta 8: Fonksiyonlar) |
| **Gorev Sayisi** | 11 gorev + cevap anahtari |

#### Hafta 10: Veritabani Islemleri (SQLite)
| Bilesen | Detay |
|---------|-------|
| **Konular** | `sqlite3` modulu, `connect()`, `cursor()`, `commit()`, `close()`, `CREATE TABLE`, `INSERT`, `SELECT` (`fetchone`, `fetchall`, `fetchmany`), `WHERE`, `ORDER BY`, `LIMIT`, SQL fonksiyonlari (`COUNT`, `AVG`, `SUM`, `MIN`, `MAX`), `UPDATE`, `DELETE`, parametreli sorgular, `with` ifadesi |
| **Kazanimlar** | Veri tabani olusturabilir, CRUD islemlerini gerceklestirebilir, SQL sorgulari yazabilir |
| **Zorluk Seviyesi** | Yuksek |
| **Kritik Nokta** | Python + SQL sentaksinin ayni anda kullanilmasi. `commit()` unutulursa degisiklikler kaybolur. SQL injection riski ve parametreli sorgularin onemi |
| **Onkosul** | Hafta 1-9 (ozellikle Hafta 7: Dosya Islemleri) |
| **Gorev Sayisi** | 12 gorev + cevap anahtari |

---

## 3. ZORLUK HARITASI VE ILERLEME EGRIS

```
Zorluk
  ^
  |                                            ██ Hafta 10
  |                                      ██ Hafta 9  (Veritabani)
  |                                ██ Hafta 8  (OOP)
  |                          ██ Hafta 7  (Fonksiyonlar)
  |                    ██ Hafta 6  (Dosya)
  |              ████ Hafta 4-5  (Listeler)
  |        ██ Hafta 3  (Donguler, Stringler)
  |  ████ Hafta 1-2  (Kosullar)
  | (Giris, Degiskenler)
  +-----------------------------------------> Hafta
    1    2    3    4    5    6    7    8    9   10
```

**Zorluk Artis Profili:**
- **Hafta 1-2:** Yavas baslangic, motivasyon olusturma
- **Hafta 3:** Ilk soyutlama adimi (kosullu dusunme)
- **Hafta 4:** Ilk buyuk zorluk sivrilmesi (donguler + sonsuz dongu riski)
- **Hafta 5-6:** Veri yapilari (mutable/immutable farki)
- **Hafta 7-8:** Paradigma gecisi (dosya + fonksiyon = moduler dusunme)
- **Hafta 9-10:** Zirve zorluk (OOP paradigma degisikligi + SQL cift dil)

---

## 4. KUMULATIF KAZANIM TABLOSU

| Donem Sonu Kazanimi | Ilgili Haftalar |
|---------------------|-----------------|
| Ekrana cikti verme ve veri tiplerini tanima | 1 |
| Kullanicidan veri alma ve isleme | 2 |
| Kosula gore karar verme | 3 |
| Tekrarlayan islemleri otomatiklestirme | 4 |
| Metin verileri uzerinde islem yapma | 5 |
| Birden fazla veriyi organize etme | 6 |
| Dosyadan okuma ve dosyaya yazma | 7 |
| Tekrar kullanilabilir kod bloku olusturma | 8 |
| Moduler ve nesne tabanli programlama | 9 |
| Veritabani ile kalici veri yonetimi | 10 |

**Donem Sonu Butunlesik Yeterlilik:**
Ogrenci, kullanicidan veri alan, bu veriyi kosullara gore isleyen, dosyalarda saklayan, veritabanina kaydeden ve tum bunlari fonksiyonlarla modüler sekilde yapan bir Python programi yazabilir hale gelir.

---

## 5. PEDAGOJIK YONTEMLER VE ARACLAR

| Yontem | Uygulama |
|--------|----------|
| **Spiral Ogrenme** | Her hafta oncekinin uzerine insa eder; onceki konular yeni bagllamarda tekrar kullanilir |
| **Google Colab** | Kurulum engeli olmadan aninda kod yazma ve calistirma |
| **Jupyter Notebook** | Teori + kod + cikti ayni dokumanda; ogrenci interaktif olarak deneyimler |
| **Inline Yorumlar** | Her kod satirinda ne yapildigini aciklayan yorumlar; ogrenci kodu satin satin okuyarak anlar |
| **Gorev + Cevap Anahtari** | Her hafta sonunda `???` yer tutuculu gorevler ve ayri hurede tamamlanmis cevaplar |
| **Pratik Ornekler** | Her haftanin sonunda gercek hayat problemlerini cozen ornekler (fatura hesaplama, parola dogrulama, hesap makinesi, banka hesabi vb.) |
| **Resmi Pedagojik Dil** | Akademik Turkce; konusma dili kullanilmaz |
| **Python Referans Belgesi** | Tum icerikler `/docs/yazbel.md` kaynagindan alinir |

---

## 6. KRITIK BASARI FAKTORLERI (Dikkat Edilmesi Gerekenler)

### OLMAZ ISE OLMAZLAR

1. **Tip Donusumu Bilinci (Hafta 2+):** `input()` her zaman string dondurur. Matematiksel islem icin `int()` veya `float()` ile donusum sarttir. Bu kavranmazsa Hafta 2'den sonra tum hesaplamalar cokertir.

2. **Girinti (Indentation) Kurali (Hafta 3+):** Python'da girinti sadece estetik degil, **sentaks zorunlulugudur**. `if`, `for`, `while`, `def`, `class` bloklarinin tamami 4 bosluk girintiye bagimlidir. Yanlis girinti = program calismaz.

3. **Mutable vs Immutable Farki (Hafta 5-6):** Karakter dizileri degistirilemez, listeler degistirilebilir. Bu fark kavranmazsa hata ayiklama (debugging) mumkun olmaz.

4. **print() vs return Farki (Hafta 8):** `print()` ekrana yazar ama deger dondurmez. `return` deger dondurur ama ekrana yazmaz. Bu ikisinin birbirine karistirilmasi en yaygin hatalardan biridir.

5. **self Kavrami (Hafta 9):** OOP'de her metot `self` parametresi alir. Bu, nesnenin kendisine referanstir. Kavranmadan sinif yazmak mumkun degildir.

6. **commit() Zorunlulugu (Hafta 10):** SQLite'ta `INSERT`, `UPDATE`, `DELETE` islemlerinden sonra `commit()` cagirilmazsa degisiklikler kaybolur.

### YAYGIN OGRENCI HATALARI VE COZUMLERI

| Hata | Hafta | Cozum |
|------|-------|-------|
| `=` yerine `==` kullanma veya tersi | 3 | `=` atama, `==` karsilastirma oldugunu vurgula |
| Sonsuz dongu | 4 | `while` dongusunde sayaci arttirmayi unutma; `Ctrl+C` ogret |
| `metin[0] = "X"` deneme | 5 | Immutability kavrami; yeniden atama yontemi ogret |
| `liste2 = liste1` ile kopya sandirma | 6 | Referans ve kopya farki; `copy()` yontemi ogret |
| `"w"` kipi ile veri kaybetme | 7 | `"a"` (ekleme) kipi ile farki goster; `with` kullanmayi aliskanlik edindirt |
| Fonksiyon tanimlamayi cagirma sanma | 8 | `def` blogunun tanim oldugunu, `fonksiyon()` cagirisinin ayri oldugunu goster |
| `self` unutma | 9 | Her metotun ilk parametresinin `self` olmasi gerektigini vurgula |
| `commit()` unutma | 10 | Her yazma isleminden sonra `commit()` cagirmayi aliskanlik edindirt |

---

## 7. DONEM BOYUNCA YAPILACAKLAR OZETI

### Ogrenci Icin
- [ ] Her hafta ilgili Jupyter Notebook'u Colab'da acmak ve calistirmak
- [ ] Her hafta sonundaki gorevleri (`???` yer tutucularini) doldurmak
- [ ] Cevap anahtari ile kendi cozumlerini karsilastirmak
- [ ] Pratik ornekleri kendi degerlerimle tekrar denemek
- [ ] Onceki haftalarin konularini yeni haftalarda uyguladigini farketmek

### Egitimci / AI Asistan Icin
- [ ] Her hafta icin notebook + README olusturmak/guncellemek
- [ ] `/docs/yazbel.md` kaynagindan resmi icerigi almak
- [ ] Inline yorumlarla her kod satirini aciklamak
- [ ] Gorevlerin zorluk seviyesini orijinal orneklerle esitlemek
- [ ] Cevap anahtarinin gorevlerle tam uyumlu olmasini saglamak

---

## 8. HAFTA BAZINDA ONKOSL VE BAGIMLILIK MATRISI

```
Hafta 1 (Giris)
  └──> Hafta 2 (Degiskenler, input)
        └──> Hafta 3 (Kosullar)
              └──> Hafta 4 (Donguler)
                    ├──> Hafta 5 (Stringler)
                    │     └──> Hafta 6 (Listeler, Demetler)
                    │           └──> Hafta 7 (Dosya Islemleri)
                    │                 └──> Hafta 10 (Veritabani)
                    └──> Hafta 8 (Fonksiyonlar)
                          └──> Hafta 9 (Moduller, OOP)
```

**Kritik Bagimliliklar:**
- Hafta 4 (Donguler) **tum sonraki haftalarin temelini olusturur**
- Hafta 8 (Fonksiyonlar) **Hafta 9 (OOP) icin sart onkosuldur**
- Hafta 7 (Dosya Islemleri) **Hafta 10 (Veritabani) ile kavramsal kardes konudur** (kalici veri saklama)
- Hafta 5 (Stringler) **Hafta 6 (Listeler) ile yapisal benzerlik gosterir** (indeksleme, dilimleme, metotlar)

---

## 9. AI DOSTU ANALITIK PROMPT FORMATI

Asagidaki blok, bu dersin tamamini ozetleyen, herhangi bir AI asistanin derse hakim olmasini saglayan analitik prompt metnidir:

```
DERS: INP104 - Bilgisayar Programlama (Python)
PLATFORM: Google Colab (Jupyter Notebook)
REFERANS: /docs/yazbel.md (Python Referans Belgesi)
SURE: 10 Hafta
HEDEF KITLE: Programlama bilgisi sifir olan universite ogrencileri
DILI: Turkce (Resmi, pedagojik, akademik)
IKON KURALI: Kullanilmaz (sadece tablo ve baslik hariclari)
YAZBEL KURALI: "Yazbel" kelimesi kullanilmaz; yerine "Python Referans Belgesi" ifadesi tercih edilir

HAFTA YAPISI:
  - Her hafta = 1 Jupyter Notebook (.ipynb) + 1 README.md
  - Notebook = Teori (markdown hucreleri) + Kod Ornekleri (inline yorumlu) + Gorevler (???) + Cevap Anahtari
  - README = Konu ozeti + Ogrenme hedefleri + Konu basliklari + Referanslar

KONU AKISI:
  Hafta 01: Python Giris → print(), veri tipleri, type(), len(), kacis dizileri
  Hafta 02: Degiskenler → input(), tip donusumleri, f-string, format(), round(), bool()
  Hafta 03: Kosullar → if/elif/else, karsilastirma operatorleri, mantiksal operatorler
  Hafta 04: Donguler → while, for, range(), break/continue/pass, ic ice donguler
  Hafta 05: Stringler → indeksleme, dilimleme, immutability, string metotlari, enumerate()
  Hafta 06: Listeler → list metotlari, mutable, kopya vs referans, tuple (immutable)
  Hafta 07: Dosyalar → open(), r/w/a kipleri, read metotlari, with, try-except
  Hafta 08: Fonksiyonlar → def, parametreler, return, *args, **kwargs, docstring
  Hafta 09: Moduller+OOP → import yontemleri, class, __init__, self, kalitim, super()
  Hafta 10: Veritabani → sqlite3, CRUD islemleri, SQL sorgulari, parametreli sorgular

ZORLUK SEVYESI (1-5):
  Hafta 01: 1 | Hafta 02: 2 | Hafta 03: 2 | Hafta 04: 3 |
  Hafta 05: 3 | Hafta 06: 3 | Hafta 07: 4 | Hafta 08: 4 |
  Hafta 09: 5 | Hafta 10: 5

GOREV TOPLAMI: 146+ gorev (her hafta cevap anahtarli)

KRITIK KAVRAMLAR (Bu kavramlar kavranmazsa donem basarisiz olur):
  1. input() daima string dondurur → tip donusumu SART
  2. Python'da girinti = sentaks (4 bosluk zorunlu)
  3. Immutable (str, tuple) vs Mutable (list) farki
  4. print() ekrana yazar, return deger dondurur
  5. Referans vs kopya (liste atamasi)
  6. self = nesnenin kendisine referans
  7. commit() = veritabani degisikliklerini kaydetme

KALITE STANDARTLARI:
  - Her kod satirinda inline yorum
  - Resmi, pedagojik Turkce dil
  - Numarali ve hiyerarsik basliklar (1.1, 1.2 vb.)
  - Kurulum bolumu EKLENMEZ (Colab kullanilir)
  - Tum icerik yazbel.md referans belgesinden alinir
```

---

## 10. DONEM SONU BEKLENEN CIKTILAR

Dersi basariyla tamamlayan bir ogrenci su programi yazabilir hale gelmelidir:

```python
# Donem sonu entegre beceri ornegi:
# - Fonksiyon tanimlama (Hafta 8)
# - Dosya okuma (Hafta 7)
# - Dongu ve kosul (Hafta 3-4)
# - Veritabani kaydi (Hafta 10)
# - String islemleri (Hafta 5)
# - Liste islemleri (Hafta 6)

import sqlite3  # Hafta 9: modul import

def ogrenci_kaydet(dosya_yolu, db_yolu):  # Hafta 8: fonksiyon
    """Dosyadan ogrenci verilerini okur ve veritabanina kaydeder."""

    baglanti = sqlite3.connect(db_yolu)  # Hafta 10: veritabani
    imlec = baglanti.cursor()
    imlec.execute("""
        CREATE TABLE IF NOT EXISTS ogrenciler (
            id INTEGER PRIMARY KEY,
            ad TEXT NOT NULL,
            not_ort REAL
        )
    """)

    with open(dosya_yolu, "r") as dosya:  # Hafta 7: dosya okuma
        satirlar = dosya.readlines()  # Hafta 7: readlines()

    for satir in satirlar:  # Hafta 4: for dongusu
        parcalar = satir.strip().split(",")  # Hafta 5: string metotlari
        if len(parcalar) == 2:  # Hafta 3: kosul
            ad = parcalar[0].title()  # Hafta 5: title()
            notlar = [float(n) for n in parcalar[1].split(";")]  # Hafta 6: liste
            ortalama = round(sum(notlar) / len(notlar), 2)  # Hafta 2: round()
            imlec.execute(
                "INSERT INTO ogrenciler (ad, not_ort) VALUES (?, ?)",
                (ad, ortalama)
            )

    baglanti.commit()  # Hafta 10: commit
    baglanti.close()
    print(f"{len(satirlar)} ogrenci kaydedildi.")  # Hafta 1: print, Hafta 2: f-string
```

**Bu ornekte tum 10 haftanin kazanimlari tek bir programda birlestirilmistir.**

---

> **Not:** Bu cerceve dokumani, dersin butununu analitik olarak gostermek icin hazirlanmistir. Her hafta icin detayli icerik, ilgili klasordeki `README.md` ve `.ipynb` dosyalarinda bulunmaktadir.