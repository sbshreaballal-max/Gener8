def filter_articles(articles, persona):
    keywords = persona["include_keywords"]
    filtered = []

    for a in articles:
        text = (a["title"] + " " + a["summary"]).lower()
        if any(k.lower() in text for k in keywords):
            filtered.append(a)

    return filtered

