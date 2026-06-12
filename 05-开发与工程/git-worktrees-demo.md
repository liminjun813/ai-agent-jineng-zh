---
name: demo-git-worktrees
description: 用using-git-worktrees隔离开发环境
category: 开发与工程
skills_used: [using-git-worktrees]
---

# 案例：Git工作树 — 隔离开发环境

## 背景

开始开发MVP时，需要保护主分支不被破坏。

## 使用using-git-worktrees技能

打开Hermes Agent，说："我要开始开发「智选AI」推荐引擎，请用using-git-worktrees技能帮我设置隔离环境。"

## 执行流程

AI Agent会自动：

```bash
# 1. 检测当前是否在隔离环境
GIT_DIR=$(cd $(git rev-parse --git-dir) 2>/dev/null && pwd -P)
GIT_COMMON=$(cd $(git rev-parse --git-common-dir) 2>/dev/null && pwd -P)

# 2. 创建新的工作树
git worktree add .worktrees/feature-ai-recommend -b feature-ai-recommend

# 3. 切换到工作树目录
cd .worktrees/feature-ai-recommend

# 4. 自动安装依赖
npm install  # 或 poetry install / pip install ...

# 5. 验证测试基线
npm test    # 确保基线是绿的
```

## 关键要点

- 工作树让每个功能有**独立的分支和目录**
- 主分支永远保持**干净、可发布**的状态
- 适合多功能**并行开发**
- 开发完成后可选择：合并 / 创建PR / 丢弃
