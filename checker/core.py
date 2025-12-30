# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class ScriptSafetyChecker:
    # Heuristic: Find <script src="..."> tags.
    # Check if they look like external CDN links.
    # Check if they have 'integrity' and 'crossorigin' attributes.
    
    # Regex find all <script ... >
    SCRIPT_TAG_PATTERN = re.compile(r'<script\b([^>]*)>', re.IGNORECASE)
    
    # Regex to extract src, integrity, crossorigin from attributes string
    SRC_PATTERN = re.compile(r'src=["\']([^"\']+)["\']', re.IGNORECASE)
    INTEGRITY_PATTERN = re.compile(r'integrity=["\']([^"\']+)["\']', re.IGNORECASE)
    
    @staticmethod
    def is_external_cdn(url):
        # List of common CDNs or typical external patterns
        # or simply check if it starts with http/https and is not localhost
        if not url.startswith(('http://', 'https://', '//')):
            return False # Likely local
        if 'localhost' in url or '127.0.0.1' in url:
            return False
        return True

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for match in ScriptSafetyChecker.SCRIPT_TAG_PATTERN.finditer(content):
                attrs = match.group(1)
                
                # Check for src
                src_match = ScriptSafetyChecker.SRC_PATTERN.search(attrs)
                if not src_match:
                    continue # Inline script or no src
                
                src = src_match.group(1)
                if not ScriptSafetyChecker.is_external_cdn(src):
                    continue
                    
                # It is external. Check integrity.
                integrity_match = ScriptSafetyChecker.INTEGRITY_PATTERN.search(attrs)
                
                line_nm = content[:match.start()].count('\n') + 1
                
                if not integrity_match:
                    issues.append({
                        'line': line_nm,
                        'file': filepath,
                        'url': src,
                        'msg': 'External script missing subresource integrity (SRI) hash'
                    })
                    
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith(('.html', '.htm', '.php', '.jsp')):
                    path = os.path.join(root, file)
                    issues = ScriptSafetyChecker.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
