# MEMORY.md - Long-Term Memory

> Last updated: 2026-04-07

---

## About Human

- **數字密碼**：87958632（2026-04-02）
- **通訊渠道**：飛書（即時）

---

## Active Projects

### GLM Skills
- **進度**：3個技能已安裝，summarize-config.json 已更新為 Z_AI_API_KEY（智譜 Zhipu）
- **API Key**：✅ 已設定
- **詳見**：notes/research/glm-skills.md

### 台股季報爬蟲
- **進度**：1841 檔已完成（2025-Q4，`台股季報/2025/Q4/` 目測），skills target ~1871 檔
- **注意**：MEMORY.md 舊記錄 862/1205 口徑待確認（可能是某次中斷後重啟的子集？）
- **詳見**：notes/projects/twse-crawler.md

### 股票報告郵件
- **進度**：每週一自動發送，正常運行中
- **詳見**：notes/projects/stock-report-email.md

### MemPalace（記憶系統）
- **進度**：✅ 已安裝（pip3 + 清華鏡像）；Palace：`~/.mempalace/palace`；1876 drawers（workspace）；無需 API Key
- **詳見**：`notes/projects/mempalace.md`（待建立）

### CF Search（個人搜尋引擎）
- **進度**：✅ cascade 完整實作（Google→被擋→fallback）；tavily API 已加入並設為 cascade 第一優先
- **Repo**：`openclawGit200/openclaw-dashboard`（GitHub Actions 部署）
- **URL 更新**：`skills/multi-search-engine/config.json` → `proxy_base` 已改為 stable URL
- **已知問題**：send_email.py msg["Subject"] 未設定 → ✅ 已修（2026-04-08）

### 備份系統
- **本地備份**：每週一 03:00 自動執行（tar.gz，~164MB）
- **GitHub 異地備份**：✅ `openclawGit200/openclaw-backup`（public repo，~26MB）
- **遷移安裝**：`bash <(curl -L https://raw.githubusercontent.com/openclawGit200/openclaw-backup/main/install.sh)`
- **詳見**：notes/projects/backup.md、notes/projects/github.md

---

## Recent Research（已完成，待用戶決定）

存於 `notes/research/`：

| 主題 | 日期 | 狀態 |
|------|------|------|
| OpenHarness | 2026-04-05 | 📖 研究完成，決定不安裝，借鑽架構 |
| Agent-Threat-Rule | 2026-04-05 | 📖 研究完成，已移除安裝 |
| GLM Skills | 2026-04-05 | ✅ 已決定安裝，已完成 |

---

## Key Decisions

- **記憶系統重構方向（2026-04-06）**：
  - 取消 MEMORY_INDEX.md，回歸 MEMORY.md（當 L1 指標）
  - notes/research/ 放研究結果（還沒決定的）
  - notes/projects/ 放執行中專案詳情
  - memory/*.md 當 L3 原始日誌
  - 每完成工作 → 被動更新 MEMORY.md 進度，不等用戶提醒

---

## Lessons Learned

### 2026-04-05 - ATR 不適合用來掃 Skills
 atr scan 是監控工具（吃 events.json），不是靜態掃描器。如需安全審計，用 npm audit / semgrep。

### 2026-04-05 - GLM Skills 安裝
 clawhub 只支援一次裝一個，需輪流執行。VirusTotal 標記不一定是真的有害（股票工具本身就需要 external API）。

---

## Relationships & People

- 飛書使用者 ID：ou_9e78476eb905d306f9f7c835bf978e8b

---

*定期清理：memory/*.md（歸檔）、notes/research/（沉澱進 projects 或保留）*
