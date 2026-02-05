# INP214 - Uygulamalı Makine Öğrenmesi (Applied Machine Learning)

> **AI Prompt Context:** Bu README, bir AI asistanının bu repo ile çalışırken ders yapısını, veri setlerini, haftalık konuları ve notebook-veri bağlantılarını hızlıca anlaması için optimize edilmiştir.

---

## Ders Kimliği

- **Ders Kodu:** INP214
- **Ders Adı:** Uygulamalı Makine Öğrenmesi (Applied Machine Learning)
- **Dil:** Türkçe (değişken isimleri, açıklamalar, markdown hücreleri Türkçe)
- **Platform:** Google Colab (tüm notebooklar `google.colab.drive` mount eder)
- **Python:** 3.13.4
- **Veri Kaynağı:** `data/` klasörü (Colab'da `/content/drive/MyDrive/Colab Notebooks/` yolundan okunur)

---

## Haftalık Müfredat ve Konu Haritası

| Hafta | Konu (TR) | Konu (EN) | Ders Notebook | Task Notebook | Veri Seti |
|-------|-----------|-----------|---------------|---------------|-----------|
| 1 | Veri Görselleştirme | Data Visualization | `docs/1_veri_gorsellestirme.ipynb` | `docs/1S_veri_gorsellestirme.ipynb` | `data/insurance.csv` |
| 2 | Veri Hazırlama | Data Preparation | `docs/2_veri_hazirlama.ipynb` | `docs/2S_veri_hazirlama.ipynb`, `docs/2S_task_veri_hazirlama.ipynb` | `data/auto-mpg.data`, `data/auto_mpg_extended.csv` |
| 3 | K-Means Kümeleme | K-Means Clustering | `docs/3_k_means.ipynb` | `docs/3S_k_means.ipynb`, `docs/IRIS_3_k_means.ipynb` | `data/mall_customers.csv` |
| 4 | Basit Doğrusal Regresyon | Simple Linear Regression | `docs/4_basit_dogReg_deneyim_maas.ipynb`, `docs/4_basit_dogReg_gelir_mutluluk.ipynb` | `docs/4S_basit_dogReg_gelir_mutluluk.ipynb`, `docs/4S_task_basit_dogReg_deneyim_maas.ipynb` | `data/Salary_dataset.csv`, `data/income.data.csv` |
| 5 | Coklu Dogrusal Regresyon | Multiple Linear Regression | `docs/5_coklu_dogReg.ipynb`, `docs/5_coklu_dogReg_day.ipynb` | `docs/5S_coklu_dogReg.ipynb`, `docs/5S_task_coklu_dogReg_day.ipynb` | `data/heart.data.csv`, `data/day.csv` |

---

## Notebook Adlandirma Kurali

### `docs/` klasoru (Colab kaynak notebooklari):
- `X_konu.ipynb` → Ders (ogretim) notebooku (tam cozumlu, aciklamali)
- `XS_konu.ipynb` → Ogrenci versiyonu (cozumlu referans)
- `XS_task_konu.ipynb` → Gorev notebooku (bosluklu, TODO formatinda)
- `IRIS_3_k_means.ipynb` → Ek ornek (Iris veri seti ile K-Means)

### `week-XX-*/` klasorleri (temiz ders notebooklari):
- `week-01-data-visualization/01-data-visualization.ipynb` → Hafta 1: `insurance.csv` ile veri gorsellestirme (line, bar, pie, scatter, histogram)
- `week-02-data-preparation/02-data-preparation.ipynb` → Hafta 2: `auto-mpg.data` ile eksik veri, binning, outlier, sampling, encoding, normalizasyon
- `week-03-kmeans-clustering/03-kmeans.ipynb` → Hafta 3: `mall_customers.csv` ile K-Means kumeleme, Elbow, Silhouette
- `week-04-simple-linear-regression/04-simple-linear-regression.ipynb` → Hafta 4: `income.data.csv` ile basit dogrusal regresyon (gelir→mutluluk)
- `week-05-multiple-linear-regression/05-multiple-linear-regression.ipynb` → Hafta 5: `heart.data.csv` ile coklu dogrusal regresyon (bisiklet+sigara→kalp hastaligi)

### Kok dizindeki dosyalar:
- `3s_task_k_means.ipynb` → K-Means gorev notebooku (bosluklu/TODO formatinda, ogrenci tamamlar; `mall_customers.csv` kullanir)

---

## Veri Setleri Detayli Haritasi

### `data/insurance.csv` → Hafta 1
- **Satir:** 1338, **Sutun:** 7
- **Sutunlar:** `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`
- **Kullanim:** Veri gorsellestirme (line, bar, pie, scatter, histogram, box plot)
- **Turkcelestirme:** `age→yas`, `sex→cinsiyet`, `bmi→vki`, `children→cocukSayisi`, `smoker→sigaraDurum`, `region→bolge`, `charges→odemeMiktari`
- **Kullanan notebooklar:** `docs/1_veri_gorsellestirme.ipynb`, `docs/1S_veri_gorsellestirme.ipynb`, `week-01-data-visualization/01-data-visualization.ipynb`

### `data/auto-mpg.data` → Hafta 2
- **Satir:** 398, **Sutun:** 9 (boslukla ayrilmis, header yok)
- **Sutunlar:** `mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`, `model_year`, `origin`, `car_name`
- **Kullanim:** Eksik veri (horsepower `?`), binning, outlier (IQR), sampling, label/dummy encoding, normalization
- **Onemli:** `horsepower` sutununda 6 adet `?` var → `NaN` → ortalama ile doldurulur
- **Kullanan notebooklar:** `docs/2_veri_hazirlama.ipynb`, `docs/2S_veri_hazirlama.ipynb`, `docs/2S_task_veri_hazirlama.ipynb`, `week-02-data-preparation/02-data-preparation.ipynb`

### `data/auto_mpg_extended.csv` → Hafta 2 (genisletilmis)
- **Satir:** 2000, **Sutun:** 9 (boslukla ayrilmis, header yok)
- **Olusan:** `data/auto-mpg_extended.ipynb` ile uretilmis sentetik veri (np.random.seed(42))
- **Sutunlar:** `mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`, `model_year`, `origin`, `car_name`
- **Onemli:** horsepower sutununda ~%5 `?` var (sentetik), orijinal auto-mpg.data ile ayni on isleme adimlari uygulanabilir
- **Kullanan notebooklar:** `docs/2S_task_veri_hazirlama.ipynb` (ek calisma verisi)

### `data/mall_customers.csv` → Hafta 3
- **Satir:** 200, **Sutun:** 5
- **Sutunlar:** `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)`
- **Kullanim:** K-Means kumeleme, Elbow yontemi, Silhouette skoru
- **Optimal k:** 5 kume (Elbow + Silhouette ile dogrulanmis)
- **Kullanan notebooklar:** `docs/3_k_means.ipynb`, `docs/3S_k_means.ipynb`, `3s_task_k_means.ipynb`, `week-03-kmeans-clustering/03-kmeans.ipynb`

### `data/Salary_dataset.csv` → Hafta 4
- **Satir:** 30, **Sutun:** 3 (index + 2 ozellik)
- **Sutunlar:** `YearsExperience`, `Salary`
- **Kullanim:** Basit dogrusal regresyon (deneyim → maas)
- **Turkcelestirme:** `YearsExperience→deneyim`, `Salary→maas`
- **Sonuc:** R²=0.957, maas = 25792.20 + 9449.96 * deneyim, Pearson r=0.978
- **Kullanan notebooklar:** `docs/4_basit_dogReg_deneyim_maas.ipynb`, `docs/4S_task_basit_dogReg_deneyim_maas.ipynb`

### `data/income.data.csv` → Hafta 4
- **Satir:** 500, **Sutun:** 3 (index + 2 ozellik)
- **Sutunlar:** `income`, `happiness`
- **Kullanim:** Basit dogrusal regresyon (gelir → mutluluk)
- **Turkcelestirme:** `income→gelir`, `happiness→mutluluk`
- **Sonuc:** R²=0.749, mutluluk = 0.228 + 0.708 * gelir, Pearson r=0.866
- **Kullanan notebooklar:** `docs/4_basit_dogReg_gelir_mutluluk.ipynb`, `docs/4S_basit_dogReg_gelir_mutluluk.ipynb`, `week-04-simple-linear-regression/04-simple-linear-regression.ipynb`

### `data/heart.data.csv` → Hafta 5
- **Satir:** 498, **Sutun:** 4 (index + 3 ozellik)
- **Sutunlar:** `biking`, `smoking`, `heart.disease`
- **Kullanim:** Coklu dogrusal regresyon (bisiklet+sigara → kalp hastaligi)
- **Turkcelestirme:** `biking→bisikletKullanimi`, `smoking→sigaraDurum`, `heart.disease→kalpHastaligi`
- **Sonuc:** R²=0.978, kalpHastaligi = 14.935 - 0.200*bisiklet + 0.181*sigara
- **Kullanan notebooklar:** `docs/5_coklu_dogReg.ipynb`, `docs/5S_coklu_dogReg.ipynb`, `week-05-multiple-linear-regression/05-multiple-linear-regression.ipynb`

### `data/day.csv` → Hafta 5
- **Satir:** 731, **Sutun:** 16
- **Sutunlar:** `instant`, `dteday`, `season`, `yr`, `mnth`, `holiday`, `weekday`, `workingday`, `weathersit`, `temp`, `atemp`, `hum`, `windspeed`, `casual`, `registered`, `cnt`
- **Kullanim:** Coklu dogrusal regresyon (sicaklik+nem → bisiklet kiralama sayisi)
- **Turkcelestirme:** `temp→havaSicakligi`, `hum→nemOrani`, `cnt→kiralamaSayisi`
- **Sonuc:** R²=0.436, kiralamaSayisi = 2716.457 + 6857.488*havaSicakligi - 2604.412*nemOrani
- **Kaynak:** UCI Bike Sharing Dataset (Fanaee-T & Gama, 2013)
- **Kullanan notebooklar:** `docs/5_coklu_dogReg_day.ipynb`, `docs/5S_task_coklu_dogReg_day.ipynb`

### `data/hcvdat0.csv` → Ek veri
- **Satir:** 616, **Sutun:** 14
- **Sutunlar:** `Category`, `Age`, `Sex`, `ALB`, `ALP`, `ALT`, `AST`, `BIL`, `CHE`, `CHOL`, `CREA`, `GGT`, `PROT`
- **Kullanim:** Hepatit C siniflandirma / ek analiz icin

---

## Kullanilan Kutuphaneler ve Versiyonlar

```
numpy>=1.26.0        # Sayisal hesaplama, diziler
pandas>=2.2.0        # Veri cerceveleri, CSV okuma
matplotlib>=3.8.0    # Grafik cizimi (line, bar, pie, scatter, histogram, box)
seaborn>=0.13.0      # Gelismis gorsellestirme (heatmap, scatterplot, boxplot, histplot)
scikit-learn>=1.4.0  # ML modelleri (KMeans, LinearRegression, train_test_split, StandardScaler, MinMaxScaler, silhouette_score)
scipy>=1.12.0        # Istatistik (pearsonr korelasyon)
statsmodels>=0.14.0  # OLS regresyon modeli (smf.ols)
yellowbrick>=1.5     # ML gorsellestirme (SilhouetteVisualizer)
ipywidgets>=8.1.0    # Colab buton ve widget destegi
```

Tum bagimliliklar: `requirements.txt`

---

## Haftalik Ogrenme Hedefleri ve Teknikler

### Hafta 1: Veri Gorsellestirme
- CSV okuma (`pd.read_csv`)
- Sutun yeniden adlandirma (`rename`)
- Kategorik tip donusumu (`astype("category")`)
- Betimsel istatistik (`describe`)
- Grafikler: `plt.plot`, `plt.bar`, `plt.barh`, `plt.pie`, `plt.scatter`, `sns.scatterplot`, `sns.histplot`

### Hafta 2: Veri Hazirlama
- Eksik veri tespiti ve doldurma (`isnull`, `fillna`, ortalama ile)
- Ayiriklastirma: `lambda+map`, `pd.cut`, `pd.qcut`
- Gruplama: `groupby + describe/mean/sum`
- Tekrar eden satirlar: `duplicated`, `drop_duplicates`
- Aykiri deger: IQR yontemi, `boxplot`, `boxplot_stats`
- Ornekleme: `sample`, `random.seed`, `train_test_split`, tabakalı (`stratify`)
- Kodlama: `cat.codes` (label), `pd.get_dummies` (one-hot/dummy)
- Normalizasyon: `MinMaxScaler` (0-1), `StandardScaler` (z-score)

### Hafta 3: K-Means Kumeleme
- Korelasyon matrisi: `df.corr()`, `sns.heatmap`
- K-Means: `KMeans(n_clusters=k)`, `fit`, `labels_`, `cluster_centers_`
- Kume sayisi belirleme: Elbow (WSS/inertia), Silhouette skoru
- Gorsellestirme: kume scatter plot, centroid isaretleme

### Hafta 4: Basit Dogrusal Regresyon
- Pearson korelasyon: `pearsonr(x, y)` → r ve p-degeri
- OLS model: `smf.ols("y ~ x", data).fit()`
- Katsayilar: `model.params`, `model.rsquared`
- Egitim/test bolme: `sample(frac=0.7)` veya `train_test_split`
- Hata metrikleri: MAE, MSE, RMSE (`mean_absolute_error`, `mean_squared_error`)
- Gorsellestirme: scatter + regresyon dogrusu + residual

### Hafta 5: Coklu Dogrusal Regresyon
- Birden fazla bagimsiz degisken: `smf.ols("y ~ x1 + x2", data).fit()`
- Model yorumlama: katsayilar, p-degerleri, R², Adj-R²
- Performans: MAE, MSE, RMSE (test seti uzerinden)
- Gorsellestirme: bir degisken sabitken digeri ile regresyon

---

## Proje Yapisi

```
INP214/
├── README.md                          # Bu dosya (AI-dostu dokumantasyon)
├── requirements.txt                   # Python bagimliliklari
├── task_README.md                     # Task notebook hazirlama kilavuzu
├── cleanup_icons.sh                   # Icon/.DS_Store temizleme scripti
├── clean_notebooks.py                 # Notebook temizleme scripti
├── 3s_task_k_means.ipynb              # K-Means gorev notebooku (bosluklu, mall_customers.csv)
├── data/                              # Tum veri setleri
│   ├── insurance.csv                  # Hafta 1 - Sigorta verisi
│   ├── auto-mpg.data                  # Hafta 2 - Otomobil yakit verisi
│   ├── auto_mpg_extended.csv          # Hafta 2 - Genisletilmis otomobil verisi
│   ├── auto-mpg_extended.ipynb        # auto_mpg_extended uretim notebooku
│   ├── mall_customers.csv             # Hafta 3 - Musteri segmentasyonu
│   ├── Salary_dataset.csv             # Hafta 4 - Deneyim/maas verisi
│   ├── income.data.csv                # Hafta 4 - Gelir/mutluluk verisi
│   ├── heart.data.csv                 # Hafta 5 - Kalp hastaligi verisi
│   ├── day.csv                        # Hafta 5 - Bisiklet paylasim verisi
│   └── hcvdat0.csv                    # Ek - Hepatit C verisi
├── docs/                              # Ders ve task notebooklari
│   ├── 1_veri_gorsellestirme.ipynb    # Hafta 1 ders
│   ├── 1S_veri_gorsellestirme.ipynb   # Hafta 1 ogrenci
│   ├── 2_veri_hazirlama.ipynb         # Hafta 2 ders
│   ├── 2S_veri_hazirlama.ipynb        # Hafta 2 ogrenci
│   ├── 2S_task_veri_hazirlama.ipynb   # Hafta 2 task
│   ├── 3_k_means.ipynb               # Hafta 3 ders
│   ├── 3S_k_means.ipynb              # Hafta 3 ogrenci
│   ├── IRIS_3_k_means.ipynb           # Hafta 3 ek (Iris)
│   ├── 4_basit_dogReg_deneyim_maas.ipynb      # Hafta 4 ders (deneyim-maas)
│   ├── 4_basit_dogReg_gelir_mutluluk.ipynb    # Hafta 4 ders (gelir-mutluluk)
│   ├── 4S_basit_dogReg_gelir_mutluluk.ipynb   # Hafta 4 ogrenci
│   ├── 4S_task_basit_dogReg_deneyim_maas.ipynb # Hafta 4 task
│   ├── 5_coklu_dogReg.ipynb                   # Hafta 5 ders (kalp hastaligi)
│   ├── 5_coklu_dogReg_day.ipynb               # Hafta 5 ders (bisiklet paylasim)
│   ├── 5S_coklu_dogReg.ipynb                  # Hafta 5 ogrenci
│   └── 5S_task_coklu_dogReg_day.ipynb         # Hafta 5 task
├── week-01-data-visualization/
│   └── 01-data-visualization.ipynb    # Hafta 1: insurance.csv gorsellestirme
├── week-02-data-preparation/
│   └── 02-data-preparation.ipynb      # Hafta 2: auto-mpg.data veri hazirlama
├── week-03-kmeans-clustering/
│   └── 03-kmeans.ipynb                # Hafta 3: mall_customers K-Means kumeleme
├── week-04-simple-linear-regression/
│   └── 04-simple-linear-regression.ipynb  # Hafta 4: income→mutluluk regresyon
└── week-05-multiple-linear-regression/
    └── 05-multiple-linear-regression.ipynb # Hafta 5: bisiklet+sigara→kalp regresyon
```

---

## Colab Ortaminda Calistirma

Notebooklar Google Colab icin tasarlanmistir. Her notebook basinda:

1. **GitHub Token butonu** → repo senkronizasyonu icin
2. **Drive & GitHub Senkronizasyon butonu** → notebook kayit/yukleme
3. **Kutuphane yukleme:** `!pip install -q numpy pandas scikit-learn matplotlib seaborn yellowbrick`
4. **Drive baglantisi:** `drive.mount('/content/drive')`
5. **Veri okuma yolu:** `/content/drive/MyDrive/Colab Notebooks/<dosya_adi>`

### Lokal Calistirma

```bash
git clone <repo_url>
cd INP214
pip install -r requirements.txt
jupyter notebook
```

> **Not:** Lokal calistirmada `google.colab` importlarini ve `drive.mount()` satirlarini yorum satirina alin. Veri yollarini `data/<dosya_adi>` olarak degistirin.

---

## docs/ vs week-XX/ Farki

| Ozellik | `docs/` klasoru | `week-XX-*/` klasoru |
|---------|-----------------|---------------------|
| Icerik | Colab kaynak dosyalari (ders + ogrenci + task) | Temiz, tekil ders notebooku |
| GitHub Token | Evet (buton olarak) | Evet (buton olarak) |
| Drive Mount | Evet | Evet |
| Cikti Hucresi | Bazi notebooklarda mevcut | Bazi notebooklarda mevcut |
| Veri Seti Referansi | `docs/` icindekiler ayni veri setlerini kullanir | Ayni veri setlerini kullanir |
| Iliskisi | Hafta 4 ders notebook → `4_basit_dogReg_gelir_mutluluk.ipynb` | `04-simple-linear-regression.ipynb` (ayni icerik) |

**Onemli:** `week-XX-*/` klasorlerindeki notebooklar, `docs/` klasorundeki ders notebooklarinin "temiz" kopyalaridir. Icerik olarak eslesirler:
- `week-01` ↔ `docs/1_veri_gorsellestirme.ipynb` → `insurance.csv`
- `week-02` ↔ `docs/2_veri_hazirlama.ipynb` → `auto-mpg.data`
- `week-03` ↔ `docs/3_k_means.ipynb` → `mall_customers.csv`
- `week-04` ↔ `docs/4_basit_dogReg_gelir_mutluluk.ipynb` → `income.data.csv` (gelir→mutluluk, R²=0.749)
- `week-05` ↔ `docs/5_coklu_dogReg.ipynb` → `heart.data.csv` (bisiklet+sigara→kalp, R²=0.978)

> **Not:** Hafta 4'te iki veri seti kullanilir: `Salary_dataset.csv` (deneyim→maas) ve `income.data.csv` (gelir→mutluluk). Week-04 klasoru `income.data.csv` versiyonunu icerir.
> **Not:** Hafta 5'te iki veri seti kullanilir: `heart.data.csv` (kalp hastaligi) ve `day.csv` (bisiklet kiralama). Week-05 klasoru `heart.data.csv` versiyonunu icerir.

---

## IRIS Ek Calismasi

`docs/IRIS_3_k_means.ipynb` notebooku, Hafta 3 K-Means konusunun ek uygulamasidir:
- **Veri seti:** sklearn icindeki dahili `iris` veri seti (150 gozlem, 4 ozellik, 3 tur)
- **Sutunlar:** `canakU` (sepal length), `canakG` (sepal width), `tacU` (petal length), `tacG` (petal width), `tur` (setosa/versicolor/virginica)
- **Optimal k:** 3 (Elbow + Silhouette)
- **Fark:** Mall Customers'tan farkli olarak sklearn dahili veri seti kullanilir, harici CSV okunmaz

---

## AI Asistan Icin Hizli Referans

**Bu repoyu anlaman gereken temel bilgiler:**

1. Ders Turkce islenilir, degisken isimleri Turkcedir
2. Her hafta farkli bir ML konusu isler (gorsellestirme → veri hazirlama → kumeleme → basit regresyon → coklu regresyon)
3. Veri setleri `data/` klasorundedir, her biri belirli haftalara aittir (yukaridaki haritaya bak)
4. `docs/` klasorundeki X_ prefiksi ders notebookunu, XS_ ogrenci versiyonunu, XS_task_ gorev versiyonunu gosterir
5. `week-XX-*/` klasorleri `docs/` ders notebooklarinin temiz kopyalaridir (ayni icerik, farkli dosya adi)
6. Notebooklar Colab icin yazilmistir (Drive mount, pip install satirlari mevcut)
7. Temel kutuphaneler: pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels, yellowbrick, scipy
8. Her notebook icinde Turkce markdown aciklamalar, kod yorumlari ve istatistik tablolari vardir
9. `task_README.md` dosyasi task notebook hazirlama kilavuzudur
10. Her ders notebooku 5 adimlik sureyi takip eder: kutuphane yukle → veri oku/temizle → EDA/gorsellestir → model kur → performans degerlendir