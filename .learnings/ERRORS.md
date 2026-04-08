# Errors Log

记录命令失败、异常和错误，以便持续改进。

---

## 模板

## [ERR-YYYYMMDD-XXX] skill_or_command_name

**Logged**: ISO-8601 timestamp
**Priority**: high
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
Brief description of what failed

### Error
```
Actual error message or output
```

### Context
- Command/operation attempted
- Input or parameters used
- Environment details if relevant

### Suggested Fix
If identifiable, what might resolve this

### Metadata
- Reproducible: yes | no | unknown
- Related Files: path/to/file.ext
- See Also: ERR-YYYYMMDD-001 (if recurring)

---


## [ERR-20260401-001] openclaw-weixin fetch failed / ENOTFOUND

**Logged**: 2026-04-01T05:33:00+08:00
**Priority**: medium
**Status**: ongoing
**Area**: infra

### Summary
openclaw-weixin plugin continuously failing with "fetch failed" and DNS resolution errors for open.feishu.cn

### Error
```
[openclaw-weixin] weixin getUpdates error (1/3): TypeError: fetch failed
[ws] getaddrinfo ENOTFOUND open.feishu.cn
```

### Context
- Plugin repeatedly trying to poll WeChat/Feishu updates
- DNS lookup for open.feishu.cn failing
- Started around 04:54 AM, still failing at 05:33 AM
- Likely network/DNS issue on host machine

### Suggested Fix
1. Check if host machine has network connectivity
2. Check DNS settings on MacBook Air
3. May need to disable weixin plugin if network unavailable

## 2026-04-08 - sessions-memory hook 長期未啟用
**問題**：OpenClaw 會在閒置後自動重啟 session（猜測約 4 小時），但 session-memory hook 未啟用，所以 session reset 時沒有自動歸檔對話。導致今天早上 session 變空白，昨日對話內容完全丢失。

**已修復**：✅ session-memory 已啟用（`openclaw hooks enable session-memory`）

**預防**：日後新 session 發現對話內容断层，先查 memory/ 目錄是否有對應的歸檔檔案
