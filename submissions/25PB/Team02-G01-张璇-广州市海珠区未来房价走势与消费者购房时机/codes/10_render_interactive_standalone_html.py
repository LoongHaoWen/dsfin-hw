"""Render report.md into a standalone interactive HTML document.

The output embeds CSS, JavaScript, and local images as data URIs so the file can
be copied to another computer and opened directly in a browser.
"""

from __future__ import annotations

import base64
import mimetypes
import re
from pathlib import Path

import mistune


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATHS = [
    ROOT / "report.pdf.html",
    ROOT / "report_interactive.html",
]


def embed_images(html: str) -> str:
    def replace_src(match: re.Match[str]) -> str:
        src = match.group(1)
        if src.startswith(("data:", "http://", "https://")):
            return match.group(0)
        image_path = (ROOT / src).resolve()
        if not image_path.exists():
            return match.group(0)
        mime = mimetypes.guess_type(image_path.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
        return f'src="data:{mime};base64,{encoded}"'

    return re.sub(r'src="([^"]+)"', replace_src, html)


def add_heading_ids(html: str) -> str:
    seen: dict[str, int] = {}

    def slugify(text: str) -> str:
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text, flags=re.UNICODE).strip("-").lower()
        text = text or "section"
        seen[text] = seen.get(text, 0) + 1
        return text if seen[text] == 1 else f"{text}-{seen[text]}"

    def replace_heading(match: re.Match[str]) -> str:
        level, content = match.group(1), match.group(2)
        return f'<h{level} id="{slugify(content)}">{content}</h{level}>'

    return re.sub(r"<h([23])>(.*?)</h\1>", replace_heading, html)


def render_body() -> str:
    markdown = mistune.create_markdown(plugins=["table", "strikethrough"])
    html = markdown((ROOT / "report.md").read_text(encoding="utf-8"))
    html = embed_images(html)
    html = add_heading_ids(html)
    html = html.replace("<table>", '<div class="table-wrap"><table>')
    html = html.replace("</table>", "</table></div>")
    html = html.replace("<img ", '<img loading="lazy" ')
    return html


def build_html(body: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>广州市海珠区未来房价走势与消费者购房时机判断</title>
<style>
:root {{
  --bg: #f5f7fb;
  --paper: #ffffff;
  --ink: #1f2b36;
  --muted: #5f6f7f;
  --line: #d7e0ea;
  --soft: #eef4f8;
  --accent: #1f5f8b;
  --accent-2: #0f7c6b;
  --warn: #9b4f12;
  --shadow: 0 18px 50px rgba(31, 43, 54, 0.12);
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.72;
}}
body.presenting {{
  --paper: #fbfdff;
  font-size: 19px;
}}
.progress {{
  position: fixed;
  inset: 0 auto auto 0;
  width: 0;
  height: 4px;
  z-index: 20;
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
}}
.app-shell {{
  display: grid;
  grid-template-columns: 292px minmax(0, 1fr);
  min-height: 100vh;
}}
.sidebar {{
  position: sticky;
  top: 0;
  height: 100vh;
  padding: 24px 20px;
  overflow: auto;
  border-right: 1px solid var(--line);
  background: #ffffff;
}}
.brand {{
  margin-bottom: 20px;
  padding-bottom: 18px;
  border-bottom: 1px solid var(--line);
}}
.brand strong {{
  display: block;
  font-size: 17px;
  line-height: 1.35;
  color: #15334e;
}}
.brand span {{
  display: block;
  margin-top: 8px;
  font-size: 13px;
  color: var(--muted);
}}
.tools {{
  display: grid;
  gap: 10px;
  margin-bottom: 18px;
}}
.search-box {{
  width: 100%;
  min-height: 40px;
  padding: 9px 11px;
  border: 1px solid var(--line);
  border-radius: 6px;
  color: var(--ink);
  background: #fbfcfd;
  font: inherit;
  font-size: 14px;
}}
.button-row {{
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 8px;
}}
button {{
  min-height: 36px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #ffffff;
  color: #21384d;
  cursor: pointer;
  font: inherit;
  font-size: 13px;
}}
button:hover, button.active {{
  border-color: #9bb9d0;
  background: #eef6fc;
}}
.toc {{
  display: grid;
  gap: 2px;
  font-size: 14px;
}}
.toc a {{
  display: block;
  padding: 7px 8px;
  border-radius: 6px;
  color: #29465f;
  text-decoration: none;
}}
.toc a[data-level="3"] {{
  padding-left: 20px;
  font-size: 13px;
  color: #627386;
}}
.toc a:hover, .toc a.active {{
  background: #eef5fb;
  color: #123c5f;
}}
.main {{
  padding: 36px min(5vw, 64px) 56px;
}}
.hero {{
  max-width: 1120px;
  margin: 0 auto 22px;
  padding: 26px 30px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: linear-gradient(135deg, #ffffff 0%, #f0f6fb 100%);
  box-shadow: var(--shadow);
}}
.hero h1 {{
  margin: 0;
  color: #15334e;
  font-size: clamp(28px, 4vw, 46px);
  line-height: 1.18;
}}
.hero p {{
  max-width: 880px;
  margin: 16px 0 0;
  color: #526577;
  font-size: 17px;
}}
.keynote-grid {{
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  max-width: 1120px;
  margin: 0 auto 24px;
}}
.keynote {{
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #ffffff;
}}
.keynote strong {{
  display: block;
  color: var(--accent);
  font-size: 14px;
}}
.keynote span {{
  display: block;
  margin-top: 6px;
  color: var(--muted);
  font-size: 14px;
}}
.content {{
  max-width: 1120px;
  margin: 0 auto;
  padding: 38px 46px;
  border-radius: 8px;
  background: var(--paper);
  box-shadow: var(--shadow);
}}
h1, h2, h3 {{
  color: #173b5a;
  line-height: 1.35;
  letter-spacing: 0;
}}
.content > h1:first-child {{
  display: none;
}}
h2 {{
  position: relative;
  margin-top: 38px;
  padding-top: 8px;
  font-size: 24px;
  border-top: 1px solid #edf2f6;
}}
h3 {{
  margin-top: 26px;
  font-size: 19px;
}}
p, li {{
  font-size: 16px;
}}
blockquote {{
  margin: 18px 0;
  padding: 12px 16px;
  border-left: 4px solid #86aeca;
  color: #526577;
  background: #f5f9fc;
}}
.table-wrap {{
  overflow-x: auto;
  margin: 16px 0 22px;
  border: 1px solid var(--line);
  border-radius: 8px;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  min-width: 680px;
  font-size: 14px;
}}
th, td {{
  padding: 10px 12px;
  border: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}}
th {{
  background: #edf4fa;
  color: #21384d;
}}
img {{
  max-width: 100%;
  display: block;
  margin: 18px auto;
  border: 1px solid #e0e7ef;
  border-radius: 8px;
  background: #ffffff;
  cursor: zoom-in;
}}
mark {{
  padding: 0 2px;
  border-radius: 3px;
  background: #fff0a8;
}}
code {{
  padding: 2px 4px;
  border-radius: 4px;
  background: #eef2f5;
}}
.section-hidden {{
  display: none;
}}
.section-toggle {{
  float: right;
  width: 32px;
  min-height: 28px;
  margin-left: 8px;
  padding: 0;
  color: var(--muted);
}}
.lightbox {{
  position: fixed;
  inset: 0;
  z-index: 50;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 28px;
  background: rgba(11, 22, 32, 0.82);
}}
.lightbox.open {{
  display: flex;
}}
.lightbox img {{
  width: auto;
  max-width: 96vw;
  max-height: 90vh;
  margin: 0;
  border-radius: 8px;
  cursor: zoom-out;
}}
.status {{
  margin: 10px 0 0;
  min-height: 20px;
  color: var(--muted);
  font-size: 13px;
}}
body.presenting .sidebar {{
  display: none;
}}
body.presenting .app-shell {{
  display: block;
}}
body.presenting .main {{
  padding-inline: 4vw;
}}
body.presenting .content {{
  max-width: 1220px;
  padding: 52px 64px;
}}
body.presenting h2 {{
  font-size: 32px;
}}
body.presenting h3 {{
  font-size: 24px;
}}
@media (max-width: 900px) {{
  .app-shell {{
    display: block;
  }}
  .sidebar {{
    position: relative;
    height: auto;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }}
  .main {{
    padding: 18px;
  }}
  .content {{
    padding: 24px 18px;
  }}
  .keynote-grid {{
    grid-template-columns: 1fr;
  }}
  .button-row {{
    grid-template-columns: 1fr;
  }}
  .hero {{
    padding: 22px 18px;
  }}
  table {{
    min-width: 760px;
  }}
}}
@media print {{
  .sidebar, .progress, .tools, .section-toggle, .lightbox {{
    display: none !important;
  }}
  .app-shell {{
    display: block;
  }}
  .main, .content {{
    padding: 0;
    box-shadow: none;
  }}
  body {{
    background: #fff;
  }}
}}
</style>
</head>
<body>
<div class="progress" id="progress"></div>
<div class="app-shell">
  <aside class="sidebar" aria-label="交互目录">
    <div class="brand">
      <strong>海珠区房价趋势与购房时机判断</strong>
      <span>离线交互展示版</span>
    </div>
    <div class="tools">
      <input id="search" class="search-box" type="search" placeholder="搜索关键词，例如 琶洲 / 月供 / 二手房" aria-label="全文搜索">
      <div class="button-row">
        <button id="toggleSections" type="button">折叠章节</button>
        <button id="presentMode" type="button">演讲模式</button>
      </div>
      <div class="button-row">
        <button id="clearSearch" type="button">清除搜索</button>
        <button id="topButton" type="button">回到顶部</button>
      </div>
      <div class="status" id="status">可点击图表放大查看。</div>
    </div>
    <nav class="toc" id="toc"></nav>
  </aside>
  <main class="main">
    <section class="hero" id="top">
      <h1>广州市海珠区未来房价走势与消费者购房时机判断</h1>
      <p>这是一份可离线演示的互动报告：用政策、价格指数、成交热度、人口产业基本面和支付能力，回答“今年是否适合在海珠区买房”。</p>
    </section>
    <section class="keynote-grid" aria-label="展示主线">
      <div class="keynote"><strong>1. 市场是否回暖</strong><span>先看广州大盘、全国周期和官方成交热度。</span></div>
      <div class="keynote"><strong>2. 海珠是否有支撑</strong><span>再看人口、产业、琶洲和一二手价格结构。</span></div>
      <div class="keynote"><strong>3. 消费者能否承受</strong><span>最后回到总价、月供和现金流安全边际。</span></div>
    </section>
    <article class="content" id="content">
{body}
    </article>
  </main>
</div>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="图表放大预览">
  <img id="lightboxImage" alt="">
</div>
<script>
(function () {{
  const content = document.getElementById('content');
  const toc = document.getElementById('toc');
  const status = document.getElementById('status');
  const progress = document.getElementById('progress');
  const search = document.getElementById('search');
  const headings = Array.from(content.querySelectorAll('h2, h3'));
  const sections = [];
  let collapsed = false;

  headings.forEach((heading) => {{
    const level = heading.tagName === 'H2' ? 2 : 3;
    const link = document.createElement('a');
    link.href = '#' + heading.id;
    link.textContent = heading.textContent;
    link.dataset.level = String(level);
    toc.appendChild(link);

    if (level === 2) {{
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'section-toggle';
      button.textContent = '−';
      button.title = '展开或折叠本章节';
      heading.prepend(button);
      button.addEventListener('click', (event) => {{
        event.preventDefault();
        toggleOneSection(heading);
      }});
    }}
  }});

  Array.from(content.querySelectorAll('h2')).forEach((h2) => {{
    const nodes = [];
    let node = h2.nextElementSibling;
    while (node && node.tagName !== 'H2') {{
      nodes.push(node);
      node = node.nextElementSibling;
    }}
    sections.push({{ heading: h2, nodes }});
  }});

  function toggleOneSection(h2, forceOpen) {{
    const section = sections.find((item) => item.heading === h2);
    if (!section) return;
    const shouldHide = forceOpen === undefined ? !section.nodes[0]?.classList.contains('section-hidden') : !forceOpen;
    section.nodes.forEach((node) => node.classList.toggle('section-hidden', shouldHide));
    const button = h2.querySelector('.section-toggle');
    if (button) button.textContent = shouldHide ? '+' : '−';
  }}

  document.getElementById('toggleSections').addEventListener('click', () => {{
    collapsed = !collapsed;
    sections.forEach((section, index) => toggleOneSection(section.heading, collapsed && index > 0 ? false : true));
    document.getElementById('toggleSections').textContent = collapsed ? '展开章节' : '折叠章节';
  }});

  document.getElementById('presentMode').addEventListener('click', () => {{
    document.body.classList.toggle('presenting');
    const active = document.body.classList.contains('presenting');
    document.getElementById('presentMode').classList.toggle('active', active);
    status.textContent = active ? '演讲模式已开启：使用方向键切换章节，Esc 退出。' : '可点击图表放大查看。';
  }});

  document.getElementById('topButton').addEventListener('click', () => window.scrollTo({{ top: 0, behavior: 'smooth' }}));
  document.getElementById('clearSearch').addEventListener('click', () => {{
    search.value = '';
    restoreHighlights();
    status.textContent = '搜索已清除。';
  }});

  function restoreHighlights() {{
    content.querySelectorAll('mark').forEach((mark) => {{
      mark.replaceWith(document.createTextNode(mark.textContent));
    }});
    content.normalize();
  }}

  function highlightText(term) {{
    restoreHighlights();
    if (!term) return 0;
    let count = 0;
    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {{
      acceptNode(node) {{
        const parent = node.parentElement;
        if (!parent || ['SCRIPT', 'STYLE', 'MARK'].includes(parent.tagName)) return NodeFilter.FILTER_REJECT;
        return node.nodeValue.toLowerCase().includes(term.toLowerCase()) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }}
    }});
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach((node) => {{
      const text = node.nodeValue;
      const re = new RegExp(term.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
      const fragment = document.createDocumentFragment();
      let lastIndex = 0;
      text.replace(re, (match, offset) => {{
        fragment.appendChild(document.createTextNode(text.slice(lastIndex, offset)));
        const mark = document.createElement('mark');
        mark.textContent = match;
        fragment.appendChild(mark);
        lastIndex = offset + match.length;
        count += 1;
      }});
      fragment.appendChild(document.createTextNode(text.slice(lastIndex)));
      node.replaceWith(fragment);
    }});
    const first = content.querySelector('mark');
    if (first) first.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    return count;
  }}

  search.addEventListener('input', () => {{
    const term = search.value.trim();
    const count = highlightText(term);
    status.textContent = term ? `找到 ${{count}} 处匹配。` : '可点击图表放大查看。';
  }});

  const lightbox = document.getElementById('lightbox');
  const lightboxImage = document.getElementById('lightboxImage');
  content.querySelectorAll('img').forEach((img) => {{
    img.addEventListener('click', () => {{
      lightboxImage.src = img.src;
      lightboxImage.alt = img.alt || '图表预览';
      lightbox.classList.add('open');
    }});
  }});
  lightbox.addEventListener('click', () => lightbox.classList.remove('open'));

  const tocLinks = Array.from(toc.querySelectorAll('a'));
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach((entry) => {{
      if (!entry.isIntersecting) return;
      tocLinks.forEach((link) => link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id));
    }});
  }}, {{ rootMargin: '-20% 0px -70% 0px' }});
  headings.forEach((heading) => observer.observe(heading));

  function updateProgress() {{
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const pct = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
    progress.style.width = pct + '%';
  }}
  window.addEventListener('scroll', updateProgress, {{ passive: true }});
  updateProgress();

  function navigateSection(direction) {{
    const visibleHeadings = headings.filter((heading) => heading.offsetParent !== null);
    const current = visibleHeadings.findIndex((heading) => heading.getBoundingClientRect().top > 80);
    const targetIndex = direction > 0
      ? Math.min(visibleHeadings.length - 1, Math.max(0, current))
      : Math.max(0, (current === -1 ? visibleHeadings.length : current) - 2);
    visibleHeadings[targetIndex]?.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }}
  document.addEventListener('keydown', (event) => {{
    if (event.key === 'Escape') {{
      lightbox.classList.remove('open');
      document.body.classList.remove('presenting');
      document.getElementById('presentMode').classList.remove('active');
    }}
    if (!document.body.classList.contains('presenting')) return;
    if (event.key === 'ArrowRight' || event.key === 'PageDown') navigateSection(1);
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') navigateSection(-1);
  }});
}}());
</script>
</body>
</html>
"""


def main() -> None:
    body = render_body()
    html = build_html(body)
    for output_path in OUTPUT_PATHS:
        output_path.write_text(html, encoding="utf-8")
        print(output_path)


if __name__ == "__main__":
    main()
