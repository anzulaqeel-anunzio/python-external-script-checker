# External Script Safety Checker

A security scanner that audits HTML files for external `<script>` tags (CDNs) missing standard **Subresource Integrity (SRI)** attributes. Using SRI protects your site if a third-party CDN is compromised.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Audit**: Flags generic `http/https` script sources without `integrity="..."`.
*   **SRI Enforcement**: Encourages security best practices.
*   **Zero Dependencies**: Pure Python.

## Usage

```bash
python run_checker.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_checker.py templates/
```

**2. Detects**
```html
<!-- Flagged: No integrity hash -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<!-- Safe: Has integrity -->
<script src="..." integrity="sha384-..."></script>
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
