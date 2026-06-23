# 手机配件店AI视频工具

> 上传PDF/PPT报价单 → AI自动生成带货短视频

---

## 📋 项目简介

这是一个专门为**手机配件批发店**设计的AI视频生成工具。

**核心流程：**
```
老板上传报价单(PDF/PPT)
    → PDF解析器提取产品信息(自动隐去价格)
    → 产品数据 + HTML模板
    → GSAP动画生成视频页面
    → Playwright渲染为短视频
    → 输出15-30秒竖屏视频
```

**特点：**
- ✅ 自动隐去价格（保护商业机密）
- ✅ 两种风格：商务风 + 同城风
- ✅ 支持中英文配音
- ✅ 动态字幕效果（跳字+变色+位置循环）
- ✅ 1080×1920竖屏（抖音/视频号标准）

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# 解析PDF
pip install pdfplumber

# 解析DOCX
pip install python-docx

# 渲染视频（可选，需要Playwright）
pip install playwright
python -m playwright install chromium
```

### 2. 解析报价单

```bash
# 解析PDF报价单
python scripts/pdf_parser.py quote.pdf --output products.json

# 解析DOCX报价单
python scripts/pdf_parser.py products.docx --output products.json
```

**输出示例：**
```json
{
  "source": "quote.pdf",
  "product_count": 5,
  "products": [
    {
      "name": "iPhone 16 Pro 保护壳",
      "desc": "防摔抗撞 · 超薄手感 · 多色可选"
    },
    {
      "name": "AirPods Pro 保护套",
      "desc": "硅胶材质 · 挂绳设计 · 防丢"
    }
  ],
  "note": "价格信息已自动移除"
}
```

### 3. 生成视频

```bash
# 商务风格
python scripts/video_generator.py products.json \
  --template templates/business-style.html \
  --output business_video.mp4 \
  --lang zh \
  --render

# 同城风格
python scripts/video_generator.py products.json \
  --template templates/local-style.html \
  --output local_video.mp4 \
  --lang zh \
  --render
```

### 4. 预览HTML

```bash
# 先看HTML效果，满意后再渲染视频
open templates/business-style.html
```

---

## 📁 项目结构

```
手机配件店AI视频工具/
├── README.md                    ← 本文件
├── templates/
│   ├── business-style.html      ← 商务风格模板（深蓝渐变）
│   └── local-style.html         ← 同城风格模板（橙黄渐变）
├── scripts/
│   ├── pdf_parser.py            ← PDF/DOCX解析器
│   └── video_generator.py       ← 视频生成器
├── examples/
│   └── sample_products.json     ← 示例产品数据
└── OUTPUTS/                     ← 生成的视频存放处
```

---

## 🎨 模板说明

### 商务风格 (business-style.html)

**适用场景：** B2B批发宣传、企业展示
**视觉特征：**
- 深蓝色渐变背景
- 毛玻璃产品卡片
- 简洁专业的字体
- 粒子动画装饰
- 循环字幕条

**时长：** 约15秒
**字幕内容：**
- "品质配件 工厂直供"
- "全国批发 一件代发"
- "西安东35号 鑫源光电"
- "iPhone配件 专注品质"

### 同城风格 (local-style.html)

**适用场景：** 抖音/视频号同城推广、C端带货
**视觉特征：**
- 橙黄色渐变背景
- 白色圆角卡片
- emoji图标装饰
- 闪烁星星效果
- 跳字变色字幕

**时长：** 约15秒
**字幕内容：**
- "品质配件 源头工厂"
- "全国批发 一件代发"
- "西安东35号 鑫源光电"
- 中英文切换

---

## 🔧 自定义产品数据

### 手动编辑JSON

```json
{
  "source": "custom",
  "product_count": 3,
  "products": [
    {
      "name": "产品名称",
      "desc": "产品描述",
      "features": ["特性1", "特性2", "特性3"]
    }
  ],
  "note": "价格信息已自动移除"
}
```

### 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| name | ✅ | 产品名称 |
| desc | ❌ | 产品描述（用·或;分隔特性） |
| features | ❌ | 特性标签数组 |

---

## 🌐 多语言支持

### 中文模式（默认）

```bash
python scripts/video_generator.py products.json \
  --template templates/local-style.html \
  --lang zh \
  --output video_zh.mp4
```

### 英文模式

```bash
python scripts/video_generator.py products.json \
  --template templates/business-style.html \
  --lang en \
  --output video_en.mp4
```

英文模式会自动替换：
- 标题 → "New Arrivals"
- 描述 → 英文翻译
- CTA → "Scan to Contact"
- 地址 → 拼音/英文

---

## 💡 使用建议

### 1. 报价单格式要求

**推荐格式：**
- PDF（文字版，非图片扫描）
- DOCX（Word文档）

**不推荐：**
- 图片/PNG/JPG（需要OCR）
- 扫描件（需要OCR）

### 2. 产品数量建议

- **最少：** 1个产品
- **推荐：** 3-5个产品
- **最多：** 10个产品（太多会拥挤）

### 3. 视频时长

- **15秒：** 适合抖音/快手/视频号（快速浏览）
- **20秒：** 适合朋友圈广告（信息量适中）
- **30秒：** 适合网站展示/展会（详细说明）

### 4. 价格处理

**自动隐去价格的功能：**
- 自动检测并移除 ¥$RMB 等价格标记
- 输出JSON中不包含任何价格信息
- 保护商业机密，供应商可以放心上传

---

## 🎬 配音方案

### 方案1：Edge TTS（免费，推荐）

```bash
# 中文配音
edge-tts --text "品质配件，源头工厂" \
  --voice zh-CN-XiaoxiaoNeural \
  --file audio.mp3

# 英文配音
edge-tts --text "Quality accessories direct from factory" \
  --voice en-US-AriaNeural \
  --file audio_en.mp3
```

### 方案2：本地CosyVoice（声音克隆）

```bash
# 使用用户的声音克隆
cosyvoice --voice-ref voice_ref.wav \
  --text "品质配件，源头工厂" \
  --output audio.mp3
```

### 方案3：手动录制

```bash
# 用手机录一句配音，然后合并到视频
ffmpeg -i video.mp4 -i audio.mp3 \
  -c:v copy -c:a aac \
  -map 0:v:0 -map 1:a:0 \
  -shortest \
  output_with_audio.mp4
```

---

## 📊 与其他方案的对比

| 方案 | 优点 | 缺点 | 适合场景 |
|------|------|------|---------|
| **本工具** | 免费、本地、自动隐价 | 需要Python环境 | 手机配件店日常使用 |
| Canva | 模板多、操作简单 | 付费、无自动隐价 | 偶尔做视频 |
| 剪映 | 免费、效果好 | 手动操作、无自动化 | 个人创作者 |
| 外包制作 | 专业、省心 | 贵（500-2000/条） | 高端品牌宣传 |

---

## 🔗 相关资源

- [Edge TTS文档](https://github.com/rany2/edge-tts)
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
- [Playwright](https://playwright.dev/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

---

*基于真实业务场景开发 · 西安·东35号·鑫源光电*
