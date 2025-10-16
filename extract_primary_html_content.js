// This code assumes you're in n8n, modify the variables according to your usecase

function extractPrimaryText(html) {
  // Remove scripts, styles, comments, head, and other non-content
  html = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
             .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
             .replace(/<head[^>]*>[\s\S]*?<\/head>/gi, '')
             .replace(/<!--[\s\S]*?-->/g, '')
             .replace(/<noscript[^>]*>[\s\S]*?<\/noscript>/gi, '')
             .replace(/<iframe[^>]*>[\s\S]*?<\/iframe>/gi, '')
             .replace(/<object[^>]*>[\s\S]*?<\/object>/gi, '')
             .replace(/<embed[^>]*>[\s\S]*?<\/embed>/gi, '');

  // Remove remaining tags, replacing with space to preserve separation
  html = html.replace(/<[^>]+>/g, ' ');

  // Normalize whitespace
  return html.trim().replace(/\s+/g, ' ');
}

return $input.all().map(item => ({ json: { text: extractPrimaryText(item.json.data) } }));
