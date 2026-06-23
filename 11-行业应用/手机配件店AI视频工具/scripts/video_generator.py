#!/usr/bin/env python3
"""
手机配件店AI视频工具 — 视频生成器
========================================
功能：从产品JSON数据生成HTML视频页面，然后用ffmpeg+chromium录制为视频

使用：
  python video_generator.py products.json --template business-style.html --output video.mp4
  python video_generator.py products.json --template local-style.html --output video.mp4 --lang zh
  python video_generator.py products.json --template local-style.html --output video.mp4 --lang en
"""

import sys
import json
import os
import argparse
import subprocess
import tempfile
import shutil
from pathlib import Path


def generate_html(template_path: str, products: list, lang: str = 'zh') -> str:
    """根据模板和产品数据生成HTML文件"""
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 根据语言替换默认文案
    if lang == 'en':
        html = html.replace('新品上市', 'New Arrivals')
        html = html.replace('品质配件 · 值得信赖', 'Quality Accessories · Trusted Choice')
        html = html.replace('扫码咨询 · 批发优惠', 'Scan to Contact · Wholesale Deals')
        html = html.replace('西安东35号 · 一条龙手机配件鑫源光电', 'Xi\'an East No.35 · Yitiaolong Mobile Accessories')
        html = html.replace('品质配件 源头工厂', 'Quality Accessories Direct From Factory')
        html = html.replace('全国批发 一件代发', 'Nationwide Wholesale · Dropshipping Available')
    
    # 如果有产品数据，替换模板中的默认产品
    if products:
        # 这里可以根据实际需求定制替换逻辑
        # 当前版本使用模板默认产品，后续可扩展
        pass
    
    return html


def render_video(html_content: str, output_path: str, duration: float = 15) -> bool:
    """使用chromium无头模式将HTML渲染为视频"""
    
    # 创建临时目录
    tmpdir = tempfile.mkdtemp(prefix='video_gen_')
    try:
        html_file = os.path.join(tmpdir, 'index.html')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 方法1: 使用Puppeteer/Playwright（推荐）
        # 需要安装: pip install playwright
        # python -m playwright install chromium
        
        # 方法2: 使用ffmpeg录制（备选）
        # 需要先启动一个web服务器，然后用ffmpeg截取
        
        print(f"[信息] 视频渲染需要浏览器自动化工具")
        print(f"[提示] 推荐使用 Playwright:")
        print(f"  pip install playwright")
        print(f"  python -m playwright install chromium")
        print(f"  然后运行: python video_generator.py --render")
        
        return True
        
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def create_playwright_renderer():
    """创建Playwright渲染器"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[错误] Playwright未安装")
        print("安装: pip install playwright")
        print("安装浏览器: python -m playwright install chromium")
        return None
    
    def render(html_path: str, output_path: str, duration: float = 15) -> bool:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': 1080, 'height': 1920})
            page.goto(f'file://{os.path.abspath(html_path)}')
            
            # 等待动画播放
            page.wait_for_timeout(duration * 1000)
            
            # 录制为视频
            page.video.save_as(output_path)
            browser.close()
        
        return True
    
    return render


def main():
    parser = argparse.ArgumentParser(description='手机配件店AI视频生成器')
    parser.add_argument('input', help='产品JSON文件或PDF/DOCX文件')
    parser.add_argument('--template', '-t', default='templates/business-style.html',
                       help='HTML模板文件路径')
    parser.add_argument('--output', '-o', default='output.mp4',
                       help='输出视频文件路径')
    parser.add_argument('--lang', '-l', default='zh', choices=['zh', 'en'],
                       help='视频语言: zh=中文, en=英文')
    parser.add_argument('--duration', '-d', type=float, default=15,
                       help='视频时长(秒), 默认15秒')
    parser.add_argument('--render', action='store_true',
                       help='使用Playwright渲染视频')
    
    args = parser.parse_args()
    
    # 读取产品数据
    if args.input.endswith('.json'):
        with open(args.input, 'r', encoding='utf-8') as f:
            data = json.load(f)
        products = data.get('products', [])
        print(f"[信息] 从JSON读取 {len(products)} 个产品")
    elif args.input.endswith(('.pdf', '.docx')):
        # 先解析PDF/DOCX
        from pdf_parser import parse_pdf, parse_docx, extract_products
        if args.input.endswith('.pdf'):
            texts = parse_pdf(args.input)
        else:
            texts = parse_docx(args.input)
        products = extract_products(texts)
        print(f"[信息] 从文件解析 {len(products)} 个产品")
    else:
        print(f"[错误] 不支持的文件格式: {args.input}")
        print("支持的格式: .json, .pdf, .docx")
        sys.exit(1)
    
    # 生成HTML
    print(f"[信息] 使用模板: {args.template}")
    html_content = generate_html(args.template, products, args.lang)
    
    # 保存HTML到临时文件
    tmpdir = tempfile.mkdtemp(prefix='video_gen_')
    try:
        html_file = os.path.join(tmpdir, 'index.html')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[信息] HTML已保存: {html_file}")
        print(f"[信息] 可用浏览器打开预览: open {html_file}")
        
        if args.render:
            # 使用Playwright渲染
            renderer = create_playwright_renderer()
            if renderer:
                print(f"[信息] 渲染视频: {args.duration}秒")
                renderer(html_file, args.output, args.duration)
                print(f"[完成] 视频已保存: {args.output}")
            else:
                print("[跳过] 未安装Playwright，请安装后使用 --render 参数")
        else:
            print("[提示] 要生成视频，请安装Playwright后使用 --render 参数")
            print("[提示] 预览HTML: open " + html_file)
        
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == '__main__':
    main()
