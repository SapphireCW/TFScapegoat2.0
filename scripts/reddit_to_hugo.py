import os
import hashlib
import re
import sys
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree as ET
import urllib.request
from urllib.error import URLError

REDDIT_USER = os.environ.get("REDDIT_USER", "ImGroot2404")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content", "reddit")

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text[:50]

def parse_reddit_date(date_str):
    if not date_str:
        return datetime.now(timezone.utc) + timedelta(hours=2)
    
    date_str = date_str.strip()
    
    try:
        if '+' in date_str:
            date_part, tz_part = date_str.split('+', 1)
        elif date_str.endswith('Z'):
            date_part = date_str[:-1]
        else:
            date_part = date_str
        
        dt = datetime.strptime(date_part, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=timezone.utc) + timedelta(hours=2)
        return dt
    except Exception as e:
        print(f"DEBUG: errore parse data '{date_str}': {e}")
        return datetime.now(timezone.utc) + timedelta(hours=2)

def main():
    feed_url = f"https://www.reddit.com/user/{REDDIT_USER}/.rss"
    print(f"Scaricando feed da: {feed_url}")
    
    try:
        req = urllib.request.Request(feed_url, headers={'User-Agent': 'HugoBlogSync/1.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            xml_data = response.read().decode('utf-8')
    except URLError as e:
        print(f"ERRORE: {e}")
        sys.exit(1)
    
    root = ET.fromstring(xml_data)
    
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entries = root.findall('atom:entry', ns)
    if not entries:
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')
    
    print(f"Trovati {len(entries)} post")
    
    if len(entries) == 0:
        print("Nessun post trovato.")
        sys.exit(0)
    
    os.makedirs(CONTENT_DIR, exist_ok=True)
    created = 0
    
    for entry in entries:
        title_elem = entry.find('atom:title', ns)
        if title_elem is None:
            continue
        title = title_elem.text or "Senza titolo"
        
        link_elem = entry.find('atom:link', ns)
        link = link_elem.get('href') if link_elem is not None else '#'
        
        date_elem = entry.find('atom:published', ns) or entry.find('atom:updated', ns)
        date_str = date_elem.text if date_elem is not None else None
        published = parse_reddit_date(date_str)
        
        post_id = hashlib.md5(link.encode()).hexdigest()[:8]
        safe_title = title.replace('"', '&quot;')
        
        content = f"""---
title: "{safe_title}"
date: {published.strftime('%Y-%m-%dT%H:%M:%S+02:00')}
draft: false
source: "reddit"
source_url: "{link}"
categories: ["Aggiornamenti"]
tags: ["reddit", "news"]
---

{title}

👉 [Leggi il post completo su Reddit]({link})
"""
        
        filename = f"{published.strftime('%Y-%m-%d')}-{slugify(title)}-{post_id}.md"
        filepath = os.path.join(CONTENT_DIR, filename)
        
        if os.path.exists(filepath):
            print(f"Già esistente: {filename}")
            continue
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Creato: {filename}")
        created += 1
    
    print(f"Creati {created} nuovi post")

if __name__ == "__main__":
    main()