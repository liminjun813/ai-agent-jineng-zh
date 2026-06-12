---
name: demo-writing-skills
description: 用writing-skills技能创建自定义技能
category: 收尾与发布
skills_used: [writing-skills]
---

# 案例：编写技能 — 为「智选AI」创建自定义技能

## 背景

我们在这个项目中使用了很多技能，现在想把经验沉淀为可复用的技能。

## 使用writing-skills技能

打开Hermes Agent，说："我要创建一个自定义技能，用于「智选AI」项目的推荐引擎配置。用writing-skills技能帮我。"

## 技能文件结构

```yaml
---
name: ai-recommend-config
description: 配置AI推荐引擎的参数和策略
tags: [ai, recommendation, config]
---

# AI推荐引擎配置

## 概述

标准化「智选AI」推荐引擎的配置流程。

## 配置步骤

### 1. 基础配置
```yaml
engine:
  algorithm: cosine_similarity
  top_n: 10
  cache_ttl: 3600
  timeout_ms: 5000
```

### 2. 权重配置
```yaml
weights:
  purchase_history: 0.4
  browse_history: 0.3
  demographic: 0.2
  trending: 0.1
```

### 3. 验证配置
运行配置验证脚本后提交。

## 常见陷阱
- 不要将API密钥硬编码到配置文件
- 缓存TTL不应超过24小时
```

## 关键要点

- 技能文件需要**YAML frontmatter**（name, description, tags）
- 内容应该**结构化、可复用**
- 包括：**概述、步骤、陷阱、验证方法**
- 创建后其他Agent也能自动加载使用
