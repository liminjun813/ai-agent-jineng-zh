---
name: demo-verification
description: 用verification-before-completion验证完工
category: 开发与工程
skills_used: [verification-before-completion]
---

# 案例：完工验证 — 上线前最后检查

## 场景

所有开发任务完成，准备上线MVP。

## 使用verification-before-completion技能

打开Hermes Agent，说："MVP开发完成了，用verification-before-completion技能做最终验证。"

## 执行流程

AI Agent会**强制自己**执行以下验证：

```
1. ✅ 运行测试套件
   $ npm test
   结果: 156/156 通过, 0 失败

2. ✅ 运行构建
   $ npm run build
   结果: exit 0, 构建成功

3. ✅ 运行lint检查
   $ npm run lint
   结果: 0 错误, 3 警告（非阻断）

4. ✅ 验证PRD需求覆盖
   列出PRD的每个需求 → 对照检查实现
   1. 用户注册 → ✅
   2. 商品搜索 → ✅
   3. AI推荐 → ✅
   4. 购物车 → ✅
   5. 订单管理 → ✅
   6. 优惠券 → ✅
   7. 后台管理 → ✅
   8. 支付集成 → ✅（集成第三方）
   9. 日志监控 → ✅
   10. 性能要求（<2s） → ✅ 平均1.2s

5. ✅ 安全扫描
   $ npm audit
   结果: 0 高危漏洞

6. ✅ 数据库迁移
   $ alembic upgrade head
   结果: 成功迁移到v1.0.0
```

## 规则

- **绝不**在没有运行验证命令的情况下说"完成了"
- 不说"应该通过了"、"看起来没问题"
- 必须**看到输出**才能声称通过
- 任何失败都如实报告，不跳过

## 关键要点

- 这是**最重要**的Superpower技能
- 防止AI"瞎报进度"
- 每次声称完成前**必须**执行验证
- 核心原则：**证据先行，断言在后**
