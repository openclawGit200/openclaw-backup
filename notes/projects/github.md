# GitHub Skill 專案記憶

## 基本資訊
- **安裝日期：** 2026-04-03
- **Skill：** github（skillhub）
- **gh 版本：** 2.89.0
- **gh 安裝方式：** brew install gh

## 雲端設定
- **Cloudflare 登入信箱：** Downtoearth.tw@gmail.com
- **Cloudflare 帳號 ID（正確）：** `4636a1d26dcf5cf8ff663c6104f12d86`（之前錯設成 `3c89a3f816871c9a2f3ef09dde0e977a`，已修正）
- **CLOUDFARE_API_KEY：** Global API Key（`cfk_...`），已設定於 GitHub Secrets
- **CLOUDFARE_EMAIL / CLOUDFARE_ACCOUNT_ID：** 已設定於 GitHub Repo Variables

## 認證狀態
- **帳號：** openclawGit200
- **已登入：** ✅（macOS Keychain）
- **Token scope：** admin:enterprise, admin:org, repo, workflow, codespace, copilot, delete:packages, delete_repo, gist, notifications, project, user, write:packages 等完整權限
- **Token 儲存位置：** macOS Keychain（`gh auth login` 自動寫入 keyring，**不再需要也不應該另外儲存 token**）

## 新備份系統
- **Repo：** `openclawGit200/openclaw-backup`（public）
- **用途：** 將 openclaw workspace 遷移到任意 Mac
- **內容：** skills、notes、memory、scripts、核心設定檔（~26MB）
- **排除：** .credentials/、台股季報 PDF、twse-reports-lib 等大型可重建資料
- **安裝：** `bash <(curl -L https://raw.githubusercontent.com/openclawGit200/openclaw-backup/main/install.sh)`
- **Repo：** `openclawGit200/openclaw-backup`
- **內容：** skills、notes、memory、scripts、核心設定檔（~26MB）
- **安裝指令：** `bash <(curl -L https://raw.githubusercontent.com/openclawGit200/openclaw-backup/main/install.sh)`

## 已啟用功能
- Issue 管理（`gh issue`）
- PR 管理（`gh pr`）
- CI/CD 工作流（`gh run`）
- API 查詢（`gh api`）

## 注意事項
- Token 已用 `gh auth login --with-token` 寫入 keychain，之後執行 `gh` 命令無需再輸入 token
- 不要把 token 寫進任何 md/json 檔案
- 若需要跨机器使用，再取出 token 來設定；一般操作在本地端已足夠
