# LEARNINGS.md - 錯誤與修正記錄

---

## 2026-03-30 - 台股季報爬蟲腳本重複犯錯

### 錯誤 1：聲稱修過但沒修
**問題**：`--check-existing` 的筆記跳過邏輯有 bug（company_name 為空時檔名湊不上），我之前說會修但實際上沒修，浪費了大量時間。
**原因**：沒有實際比對 `note_filename` 變數和實際產出檔名。
**預防**：任何聲稱「已修復」的問題，必須實際執行驗證，不能只靠記憶或猜測。

### 錯誤 2：全季檢查邏輯錯誤
**問題**：`check_existing_reports` 只要找到 1 個筆記就回傳 `has_existing=True`，導致 `--check-existing` 時直接 `return` 結束整個程式，後續所有股票都不跑了。
**正確行為**：應該是「全部股票都有筆記」才 skip，否則應該繼續讓逐檔檢查處理。
**預防**：邏輯判斷要想到「0 筆記」和「部分筆記」的中間狀態。

### 錯誤 3：sleep 在 Mac 睡眠後失效
**問題**：`run_at_23h.py` 使用 `time.sleep()` 等待，Mac 進入睡眠後 sleep 不會跟著延長，導致行程在系統恢復後立刻結束，沒有觸發爬蟲。
**預防**：`time.sleep()` 不適合用於長時間等待場景，應該用 `launchd` 的 `StartCalendarInterval` 來定時。

### 錯誤 4：twse_crawler.py 對同一變數有不同理解
**問題**：`create_obsidian_note` 的 `quarter` 參數帶有 "Q" 字，但 `args.quarter` 是純數字。同一變數在兩個地方意義不同，造成混淆。
**預防**：統一定義，明確定義每個變數的格式和來源。

### 錯誤 5：重複下載浪費時間
**問題**：今晚多次重跑了已有筆記的股票（1101、1102 等），浪費約 30 分鐘。
**原因**：`--check-existing` 邏輯有 bug，變成假的。
**預防**：修復後一定要驗證，確認跳過邏輯確實生效。

---

## 通用原則

1. **驗證比聲稱重要**：說「已修復」不算數，要實際跑一次確認
2. **所有狀態都要考慮**：空、1個、部分、全部——四種狀態都要測試
3. **Mac 睡眠問題**：`time.sleep()` 不抗睡眠，長時間任務用 launchd
4. **不要重複承認同樣的錯**：同一錯誤寫入 LEARNINGS.md 後，下次遇到要先查檔案再動手
5. **跨 session 專案要查記憶**：接手曾在 notes/projects/ 有記錄的專案，第一步先讀該檔案，不要重蹈今天折騰 GitHub secrets / Cloudflare Pages 建置的老路

## 2026-04-03 - Cloudflare Pages + GitHub Actions 部署（7個錯誤）

### 錯誤 10：帳號 ID 填錯
**問題**：`CLOUDFARE_ACCOUNT_ID` 填成 `3c89a3f816871c9a2f3ef09dde0e977a`（錯誤），正確是 `4636a1d26dcf5cf8ff663c6104f12d86`。
**預防**：收到帳號 ID 後立刻和 Cloudflare Dashboard 核對，不要假設。

### 錯誤 11：Global API Key (`cfk_`) 不被 wrangler v4 接受
**問題**：wrangler v4 需要 API Token (`cfat_`)，不接受 Global API Key。
**預防**：看清楚錯誤訊息，優先用正確類型的 key。

### 錯誤 12：wrangler `--output-dir` 參數已廢棄
**問題**：wrangler v4 把 `--output-dir` 改為 `--outdir`，舊參數直接忽略。
**預防**：每次部署失敗都要實際驗證 flag 正確性。

### 錯誤 13：編譯輸出 `index.js`，但 Cloudflare Pages Functions 要 `_worker.js`
**問題**：wrangler 編譯後輸出 `dist/index.js`，Cloudflare 把它當普通 JS 檔，不是 Worker。
**修復**：部署前 `mv dist/index.js dist/_worker.js`。

### 錯誤 14：缺少 `_routes.json`，所有路徑都 404
**問題**：沒有 routes config，Cloudflare 不知道哪些路徑走 Worker，全部當靜態檔案，導致 404。
**修復**：加上 `{"version":1,"include":["/*"],"exclude":[]}`。

### 錯誤 15：路徑格式錯誤，`/search?q=` 拿不到結果
**問題**：`functions/search/[route].js` 需要子路徑如 `/search/foo`，不支援 `/search?q=`。
**修復**：改用 `functions/search/index.js` 來處理 `/search` 根路徑。

### 錯誤 16：智譜 API `search_engine` 參數錯誤
**問題**：`search_engine` 設為 `"google"`（錯誤），正確值是 `"search_pro_quark"`。
**預防**：有 shell script 參考時，直接看 script 裡的實際格式，不要主觀猜測。

## 2026-04-03 - 跨 session 記憶斷層

### 錯誤 17：接手曾在 notes/projects/ 有記錄的專案，沒先查記憶
**問題**：今天做 Cloudflare Pages 部署浪費大量時間，因為：
- 昨天已建立 GitHub repo、Cloudflare Workers/ Pages 專案
- 昨天已知 `openclaw-search-proxy` 的完整實作（`worker.js`）
- 但今天完全沒查 notes/projects/cloudflare.md，直接從零開始重蹈覆轍
**根本原因**：拿到新任務時沒有第一步執行被動記憶查詢（AGENTS.md 第 8 條）
**預防**：任何曾在 notes/projects/ 有記錄的專案，第一步先讀該檔案

---

## 2026-03-31 - Q4/Q04 路徑不一致 + 先建資料夾邏輯錯誤

### 錯誤 6：相對路徑在 不同執行上下文 飄移（路徑飄移 Bug）
**問題**：`--base-dir` 預設 `../台股季報`，從 workspace 執行時解析到 `.openclaw/台股季報`，導致第二次跑的 1209 筆全部存到錯誤位置，與第一次的 431 筆完全分開。
**root cause**：`../台股季報` 是相對路徑，LaunchAgent 的 WorkingDirectory 設定為 workspace，但手動執行和 cron 行程的 cwd 各有不同，造成解析結果不一致。
**修復**：`--base-dir` 改為絕對路徑 `/Users/downtoearth/.openclaw/workspace/台股季報`
**預防**：所有涉及路徑的設定，特別是排程任務，一律使用絕對路徑，嚴禁相對路徑。（已新增 AGENTS.md 第 11 條）

### 錯誤 7：先建資料夾、後下載 → 空殘留
**問題**：舊邏輯在找到 PDF 連結之前就建立資料夾， TWSE 無季報時留下 325 個空資料夾，造成「假完成」混淆。
**修復**：改為「先 `find_pdf_link()` 確認連結存在 → 再 `create_directory_structure()` → 後續下載」。連結找不到就直接 failed，不留任何東西。
**預防**：任何「準備階段」和「執行階段」之間如果會留下副產品（前例為資料夾），要先確認主動作成功再產生副產品。

---

### 通用原則（更新）

5. **絕對路徑強制要求**：所有檔案路徑，無例外使用絕對路徑存入 AGENTS.md（第 11 條）
6. **驗證路徑要實物確認**：不只看 log 的 `print`，實際 `ls` 檢查實體目錄

---

## 2026-04-01 - chromedriver session 共享導致下載失敗

### 錯誤 8：find_pdf_link + download_pdf 共享同一 driver 但中間 quit
**問題**：修改「先找連結再下載」時，在 `find_pdf_link()` 完成後馬上 `driver.quit()`，但 `download_pdf()` 仍接收同一個已死亡的 driver 物件。CDP commands 送到已斷連的 Chrome debugging port → `Connection refused`，210 個股票全部下載失敗，但資料夾已建立（留下空資料夾）。
**root cause**：`find_pdf_link()` → `driver.quit()` → `download_pdf(driver, ...)` → driver 已是無效物件
**修復**：
1. `find_pdf_link()` 完成後**不 quit**，driver 保持活著
2. `download_pdf()` 做完後才統一 `driver.quit()`
3. 所有 `continue` 分支前確認 driver 已 quit
**預防**：任何「準備階段」和「執行階段」共用同一 resource 時，quit 必須發生在**最後一個階段完成後**，不能在中間提前釋放。

---

## 2026-04-01 - 回報數字前後邏輯不符

### 錯誤 9：回報時數字湊不起來
**問題**：聲稱「只跑 862 檔，但完整的有 1205 檔」，兩個數字前後矛盾。實際原因是 1205 筆是 3/31 凌晨舊批次累積的，不是今晚 862 檔的子集，兩者不該拿來直接比較。
**正確態度**：回報數字前，必須：
1. 先確認各項數字的**口徑是否一致**（同一批？同一時間點？）
2. **加減驗算**：部分相加是否等於總計？差額是否解釋得通？
3. 發現矛盾主動說明，不強行拼湊
**預防**：回報數字爛掉了，就先查清楚再回報，絕對不要邊想邊寫，數字對不上還硬髮夾子。
