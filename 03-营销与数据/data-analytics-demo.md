---
name: demo-data-analytics
description: 用pm-data-analytics做数据分析
category: 营销与数据
skills_used: [pm-data-analytics: sql-queries, ab-test-analysis]
---

# 案例：数据分析 — SQL查询与A/B测试

## 背景

产品上线后，需要数据分析来驱动决策。

## 使用pm-data-analytics技能

### 1. sql-queries — SQL查询生成
```
请帮我写以下SQL查询（PostgreSQL语法）：

表结构：
- users: id, name, city_level, age, gender, create_time
- orders: id, user_id, amount, discount, ai_recommend_click, create_time
- sessions: id, user_id, duration, page_views, create_time

查询需求：
1. 每个城市级别的活跃用户数（周活跃）
2. AI推荐点击率按品类统计
3. 用户留存率（第1/7/30天）
4. 月GMV趋势（按月）
```

### 2. ab-test-analysis — A/B测试分析
```
A/B测试结果：
- 对照组：5000用户，转化率2.3%，平均订单金额85元
- 实验组：5000用户，转化率3.1%，平均订单金额92元
- 持续时间：14天

请分析：
1. 统计显著性（p-value）
2. 样本量是否充足
3. 置信区间
4. 是否应该全量上线实验方案
```

## 关键要点

- SQL查询生成让**非技术PM也能快速取数**
- A/B测试分析确保**数据驱动决策**而非直觉
