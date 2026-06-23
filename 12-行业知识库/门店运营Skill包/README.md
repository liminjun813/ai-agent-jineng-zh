# 门店运营Skill包

> 5个Hermes Agent技能，覆盖手机配件店日常运营的方方面面

---

## 技能列表

| 技能名 | 用途 | 触发关键词 |
|--------|------|-----------|
| `store-ops` | 店铺运营总控 | 店铺/SOP/流程/规范 |
| `store-inventory` | 库存管理 | 盘点/缺货/进货/上架/补货 |
| `store-marketing` | 营销内容 | 朋友圈/文案/推送/营销/活动 |
| `store-cutting-machine` | 裁膜机专家 | 裁膜机/裁膜/刀片/耗材 |
| `store-order` | 订单管理 | 订单/开单/核对/接待/客户 |

---

## 使用方式

### 方式1：员工用暗号

员工在微信里发送暗号，智能体自动路由到对应技能：

```
员工：#SOP库房
→ store-ops 返回库房整理SOP

员工：#盘点
→ store-inventory 执行盘点流程

员工：朋友圈文案
→ store-marketing 生成朋友圈文案

员工：客户说iPhone 16膜有没有
→ store-order 查询价格并回复
```

### 方式2：Hermes Agent调用

在Hermes中直接调用技能：

```
"用store-inventory帮我盘点一下钢化膜库存"
"用store-marketing生成一条朋友圈文案"
```

---

## 日常运营流程图

```
早晨(8:30-9:00)
  ↓  store-ops: 开店准备检查
  ↓
上午(9:00-12:00)
  ↓  store-order: 接待客户+开单
  ↓  store-marketing: 发布朋友圈
  ↓
下午(13:30-18:00)
  ↓  store-inventory: 库存盘点
  ↓  store-order: 处理订单
  ↓
晚间(18:00-19:30)
  ↓  store-order: 发货安排
  ↓  store-inventory: 当日盘点
  ↓  store-ops: 记录数据
```

---

## 安装

```bash
# 安装全部5个技能
hermes skills install store-ops
hermes skills install store-inventory
hermes skills install store-marketing
hermes skills install store-cutting-machine
hermes skills install store-order
```

---

*门店运营Skill包 · 西安·东35号·鑫源光电*
