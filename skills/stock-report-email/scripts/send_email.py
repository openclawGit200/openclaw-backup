#!/usr/bin/env python3
"""
send_email.py — 發送 HTML 郵件（163 SMTP）
用法：
  python3 send_email.py --to "allen.chen@titanlight.com;cheelsu@gmail.com" \
    --subject "符合指標的標的 AI版" \
    --body /tmp/stock_email_body.html
"""

import argparse
import json
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

CRED_PATH = Path.home() / ".openclaw" / "workspace" / ".credentials" / "163email.json"


def html_to_plain(html):
    """簡單剷除 HTML 標籤，保留文字"""
    import re
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--to", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", default="/tmp/stock_email_body.html")
    parser.add_argument("--cc", default="")
    args = parser.parse_args()

    creds = json.load(open(CRED_PATH))

    with open(args.body, "r", encoding="utf-8") as f:
        html_body = f.read()

    msg = MIMEMultipart("alternative")
    # 支援分號分隔的多收件人
    to_list = [e.strip() for e in args.to.split(";") if e.strip()]
    msg["From"] = creds["email"]
    msg["To"] = "; ".join(to_list)
    msg["Subject"] = args.subject
    if args.cc:
        msg["Cc"] = args.cc

    plain = html_to_plain(html_body)
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    recipients = to_list[:]
    if args.cc:
        recipients += [e.strip() for e in args.cc.split(";") if e.strip()]

    try:
        server = smtplib.SMTP_SSL(creds["smtp_host"], creds["smtp_port"])
        server.login(creds["email"], creds["auth_code"])
        server.sendmail(creds["email"], recipients, msg.as_string())
        server.quit()
        print(f"✅ 郵件已發送至 {', '.join(to_list)}", file=sys.stderr)
    except Exception as e:
        print(f"❌ 發送失敗：{e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
