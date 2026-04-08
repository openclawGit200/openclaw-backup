# HEARTBEAT.md

> OpenClaw polls this file. If it contains tasks, the agent executes them.
> Update project statuses → then clear the tasks below after completing.

---

## MEMORY.md 進度同步（每次 poll 更新）

- [x] **GLM Skills**：ZHIPU_API_KEY 已設定（glm-4-flash/glm-5）；glmv-stock-analyst 對台股（2101.TW）支援有限（financials/technicals 均 empty）
- [x] **台股季報爬蟲**：1841 檔（2025-Q4，目測）
- [x] **股票報告郵件**：每週一～五 07:00，下次 2026-04-09（四）07:00；已修復：msg["Subject"] 未設定 ✅；tavily 加入 cascade ✅；engine=cascade 已實作 ✅
  [x] **CF Search**：✅ cascade 完整實作；tavily 已加入 cascade 第一優先；Repo: `openclawGit200/openclaw-search`
- [x] **備份系統**：✅ GitHub backup 已建立，每週六 03:00 自動執行
- [x] **summarize API key**：已更新為 Zhipu（Z_AI_API_KEY），summarize + Zhipu(glm-5) URL/中文/stdin 正常；本地大檔案（>10KB TXT）仍 empty，是 summarize CLI 對長檔案的已知問題
- [x] **summarize API key**：Z_AI_API_KEY 已設定並驗證（glm-5）；URL/stdin 正常，本地大檔 >10KB 仍 empty（summarize CLI bug）
- [x] **PDF OCR**：南港 PDF 第9-11頁為圖片掃描，pypdf 讀不到，需整合 tesseract OCR（待處理）
- [x] **CF Dashboard**：✅ v3 完成（統一記憶：notes+twse+memory+obsidian）；Jobs 改為中文名+可點擊看歷史+trigger顯示；Research tab 移除；URL: `https://594bb710.openclaw-dashboard-dv8.pages.dev/`（2026-04-08）；Repo: `openclawGit200/openclaw-dashboard`；排程已更新：crawler-sync=週日23:00, semantic-sync=週一23:00；⚠️ 自訂網域仍指向舊預設頁
- [x] **MemPalace 安裝**：✅ 已安裝（pip3 + 清華鏡像）；Palace 路徑 `~/.mempalace/palace`；1876 drawers（workspace）；無需 API Key
- [x] **Skills 清理**：移除 glmv-stock-analyst、glmocr-formula、glmv-doc-based-writing（glmv-doc-based-writing）；保留 zhipu-web-search

---

## 執行完後

1. 把上方 `[ ]` 任務狀態更新（打勾或填入狀態）
2. 如果有進度變化 → 主動更新 MEMORY.md 的對應進度
3. 回 `HEARTBEAT_OK`

---

> 有新問題或卡點，隨時寫進 HEARTBEAT.md，OpenClaw 會通知我。
