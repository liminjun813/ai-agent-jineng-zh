---
name: demo-ai-shipping
description: 用pm-ai-shipping审计AI生成的代码
category: 开发与工程
skills_used: [pm-ai-shipping: shipping-artifacts, intended-vs-implemented]
---

# 案例：AI代码审计 — 检查「智选AI」的安全性

## 背景

MVP即将上线，需要审计AI生成的代码是否存在安全漏洞。

## 使用pm-ai-shipping技能

打开Hermes Agent，说："用pm-ai-shipping技能审计我们的代码库。"

## 执行流程

### Step 1: ship-check（完整审计）

```
AI Agent会执行完整流程：
1. 文档化系统（架构、权限流、变量/密钥）
2. 审计意图与实现的差距
3. 安全审计（静态分析）
4. 性能审计
5. 测试覆盖率映射
6. 输出完整审计包
```

### Step 2: 审计输出示例

```
## 安全审计报告

### 发现的风险

1. 🔴 CRITICAL: API密钥硬编码
   - 位置：config/settings.py line 12
   - 描述：OpenAI API密钥直接写在代码中
   - 修复：使用环境变量

2. 🟡 IMPORTANT: SQL注入风险
   - 位置：recommend/search.py line 38
   - 描述：用户搜索词直接拼接到SQL
   - 修复：使用参数化查询

3. 🟢 MINOR: 缺少速率限制
   - 位置：api/v1/recommend
   - 描述：推荐接口无请求频率限制
   - 修复：添加RateLimiter中间件
```

### Step 3: 测试覆盖率

```
| 模块 | 已测 | 未测 | 建议 |
|------|------|------|------|
| recommend/ | 85% | 5% | 添加极端用例 |
| auth/ | 70% | 15% | 添加边界测试 |
| api/ | 90% | 3% | 覆盖率高 ✅ |
```

## 关键要点

- pm-ai-shipping专门用于**审计AI生成的代码**
- 找的是**意图与实现的差距**（普通扫描器找不到）
- 审计包可以作为**上线审批的依据**
- 每个问题都有**代码级证据**，不是模糊的判断
