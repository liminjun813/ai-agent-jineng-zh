---
name: demo-agentmemory
description: AgentMemory持久记忆系统分析 — 跨会话记忆、自动捕获、智能检索
category: 好工具推荐
skills_used: [agentmemory]
---

# 案例：AgentMemory — AI Agent持久记忆引擎

## 什么是AgentMemory？

一个专为AI编码智能体设计的**持久记忆系统**。它自动捕获Agent做了什么，压缩成可搜索的记忆，下次会话启动时自动注入相关上下文。

**核心一句话：** 不用再每次新会话都重新解释项目了。

**GitHub:** https://github.com/rohitg00/agentmemory
**License:** Apache-2.0
**Version:** 0.9.27

## 我们分析的核心数据

| 指标 | AgentMemory | 传统方案 | 提升 |
|------|------------|---------|------|
| 召回率@5 | 95.2% | 86.2% | +9% |
| 召回率@10 | 98.6% | 94.6% | +4% |
| Token消耗/年 | 0（本地） | 170K+ | 节省92% |
| 外部依赖 | SQLite | Qdrant/pgvector | 零依赖 |
| 检索延迟 | 14ms | 依赖API | 极低 |

## 它怎么工作的？

```
Session 1: Agent做了一堆操作 → 12个hook自动捕获
    ↓
LLM自动压缩 → 存入本地SQLite
    ↓
Session 2: Agent启动 → 自动检索相关上下文 → 注入prompt
```

**不再需要：**
- 每次新会话重新解释"鑫源光电东35号手机配件批发"
- 重新解释微信导出调试经验
- 重新解释HyperFrames视频模板配置
- CLAUDE.md/AGENTS.md 塞满200行还会过时

## 架构原理

AgentMemory 基于 **iii-engine**（三原语：Worker/Function/Trigger）构建：

1. **iii-engine** — WebSocket服务（端口49134），管理所有Worker和Trigger
2. **HTTP Server** — 端口3111，提供REST API和MCP工具
3. **Stream** — 端口3112，实时观察记忆构建过程
4. **Viewer** — 端口3113，浏览器实时查看记忆图谱
5. **State** — 文件级SQLite（`data/state_store.db`），零外部依赖
6. **Hybrid Search** — BM25关键词 + 向量语义 + 知识图谱，RRF融合排序

**记忆生命周期（4级）：**
- **短期**：当前会话内
- **中期**：跨会话（保留7-30天）
- **长期**：固化记忆（永久保留）
- **自动遗忘**：过期记忆自动衰减

## 对我们业务的价值

### 1. 跨会话项目上下文自动恢复
每次新会话启动，自动记住：
- 我们做了什么（微信解密、视频生成、批量处理）
- 踩过的坑（sudo管道被拦截、FFmpeg音频截断问题）
- 用户偏好（中文命名、15秒9:16视频、Ting-Ting语音）

### 2. 经验知识持久化
微信解密工具链的调试经验、各种技能的安装方法，不会随着会话结束而丢失。

### 3. 客户信息跨会话
Agent自动记录与不同客户的沟通模式，保持一致的服务质量。

### 4. 视频批量生产流程
记住HyperFrames三种风格模板的配置，自动记住客户对视频风格的偏好。

## 在Hermes中的集成方式

### 方式一：MCP Server（推荐）

在 `~/.hermes/config.yaml` 中添加MCP配置：

```yaml
mcp:
  servers:
    agentmemory:
      command: "npx"
      args: ["-y", "@agentmemory/mcp"]
      env:
        AGENTMEMORY_URL: "http://localhost:3111"
        AGENTMEMORY_SECRET: ""
        AGENTMEMORY_TOOLS: "all"
```

启动后可用53个MCP工具：
- `memory_save` — 手动保存记忆
- `memory_smart_search` — 智能搜索记忆
- `memory_sessions` — 查看会话历史
- `memory_recap` — 会话回顾
- `memory_forget` — 删除记忆
- `memory_handoff` — 恢复上次工作
- `memory_commit_context` — 追溯代码来源

### 方式二：自动安装8个技能

```bash
npx skills add rohitg00/agentmemory -y
```

这会自动安装8个原生技能：
- `remember` — 显式保存记忆（用户说"记住这个"时）
- `recall` — 搜索过去记忆（用户说"回想一下"时）
- `forget` — 删除特定记忆
- `handoff` — 恢复上次会话
- `session-history` — 查看会话历史
- `recap` — 回顾最近N次会话
- `commit-context` — 追溯代码来源
- `commit-history` — 列出Agent关联的Git提交

### 快速体验

```bash
# 1. 启动服务器
agentmemory

# 2. 验证工作（种子数据+检索演示）
agentmemory demo

# 3. 查看实时记忆视图
open http://localhost:3113

# 4. 关闭
agentmemory stop
```

## 与Hermes内置memory的关系

| | Hermes内置memory | AgentMemory |
|--|-----------------|-------------|
| 触发 | 手动save() | **自动捕获** |
| 存储 | SQLite | SQLite |
| 检索 | 全量注入prompt | **按需检索** |
| 结构化 | 简单文本 | BM25+向量+图谱 |
| 外部依赖 | 无 | 无（SQLite） |
| Token效率 | 全量注入 | 按需检索 |
| 适用 | 用户偏好/规则 | **项目上下文+经验** |

**建议：两者互补使用。** Hermes memory存用户偏好和规则，AgentMemory存项目上下文和调试经验。

## 常见问题

### 数据隐私？
**完全本地部署**。所有数据存在本地SQLite，无需联网，零云端。

### 对Hermes性能影响？
Hook捕获是异步的，记忆检索14ms。启动时有上下文加载开销（约几百ms），但每次会话节省大量Token。

### 需要配置外部数据库吗？
**不需要**。内置iii-engine + SQLite，零外部依赖。
