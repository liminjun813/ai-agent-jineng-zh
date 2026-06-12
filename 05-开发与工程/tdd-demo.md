---
name: demo-tdd
description: 用test-driven-development测试驱动开发
category: 开发与工程
skills_used: [test-driven-development]
---

# 案例：TDD — 推荐引擎单元测试

## 背景

开始编写AI推荐引擎代码前，先用TDD。

## 使用test-driven-development技能

打开Hermes Agent，说："我要用TDD为推荐引擎编写测试驱动开发。"

## RED — 先写失败的测试

```python
# test_recommend.py

import unittest
from recommend import calculate_similarity, generate_recommendations

class TestRecommend(unittest.TestCase):
    
    def test_calculate_similarity_same_user(self):
        """相同用户的相似度应为1.0"""
        user_items = {"手机壳": 5, "充电宝": 3, "数据线": 2}
        similarity = calculate_similarity(user_items, user_items)
        self.assertAlmostEqual(similarity, 1.0)
    
    def test_calculate_similarity_different_users(self):
        """不同用户的相似度应<1.0"""
        user_a = {"手机壳": 5, "充电宝": 3}
        user_b = {"耳机": 4, "手机膜": 3}
        similarity = calculate_similarity(user_a, user_b)
        self.assertLess(similarity, 1.0)
    
    def test_generate_recommendations_min_items(self):
        """推荐结果至少包含3个商品"""
        user_history = {"手机壳": 5, "充电宝": 3}
        recommendations = generate_recommendations(user_history, top_n=3)
        self.assertGreaterEqual(len(recommendations), 3)
    
    def test_recommendations_no_duplicate(self):
        """推荐结果不应包含用户已经买过的商品"""
        user_history = {"手机壳": 5}
        recommendations = generate_recommendations(user_history)
        recommended_items = [r["item"] for r in recommendations]
        self.assertNotIn("手机壳", recommended_items)
```

**运行测试 → 全部失败（RED）** ✅

## GREEN — 写最少的代码让它通过

```python
# recommend.py

def calculate_similarity(user_a, user_b):
    if not user_a or not user_b:
        return 0.0
    items_a = set(user_a.keys())
    items_b = set(user_b.keys())
    intersection = len(items_a & items_b)
    union = len(items_a | items_b)
    return intersection / union if union > 0 else 0.0

def generate_recommendations(user_history, top_n=3):
    """生成推荐（简化版）"""
    all_items = ["手机膜", "充电宝", "耳机", "数据线", "手机壳", "支架"]
    bought = set(user_history.keys())
    recommendations = []
    for item in all_items:
        if item not in bought:
            recommendations.append({"item": item, "score": 0.5})
        if len(recommendations) >= top_n:
            break
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)[:top_n]
```

**运行测试 → 全部通过（GREEN）** ✅

## REFACTOR — 重构

提取相似度计算为独立的余弦相似度函数，但保持测试通过。

## 关键要点

- **核心规则**：先写失败的测试，再写代码
- 不要跳过RED（看到测试失败）
- 绿色后**不要**再添加功能
- TDD确保代码质量，防止回归
