---
name: demo-systematic-debugging
description: 用systematic-debugging系统化调试bug
category: 开发与工程
skills_used: [systematic-debugging]
---

# 案例：系统化调试 — 推荐引擎响应超时

## 场景

MVP测试中，推荐引擎API响应超过5秒（要求<2秒），触发超时。

## 错误信息

```
ERROR: Recommendation API timeout after 5000ms
Endpoint: POST /api/v1/recommend
User: user_12345
Response: {"error": "TimeoutError", "status": 504}
```

## 使用systematic-debugging技能

打开Hermes Agent，说："推荐引擎API响应超时，用systematic-debugging技能帮我调试。"

## Phase 1: 根因调查

```
不要直接说"增加超时时间"！

按流程来：
1. 读错误信息 → TimeoutError from API endpoint
2. 复现 → 能稳定复现，所有用户都一样
3. 查最近修改 → 昨天改了推荐算法，从基于规则改成了向量相似度
4. 加诊断日志 → 追踪数据流
```

## Phase 2: 模式分析

```
找工作代码：
- 之前用基于规则的推荐，响应<500ms
- 现在用向量相似度，响应>5000ms
- 差异：多了向量计算步骤
```

## Phase 3: 假设与测试

```
假设：向量相似度计算是瓶颈

最小测试：
# 单独测试向量计算时间
python -c "from vector import compute_similarity; import time;
start=time.time(); [compute_similarity(a,b) for _ in range(1000)];
print(f'1000次计算: {time.time()-start:.3f}s')"
```

输出：`1000次计算: 3.2s` → 每次3.2ms，但用户查询需要计算10000次 → 32s

## Phase 4: 实施修复

```
根因：用户查询时计算了过多商品向量

修复方案：
1. 添加缓存层：热门商品向量化结果缓存1小时
2. 限制计算范围：先过滤后1000商品，再算相似度
3. 使用近似最近邻（ANN）算法替代暴力计算

修复后验证：
- 单元测试通过
- API响应<500ms（1000次请求）
- 回归测试通过
```

## 关键要点

- **核心规则**：先找根因，再修复，绝不瞎改
- 3次修复失败 → 说明是架构问题，需要重新评估
- 适用于：**任何bug、测试失败、性能问题**
