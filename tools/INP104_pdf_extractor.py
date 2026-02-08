#!/usr/bin/env python3
"""
INP104 PDF to Markdown Converter
yazbel.pdf dosyasını yazbel.md formatına dönüştürür

Kullanım:
    python INP104_pdf_extractor.py

Çıktı:
    /Users/zuber/INP104/docs/python.md
"""

import pdfplumber
import re
import os
from pathlib import Path

# Konfigürasyon
PDF_PATH = "/Users/zuber/INP104/docs/yazbel.pdf"
OUTPUT_PATH = "/Users/zuber/INP104/docs/python.md"

# Yasaklı kelimeler (bu kelimeler çıktıda yer almayacak)
FORBIDDEN_WORDS = ['yazbel', 'istihza', 'Yazbel', 'İstihza', 'YAZBEL', 'İSTİHZA']


def clean_text(text):
    """Metinden yasaklı kelimeleri temizle"""
    for word in FORBIDDEN_WORDS:
        text = text.replace(word, '')
    
    # Fazla boşlukları temizle
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    
    return text.strip()


def extract_code_blocks(text):
    """Metindeki kod bloklarını tespit et ve formatla"""
    lines = text.split('\n')
    result_lines = []
    in_code_block = False
    code_buffer = []
    
    # Kod satırı belirleyicileri
    code_indicators = [
        'print(', 'def ', 'class ', 'import ', 'from ', 'if ', 'elif ', 'else:',
        'for ', 'while ', 'try:', 'except', 'with ', 'return ', '>>> ',
        '= ', '+= ', '-= ', '*= ', '/= ', '== ', '!= ', '<= ', '>= ',
    ]
    
    for line in lines:
        stripped = line.strip()
        
        # Kod satırı mı kontrol et
        is_code = any(indicator in stripped for indicator in code_indicators)
        is_code = is_code or stripped.startswith('#')
        is_code = is_code or (stripped.startswith('>>>') or stripped.startswith('...'))
        
        if is_code and not in_code_block:
            # Kod bloğu başlıyor
            if result_lines and result_lines[-1] != '':
                result_lines.append('')
            result_lines.append('```python')
            in_code_block = True
        
        if in_code_block:
            if is_code or stripped == '' or stripped.startswith('#'):
                result_lines.append(line)
            else:
                # Kod bloğu bitiyor
                result_lines.append('```')
                result_lines.append('')
                result_lines.append(line)
                in_code_block = False
        else:
            result_lines.append(line)
    
    # Açık kalan kod bloğunu kapat
    if in_code_block:
        result_lines.append('```')
    
    return '\n'.join(result_lines)


def format_as_markdown(text):
    """Metni Markdown formatına dönüştür"""
    lines = text.split('\n')
    result_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Başlık tespiti
        if stripped and len(stripped) < 100:
            # Büyük harfle başlayan ve kısa satırlar başlık olabilir
            if stripped.isupper() and len(stripped) > 3:
                result_lines.append(f'\n## {stripped.title()}\n')
                continue
            
            # Numaralı başlıklar
            if re.match(r'^\d+\.\s+[A-ZÜĞŞÇÖİ]', stripped):
                result_lines.append(f'\n### {stripped}\n')
                continue
            
            # Alt başlıklar
            if re.match(r'^\d+\.\d+\s+', stripped):
                result_lines.append(f'\n#### {stripped}\n')
                continue
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def add_inline_comments(text):
    """Kod satırlarına açıklayıcı yorumlar ekle"""
    lines = text.split('\n')
    result_lines = []
    
    # Yorum açıklamaları
    comment_map = {
        'print(': '# Ekrana çıktı verir',
        'input(': '# Kullanıcıdan veri alır',
        'len(': '# Uzunluk/eleman sayısı verir',
        'type(': '# Veri tipini gösterir',
        'int(': '# Tam sayıya çevirir',
        'float(': '# Ondalıklı sayıya çevirir',
        'str(': '# Karakter dizisine çevirir',
        'list(': '# Listeye çevirir',
        'range(': '# Sayı aralığı oluşturur',
        'def ': '# Fonksiyon tanımı',
        'class ': '# Sınıf tanımı',
        'import ': '# Modül içe aktarma',
        'from ': '# Modülden içe aktarma',
        'if ': '# Koşul kontrolü',
        'elif ': '# Alternatif koşul',
        'else:': '# Varsayılan durum',
        'for ': '# Döngü başlangıcı',
        'while ': '# Koşullu döngü',
        'try:': '# Hata yakalama bloğu',
        'except': '# Hata işleme',
        'with ': '# Kaynak yönetimi',
        'return ': '# Değer döndürür',
        'break': '# Döngüyü sonlandırır',
        'continue': '# Sonraki adıma geçer',
        'pass': '# Boş işlem (yer tutucu)',
        '.append(': '# Listeye eleman ekler',
        '.insert(': '# Belirtilen konuma ekler',
        '.remove(': '# Elemanı siler',
        '.sort(': '# Sıralar',
        '.reverse(': '# Ters çevirir',
        '.split(': '# Böler',
        '.join(': '# Birleştirir',
        '.replace(': '# Değiştirir',
        '.lower()': '# Küçük harfe çevirir',
        '.upper()': '# Büyük harfe çevirir',
        'open(': '# Dosya açar',
        '.read()': '# Dosyayı okur',
        '.write(': '# Dosyaya yazar',
        '.close()': '# Dosyayı kapatır',
        'sqlite3.connect': '# Veritabanı bağlantısı',
        '.cursor()': '# İmleç oluşturur',
        '.execute(': '# SQL sorgusu çalıştırır',
        '.fetchall()': '# Tüm sonuçları alır',
        '.commit()': '# Değişiklikleri kaydeder',
    }
    
    in_code_block = False
    
    for line in lines:
        # Kod bloğu içinde miyiz kontrol et
        if line.strip().startswith('```python'):
            in_code_block = True
            result_lines.append(line)
            continue
        elif line.strip() == '```':
            in_code_block = False
            result_lines.append(line)
            continue
        
        if in_code_block and line.strip() and not line.strip().startswith('#'):
            # Satırda zaten yorum var mı kontrol et
            if '#' not in line:
                # Uygun yorum bul
                for pattern, comment in comment_map.items():
                    if pattern in line:
                        # Satırı düzgün hizala ve yorum ekle
                        padded_line = line.ljust(50)
                        line = f'{padded_line}{comment}'
                        break
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def extract_pdf_to_markdown():
    """PDF'i Markdown formatına dönüştür"""
    
    if not os.path.exists(PDF_PATH):
        print(f"PDF dosyası bulunamadı: {PDF_PATH}")
        return False
    
    print("=" * 60)
    print("INP104 PDF TO MARKDOWN CONVERTER")
    print("=" * 60)
    print(f"Kaynak: {PDF_PATH}")
    print(f"Hedef: {OUTPUT_PATH}")
    print()
    
    try:
        with pdfplumber.open(PDF_PATH) as pdf:
            total_pages = len(pdf.pages)
            print(f"Toplam sayfa: {total_pages}")
            print()
            
            # Tüm içeriği topla
            all_text = []
            
            for page_num, page in enumerate(pdf.pages):
                print(f"Sayfa {page_num + 1}/{total_pages} isleniyor...")
                
                text = page.extract_text() or ""
                if text.strip():
                    all_text.append(text)
            
            # Metni birleştir
            full_text = '\n\n'.join(all_text)
            
            print()
            print("Metin temizleniyor...")
            
            # Yasaklı kelimeleri temizle
            full_text = clean_text(full_text)
            
            print("Markdown formatına dönüştürülüyor...")
            
            # Markdown formatla
            full_text = format_as_markdown(full_text)
            
            print("Kod blokları işleniyor...")
            
            # Kod bloklarını işle
            full_text = extract_code_blocks(full_text)
            
            print("Satır içi açıklamalar ekleniyor...")
            
            # Yorum ekle
            full_text = add_inline_comments(full_text)
            
            # Markdown başlığı ekle
            header = """# Python Programlama Dili Referans Belgesi

Bu belge, Python programlama dilinin temel kavramlarını içermektedir.
Resmi akademik dil kullanılmış ve kod örnekleri açıklayıcı yorumlarla desteklenmiştir.

---

"""
            
            final_text = header + full_text
            
            # Dosyaya yaz
            with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
                f.write(final_text)
            
            print()
            print("=" * 60)
            print("TAMAMLANDI!")
            print(f"Çıktı dosyası: {OUTPUT_PATH}")
            print("=" * 60)
            
            return True
            
    except Exception as e:
        print(f"HATA: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    extract_pdf_to_markdown()
