# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from checker.core import ScriptSafetyChecker

def main():
    parser = argparse.ArgumentParser(description="External Script Safety Checker")
    parser.add_argument("path", help="Directory or file to scan (defaults to current dir)", nargs='?', default=".")
    
    args = parser.parse_args()
    path = os.path.abspath(args.path)
    
    issues = []
    
    if os.path.isfile(path):
        issues = ScriptSafetyChecker.scan_file(path)
    elif os.path.isdir(path):
        issues = ScriptSafetyChecker.scan_directory(path)
    else:
        print(f"Error: Path '{path}' not found.")
        sys.exit(1)
        
    if not issues:
        print("Secure! All external scripts have integrity checks (or none found).")
        sys.exit(0)
        
    print(f"Found {len(issues)} potentially unsafe external scripts:\n")
    for issue in issues:
        print(f"[{issue['file']}:{issue['line']}] {issue['msg']}")
        print(f"  URL: {issue['url']}")
        
    sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
