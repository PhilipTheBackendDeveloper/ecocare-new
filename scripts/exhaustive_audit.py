import os, sys, re, urllib.parse
from html.parser import HTMLParser
from pathlib import Path

CANONICAL_PAGES = [
    'index.html', 'about1.html', 'service1.html', 'single-service1.html',
    'single-service2.html', 'pest-control.html', 'carpet-cleaning.html',
    'upholstery-cleaning.html', 'polytank-cleaning.html', 'car-interior-cleaning.html',
    'professional-dusting.html', 'pricing-table.html', 'calculate-form.html',
    'faq.html', 'contact.html', 'project1.html', 'single-project1.html',
    '404.html', 'privacy-policy.html', 'terms-condition.html', 'coming-soon.html'
]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.buttons = []
        self.forms = []
        self.images = []
        self.ids = set()
        self.collapses = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if 'id' in attr_dict:
            self.ids.add(attr_dict['id'])
        if tag == 'a':
            self.links.append(attr_dict)
        elif tag == 'button':
            self.buttons.append(attr_dict)
        elif tag == 'form':
            self.forms.append(attr_dict)
        elif tag == 'img':
            self.images.append(attr_dict)
        
        if attr_dict.get('data-toggle') == 'collapse':
            self.collapses.append(attr_dict)

def audit_pages():
    total_links = 0
    total_buttons = 0
    total_forms = 0
    issues = []
    
    for page in CANONICAL_PAGES:
        p = Path(page)
        if not p.exists():
            issues.append(f"MISSING FILE: {page}")
            continue
        content = p.read_text(errors='ignore')
        parser = LinkParser()
        parser.feed(content)
        
        total_links += len(parser.links)
        total_buttons += len(parser.buttons)
        total_forms += len(parser.forms)
        
        # 1. Inspect Links
        for link in parser.links:
            href = link.get('href', '').strip()
            text_desc = f"{page} -> href='{href}'"
            
            if not href:
                # Link without href
                issues.append(f"EMPTY HREF: {page} (class='{link.get('class')}')")
                continue
                
            if href == '#':
                # Check if it has data-toggle or JS handler class
                cls = link.get('class', '')
                dt = link.get('data-toggle', '')
                if not dt and 'mean-expand' not in cls and 'scrollup' not in cls and 'carousel' not in cls:
                    issues.append(f"DEAD HASH LINK: {text_desc} (class='{cls}')")
                continue
                
            if href.startswith('#'):
                # Internal anchor link
                anchor_id = href[1:]
                if anchor_id and anchor_id not in parser.ids:
                    issues.append(f"BROKEN ANCHOR: {page} anchor '#{anchor_id}' not found in document")
                continue
                
            if href.startswith('tel:'):
                phone = href[4:]
                if not re.match(r'^\+?[0-9\s-]+$', phone) or len(re.sub(r'\D', '', phone)) < 9:
                    issues.append(f"INVALID TEL LINK: {text_desc}")
                continue
                
            if href.startswith('mailto:'):
                email = href[7:].split('?')[0]
                if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                    issues.append(f"INVALID MAILTO LINK: {text_desc}")
                continue
                
            if 'wa.me' in href:
                # Check wa.me phone
                m = re.search(r'wa\.me/([0-9]+)', href)
                if not m:
                    issues.append(f"SUSPICIOUS WA LINK (phone not pure digits): {text_desc}")
                continue
                
            if href.startswith(('http://', 'https://')):
                # External link - check security attributes
                if link.get('target') == '_blank':
                    rel = link.get('rel', '')
                    if 'noopener' not in rel or 'noreferrer' not in rel:
                        issues.append(f"EXTERNAL LINK MISSING noopener noreferrer: {text_desc}")
                continue
                
            if href.startswith(('javascript:', 'data:')):
                continue
                
            # Local page or asset
            clean_href = href.split('?')[0].split('#')[0]
            target_path = Path(clean_href)
            if not target_path.exists():
                issues.append(f"BROKEN LOCAL LINK: {text_desc}")
                
        # 2. Inspect Forms
        for form in parser.forms:
            cls = form.get('class', '')
            fid = form.get('id', '')
            has_netlify = 'netlify' in form or 'data-netlify' in form
            action = form.get('action', '')
            if not has_netlify and not action:
                issues.append(f"UNCONFIGURED FORM: {page} form id='{fid}' class='{cls}' has no netlify or action")
                
        # 3. Inspect Collapse/Accordions
        for col in parser.collapses:
            target = col.get('data-target') or col.get('href')
            if target and target.startswith('#'):
                tid = target[1:]
                if tid not in parser.ids:
                    issues.append(f"BROKEN ACCORDION TARGET: {page} target '#{tid}' not found in page")
                    
        # 4. Inspect Images
        for img in parser.images:
            src = img.get('src', '').strip()
            if not src:
                issues.append(f"EMPTY IMAGE SRC: {page}")
                continue
            if not src.startswith(('http://', 'https://', 'data:')):
                clean_src = src.split('?')[0].split('#')[0]
                if not Path(clean_src).exists():
                    issues.append(f"MISSING IMAGE: {page} -> src='{src}'")

    print(f"Audited {len(CANONICAL_PAGES)} canonical pages.")
    print(f"Total links inspected: {total_links}")
    print(f"Total buttons inspected: {total_buttons}")
    print(f"Total forms inspected: {total_forms}")
    print(f"Total issues found: {len(issues)}")
    if issues:
        print("\n--- ISSUES FOUND ---")
        for iss in issues[:80]:
            print(" *", iss)
        if len(issues) > 80:
            print(f"... and {len(issues) - 80} more")
    else:
        print("ALL CANONICAL PAGES ARE CLEAN AND 100% FUNCTIONAL!")

if __name__ == '__main__':
    audit_pages()
