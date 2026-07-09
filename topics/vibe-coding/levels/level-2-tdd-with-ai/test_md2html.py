from md2html import convert

def test_h1_heading():
    assert "<h1>Hello</h1>" in convert("# Hello")

def test_h2_heading():
    assert "<h2>World</h2>" in convert("## World")

def test_h3_heading():
    assert "<h3>Python</h3>" in convert("### Python")

def test_bold():
    assert "<strong>bold</strong>" in convert("**bold**")

def test_italic():
    assert "<em>italic</em>" in convert("*italic*")

def test_inline_code():
    assert "<code>code</code>" in convert("`code`")

def test_unordered_list():
    html = convert("- Apple\n- Banana")
    assert "<li>Apple</li>" in html
    assert "<li>Banana</li>" in html

def test_ordered_list():
    html = convert("1. One\n2. Two")
    assert "<li>One</li>" in html
    assert "<li>Two</li>" in html

def test_link():
    html = convert("[OpenAI](https://openai.com)")
    assert '<a href="https://openai.com">OpenAI</a>' in html

def test_paragraph():
    html = convert("Hello")
    assert "<p>Hello</p>" in html

def test_empty():
    assert convert("").strip() != ""

def test_code_block():
    html = convert("```\nprint('Hi')\n```")
    assert "<pre><code>" in html
    assert "</code></pre>" in html
