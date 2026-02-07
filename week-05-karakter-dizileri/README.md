# Hafta 5: Karakter Dizileri ve Metotları

## Konu Özeti

Bu hafta, Python'da karakter dizileri (string) ve string metotları öğrenilir.

---

## Öğrenme Hedefleri

- String indeksleme ve dilimleme yapmak
- String metotlarını kullanmak
- Karakter dizilerinde arama ve değiştirme yapmak
- enumerate() fonksiyonunu kullanmak

---

## Konu Başlıkları

### 5.1 String İndeksleme
```python
isim = "züber"
print(isim[0])  # z (ilk karakter)
print(isim[-1]) # r (son karakter)
```

### 5.2 String Dilimleme (Slicing)
```python
metin = "Python"
print(metin[0:3])   # Pyt
print(metin[3:])    # hon
print(metin[::-1])  # nohtyP (ters)
```

### 5.3 String Metotları
| Metot | Açıklama |
|-------|----------|
| `replace()` | Değiştirme |
| `lower()` | Küçük harfe |
| `upper()` | Büyük harfe |
| `split()` | Bölme |
| `join()` | Birleştirme |
| `count()` | Sayma |
| `find()` | Bulma |

---

## Notebooklar

| Dosya | Açıklama |
|-------|----------|
| `05-karakter-dizileri.ipynb` | Haftalık ders notebooku |
