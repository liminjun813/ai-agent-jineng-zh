---
name: demo-writing-plans
description: 用writing-plans技能为「智选AI」项目制定实施计划
category: 创意发想
skills_used: [writing-plans, using-superpowers]
---

# 案例：写实施计划 — 6个月MVP路线图

## 背景

头脑风暴后，我们决定：「智选AI」聚焦三四线城市宝妈群体，6个月内推出MVP。

## 使用writing-plans技能

打开Hermes Agent，加载 `superpowers:writing-plans` 技能，输入以下prompt：

```
我正在创建「智选AI」AI电商推荐平台MVP，目标：
- 目标用户：三四线城市宝妈
- 核心功能：AI商品推荐、比价、优惠券聚合
- 时间：6个月
- 团队：2名开发 + 1名产品 + 1名运营

请用writing-plans技能帮我制定实施计划，包含：
1. 阶段划分（每个阶段2-3个月）
2. 每阶段的具体任务（拆解到可执行级别）
3. 任务依赖关系
4. 每个任务的验收标准
```

## 预期输出

技能会引导AI生成标准格式的plan文件：

```markdown
# 智选AI MVP实施计划

## Phase 1: 需求与设计 (Week 1-4)
- Task 1.1: 竞品分析报告
  - 验收标准: 输出5个竞品的功能对比矩阵
- Task 1.2: 用户画像与需求文档
  - 验收标准: 至少3个细分用户画像，每个有明确需求列表
...

## Phase 2: 核心功能开发 (Week 5-12)
...

## Phase 3: 测试与上线 (Week 13-24)
...
```

## 关键要点

- writing-plans确保计划**结构化、可执行**
- 每个任务都有明确的**验收标准**（不是模糊的"完成开发"）
- 任务之间有清晰的**依赖关系**
- 生成的计划文件后续会被 `subagent-driven-development` 或 `executing-plans` 读取执行
