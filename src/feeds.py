import feedparser
from datetime import datetime, timedelta

def fetch_articles(rss_url, days_back=30):
    feed = feedparser.parse(rss_url)
    cutoff = datetime.now() - timedelta(days=days_back)

    articles = []
    for entry in feed.entries:
        published = getattr(entry, "published_parsed", None)
        if not published:
            continue

        published_date = datetime(*published[:6])
        if published_date >= cutoff:
            articles.append({
                "title": entry.title,
                "summary": entry.get("summary", ""),
                "link": entry.link,
                "date": published_date
            })

    return articles
