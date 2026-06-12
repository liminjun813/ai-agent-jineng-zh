---
name: demo-product-discovery
description: 用pm-product-discovery做产品发现
category: 市场与产品
skills_used: [pm-product-discovery: identify-assumptions, brainstorm-experiments, interview-script]
---

# 案例：产品发现 — 验证核心假设

## 背景

策略确定后，需要在投入大量开发资源前验证关键假设。

## 使用pm-product-discovery技能

### 1. identify-assumptions — 识别风险假设
```
请识别「智选AI」的核心假设风险：
- 假设1：三四线城市宝妈愿意使用AI推荐购物
- 假设2：我们能在6个月内搭建出可用的推荐系统
- 假设3：用户愿意把购物决策权交给AI
```

输出格式（8个风险类别）：
```
价值风险：用户真的需要AI推荐吗？→ 最危险的假设
可行性风险：推荐系统的技术门槛有多高？
可用性风险：AI推荐界面是否足够简单？
 viability风险：商业模式是否跑得通？
...
```

### 2. brainstorm-experiments — 实验设计
```
请为上述每个风险假设设计最小可行实验（Pretotype）：
- 实验名称
- 实验方法
- 成功标准
- 执行成本
- 预计时间
```

示例实验：
```
实验：纸面原型测试
方法：用Figma做一个简单的AI推荐界面，找10个目标用户测试
成功标准：80%的用户能独立完成任务
成本：2天
时间：1周
```

### 3. interview-script — 用户访谈脚本
```
请设计用户访谈脚本，目标用户：三线城市的宝妈
包含：
- 热身问题
- JTBD核心问题（When..., I want to..., so I can...）
- 痛点深挖
- 现有解决方案探索
- 收尾问题
```

## 关键要点

- 产品发现的核心是**快速验证假设**，而不是直接写代码
- pm-product-discovery提供**系统化的验证框架**
- 适用于：**新产品验证、功能验证、市场验证**
