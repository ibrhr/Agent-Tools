# This code assumes you're in n8n, modify the variables according to your usecase


import re

def extract_primary_text(html):
    # Remove scripts, styles, comments, head, and other non-content
    html = re.sub(r'<script[^>]*>[\s\S]*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<style[^>]*>[\s\S]*?</style>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<head[^>]*>[\s\S]*?</head>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<!--[\s\S]*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'<noscript[^>]*>[\s\S]*?</noscript>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<iframe[^>]*>[\s\S]*?</iframe>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<object[^>]*>[\s\S]*?</object>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<embed[^>]*>[\s\S]*?</embed>', '', html, flags=re.IGNORECASE | re.DOTALL)

    # Remove remaining tags, replacing with space to preserve separation
    html = re.sub(r'<[^>]+>', ' ', html)

    # Normalize whitespace
    return re.sub(r'\s+', ' ', html).strip()

# In n8n Python Code node, input is 'items' (list of dicts)
# Assuming HTML is in item['json']['data'] (adjust field name if needed)
return [{'json': {'text': extract_primary_text(item['json']['data'])}} for item in items]
