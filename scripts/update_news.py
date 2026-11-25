#!/usr/bin/env python3
"""Collect recent privacy headlines from public RSS/Atom feeds into news.json.

Runs daily in GitHub Actions. Standard library only. Stores only the headline,
source name, date and link (the original publisher keeps the content).
If too few items are collected, the existing news.json is left untouched.
"""
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "news.json")
UA = "Mozilla/5.0 (compatible; PrivarynNewsBot/1.0; headlines only)"
MAX_BYTES = 3_000_000
MAX_AGE_DAYS = 45
PER_SOURCE = 2
TOTAL = 8

# (label, feed url, keyword_filter)
SOURCES = [
    ("EDPB", "https://www.edpb.europa.eu/feed/news_en", False),
    ("FTC", "https://www.ftc.gov/feeds/press-release-consumer-protection.xml", True),
    ("California AG", "https://oag.ca.gov/news/feed", True),
    ("Data Protection Report", "https://www.dataprotectionreport.com/feed/", False),
    ("Privacy World", "https://www.privacyworld.blog/feed/", False),
    ("Inside Privacy", "https://www.insideprivacy.com/feed/", False),
    ("The Record", "https://therecord.media/feed", True),
    ("Infosecurity Magazine", "https://www.infosecurity-magazine.com/rss/news/", True),
]

KEYWORDS = re.compile(
    r"privacy|data protection|data breach|gdpr|ccpa|cpra|coppa|consent|biometric|"
    r"surveillance|personal (data|information)|data broker|cookie|tracking|ai act",
    re.I,
)


def local(tag):
    return tag.rsplit("}", 1)[-1]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/atom+xml, text/xml"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("feed too large")
    head = data[:4000].lower()
    # Refuse DTD/entity declarations (entity-expansion attacks).
    if b"<!doctype" in head and b"<!entity" in data.lower():
        raise ValueError("entity declarations not allowed")
    if b"<!entity" in data.lower():
        raise ValueError("entity declarations not allowed")
    return data


def parse_date(text):
    if not text:
        return None
    text = text.strip()
    try:
        d = parsedate_to_datetime(text)
    except Exception:
        d = None
    if d is None:
        try:
            d = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except Exception:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def clean(text):
    text = unescape(re.sub(r"<[^>]+>", "", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text[:170].rstrip()


def entries(root):
    for el in root.iter():
        name = local(el.tag)
        if name not in ("item", "entry"):
            continue
        title = link = date = None
        for ch in el:
            n = local(ch.tag)
            if n == "title":
                title = "".join(ch.itertext())
            elif n == "link":
                href = ch.get("href")
                if href:
                    if ch.get("rel") in (None, "alternate") or link is None:
                        link = href
                elif ch.text and not link:
                    link = ch.text.strip()
            elif n in ("pubDate", "published", "date", "updated") and not date:
                date = ch.text
        yield title, link, parse_date(date)


def collect():
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=MAX_AGE_DAYS)
    items, seen = [], set()
    for label, url, filt in SOURCES:
        try:
            root = ET.fromstring(fetch(url))
        except Exception as exc:  # one bad feed must not break the rest
            print("skip %s: %s" % (label, exc), file=sys.stderr)
            continue
        got = 0
        rows = []
        for title, link, date in entries(root):
            title = clean(title)
            if not title or not link or not date:
                continue
            link = link.strip()
            if not link.lower().startswith("https://"):
                continue
            if date < cutoff or date > now + timedelta(days=1):
                continue
            if filt and not KEYWORDS.search(title):
                continue
            key = re.sub(r"\W+", "", title.lower())
            if link in seen or key in seen:
                continue
            rows.append((date, title, link, key))
        rows.sort(reverse=True)
        for date, title, link, key in rows[:PER_SOURCE]:
            seen.add(link)
            seen.add(key)
            items.append({"title": title, "url": link, "source": label, "date": date.strftime("%Y-%m-%d")})
            got += 1
        print("%s: %d" % (label, got), file=sys.stderr)
    items.sort(key=lambda i: i["date"], reverse=True)
    return items[:TOTAL]


def main():
    items = collect()
    if len(items) < 3:
        print("too few items (%d); leaving news.json unchanged" % len(items), file=sys.stderr)
        return 0
    try:
        with open(OUT, encoding="utf-8") as f:
            old = json.load(f)
    except Exception:
        old = {}
    if old.get("items") == items:
        print("no change", file=sys.stderr)
        return 0
    payload = {"updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "items": items}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote %d items" % len(items), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
