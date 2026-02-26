#!/usr/bin/env python3
"""
将 Confluence 导出的 .doc (MIME/HTML) 文件转换为 Markdown
"""

import sys
import os
import email
import quopri
import re
import subprocess
from pathlib import Path


def extract_html_from_confluence_doc(filepath):
    """从 Confluence 导出的 .doc 文件中提取 HTML 内容"""
    with open(filepath, "rb") as f:
        raw = f.read()

    # 尝试解析为 MIME 邮件格式
    msg = email.message_from_bytes(raw)

    html_content = None

    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            if "html" in ct:
                payload = part.get_payload(decode=True)
                if payload:
                    html_content = payload.decode("utf-8", errors="replace")
                    break
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            html_content = payload.decode("utf-8", errors="replace")

    # 如果 MIME 解析失败，尝试直接 quoted-printable 解码
    if not html_content:
        try:
            decoded = quopri.decodestring(raw).decode("utf-8", errors="replace")
            if "<html" in decoded.lower():
                html_content = decoded
        except Exception:
            pass

    return html_content


def html_to_markdown(html_content, output_path):
    """使用 pandoc 将 HTML 转为 Markdown"""
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none", "-o", output_path],
        input=html_content.encode("utf-8"),
        capture_output=True,
    )
    return result.returncode == 0


def convert_file(doc_path, md_path):
    html = extract_html_from_confluence_doc(doc_path)
    if not html:
        print(f"FAIL (no HTML): {doc_path}")
        return False

    if html_to_markdown(html, md_path):
        print(f"OK: {md_path}")
        return True
    else:
        print(f"FAIL (pandoc): {doc_path}")
        return False


def main():
    docs_dir = Path("/Users/doris/Documents/cctest/Hertzflow/docs")

    doc_files = list(docs_dir.rglob("*.doc"))
    print(f"找到 {len(doc_files)} 个 .doc 文件\n")

    ok, fail = 0, 0
    for doc_path in sorted(doc_files):
        md_path = str(doc_path.with_suffix(".md"))
        if convert_file(str(doc_path), md_path):
            ok += 1
        else:
            fail += 1

    print(f"\n完成：成功 {ok} 个，失败 {fail} 个")


if __name__ == "__main__":
    main()
