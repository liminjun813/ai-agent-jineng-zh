---
name: demo-subagent-dev
description: 用subagent-driven-development执行开发计划
category: 开发与工程
skills_used: [subagent-driven-development]
---

# 案例：子Agent驱动开发 — 执行MVP开发计划

## 背景

MVP开发计划已完成，包含8个任务，现在需要执行。

## 使用subagent-driven-development技能

打开Hermes Agent，说："用subagent-driven-development技能执行MVP开发计划。"

## 执行流程

### 第一步：读取计划，提取所有任务

```markdown
计划文件：mvp-plan.md

Tasks:
T1. 用户注册登录模块
T2. 商品搜索与筛选
T3. AI推荐引擎核心
T4. 购物车功能
T5. 订单管理
T6. 优惠券系统
T7. 后台管理面板
T8. 部署与监控
```

### 第二步：逐个派发给子Agent

```
每个任务：
  1. 派给Implementer Agent（实现代码）
  2. Implementer完成后，派给Spec Reviewer（检查是否符合规格）
  3. Spec通过后，派给Code Quality Reviewer（代码质量检查）
  4. 三个都通过 → 标记Task完成
  5. 进入下一个Task

注意：每个Agent是全新的，不继承前一个的状态
```

### 第三步：最终审查

所有Task完成后：
```
派给Final Code Reviewer：
- 审查整个项目的代码一致性
- 检查是否有遗漏的需求
- 确认可以合并
```

## 质量门控

```
Implementer报告状态:
  - DONE → 进入审查
  - DONE_WITH_CONCERNS → 阅读担忧，决定是否继续
  - NEEDS_CONTEXT → 提供更多信息
  - BLOCKED → 提供解决方向，重新派发

Spec Reviewer发现gap：
  Implementer修复 → Spec Reviewer再次审查 → 通过后才进入Code Quality Review
```

## 关键要点

- **每个任务独立的Agent**，不污染上下文
- **两阶段审查**：先规格合规，再代码质量
- **不暂停**：持续执行所有Task，不停止询问
- 适合**2-8个任务**的中型项目
- 每个Task完成后自动Commit
