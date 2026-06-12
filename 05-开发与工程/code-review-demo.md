---
name: demo-code-review
description: 用requesting-code-review和receiving-code-review做代码审查
category: 开发与工程
skills_used: [requesting-code-review, receiving-code-review]
---

# 案例：代码审查 — 推荐引擎自审

## 场景

推荐引擎核心模块开发完成，需要自我审查。

## 使用requesting-code-review技能

```
AI Agent会自动：
1. 获取git SHA范围
2. 派发给Code Reviewer Agent
3. Reviewer输出审查报告
```

审查报告示例：
```
## 审查结果：推荐引擎模块 (commit A → commit B)

### 优点
- 代码结构清晰，职责分明
- 测试覆盖率 85%
- 边界情况处理完善

### 问题
- 🔴 Critical: 向量计算无超时保护，可能导致OOM
- 🟡 Important: 缓存没有设置TTL，内存持续增长
- 🟢 Minor: 魔法数字 0.5 应提取为常量

### 建议
- 添加向量计算的超时控制
- 缓存添加L1+L2两级TTL
- 提取常量 MAX_SIMILARITY_THRESHOLD
```

## 使用receiving-code-review技能

AI Agent收到审查反馈后的处理：

```
1. 读取全部反馈，不急于实现
2. 对不清楚项提问
3. 验证每个问题是否属实（不是盲目接受）
4. 按优先级修复：Critical → Important → Minor
5. 修复后不写"谢谢"，直接展示修改

收到反馈：
"向量计算无超时保护"

修复后：
"添加了计算超时保护（默认5s），超过则降级到简化算法。
  修改文件：recommend/vector.py line 45-52"
```

## 关键要点

- 代码审查**不能跳过**
- 审查报告分三级：Critical/Important/Minor
- 收到反馈后**不表演性同意**，先验证再执行
- 不要写"谢谢"，直接展示修改
