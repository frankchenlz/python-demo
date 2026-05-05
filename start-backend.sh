#!/bin/bash

echo "启动后台管理系统后端..."

# 检查Python版本
python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
echo "Python版本: $python_version"

# 检查是否在正确的目录
if [ ! -f "backend/requirements.txt" ]; then
    echo "错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 进入后端目录
cd backend

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "创建Python虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 升级pip到最新版本
echo "升级pip..."
python -m pip install --upgrade pip

# 安装依赖
echo "安装Python依赖..."
python -m pip install -r requirements.txt

# 运行数据库迁移
echo "运行数据库迁移..."
python -m alembic upgrade head

# 启动服务器
echo "启动FastAPI服务器..."
python main.py