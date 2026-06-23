---
name: mobile-accessory-video-tool
description: 手机配件店AI视频工具 — 上传PDF报价单自动隐去价格，生成15-30秒带货短视频（商务风/同城风）
tags: [video, ecommerce, accessories, automation]
category: 行业应用
---

# 手机配件店AI视频工具

## 一句话
老板上传PDF/PPT报价单 → AI自动生成15-30秒带货短视频

## 适用场景
- 手机配件批发店日常短视频推广
- 抖音/视频号同城引流
- 产品上新宣传
- B2B批发宣传

## 核心功能
1. PDF/DOCX报价单解析（自动隐去价格）
2. 两种视频风格：商务风（深蓝）+ 同城风（橙黄）
3. 中英文双语支持
4. 动态字幕效果（跳字+变色+位置循环）
5. 1080×1920竖屏（抖音/视频号标准）

## 使用步骤

### Step 1: 安装依赖
```bash
pip install pdfplumber python-docx playwright
python -m playwright install chromium
pip install edge-tts  # 如需配音
```

### Step 2: 解析报价单
```bash
# 从PDF解析
python scripts/pdf_parser.py quote.pdf --output products.json

# 从DOCX解析
python scripts/pdf_parser.py products.docx --output products.json
```

### Step 3: 预览HTML效果
```bash
# 商务风格
open templates/business-style.html
# 同城风格
open templates/local-style.html
```

### Step 4: 生成视频
```bash
# 中文商务风
python scripts/video_generator.py products.json \
  --template templates/business-style.html \
  --output business_video.mp4 \
  --lang zh \
  --render

# 中文同城风
python scripts/video_generator.py products.json \
  --template templates/local-style.html \
  --output local_video.mp4 \
  --lang zh \
  --render

# 英文商务风
python scripts/video_generator.py products.json \
  --template templates/business-style.html \
  --output video_en.mp4 \
  --lang en \
  --render
```

### Step 5: 添加配音（可选）
```bash
# 中文配音
edge-tts --text "品质配件，源头工厂，全国批发一件代发" \
  --voice zh-CN-XiaoxiaoNeural --rate=-10% \
  --output audio.mp3

# 合并音频到视频
ffmpeg -i video.mp4 -i audio.mp3 \
  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
  -shortest output_with_audio.mp4
```

## 文件位置
```
11-行业应用/手机配件店AI视频工具/
├── README.md                    ← 完整文档
├── templates/
│   ├── business-style.html      ← 商务风模板
│   └── local-style.html         ← 同城风模板
├── scripts/
│   ├── pdf_parser.py            ← PDF解析器
│   └── video_generator.py       ← 视频生成器
├── examples/sample_products.json ← 示例数据
└── OUTPUTS/                     ← 输出视频
```

## 关键参数
- `--template`: 选择模板（business-style 或 local-style）
- `--lang`: 语言（zh=中文, en=英文）
- `--duration`: 视频时长（默认15秒，范围15-30）
- `--render`: 启用Playwright渲染为视频
- `--output`: 输出文件名

## 注意事项
1. 报价单必须是文字版PDF/DOCX，扫描件需要OCR预处理
2. 产品数量建议3-5个，最多不超过10个
3. 首次使用需要先安装Playwright浏览器
4. 价格信息会被自动移除，保护商业机密
5. 所有输出不含价格，供应商可以放心上传

## 视频风格对比
| 风格 | 配色 | 适用场景 | 特点 |
|------|------|---------|------|
| 商务风 | 深蓝渐变 | B2B批发、企业展示 | 专业、简洁、毛玻璃效果 |
| 同城风 | 橙黄渐变 | 抖音/视频号、C端带货 | 活泼、emoji、闪烁星星 |

## 快速体验
```bash
# 1. 安装
pip install pdfplumber python-docx playwright edge-tts
python -m playwright install chromium

# 2. 用示例数据测试
python scripts/video_generator.py examples/sample_products.json \
  --template templates/local-style.html \
  --output test_video.mp4 \
  --lang zh \
  --render

# 3. 预览
open templates/local-style.html
```
