# Cloudflare 專案

## 摘要
在中國境內透過 Cloudflare Worker 代理訪問被封鎖的國外搜尋引擎。

## 架構
```
境內用戶 → Worker → 國外搜尋引擎（Google/Bing/DuckDuckGo）
```

## 現況（2026-04-07 更新）

### ⚠️ Worker SSL 故障
- `worker.downtoearthclf.ddns-ip.net` — SSL handshake failure（三層 subdomain 證書問題）
- 原因：Cloudflare Universal SSL 不支援三層 subdomain（worker.xxx.xxx.xxx）

### ✅ 目前可用：Cloudflare Pages
- **Pages Project**: `openclaw-search`
- **穩定 URL**: `https://openclaw-search.pages.dev`
- **部署方式**: GitHub Actions（`openclawGit200/openclaw-dashboard` → `deploy-search.yml`）
- **Repo**: https://github.com/openclawGit200/openclaw-dashboard
- **Function 路徑**: `functions/search/index.js` → 處理 `/search/` 路由
- **正確 URL 格式**:
  ```
  https://openclaw-search.pages.dev/search?q=關鍵詞&engine=bing
  ```
- **API Token**: `.credentials/CLOUDFLARE_token.json` ✅ 已更新（cfat_...）
- **手動觸發部署**: `gh workflow run deploy-search.yml --repo openclawGit200/openclaw-dashboard`
- **Custom Domain**（未啟用）: `search.downtoearthclf.ddns-ip.net`

### 支援的 Engine 參數（線上 18 個）
| engine | 目標 | 狀態 |
|--------|------|------|
| google | Google | ✅ |
| google_hk | Google HK | ✅ |
| bing | Bing | ✅ |
| bing_cn | Bing CN | ✅ |
| duckduckgo | DuckDuckGo | ✅ |
| brave | Brave | ✅ |
| startpage | Startpage | ✅ |
| ecosia | Ecosia | ✅ |
| qwant | Qwant | ✅ |
| yahoo | Yahoo | ✅ |
| baidu | 百度 | ✅ |
| 360 | 360 搜索 | ✅ |
| **sogou** | **搜狗** | **❌ 已移除（2026-04-07）** |
| weixin | 微信搜尋 | ✅ |
| toutiao | 頭條搜索 | ✅ |
| jisilu | 集思錄 | ✅ |
| **tavily** | **Tavily AI 搜尋** | **✅ 新增（2026-04-08）** |
| cascade | 引擎級聯（tavily 優先） | ✅ |
| zhipu | 智譜（AI 總結） | ✅ |

### Cascade 順序（目前線上）
```
tavily → google → bing → duckduckgo → baidu → 360 → toutiao → weixin → jisilu → bing_cn → google_hk → brave → startpage → ecosia → qwant → yahoo
```

### Worker 路由格式
```
https://worker.downtoearthclf.ddns-ip.net/?q={關鍵詞}&engine={引擎名}
```

### SSL 問題（已擱置）
- `worker.downtoearthclf.ddns-ip.net` 三層 subdomain 的 SSL 問題，決定不再處理。
- 備援方案：直接使用 Pages URL `https://a13fd96d.openclaw-search.pages.dev` 或已連接的 `search.downtoearthclf.ddns-ip.net`（兩層 subdomain，Universal SSL 正常）

### Cloudflare Pages: `openclaw-search`
- **URL**: `https://0bb3e347.openclaw-search.pages.dev`
- **wrangler 部署成功**（2026-04-02）
- **Custom Domain**: 嘗試加入 `search.downtoearthclf.ddns-ip.net`，但 API 回傳 TLD 不支援
- 需手動透過 Dashboard 加入 Custom Domain

## 帳號
- Email: downtoearth.tw@gmail.com
- Account ID: 4636a1d26dcf5cf8ff663c6104f12d86
- API Token：`.credentials/CLOUDFLARE_token.json` ✅ 已更新（2026-04-08）

## 待辦
1. ~~CF API Token 已過期~~ ✅ **已解決（2026-04-08）**：Token 已更新，GitHub Actions 部署正常運行
2. ~~移除 Sogou~~ ✅ **已完成（2026-04-07）**，透過 GitHub Actions 部署，sogou 從 engine list 移除
3. 在 Cloudflare Pages Dashboard 加入 `search.downtoearthclf.ddns-ip.net` 為 Custom Domain
4. ~~修復路由 `[route].js` → `search/index.js`~~ ✅ **已完成（2026-04-08）**，部署後測試成功（200 OK）

---

## twse-reports-lib 語意搜尋計畫（開放台股 MD）

### 目標
將 GitHub 開放資料庫 `openclawGit200/twse-reports-lib`（2025 Q3+Q4 季報 MD）建構為可語意搜尋的網站。

### 資料現況
- Repo: https://github.com/openclawGit200/twse-reports-lib
- Q4: 1,643 檔 MD | Q3: 434 檔 MD
- 附 `scripts/summarize_stock.py` 供自行用 AI 產生新摘要

### 技術方案（規劃中）
- **Embedding**: Workers AI `@cf/baai/bge-base-en-v1.5`（768維）
- **Index**: 本地建好後上傳至 CF KV Namespace
- **Worker**: 接收用戶查詢 → 線上 embedding → Cosine similarity 搜 KV → 回傳最相關段落
- **Frontend**: CF Pages 部署簡單搜尋介面
- **URL**: `https://twse-reports-lib.pages.dev`（待設定）

### 待解決
- [ ] CF API token（有 Workers & Pages 權限）— 舊 token 無法通过 wrangler 認證

## multi-search-engine Skill 設定
- 設定檔: `skills/multi-search-engine/config.json`
- `proxy_base`: `https://a13fd96d.openclaw-search.pages.dev`
- **Sogou 已設為 `disabled: true`**（本地優先，線上 Worker 移除待部署）

## 重要教訓
- Cloudflare Universal SSL 只涵蓋 apex + 一層 subdomain
- `*.ddns-ip.net` 的二層 subdomain（`downtoearthclf.ddns-ip.net`）可以，三層不行
- Free 方案無法用 Total TLS
- ClouDNS NS 委託的 zone 在 Cloudflare 的 SSL 覆蓋範圍有特殊限制
