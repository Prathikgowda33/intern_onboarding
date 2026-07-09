#!/usr/bin/env python3

import argparse
import html
import os
import re
import sys


def inline(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        text,
    )
    return text


def convert(md):
    lines = md.splitlines()
    out = []
    in_ul = False
    in_ol = False
    in_code = False

    for line in lines:

        if line.startswith("```"):
            if not in_code:
                out.append("<pre><code>")
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue

        if in_code:
            out.append(html.escape(line))
            continue

        if line.startswith("# "):
            out.append(f"<h1>{inline(line[2:])}</h1>")
            continue

        if line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
            continue

        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
            continue

        if re.match(r"^- ", line):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(line[2:])}</li>")
            continue
        elif in_ul:
            out.append("</ul>")
            in_ul = False

        if re.match(r"^\d+\. ", line):
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            item = re.sub(r"^\d+\. ", "", line)
            out.append(f"<li>{inline(item)}</li>")
            continue
        elif in_ol:
            out.append("</ol>")
            in_ol = False

        if line.startswith("> "):
            out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
            continue

        if line.strip() == "---":
            out.append("<hr>")
            continue

        if line.strip():
            out.append(f"<p>{inline(line)}</p>")

    if in_ul:
        out.append("</ul>")
    if in_ol:
        out.append("</ol>")

    body = "\n".join(out)

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Markdown Output</title>
</head>
<body>
{body}
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown to HTML."
    )
    parser.add_argument("input", nargs="?", help="Input markdown file")
    parser.add_argument("-o", "--output", help="Output HTML file")

    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        sys.exit(1)

    if not os.path.exists(args.input):
        print(f"Error: '{args.input}' not found.")
        sys.exit(1)

    if not args.output:
        print("Error: output file required (-o)")
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
        md = f.read()

    html_doc = convert(md)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html_doc)

    print(f"HTML written to {args.output}")


if __name__ == "__main__":
    main()
