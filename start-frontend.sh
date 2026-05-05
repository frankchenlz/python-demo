#!/bin/bash

echo "启动后台管理系统前端..."

# 检查Node.js版本
node_version=$(node --version)
echo "Node.js版本: $node_version"

# 检查是否在正确的目录
if [ ! -f "frontend/package.json" ]; then
    echo "错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 进入前端目录
cd frontend

# 检查node_modules是否存在
if [ ! -d "node_modules" ]; then
    echo "安装Node.js依赖..."
    npm install
fi

# 启动开发服务器
echo "启动Vite开发服务器..."
npm run dev