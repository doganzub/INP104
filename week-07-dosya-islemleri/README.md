# Hafta 7: Dosya İşlemleri

## Konu Özeti

Bu hafta, Python'da dosya oluşturma, yazma ve okuma işlemleri öğrenilir.

---

## Öğrenme Hedefleri

- Dosya oluşturma ve yazma
- Dosya okuma
- `with` ifadesi ile otomatik dosya kapama
- Dosya modlarını anlamak

---

## Konu Başlıkları

### 7.1 Dosya Açma Modları
| Mod | Açıklama |
|-----|----------|
| `"r"` | Okuma (varsayılan) |
| `"w"` | Yazma (üzerine yazar) |
| `"a"` | Ekleme (sona ekler) |
| `"x"` | Oluşturma (dosya varsa hata) |

### 7.2 Dosya Yazma
```python
dosya = open("dosya.txt", "w")
dosya.write("Merhaba Dünya")
dosya.close()
```

### 7.3 Dosya Okuma
```python
dosya = open("dosya.txt", "r")
icerik = dosya.read()
dosya.close()
```

### 7.4 with İfadesi (Önerilen)
```python
with open("dosya.txt", "r") as dosya:
    icerik = dosya.read()
# Dosya otomatik kapanır
```

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `07-dosya-islemleri.ipynb` | Haftalık ders notebooku |
