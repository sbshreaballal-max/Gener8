from datetime import date

def generate_brief(persona, summary, articles):
    today = date.today().isoformat()

    brief = f"""
# 📰 AI News Brief — {persona['persona']['name']}
**Date:** {today}

## TL;DR
{summary}

## Top Articles
"""

    for a in articles[:5]:
        brief += f"""
### {a['title']}
{a['summary']}

🔗 {a['link']}
"""

    return brief

