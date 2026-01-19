import re

def summarize_articles(articles, max_sentences=3):
    if not articles:
        return "No relevant articles found for this persona."

    text = " ".join(a["summary"] for a in articles)
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Clean + dedupe
    seen = set()
    clean_sentences = []
    for s in sentences:
        s = s.strip()
        if len(s) > 40 and s not in seen:
            clean_sentences.append(s)
            seen.add(s)

    return " ".join(clean_sentences[:max_sentences])

