---
name: demo-pm-execution
description: 用pm-execution做项目管理与执行
category: 执行与规划
skills_used: [pm-execution: create-prd, brainstorm-okrs, sprint-plan, user-stories]
---

# 案例：执行管理 — PRD、OKR、Sprint

## 背景

产品策略确定后，需要将其转化为可执行的计划和文档。

## 使用pm-execution技能

### 1. create-prd — 撰写PRD
```
请为「智选AI」的AI推荐核心功能撰写PRD：
- 功能：用户进入APP → AI分析历史购物记录 → 推荐个性化商品列表
- 用户：三四线城市宝妈
- 约束：首屏加载<2秒，推荐响应<500ms
```

PRD包含8个标准章节：
```
1. 概述
2. 背景
3. 目标
4. 目标市场细分
5. 价值主张
6. 解决方案细节
7. 发布计划
8. 成功指标
```

### 2. brainstorm-okrs — 制定OKR
```
请为Q1制定OKR：
- 公司目标：完成MVP上线并获取首批10万用户
- 产品团队目标：...
- 技术团队目标：...
- 运营团队目标：...
```

### 3. sprint-plan — Sprint规划
```
请规划2周Sprint：
- 团队：2名前端 + 2名后端 + 1名测试
- 优先级最高的需求：AI推荐引擎、用户注册登录、商品搜索
- 约束：2周 Sprint，每日站会
```

### 4. user-stories — 用户故事
```
请为以下功能编写用户故事（INVEST标准）：
- 功能：AI个性化推荐
- 用户角色：三线城市的宝妈
```

输出格式：
```
作为[三线城市的宝妈]
当我[打开APP首页时]
我希望[看到基于我之前购物偏好的商品推荐]
以便[快速找到划算的好东西，不用自己搜索]

验收标准：
- 推荐商品与用户历史购买品类相关度>80%
- 首屏加载时间<2秒
- 推荐商品中包含至少3个不同品类的商品
```

## 关键要点

- pm-execution覆盖了**产品经理的90%日常需求**
- 每个子技能都有**标准模板**，直接可用
- PRD → OKR → Sprint → User Stories 形成完整的执行链条
