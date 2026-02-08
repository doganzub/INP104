#!/usr/bin/env python3
"""
Yazbel PDF to Markdown Converter - Improved Version
yazbel.pdf dosyasını okunabilir yazbel.md formatına dönüştürür

Kullanım:
    python yazbel_pdf_extractor.py

Çıktı:
    /Users/zuber/INP104/docs/yazbel.md
"""

import pdfplumber
import re
import os
from pathlib import Path

# Konfigürasyon
PDF_PATH = "/Users/zuber/INP104/docs/yazbel.pdf"
OUTPUT_PATH = "/Users/zuber/INP104/docs/yazbel.md"


def fix_broken_words(text):
    """PDF'den gelen bitişik kelimeleri düzelt"""
    
    # Türkçe karakter kümeleri
    lower = "abcçdefgğhıijklmnoöpqrsştuüvwxyzâîû"
    upper = "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZÂÎÛ"
    
    # Bitişik büyük harfle başlayan kelimeleri ayır (örn: "NedenPython" -> "Neden Python")
    # Küçük harften büyük harfe geçişlerde boşluk ekle
    result = []
    prev_char = ''
    
    for i, char in enumerate(text):
        if i > 0 and prev_char in lower and char in upper:
            # Önceki karakter küçük, şimdiki büyük - boşluk ekle
            result.append(' ')
        result.append(char)
        prev_char = char
    
    text = ''.join(result)
    
    # Fazla boşlukları temizle
    text = re.sub(r' {2,}', ' ', text)
    
    return text


def clean_page_text(text):
    """Sayfa metnini temizle ve formatla"""
    
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        
        # Boş satırları atla
        if not line:
            cleaned_lines.append('')
            continue
        
        # Sayfa numaralarını atla (tek başına sayı olan satırlar)
        if re.match(r'^\d+$', line):
            continue
        
        # Roma rakamlarını atla (i, ii, iii, iv, v, vi, vii, viii, ix, x, xi, xii vb.)
        if re.match(r'^[ivxlcdm]+$', line.lower()):
            continue
        
        # Bitişik kelimeleri düzelt
        line = fix_broken_words(line)
        
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)


def detect_headings(text):
    """Başlıkları tespit et ve formatla"""
    
    lines = text.split('\n')
    result_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            result_lines.append('')
            continue
        
        # Bölüm başlıkları: "1 Bu Kitap Hakkında", "6 print() Fonksiyonu" gibi
        match = re.match(r'^(\d+)\s+([A-ZÜĞŞÇÖİ][^\n]+)$', stripped)
        if match and len(stripped) < 80:
            num = match.group(1)
            title = match.group(2)
            result_lines.append(f'\n# Bölüm {num}: {title}\n')
            continue
        
        # Alt başlıklar: "1.1 Bu Kitaptan Nasıl Yararlanabilirim?"
        match = re.match(r'^(\d+\.\d+)\s+([A-ZÜĞŞÇÖİ][^\n]+)$', stripped)
        if match and len(stripped) < 100:
            num = match.group(1)
            title = match.group(2)
            result_lines.append(f'\n## {num} {title}\n')
            continue
        
        # Alt-alt başlıklar: "1.1.1 Başlık"
        match = re.match(r'^(\d+\.\d+\.\d+)\s+([A-ZÜĞŞÇÖİ][^\n]+)$', stripped)
        if match and len(stripped) < 100:
            num = match.group(1)
            title = match.group(2)
            result_lines.append(f'\n### {num} {title}\n')
            continue
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def format_code_blocks(text):
    """Kod bloklarını düzgün formatla"""
    
    lines = text.split('\n')
    result_lines = []
    in_code_block = False
    
    # Kod satırı göstergeleri
    code_patterns = [
        r'^\s*>>>\s',           # Python interactive prompt
        r'^\s*\.\.\.\s',        # Python continuation
        r'^\s*#\s',             # Yorum satırı
        r'^\s*print\s*\(',      # print fonksiyonu
        r'^\s*def\s+\w+\s*\(',  # fonksiyon tanımı
        r'^\s*class\s+\w+',     # sınıf tanımı
        r'^\s*import\s+',       # import
        r'^\s*from\s+\w+',      # from import
        r'^\s*if\s+.*:',        # if bloğu
        r'^\s*elif\s+.*:',      # elif
        r'^\s*else\s*:',        # else
        r'^\s*for\s+\w+\s+in',  # for döngüsü
        r'^\s*while\s+.*:',     # while döngüsü
        r'^\s*try\s*:',         # try
        r'^\s*except',          # except
        r'^\s*with\s+',         # with
        r'^\s*return\s+',       # return
        r'^\s*\w+\s*=\s*',      # değişken ataması
        r"^'.*'$",              # tek tırnak içinde çıktı
    ]
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Bu satır kod mu?
        is_code = any(re.match(pattern, stripped) for pattern in code_patterns)
        
        if is_code and not in_code_block:
            # Kod bloğu başlat
            if result_lines and result_lines[-1] != '':
                result_lines.append('')
            result_lines.append('```python')
            in_code_block = True
        
        if in_code_block:
            if is_code or (stripped == '' and i + 1 < len(lines) and 
                          any(re.match(p, lines[i + 1].strip()) for p in code_patterns)):
                result_lines.append(stripped)
            else:
                # Kod bloğunu kapat
                result_lines.append('```')
                result_lines.append('')
                in_code_block = False
                result_lines.append(line)
        else:
            result_lines.append(line)
    
    # Açık kalan kod bloğunu kapat
    if in_code_block:
        result_lines.append('```')
    
    return '\n'.join(result_lines)


def post_process(text):
    """Son işlemler"""
    
    # Ardışık boş satırları azalt (max 2)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    # Başlangıç ve sondaki boşlukları temizle
    text = text.strip()
    
    return text


def extract_pdf_to_markdown():
    """PDF'i Markdown formatına dönüştür"""
    
    if not os.path.exists(PDF_PATH):
        print(f"PDF dosyası bulunamadı: {PDF_PATH}")
        return False
    
    print("=" * 60)
    print("YAZBEL PDF TO MARKDOWN CONVERTER")
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
            all_pages = []
            
            for page_num, page in enumerate(pdf.pages):
                print(f"Sayfa {page_num + 1}/{total_pages} işleniyor...")
                
                text = page.extract_text() or ""
                if text.strip():
                    # Her sayfayı temizle
                    cleaned = clean_page_text(text)
                    all_pages.append(cleaned)
            
            print()
            print("Sayfalar birleştiriliyor...")
            
            # Sayfaları birleştir
            full_text = '\n\n'.join(all_pages)
            
            print("Başlıklar tespit ediliyor...")
            full_text = detect_headings(full_text)
            
            print("Kod blokları formatlanıyor...")
            full_text = format_code_blocks(full_text)
            
            print("Son düzenlemeler yapılıyor...")
            full_text = post_process(full_text)
            
            # Markdown başlığı
            header = """# Python Programlama Dili Referans Belgesi

Bu belge, Python programlama dilinin temel kavramlarını Türkçe olarak açıklamaktadır.

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
            print(f"Dosya boyutu: {os.path.getsize(OUTPUT_PATH):,} bayt")
            print("=" * 60)
            
            return True
            
    except Exception as e:
        print(f"HATA: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    extract_pdf_to_markdown()
