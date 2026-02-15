# Hafta 0: Programlama - Derse Genel Bakis ve Kritik Onemi

## Konu Ozeti

Bu ders, INP104 mufredatina baslamadan once ogrenciye **buyuk resmi** gosterir: Programlama bilgisi neden bilisim kariyerinin vazgecilmezidir? Bu soru, somut piyasa verileri, akademik arastirmalar ve gercek is ilanlari ile cevaplanir. Bu hafta, ogrenci hangi kariyer yolunu secerse secsin programlamanin **kritik ve kacinilamaz** oldugunu kavrar.

---

## Ogrenme Hedefleri

Bu dersin sonunda ogrenci:
- Bilisim sektorundeki 4 ana kariyer yolunu (AI, Cloud/DevOps, Veri, Siber Guvenlik) tanimlar
- Her yolda programlamanin neden **vazgecilmez** oldugunu somut orneklerle aciklar
- PATIKA sistemi uzerinden kariyer agirliklendirmasinin ne anlama geldigini kavrar
- INP104 dersinin 10 haftalik iceriginin bu kariyer yollarini nasil destekledigini anlar

---

## 1. Bu Ders Neden Kritik?

### 1.1 Temel Gercek

Bilisim sektorunde calisan bir profesyonel icin programlama bilgisi, bir doktor icin anatomi bilgisi ne ise **odur**. Bu, secimlik bir yetkinlik degildir; **mesleki var olma kosulu**dur.

Asagidaki tablo, akademik ve endustri kaynaklarina dayanan bir calismanin (Bilisim Kariyer Secimi AHP Modeli) ortaya koydugu 4 kariyer yolunu gosterir. Dikkat edilmesi gereken nokta sudur: **4 alternatifin tamami programlama bilgisini zorunlu yetkinlik olarak talep eder.**

### 1.2 Kaynaklar ve Dayanak

Bu dersin kritik onem argumanlari iki temel calismaya dayanir:

**Calisma 1: Bilisimde Somut Meslek ve Ilan Haritasi (Subat 2026)**
- Gercek is ilanlari ve aktif pozisyonlarla desteklenmis piyasa analizi
- 4 kariyer alaninda somut rol isimleri, ornek sirketler ve ilan linkleri
- Kaynak: `/docs/active_it_roles_report.md`

**Calisma 2: Bilisim Kariyer Secimi AHP Modeli - Akademik Arastirma Raporu**
- WEF Future of Jobs 2025, SFIA 9, ACM CS2023, NIST NICE Framework gibi uluslararasi standartlara dayanan akademik model
- 4 alternatif, 8 ana kriter, 16 alt kriter ile yapılandırılmis karar destek sistemi
- Kaynak: `/docs/bilisim_model_academic_research.md`

---

## 2. 4 Kariyer Yolu ve Programlamanin Rolu

### Kritik Mesaj: Hangi Yol Cikarsa Ciksin, Programlama SART

PATIKA sistemi uzerinden yapacaginiz agirliklandirma sonucunda asagidaki 4 kariyer yolundan biri size uygun cikacaktir. **Hangisi cikarsa ciksin, bu derste ogrenecekleriniz o kariyer icin temel taslardir.**

---

### 2.1 AI ve Agent Sistemleri

> "Kod yazmaktan ote, AI modellerini is sureclerine baglayan ve AI Agent'lari yoneten muhendislik dali"

**Neden programlama sart?**
- ML modeli egitimi ve MLOps sureclerinin tamami Python uzerine kuruludur
- AI Agent gelistirme, API entegrasyonu ve surec otomasyonu kod yazma becerisini zorunlu kilar
- Teknoloji adaptasyonu (yeni araclar, yeni frameworkler) icin programlama altyapisi olmazsa olmazdir

**INP104 baglantisi:**
| INP104 Haftasi | AI Kariyerindeki Karsiligi |
|----------------|---------------------------|
| Hafta 2: Degiskenler, Input | Model parametrelerini tanimlama |
| Hafta 4: Donguler | Veri setleri uzerinde iterasyon |
| Hafta 7: Dosya Islemleri | Veri okuma/yazma, log yonetimi |
| Hafta 8: Fonksiyonlar | Moduler model pipeline'lari |
| Hafta 9: OOP | ML framework'leri (sinif yapilari) |
| Hafta 10: Veritabani | Egitim verisi yonetimi |

---

### 2.2 Cloud, DevOps ve Platform Muhendisligi

> "Yazilimin calisacagi altyapiyi kuranlar. Turkiye'de en garanti is kapisi"

**Neden programlama sart?**
- Infrastructure as Code (IaC): Altyapi artik kod ile yonetilir, elle konfigürasyon donemi bitmistir
- CI/CD pipeline'lari tamamen script ve otomasyon uzerine kuruludur
- Kubernetes, Docker, Terraform gibi tum modern araclar programlama bilgisi gerektirir

**INP104 baglantisi:**
| INP104 Haftasi | Cloud/DevOps Kariyerindeki Karsiligi |
|----------------|--------------------------------------|
| Hafta 3: Kosullar | Deployment kosullari, feature flag'ler |
| Hafta 4: Donguler | Toplu sunucu yonetimi, batch islemler |
| Hafta 7: Dosya Islemleri | Konfigurasyon dosyalari, YAML/JSON islemleri |
| Hafta 8: Fonksiyonlar | Otomasyon scriptleri |
| Hafta 9: Moduller | Harici kutuphane kullanimi (boto3, azure-sdk) |

---

### 2.3 Veri Analitigi ve Muhendisligi

> "FinTech ve E-ticaretin bel kemigi. AI'nin yakitini hazirlayanlar"

**Neden programlama sart?**
- Veri analizi ve icgoru cikarma sureclerinin standart araci Python ve SQL'dir
- ETL/ELT pipeline tasarimi tamamen kod ile yapilir
- Veri gorsellestirme ve BI dashboard'lari programlama bilgisi gerektirir

**INP104 baglantisi:**
| INP104 Haftasi | Veri Kariyerindeki Karsiligi |
|----------------|------------------------------|
| Hafta 2: Degiskenler, f-string | Veri formatlama ve raporlama |
| Hafta 4: Donguler | Veri setleri uzerinde islem |
| Hafta 5: Stringler | Metin verisi temizleme, parsing |
| Hafta 6: Listeler | Veri koleksiyonlari yonetimi |
| Hafta 7: Dosya Islemleri | CSV/JSON dosya okuma/yazma |
| Hafta 10: Veritabani | SQL sorgulari, CRUD islemleri |

---

### 2.4 Siber Guvenlik

> "Saldirilar arttikca 7/24 izleme (SOC) ihtiyaci bitmiyor"

**Neden programlama sart?**
- Tehdit tespiti ve log analizi icin otomasyon scriptleri yazilir
- Sizma testi (pentest) araclari gelistirmek ve ozellestirmek kod bilgisi gerektirir
- SIEM entegrasyonu ve olay mudahale sureclerinde scripting vazgecilmezdir

**INP104 baglantisi:**
| INP104 Haftasi | Siber Guvenlik Kariyerindeki Karsiligi |
|----------------|----------------------------------------|
| Hafta 3: Kosullar | Kural tabanli tehdit tespiti |
| Hafta 4: Donguler | Log dosyalari uzerinde tarama |
| Hafta 5: Stringler | Log satirlarini parse etme |
| Hafta 7: Dosya Islemleri | Log okuma, rapor yazma |
| Hafta 8: Fonksiyonlar | Otomasyon araclari gelistirme |
| Hafta 9: Moduller | Guvenlik kutuphaneleri kullanimi |

---

## 3. Kariyer Dogrulama Matrisi

| Alan | Piyasa Durumu | Trend | Python Kritikligi |
|------|---------------|-------|-------------------|
| **AI / Agent** | 50.000 yeni istihdam beklentisi | Patlama noktasi | ZORUNLU - Birincil dil |
| **Cloud / DevOps** | Stabil yuksek talep | Her sirketin demirbasi | ZORUNLU - Otomasyon dili |
| **Veri (Data)** | AI arttikca buyuyor | Kritik buyume | ZORUNLU - Analiz dili |
| **Siber Guvenlik** | Regulasyonlar alimi zorunlu kiliyor | Zorunlu niş | ZORUNLU - Scripting dili |

**Sonuc:** Tablonun son sutununa bakin. 4 kariyer yolunun **tamaminda** Python "ZORUNLU" olarak isaretlenmistir. Bu, INP104 dersinin kariyer yolculugunuzdaki **kritik onemi**nin en net ifadesidir.

---

## 4. PATIKA Sistemi ve Bu Ders

### PATIKA Nedir?

PATIKA, Analitik Hiyerarsi Sureci (AHP) yontemini kullanan bir karar destek sistemidir. Bu sistem, bilisim kariyer seciminde ogrencilerin kendi onceliklerini belirlemelerine ve buna gore en uygun kariyer yolunu bulmalarına yardimci olur.

### Nasil Calisir?

1. Ogrenci, PATIKA uzerinden 8 ana kriter ve 16 alt kriteri kendi onceliklerine gore agirliklandirir
2. Sistem, AHP pairwise karsilastirma ile 4 alternatif arasindan en uygun kariyer yolunu belirler
3. Sonuc ne cikarsa ciksin, **INP104 bu kariyer icin temel programlama altyapisini saglar**

### PATIKA Model Yapisi

```
Bilisim Kariyer Secimi
├── AI ve Agent Sistemleri
│   ├── Yapay Zeka Muhendisligi (Model Egitimi, Teknoloji Adaptasyonu)
│   └── AI Otomasyon ve Ajanlar (Surec Otomasyonu, Sistem Entegrasyonu)
├── Cloud/DevOps Platform Muhendisligi
│   ├── Bulut Altyapi Yonetimi (Mimari Tasarim, FinOps)
│   └── DevOps ve Surekli Teslimat (CI/CD, SRE)
├── Veri Analitigi ve Muhendisligi
│   ├── Veri Analizi ve Is Zekasi (Icgoru, Gorsellestirme)
│   └── Veri Muhendisligi (ETL, Veri Kalitesi)
└── Siber Guvenlik
    ├── Tehdit Izleme ve SOC (SIEM, Olay Mudahalesi)
    └── Guvenlik Denetimi ve Uyum (Pentest, KVKK/GDPR)
```

**Her dalda ortak payda: PROGRAMLAMA**

---

## 5. INP104 Ders Haritasi: 10 Haftada Ne Ogreneceksiniz?

Asagidaki tablo, bu donem boyunca islenecek 10 haftanin kariyer degerini gosterir:

| Hafta | Konu | Bu Beceri Nerede Kullanilir? |
|-------|------|------------------------------|
| 1 | Python'a Giris, print(), veri tipleri | Herhangi bir Python kodu yazmanin temeli |
| 2 | Degiskenler, input(), tip donusumleri | Kullanici verisi isleme, parametre tanimlama |
| 3 | Kosullu Ifadeler (if/elif/else) | Karar mekanizmalari, is kurallari |
| 4 | Donguler (while, for) | Veri isleme, otomasyon, tekrarlı gorevler |
| 5 | Karakter Dizileri | Metin isleme, log analizi, veri temizleme |
| 6 | Listeler ve Demetler | Veri koleksiyonlari, toplu islemler |
| 7 | Dosya Islemleri | Konfigurasyon, log, veri dosyalari |
| 8 | Fonksiyonlar | Moduler kod, tekrar kullanilabilirlik |
| 9 | Moduller ve OOP | Buyuk projeler, framework kullanimi |
| 10 | Veritabani (SQLite) | Veri yonetimi, CRUD, backend temelleri |

---

## 6. Bu Dersin Olmaz Ise Olmazlari

Bu dersi basariyla tamamlamak icin ogrencinin bilmesi gereken temel gercekler:

1. **Programlama bir SECIM degil, ZORUNLULUKTUR.** 4 kariyer yolunun tamami programlama bilgisi talep eder. "Ben kod yazmayacagim" diye dusunmek, kariyer seceneklerinizi sifirlar.

2. **Bu ders TEMELI atar.** INP104'te ogrenilenler, ileride ogrenilecek ileri konularin (web gelistirme, makine ogrenmesi, veri bilimi, siber guvenlik otomasyonu) on kosullarıdir.

3. **Her hafta bir oncekinin uzerine insa edilir.** Bir haftayi atlamak, sonraki tum haftalari anlamsiz kilar. Hafta 4'teki donguler anlasilmazsa Hafta 7'deki dosya islemleri yapilamaz.

4. **Pratik yapmadan ogrenilmez.** Her haftanin sonundaki gorevleri (`???` yer tutucularini) doldurun. Cevap anahtarina bakmadan once kendiniz deneyin.

5. **Google Colab kullaniliyor.** Bilgisayariniza hicbir sey yuklemeniz gerekmez. Tarayicidan Colab'a girin ve kodlamaya baslayin.

---

## 7. Akademik Dayanak Ozeti

Bu dersin kritik onem argumanlari asagidaki uluslararasi standartlara ve akademik kaynaklara dayanir:

| Kaynak | Katkisi |
|--------|---------|
| WEF Future of Jobs Report 2025 | Analitik dusunme #1 yetkinlik; AI/big data en hizli buyuyen alan |
| SFIA 9 | Dijital yetkinlik ve kariyer seviye cercevesi |
| ACM/IEEE-CS/AAAI CS2023 | Bilisim mufredat ve yetkinlik modeli |
| NIST NICE Framework | Siber guvenlik is gucu yetkinlik yapisi |
| IDC Turkiye 2025 | 117 Milyar $ pazar, 50.000 AI uzman acigi |
| Indeed/LinkedIn 2025 | AI ilanlari %9, siber guvenlik %4, bulut (AWS) %14 |
| CompTIA 2025 | Siber guvenlik istihdami 2034'e kadar %29 buyume |

Detayli akademik analiz: `/docs/bilisim_model_academic_research.md`
Somut ilan verileri: `/docs/active_it_roles_report.md`

---

## Dosyalar

| Dosya | Aciklama |
|-------|----------|
| `00-programlama-giris.ipynb` | Haftalik ders notebooku |

---

## Referanslar

- Python Programlama Dili Referans Belgesi (`/docs/yazbel.md`)
- Bilisimde Somut Meslek ve Ilan Haritasi (`/docs/active_it_roles_report.md`)
- Bilisim Kariyer Secimi AHP Modeli (`/docs/bilisim_model_academic_research.md`)

---

## Colab Ortami

Bu ders Google Colab uzerinde calisilmaktadir.

---

> **Bu ders, kariyer yolculugunuzun baslangic noktasidir. Hangi bilisim alanini secerseniz secin, burada ogreneceginiz Python temelleri sizi o kariyere tasiyan koprudur.**
