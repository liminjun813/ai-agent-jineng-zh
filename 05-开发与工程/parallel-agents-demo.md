---
name: demo-parallel-agents
description: 用dispatching-parallel-agents并行处理多个任务
category: 开发与工程
skills_used: [dispatching-parallel-agents]
---

# 案例：并行Agent — 同时修复多个测试失败

## 场景

代码提交后，CI运行发现6个测试失败，分布在3个不同的文件中。

## 失败的测试

```
failures:
  - tests/test_recommend.py: 3 failures (timing issues)
  - tests/test_cart.py: 2 failures (item not added correctly)
  - tests/test_search.py: 1 failure (pagination broken)
```

## 使用dispatching-parallel-agents技能

打开Hermes Agent，说："有6个测试失败，分布在3个文件中，用parallel-agents技能并行处理。"

## 执行流程

AI Agent会：

```
Agent 1 (task: fix-recommend) → 处理 test_recommend.py 的3个失败
Agent 2 (task: fix-cart) → 处理 test_cart.py 的2个失败  
Agent 3 (task: fix-search) → 处理 test_search.py 的1个失败

3个Agent并行工作，互不干扰
```

每个Agent的指令示例：

```
Agent 1:
"修复 tests/test_recommend.py 中失败的3个测试：
 1. test_recommend_timing — 期望响应<2秒
 2. test_recommend_cache — 缓存未命中处理错误
 3. test_recommend_empty_user — 空用户边界情况

错误日志：
[粘贴具体错误信息]

不要修改其他文件，只修复指定问题。
完成后返回：修复了什么 + 原因分析。"
```

## 验证

所有Agent完成后：
```bash
# 运行完整测试套件
npm test
# 确认全部通过
```

## 关键要点

- 适用于**多个独立问题同时出现**时
- 每个Agent有**独立上下文**，互不干扰
- 速度是**串行执行的3倍**
- ⚠️ 注意：确保问题之间**确实独立**，不共享状态
