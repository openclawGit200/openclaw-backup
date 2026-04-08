# HEARTBEAT.md

> OpenClaw polls this file. If it contains tasks, the agent executes them.
> Update project statuses → then clear the tasks below after completing.

---

## MEMORY.md 進度同步（每次 poll 更新）

- [x] **台股季報爬蟲**：1841 檔已完成（2025-Q4）
- [x] **股票報告郵件**：每週一～五 07:00，下次 2026-04-09（四）07:00；已修復 msg["Subject"] ✅；engine=cascade ✅；tavily 加入 cascade ✅
- [x] **CF Search**：✅ cascade 完整實作；tavily 加入 cascade 第一優先；Repo: `openclawGit200/openclaw-search`
- [x] **CF Dashboard**：✅ v3 完成（統一記憶；Jobs 中文名+可點擊看歷史）；URL: `https://dc6a096a.openclaw-dashboard-dv8.pages.dev/`；Repo: `openclawGit200/openclaw-dashboard`；crawler-sync=週日23:00；semantic-sync=週一23:00
- [x] **備份系統**：✅ GitHub backup 每週六 03:00；local backup 每週一 03:00
- [x] **MemPalace**：✅ 已安裝；Palace 路徑 `~/.mempalace/palace`；1876 drawers
- [x] **summarize API key**：Z_AI_API_KEY 已設定並驗證（glm-5）；本地大檔 >10KB 仍 empty（summarize CLI bug）
- [x] **PDF OCR**：南港 PDF 第9-11頁為圖片掃描，pypdf 讀不到，待處理（tesseract OCR）
- [x] **sessions-memory hook**：✅ 已啟用（2026-04-08）；session reset 時自動歸檔

---

## 執行完後

1. 把上方 `[ ]` 任務狀態更新（打勾或填入狀態）
2. 如果有進度變化 → 主動更新 MEMORY.md 的對應進度
3. 回 `HEARTBEAT_OK`

---

> 有新問題或卡點，隨時寫進 HEARTBEAT.md，OpenClaw 會通知我。
