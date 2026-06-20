# AI Agent Skills 快速入门指南

> 30分钟上手：从安装到产出第一个AI驱动的项目

---

## 一、项目概览

这个项目演示了如何用 **23个AI Agent技能 + 1个记忆引擎**，从0到1完成一个完整的AI电商创业项目。

**核心思想：** 不是讲理论，而是用一条完整的故事线串联所有技能，每个技能都有落地场景。

**技术栈：**
- AI工具：Hermes Agent、Claude Code、Copilot CLI
- 技能库：14个Superpowers（工程）+ 9个PM-Skills（产品）
- 记忆：AgentMemory（跨会话持久记忆）

---

## 二、Hermes技能速查

### 安装技能（如果你还没装）

这些技能需要单独安装到你的Hermes环境中：

```bash
# 方法1：从GitHub拉取（推荐）
cd ~/.hermes/skills/
# 把对应的技能目录clone进来

# 方法2：复制本地技能
# 技能文件在 ~/Desktop/JiNeng_ZhiShiKu/ai-agent-skills-zh/skills/ 目录下
```

### 技能安装清单

**Superpowers技能（14个）：**
```
brainstorming              — 创意头脑风暴
using-superpowers          — 总纲/入口
writing-plans              — 写实施计划
executing-plans            — 执行实施计划
test-driven-development    — 测试驱动开发
systematic-debugging       — 系统化调试
subagent-driven-development — 子Agent驱动开发
dispatching-parallel-agents — 并行Agent分发
requesting-code-review     — 请求代码审查
receiving-code-review      — 接收代码审查
verification-before-completion — 完工前验证
finishing-a-development-branch — 分支收尾
using-git-worktrees        — Git工作树隔离
writing-skills             — 编写技能
```

**PM-Skills技能（9个）：**
```
pm-execution               — PRD/OKR/Sprint
pm-product-strategy        — 商业策略
pm-product-discovery       — 产品发现
pm-market-research         — 市场调研
pm-go-to-market            — GTM上市计划
pm-marketing-growth        — 营销增长
pm-data-analytics          — 数据分析
pm-toolkit                 — 法律文档工具包
pm-ai-shipping             — AI代码审计
```

**AgentMemory：**
```
agentmemory                — 跨会话持久记忆（已安装）
```

---

## 三、30分钟快速上手

### Step 1：确认技能已加载

```bash
# 在Hermes中测试
skill_view(name='agentmemory')
```

如果看到技能内容，说明安装成功。

### Step 2：启动AgentMemory

```bash
# 启动内存服务器
agentmemory
# 看到 "AgentMemory server running on http://localhost:3111" 表示成功

# 浏览器打开实时视图
open http://localhost:3113
```

### Step 3：试用核心技能

**场景1：写一个项目计划**
```
在Hermes中对我说：
"请用writing-plans技能帮我写一个手机配件批量采购计划"
```

**场景2：搜索过去记忆**
```
在Hermes中对我说：
"用recall技能回想一下上次我们做的视频脚本"
```

**场景3：保存重要信息**
```
在Hermes中对我说：
"记住这个：我们的手机配件批发店在西安东35号"
```

### Step 4：阅读实战案例

```bash
# 从Phase 1开始读
open ~/Desktop/JiNeng_ZhiShiKu/ai-agent-skills-zh/01-创意发想/brainstorming-demo.md

# 或者从你的角色选读
# 产品经理 → 重点看 02、03、04
# 开发工程师 → 重点看 05
# 创业者 → 全部
```

---

## 四、按角色选读

### 📱 产品经理

**重点读：** Phase 02-04

1. `02-市场与产品/market-research-demo.md` — 用户画像怎么做
2. `02-市场与产品/product-strategy-demo.md` — 商业模式怎么设计
3. `04-执行与规划/pm-execution-demo.md` — PRD和OKR怎么写
4. `templates/prd-template.md` — 直接复用模板

### 💻 开发工程师

**重点读：** Phase 05 + 01

1. `05-开发与工程/systematic-debugging-demo.md` — 调试不瞎改
2. `05-开发与工程/tdd-demo.md` — 测试驱动开发
3. `05-开发与工程/subagent-dev-demo.md` — 批量开发提速
4. `05-开发与工程/verification-demo.md` — 上线前必验证

### 🚀 创业者/负责人

**全部读一遍**，重点关注：
1. `README.md` — 全局概览
2. `01-创意发想/brainstorming-demo.md` — 怎么找切入点
3. `02-市场与产品/gtm-strategy-demo.md` — 怎么上市
4. `04-执行与规划/pm-execution-demo.md` — 怎么落地

---

## 五、常见问题

### Q: 我没有Hermes怎么办？

这个项目的设计不依赖特定工具。所有案例都是Markdown文档，直接阅读即可理解每个技能的使用场景和方法论。

### Q: AgentMemory安装失败？

```bash
# 试试npx方式（不需要全局安装）
npx @agentmemory/agentmemory demo

# 如果网络慢，检查npm源
npm config set registry https://registry.npmmirror.com
```

### Q: 想学习某个技能更多细节？

每个技能目录下都有对应的`SKILL.md`文件：
```bash
skill_view(name='systematic-debugging')
skill_view(name='writing-plans')
```

---

## 六、下一步

1. **阅读完整项目** — 从Phase 1到Phase 7
2. **试用AgentMemory** — `agentmemory demo`
3. **创建你的第一个AI项目** — 参考模板
4. **贡献更多案例** — 提PR！

---

## 📚 项目结构速览

```
ai-agent-skills-zh/
├── README.md                    ← 项目总览（必读）
├── README-快速入门.md           ← 本文件（新手必读）
├── SKILL_INDEX.md               ← 24个技能完整索引
├── LICENSE                      ← MIT
├── 01-创意发想/                 ← brainstorming, writing-plans
├── 02-市场与产品/               ← 市场调研、产品策略、GTM
├── 03-营销与数据/               ← 营销增长、数据分析
├── 04-执行与规划/               ← PRD、OKR、Sprint
├── 05-开发与工程/               ← 开发全流程14个技能
├── 06-收尾与发布/               ← 收尾、编写技能
├── 07-好工具推荐/               ← AgentMemory等工具推荐
└── templates/                   ← PRD、OKR、Sprint、GTM模板
```
