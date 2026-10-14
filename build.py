"""Builds the GitHub Pages site (docs/index.html) from src/page.html.

src/page.html is the page body with its own <title>, styles and script; the
same file is published as a Claude artifact, which adds the document shell
itself. For GitHub Pages it gets a full document around it here.
"""

import pathlib

root = pathlib.Path(__file__).parent
page = (root / "src" / "page.html").read_text(encoding="utf-8")
head, _, body = page.partition("</style>")
shell = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Hamdan Rijali Triyadi, Senior Backend Software Engineer in Bandung: Java, Spring Boot, NestJS, and self-hosted AI products.">
<meta property="og:title" content="Hamdan Rijali Triyadi">
<meta property="og:description" content="Senior Backend Software Engineer: experience, projects and contact.">
{head}</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""
out = root / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(shell, encoding="utf-8", newline="\n")
print(f"wrote {out} ({len(shell)} bytes)")
