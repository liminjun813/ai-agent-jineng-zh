# Hermes Agent 技能速查卡

> 一页纸速查：什么时候用什么技能？怎么用它？

---

## 🚨 每次开发都用（必读！）

| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 完工要验证 | `verification-before-completion` | "用verification-before-completion验证所有任务完成" |
| 遇到bug | `systematic-debugging` | "用systematic-debugging系统排查这个问题" |
| 多步任务 | `writing-plans` | "用writing-plans写一个实施计划" |
| 批量任务 | `subagent-driven-development` | "用subagent-driven-development执行这个计划" |
| 保护主分支 | `using-git-worktrees` | "用using-git-worktrees隔离开发环境" |

---

## 📋 产品管理（PM-Skills）

### 市场调研阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 画用户画像 | `pm-market-research` | "用pm-market-research分析目标用户画像" |
| 竞品分析 | `pm-market-research` | "用pm-market-research做竞品分析" |
| 市场细分 | `pm-market-research` | "用pm-market-research做市场细分" |

### 产品设计阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 商业画布 | `pm-product-strategy` | "用pm-product-strategy设计商业模式" |
| 价值主张 | `pm-product-strategy` | "用pm-product-strategy写价值主张" |
| SWOT分析 | `pm-product-strategy` | "用pm-product-strategy做SWOT分析" |
| 假设识别 | `pm-product-discovery` | "用pm-product-discovery识别关键假设" |
| 实验设计 | `pm-product-discovery` | "用pm-product-discovery设计实验" |

### 上线准备阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 上市计划 | `pm-go-to-market` | "用pm-go-to-market制定上市计划" |
| 增长飞轮 | `pm-go-to-market` | "用pm-go-to-market设计增长飞轮" |
| 北极星指标 | `pm-marketing-growth` | "用pm-marketing-growth确定北极星指标" |
| 营销创意 | `pm-marketing-growth` | "用pm-marketing-growth生成营销创意" |
| SQL查询 | `pm-data-analytics` | "用pm-data-analytics生成SQL查询" |
| A/B测试 | `pm-data-analytics` | "用pm-data-analytics设计A/B测试" |
| PRD | `pm-execution` | "用pm-execution写一个PRD" |
| OKR | `pm-execution` | "用pm-execution制定OKR" |
| Sprint | `pm-execution` | "用pm-execution规划Sprint" |
| NDA | `pm-toolkit` | "用pm-toolkit起草NDA" |

### AI代码审计
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 安全审计 | `pm-ai-shipping` | "用pm-ai-shipping审计AI生成代码的安全性" |

---

## 🔧 软件开发（Superpowers）

### 创意阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 头脑风暴 | `brainstorming` | "用brainstorming帮我们头脑风暴" |

### 计划阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 写计划 | `writing-plans` | "用writing-plans写实施计划" |

### 开发阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 隔离开发 | `using-git-worktrees` | "用using-git-worktrees隔离功能分支" |
| 测试驱动 | `test-driven-development` | "用test-driven-development写测试" |
| 并行处理 | `dispatching-parallel-agents` | "用dispatching-parallel-agents并行处理" |
| 子Agent | `subagent-driven-development` | "用subagent-driven-development执行开发" |
| 执行计划 | `executing-plans` | "用executing-plans执行这个计划" |

### 质量保障
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 代码审查 | `requesting-code-review` | "用requesting-code-review审查这段代码" |
| 系统化调试 | `systematic-debugging` | "用systematic-debugging排查这个bug" |
| 完工验证 | `verification-before-completion` | "用verification-before-completion验证完工" |

### 收尾阶段
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 分支合并 | `finishing-a-development-branch` | "用finishing-a-development-branch合并到主分支" |
| 编写技能 | `writing-skills` | "用writing-skills创建新技能" |

### 总纲
| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 导入技能 | `using-superpowers` | "用using-superpowers导入技能" |

---

## 🧠 记忆系统（AgentMemory）

| 场景 | 技能 | 怎么说 |
|------|------|--------|
| 记住重要信息 | `remember` | "记住这个：[内容]" |
| 搜索过去记忆 | `recall` | "回想一下[内容]" |
| 查看会话历史 | `session-history` | "我们上次在做什么？" |
| 回顾近期工作 | `recap` | "recap最近一周的工作" |
| 恢复上次工作 | `handoff` | "继续上次的工作" |
| 删除记忆 | `forget` | "忘掉这个：[内容]" |
| 追溯代码来源 | `commit-context` | "这段代码是什么时候写的？" |

---

## 📌 记忆口诀

**开发流程记忆法：想 → 写 → 做 → 查 → 收**

1. **想**：brainstorming（创意）→ pm-market-research（调研）→ pm-product-strategy（策略）
2. **写**：writing-plans（计划）→ pm-execution（PRD/OKR/Sprint）
3. **做**：subagent-driven-development（执行）→ executing-plans（执行计划）→ dispatching-parallel-agents（并行）
4. **查**：test-driven-development（测试）→ requesting-code-review（审查）→ systematic-debugging（调试）→ verification-before-completion（验证）
5. **收**：finishing-a-development-branch（合并）→ writing-skills（技能沉淀）

**记忆口诀：先想后写，边做边查，最后收尾！**

---

## 🎯 推荐搭配

| 你的角色 | 建议搭配 |
|---------|---------|
| 产品经理 | brainstorming → market-research → product-strategy → execution → go-to-market |
| 开发工程师 | writing-plans → git-worktrees → tdd → subagent → code-review → verification → finishing |
| 创业者 | 全套，从01到06 |
| AI Agent用户 | 重点看：writing-plans、subagent-driven-development、verification-before-completion、systematic-debugging |

---

*共24个技能 | MIT License | 来源：Hermes Agent Skills 中文实战项目*
