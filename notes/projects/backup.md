# 備份系統（GitHub 異地備份）

## 基本資訊
- **建立日期：** 2026-04-06
- **Repo：** `openclawGit200/openclaw-backup`
- **類型：** public（不含敏感資料）
- **大小：** ~26MB

---

## 目的
將 openclaw workspace 完整遷移到任意 Mac 電腦，透過 GitHub 作為載體。

---

## 內容（已包含）

| 項目 | 說明 |
|------|------|
| `skills/` | 所有已安裝 skills（24 個，含台股季報、163郵箱、記憶管理等）|
| `notes/` | 專案記憶、學習記錄 |
| `memory/` | 對話記憶檔（~21MB）|
| `scripts/` | 爬蟲、郵件腳本 |
| 核心設定檔 | AGENTS / SOUL / IDENTITY / USER / MEMORY / BOOTSTRAP / HEARTBEAT |
| LaunchAgent plist | `ai.openclaw.gateway.plist`、`taiwan-stock-crawler.plist` |

---

## 排除（安全 / 太大 / 可重建）

| 排除項目 | 原因 |
|------|------|
| `.credentials/` | 含 API key、token（嚴格排除）|
| `台股季報/` | PDF 可從 TWSE 重新下載 |
| `twse-reports-lib/` | 可重建 |
| `twse-semantic-search/` | 可重建 |
| `financial_reports/` | 可重建 |
| `twse-pdf-downloads/` | 可重建 |
| 各種 `test*.py`、`debug*.py` | 臨時檔案 |

完整排除規則：`.gitignore`

---

## 安裝方式（新 Mac 執行）

```bash
bash <(curl -L https://raw.githubusercontent.com/openclawGit200/openclaw-backup/main/install.sh)
```

**install.sh 做的事：**
1. 檢查 Homebrew
2. 安裝系統依賴（chromedriver、gh、summarize）
3. 安裝 Python pip 套件
4. 互動式引導輸入 API keys（**不寫進 repo**）
5. Clone backup repo 到 `~/.openclaw/workspace/`
6. 安裝 workspace skills
7. 設定 LaunchAgent（路徑自動置換）
8. 啟動 Gateway

---

## 依賴對照表

| 依賴 | 安裝方式 |
|------|----------|
| `chromedriver` | `brew install chromedriver` |
| `gh` | `brew install gh` |
| `summarize` | `brew install steipete/tap/summarize` |
| `selenium` `beautifulsoup4` `requests` `pypdf` `pandas` | `pip3 install -r requirements.txt` |
| `openclaw` | `brew install openclaw` |

> **記憶管理（memory-never-forget）：純 Markdown，不需要 SQLite**

---

## 同步頻率

目前為**手動触发**，未設定自動 sync。
日後可考慮在 HEARTBEAT 加入自動 commit + push。

---

## Related
- `notes/projects/github.md` — GitHub 設定
- `notes/projects/twse-crawler.md` — 台股季報爬蟲
- `.gitignore` — 完整排除規則
