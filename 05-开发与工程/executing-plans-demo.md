---
name: demo-executing-plans
description: 用executing-plans执行实施计划（并行会话）
category: 开发与工程
skills_used: [executing-plans]
---

# 案例：执行计划 — 跨会话执行大型功能

## 场景

当任务太大或需要跨会话执行时，使用executing-plans而非subagent-driven-development。

## 区别

| | subagent-driven-development | executing-plans |
|---|---|---|
| 执行位置 | 同一个会话 | 并行会话 |
| 上下文 | 共享主会话 | 独立会话 |
| 适合场景 | 中小型项目 | 大型项目、跨模块 |
| 速度 | 快（同会话） | 较慢（有开销） |
| 隔离性 | 部分隔离 | 完全隔离 |

## 使用方法

打开Hermes Agent，说："用executing-plans技能执行MVP的支付模块开发。"

AI Agent会：
1. 读取plan文件
2. 将每个Task派发到**独立的并行会话**
3. 每个会话独立执行
4. 完成后汇总结果

## 关键要点

- 适合**大型项目**或需要**完全隔离**的场景
- 当任务需要大量上下文但不想污染主会话时使用
- 是subagent-driven-development的"升级版"
