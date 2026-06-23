# AI Agent Skills 中文实战项目

> 🚀 **从0到1创建AI电商创业公司 —— 用全部23个Hermes Agent技能完成全流程实战**

本项目演示了如何在一个真实创业场景中，系统化地使用23个AI Agent技能，从创意发想到产品上线，覆盖**产品管理、软件工程、市场营销、数据分析**四大领域。

## 📖 项目故事线

### 公司背景
- **项目名称**：「智选AI」— AI驱动的个性化电商推荐平台
- **市场**：中国下沉市场（三四线城市消费者）
- **创始人**：产品负责人 + AI工程团队
- **目标**：6个月内MVP上线，12个月内实现盈亏平衡

### 全流程概览

```
Phase 1: 创意与探索 (Week 1-2)
    ├── 头脑风暴 → brainstorming
    ├── 写实施计划 → writing-plans
    └── 总纲导入 → using-superpowers

Phase 2: 市场与产品 (Week 3-4)
    ├── 市场研究 → pm-market-research
    │     ├── 用户画像 (user-personas)
    │     ├── 竞品分析 (competitor-analysis)
    │     ├── 市场细分 (market-segments)
    │     └── 情绪分析 (sentiment-analysis)
    ├── 产品策略 → pm-product-strategy
    │     ├── 商业画布 (business-model)
    │     ├── 价值主张 (value-proposition)
    │     ├── SWOT分析 (swot-analysis)
    │     └── 定价策略 (pricing-strategy)
    ├── 产品发现 → pm-product-discovery
    │     ├── 假设识别 (identify-assumptions)
    │     ├── 实验设计 (brainstorm-experiments)
    │     └── 用户访谈 (interview-script)
    └── GTM策略 → pm-go-to-market
          ├── 上市计划 (gtm-strategy)
          ├── 增长飞轮 (growth-loops)
          └── 竞争战卡 (competitive-battlecard)

Phase 3: 营销与数据 (Week 5)
    ├── 营销增长 → pm-marketing-growth
    │     ├── 北极星指标 (north-star-metric)
    │     └── 营销创意 (marketing-ideas)
    └── 数据分析 → pm-data-analytics
          ├── SQL查询生成 (sql-queries)
          └── A/B测试分析 (ab-test-analysis)

Phase 4: 执行与规划 (Week 6-7)
    ├── 执行管理 → pm-execution
    │     ├── PRD撰写 (create-prd)
    │     ├── OKR制定 (brainstorm-okrs)
    │     ├── Sprint规划 (sprint-plan)
    │     └── 用户故事 (user-stories)
    └── PM工具包 → pm-toolkit
          ├── NDA起草 (draft-nda)
          └── 隐私政策 (privacy-policy)

Phase 5: 开发与工程 (Week 8-12)
    ├── Git工作树隔离 → using-git-worktrees
    ├── 测试驱动开发 → test-driven-development
    ├── 系统化调试 → systematic-debugging
    ├── 并行Agent分发 → dispatching-parallel-agents
    ├── 子Agent开发 → subagent-driven-development
    ├── 执行实施计划 → executing-plans
    ├── 请求代码审查 → requesting-code-review
    ├── 接收代码审查 → receiving-code-review
    ├── AI代码审计 → pm-ai-shipping
    └── 完工验证 → verification-before-completion

Phase 6: 收尾与发布 (Week 13)
    ├── 分支收尾 → finishing-a-development-branch
    └── 技能编写 → writing-skills

Phase 7: 好工具推荐 (Bonus)
    └── AgentMemory 持久记忆 → agentmemory

Phase 8: 实战案例 (Bonus)
    └── 从0到1创建电商公司 → real-world-ecommerce

Phase 9: 最佳实践 (Bonus)
    ├── 技能选择决策树 → 什么时候用什么技能
    ├── 最佳实践与避坑指南 → 10大高频踩坑
    └── 进阶玩法 → 技能组合拳、并行加速

Phase 10: 对比分析 (Bonus)
    └── 技能对比分析 → 主流方案横向对比

Phase 11: 行业应用 (Bonus)
    └── 手机配件店AI视频工具 → PDF报价单→短视频自动生成
```

## 🏗️ 项目结构

```
ai-agent-skills-zh/
├── README.md                    # 项目总览（你正在看的这个）
├── SKILL_INDEX.md               # 23个技能的完整索引
├── LICENSE                      # MIT许可证
├── 01-创意发想/                   # Phase 1: 创意与探索
│   ├── brainstorming-demo.md
│   ├── writing-plans-demo.md
│   └── using-superpowers-guide.md
├── 02-市场与产品/                 # Phase 2: 市场与产品
│   ├── market-research-demo.md
│   ├── product-strategy-demo.md
│   ├── product-discovery-demo.md
│   └── gtm-strategy-demo.md
├── 03-营销与数据/                 # Phase 3: 营销与数据
│   ├── marketing-growth-demo.md
│   └── data-analytics-demo.md
├── 04-执行与规划/                 # Phase 4: 执行与规划
│   ├── pm-execution-demo.md
│   └── pm-toolkit-demo.md
├── 05-开发与工程/                 # Phase 5: 开发与工程
│   ├── git-worktrees-demo.md
│   ├── tdd-demo.md
│   ├── systematic-debugging-demo.md
│   ├── parallel-agents-demo.md
│   ├── subagent-dev-demo.md
│   ├── executing-plans-demo.md
│   ├── code-review-demo.md
│   ├── pm-ai-shipping-demo.md
│   └── verification-demo.md
├── 06-收尾与发布/                 # Phase 6: 收尾与发布
│   ├── finishing-branch-demo.md
│   └── writing-skills-demo.md
├── 07-好工具推荐/                 # Phase 7: 好工具推荐
│   └── agentmemory-demo.md
├── 08-实战案例/                   # Phase 8: 实战案例
│   └── real-world-ecommerce.md
├── 09-最佳实践/                   # Phase 9: 最佳实践
│   ├── 技能选择决策树.md
│   ├── 最佳实践与避坑指南.md
│   └── 进阶玩法.md
├── 10-对比分析/                   # Phase 10: 对比分析
│   └── 技能对比分析.md
├── 11-行业应用/                   # Phase 11: 行业应用
│   └── 手机配件店AI视频工具/
│       ├── README.md              ← 完整文档
│       ├── SKILL.md               ← Hermes技能
│       ├── templates/             ← 2种视频模板
│       ├── scripts/               ← PDF解析+视频生成
│       └── examples/              ← 示例数据
└── templates/                     # 可直接复用的模板
    ├── prd-template.md
    ├── okr-template.md
    ├── sprint-template.md
    └── gtm-template.md
```

## 🎯 使用方式

### 方法一：按阶段学习
从 `01-创意发想/` 开始，依次完成每个阶段，体验完整的创业流程。

### 方法二：按技能搜索
参考 `SKILL_INDEX.md` 查找特定技能的实战用法。

### 方法三：按角色使用
- **产品经理** → 重点看 02、03、04 阶段
- **开发工程师** → 重点看 05 阶段
- **创业创始人** → 全部阶段
- **AI Agent 用户** → 作为技能学习手册

## 🔑 核心设计理念

1. **每个技能都有明确的落地场景**，不是空洞的理论
2. **技能之间有清晰的依赖关系**，理解顺序执行逻辑
3. **全部使用真实可复用的模板**，拿来即用
4. **面向中文用户**，解决"Get Up"等国外工具在国内不便使用的问题

## 📊 技能分类

| 类别 | 技能数 | 阶段 |
|------|--------|------|
| 产品管理 (PM-Skills) | 9个 | 02, 03, 04 |
| 软件工程（Superpowers） | 14个 | 01, 05, 06 |
| 好工具推荐 | 1个 | 07 |
| 实战案例 | 1个 | 08 |
| 最佳实践 | 3个 | 09 |
| 对比分析 | 1个 | 10 |
| 行业应用 | 1个 | 11 |
## 🤝 开源许可

本项目基于 **MIT License** 开源。你可以：
- ✅ 自由使用、修改、分发
- ✅ 商业使用
- ✅ 闭源分发
- 唯一要求：保留原作者声明

## 🌟 贡献指南

欢迎提 PR！无论是：
- 补充更多实战案例
- 翻译成其他语言
- 修复文档错误
- 添加新技能演示

## 📮 联系方式

- GitHub Issues: 提交建议或问题
- QQ群: 等待建立

---

> 💡 **开源的力量**：只有当每个人都把自己的经验开源出来，才能帮助更多人，包括AI在开源库中学习理解，形成良性循环。
