#!/bin/bash
# Project 0 Structure Verification Script

echo "=== 执行 Project 0 结构验证 ==="

# 1. Check Critical Paths
if [ ! -f "index.html" ]; then
    echo "错误: index.html 缺失"
    exit 1
fi

if [ ! -d "src/scripts" ]; then
    echo "错误: src/scripts 目录缺失"
    exit 1
fi

if [ ! -f "public/assets/main.css" ]; then
    echo "错误: 编译后的 CSS 缺失，请运行 npm run build"
    exit 1
fi

# 2. Check i18n Integrity (Check for a known key in content.js)
if ! grep -q "project-grid" index.html; then
    echo "错误: HTML 结构不匹配"
    exit 1
fi

if ! grep -q "translations" src/scripts/content.js; then
    echo "错误: 翻译数据源缺失"
    exit 1
fi

# 3. Check Archaeology
if [ ! -f "docs/archaeology/MEMORIAL.md" ]; then
    echo "警告: 考古文档缺失"
fi

echo "=== 验证通过: 工程结构 100% 合规 ==="
