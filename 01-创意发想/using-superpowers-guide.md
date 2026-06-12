---
name: demo-using-superpowers
description: using-superpowers技能总纲 — 如何使用全部超级技能
category: 创意发想
skills_used: [using-superpowers]
---

# 案例：using-superpowers 总纲

## 背景

这是所有Superpowers技能的入口文档。它告诉AI Agent：
1. 有哪些技能可用
2. 每个技能在什么场景使用
3. 技能之间的依赖关系

## 使用方法

当你第一次加载superpowers技能包时，AI Agent会自动读取这个总纲。它定义了：

```
当我说"用超级技能"时，AI应该：
1. 先读using-superpowers了解全部选项
2. 根据当前任务选择合适的技能
3. 按正确顺序执行（如先写计划再执行）
4. 验证每个步骤的输出
```

## 技能调用规则

| 场景 | 优先调用的技能 |
|------|--------------|
| 开始新项目 | brainstorming → writing-plans |
| 多步任务 | subagent-driven-development |
| 发现bug | systematic-debugging |
| 写完代码 | requesting-code-review → verification-before-completion |
| 项目收尾 | finishing-a-development-branch |

## 关键要点

- `using-superpowers` 是**元技能**，它不直接执行任务，而是告诉AI如何调用其他技能
- 加载它意味着你希望AI**遵循最佳实践**而非随机执行
