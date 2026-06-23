#!/usr/bin/env python3
"""
手机配件店AI视频工具 — PDF解析器
========================================
功能：解析PDF/报价单，提取产品信息（自动隐去价格）
输入：PDF文件或报价单图片
输出：结构化JSON数据（不含价格）

使用：
  python pdf_parser.py input.pdf
  python pdf_parser.py input.pdf --output products.json
"""

import sys
import json
import os
import re
from typing import List, Dict, Any, Optional

try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False


def remove_price(text: str) -> str:
    """从文本中移除价格信息"""
    # 匹配各种价格格式
    patterns = [
        r'¥\s*\d+\.?\d*',       # ¥12.5
        r'\$\s*\d+\.?\d*',       # $12.5
        r'RMB?\s*\d+\.?\d*',     # RMB12.5
        r'人民币\s*\d+\.?\d*',   # 人民币12.5
        r'价格[：:]?\s*\d+\.?\d*',  # 价格:12.5
        r'报价[：:]?\s*\d+\.?\d*',  # 报价:12.5
        r'[Cc]NY?\s*\d+\.?\d*',   # CNY12.5
        r'￥\s*\d+\.?\d*',       # ￥12.5 (全角)
    ]
    result = text
    for pattern in patterns:
        result = re.sub(pattern, '', result, flags=re.IGNORECASE)
    # 清理多余空格和标点
    result = re.sub(r'\s*[，,;；.。]+\s*', ' ', result)
    result = re.sub(r'\s+', ' ', result).strip()
    return result


def parse_pdf_pypdf2(filepath: str) -> List[str]:
    """使用PyPDF2解析PDF"""
    texts = []
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
    return texts


def parse_pdf_pdfplumber(filepath: str) -> List[str]:
    """使用pdfplumber解析PDF（推荐，效果更好）"""
    texts = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
    return texts


def parse_pdf_pymupdf(filepath: str) -> List[str]:
    """使用PyMuPDF解析PDF"""
    texts = []
    doc = fitz.open(filepath)
    for page in doc:
        text = page.get_text()
        if text.strip():
            texts.append(text)
    doc.close()
    return texts


def parse_pdf(filepath: str) -> List[str]:
    """解析PDF文件，优先使用pdfplumber"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"文件不存在: {filepath}")
    
    if HAS_PDFPLUMBER:
        print(f"[pdfplumber] 解析PDF: {filepath}")
        return parse_pdf_pdfplumber(filepath)
    elif HAS_PYMUPDF:
        print(f"[PyMuPDF] 解析PDF: {filepath}")
        return parse_pdf_pymupdf(filepath)
    elif HAS_PYPDF2:
        print(f"[PyPDF2] 解析PDF: {filepath}")
        return parse_pdf_pypdf2(filepath)
    else:
        print("[警告] 未找到PDF解析库，尝试安装...")
        print("推荐安装: pip install pdfplumber")
        print("备选安装: pip install PyMuPDF")
        print("备选安装: pip install PyPDF2")
        return []


def parse_docx(filepath: str) -> List[str]:
    """解析DOCX文件（PPT导出为DOCX的情况）"""
    if not HAS_DOCX:
        print("[警告] python-docx未安装，跳过DOCX解析")
        print("安装: pip install python-docx")
        return []
    
    texts = []
    doc = Document(filepath)
    for para in doc.paragraphs:
        if para.text.strip():
            texts.append(para.text)
    return texts


def extract_products(texts: List[str]) -> List[Dict[str, Any]]:
    """从文本中提取产品信息"""
    products = []
    
    for text in texts:
        # 清理文本
        text = remove_price(text)
        
        # 尝试分割产品条目
        # 常见分隔符：换行、空行、产品编号
        lines = text.split('\n')
        current_product = {}
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_product.get('name'):
                    products.append(current_product)
                    current_product = {}
                continue
            
            # 检测产品名称（通常包含"iPhone""AirPods""数据线"等关键词）
            phone_keywords = ['iPhone', 'iPad', 'AirPods', 'Apple', '华为', '小米', 'OPPO', 'vivo']
            accessory_keywords = ['壳', '膜', '线', '充电器', '耳机', '支架', '指环', '磁吸', '快充', '保护']
            
            is_product = any(kw in line for kw in phone_keywords + accessory_keywords)
            
            if is_product and not current_product.get('name'):
                current_product['name'] = line
            elif is_product and current_product.get('name'):
                # 新产品
                products.append(current_product)
                current_product = {'name': line}
            elif current_product.get('name'):
                # 描述或特性
                if 'desc' not in current_product:
                    current_product['desc'] = line
                else:
                    current_product['desc'] += '; ' + line
        
        # 最后一个产品
        if current_product.get('name'):
            products.append(current_product)
    
    # 去重和清理
    seen_names = set()
    unique_products = []
    for p in products:
        name = p.get('name', '').strip()
        if name and name not in seen_names:
            seen_names.add(name)
            unique_products.append(p)
    
    return unique_products


def main():
    if len(sys.argv) < 2:
        print("用法: python pdf_parser.py <input_file> [--output output.json]")
        print("")
        print("支持的格式: PDF, DOCX")
        print("")
        print("示例:")
        print("  python pdf_parser.py quote.pdf")
        print("  python pdf_parser.py quote.pdf --output products.json")
        print("  python pdf_parser.py products.docx")
        sys.exit(1)
    
    filepath = sys.argv[1]
    output_json = None
    
    if '--output' in sys.argv:
        idx = sys.argv.index('--output')
        if idx + 1 < len(sys.argv):
            output_json = sys.argv[idx + 1]
    
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.pdf':
        texts = parse_pdf(filepath)
    elif ext in ['.docx', '.doc']:
        texts = parse_docx(filepath)
    else:
        print(f"[错误] 不支持的文件格式: {ext}")
        print("支持的格式: .pdf, .docx")
        sys.exit(1)
    
    if not texts:
        print("[警告] 未提取到任何文本内容")
        print("提示: 如果是扫描件图片，需要使用OCR工具先转换")
        sys.exit(1)
    
    products = extract_products(texts)
    
    if not products:
        print("[警告] 未识别到产品信息")
        print("提示: 尝试手动指定产品字段")
        products = [{'name': '产品', 'desc': '请手动填写'}]
    
    result = {
        'source': filepath,
        'product_count': len(products),
        'products': products,
        'note': '价格信息已自动移除'
    }
    
    # 输出JSON
    if output_json:
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"[完成] 已保存 {len(products)} 个产品到: {output_json}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 打印摘要
    print(f"\n[摘要] 提取到 {len(products)} 个产品:")
    for i, p in enumerate(products[:10], 1):  # 只显示前10个
        name = p.get('name', '未知')
        desc = p.get('desc', '')
        print(f"  {i}. {name}" + (f" — {desc}" if desc else ""))
    if len(products) > 10:
        print(f"  ... 还有 {len(products)-10} 个产品")


if __name__ == '__main__':
    main()
