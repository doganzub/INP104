#!/usr/bin/env python3
"""
Yazbel Web Scraper
Web sitesinden içeriği çeker ve temiz markdown formatına dönüştürür
"""

import requests
from bs4 import BeautifulSoup
import re
import os

URL = "https://python.yazbel.com/YazbelPythonProgramlamaDiliBelgeleri.html"
OUTPUT_PATH = "/Users/zuber/INP104/docs/yazbel.md"


def clean_text(text):
    """Metni temizle"""
    # Fazla boşlukları temizle
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()


def extract_content():
    """Web sitesinden içeriği çek"""
    
    print("=" * 60)
    print("YAZBEL WEB SCRAPER")
    print("=" * 60)
    print(f"URL: {URL}")
    print(f"Çıktı: {OUTPUT_PATH}")
    print()
    
    try:
        print("Web sayfası indiriliyor...")
        response = requests.get(URL, timeout=60)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"Hata: HTTP {response.status_code}")
            return False
        
        print(f"Sayfa boyutu: {len(response.text):,} karakter")
        
        print("HTML ayrıştırılıyor...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ana içerik alanını bul
        content = soup.find('div', class_='body')
        if not content:
            content = soup.find('div', class_='document')
        if not content:
            content = soup.find('main')
        if not content:
            content = soup.body
        
        if not content:
            print("Hata: İçerik bulunamadı")
            return False
        
        print("Markdown'a dönüştürülüyor...")
        
        markdown_lines = []
        markdown_lines.append("# Python Programlama Dili Referans Belgesi\n")
        markdown_lines.append("Bu belge, Python programlama dilinin temel kavramlarını Türkçe olarak açıklamaktadır.\n")
        markdown_lines.append("---\n")
        
        # Tüm bölümleri işle
        for element in content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'ul', 'ol', 'table', 'div']):
            
            # Başlıklar
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(element.name[1])
                text = element.get_text(strip=True)
                # Permalink işaretlerini kaldır
                text = text.replace('¶', '').strip()
                if text:
                    markdown_lines.append(f"\n{'#' * level} {text}\n")
            
            # Paragraflar
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text:
                    markdown_lines.append(f"\n{text}\n")
            
            # Kod blokları
            elif element.name == 'pre':
                code = element.get_text()
                markdown_lines.append(f"\n```python\n{code}\n```\n")
            
            # Listeler
            elif element.name in ['ul', 'ol']:
                for li in element.find_all('li', recursive=False):
                    text = li.get_text(strip=True)
                    if text:
                        prefix = '-' if element.name == 'ul' else '1.'
                        markdown_lines.append(f"{prefix} {text}\n")
                markdown_lines.append("\n")
            
            # Tablolar
            elif element.name == 'table':
                rows = element.find_all('tr')
                if rows:
                    for i, row in enumerate(rows):
                        cells = row.find_all(['th', 'td'])
                        cell_texts = [cell.get_text(strip=True) for cell in cells]
                        markdown_lines.append('| ' + ' | '.join(cell_texts) + ' |\n')
                        if i == 0:
                            markdown_lines.append('| ' + ' | '.join(['---'] * len(cells)) + ' |\n')
                    markdown_lines.append("\n")
            
            # Uyarı kutuları
            elif element.name == 'div' and 'admonition' in element.get('class', []):
                title_elem = element.find('p', class_='admonition-title')
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    markdown_lines.append(f"\n> **{title}**\n")
                for p in element.find_all('p')[1:]:
                    text = p.get_text(strip=True)
                    if text:
                        markdown_lines.append(f"> {text}\n")
                markdown_lines.append("\n")
        
        # Birleştir ve temizle
        full_text = ''.join(markdown_lines)
        full_text = clean_text(full_text)
        
        # Dosyaya yaz
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print()
        print("=" * 60)
        print("TAMAMLANDI!")
        print(f"Çıktı dosyası: {OUTPUT_PATH}")
        print(f"Dosya boyutu: {os.path.getsize(OUTPUT_PATH):,} bayt")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"Hata: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    extract_content()
