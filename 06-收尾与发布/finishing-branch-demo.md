---
name: demo-finishing-branch
description: 用finishing-a-development-branch收尾开发
category: 收尾与发布
skills_used: [finishing-a-development-branch]
---

# 案例：分支收尾 — 合并MVP到主分支

## 场景

MVP开发完成，验证通过，准备合并到主分支并创建发布。

## 使用finishing-a-development-branch技能

```
AI Agent会：
1. 验证所有测试通过
2. 检测当前工作环境（主分支还是工作树）
3. 呈现选项菜单
```

## 呈现的选项

```
开发已完成。请选择：

1. 合并到 main 分支（本地）
2. 推送并创建 Pull Request
3. 保留分支（稍后处理）
4. 丢弃所有工作

你选哪个？
```

## 选择2：创建PR

AI Agent会自动：
```bash
# 推送分支
git push -u origin feature-mvp

# 创建PR
gh pr create \
  --title "MVP: AI推荐电商推荐平台核心功能" \
  --body "## 摘要
- 用户注册登录模块
- AI个性化推荐引擎
- 购物车与订单管理
- 优惠券系统
- 后台管理面板

## 测试计划
- [x] 单元测试 156/156 通过
- [x] 集成测试 45/45 通过
- [x] 性能测试 平均响应 1.2s

## 审计结果
- [x] 安全审计通过，0 高危漏洞
- [x] 代码审查通过
- [x] PRD需求全覆盖"
```

## 关键要点

- **合并前必须验证测试通过**
- 创建PR时**不删除工作树**（需要迭代反馈）
- 丢弃工作**必须确认**
- 遵循正确的清理顺序
