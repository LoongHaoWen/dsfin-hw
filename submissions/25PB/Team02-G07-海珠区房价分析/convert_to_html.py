import markdown
import os

# 读取 Markdown 文件
md_file = "report.md"
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# 转换为 HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])

# 生成完整的 HTML 页面
html_page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>广州海珠区二手房价走势与影响因素分析</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif;
            line-height: 1.8;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 30px;
            color: #333;
            background-color: #ffffff;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 1.2em;
            margin-bottom: 0.6em;
            font-weight: 600;
        }}
        h1 {{
            font-size: 1.8em;
            border-bottom: 3px solid #3498db;
            padding-bottom: 12px;
            margin-bottom: 0.8em;
        }}
        h2 {{
            font-size: 1.4em;
            border-left: 4px solid #3498db;
            padding-left: 12px;
            margin-top: 1.5em;
        }}
        h3 {{
            font-size: 1.1em;
            color: #34495e;
            margin-top: 1.2em;
        }}
        p {{
            margin-bottom: 1em;
            text-align: justify;
        }}
        ul, ol {{
            margin-left: 2em;
            margin-bottom: 1em;
        }}
        li {{
            margin-bottom: 0.6em;
            line-height: 1.6;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1.5em 0;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
            border: 1px solid #e0e0e0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 14px 16px;
            text-align: left;
            font-size: 0.95em;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: 600;
            padding: 16px;
        }}
        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        tr:hover {{
            background-color: #f0f4f8;
        }}
        code {{
            background-color: #f5f5f5;
            padding: 3px 8px;
            border-radius: 3px;
            font-family: 'Courier New', 'Monaco', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 16px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 1em 0;
            font-size: 0.9em;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
            color: inherit;
        }}
        blockquote {{
            border-left: 5px solid #3498db;
            margin: 1.5em 0;
            padding: 12px 16px;
            background-color: #f0f7ff;
            color: #2c3e50;
            font-style: italic;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
            color: #2980b9;
        }}
        hr {{
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 2em 0;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .content {{
            line-height: 1.8;
        }}
    </style>
</head>
<body>
    <div class="content">
        {html_content}
    </div>
</body>
</html>"""

# 保存为 HTML 文件
html_file = "report.html"
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_page)

print("Report converted successfully")
