# 后台管理系统

基于Python 3.12 + FastAPI + PostgreSQL + Vue 3 + TypeScript的完整后台管理系统。

## 技术栈

### 后端
- **Python 3.12+** - 现代Python开发
- **FastAPI** - 高性能异步Web框架
- **PostgreSQL** - 企业级关系数据库
- **SQLAlchemy 2.0** - 现代ORM
- **Alembic** - 数据库迁移工具
- **JWT** - 安全认证机制

### 前端
- **Vue 3** - 组合式API
- **TypeScript** - 类型安全
- **Element Plus** - UI组件库
- **Vite** - 快速构建工具
- **Pinia** - 状态管理
- **Vue Router** - 路由管理

## 功能特性

- ✅ 用户管理（增删改查）
- ✅ JWT Token认证
- ✅ 分页、搜索、筛选
- ✅ 权限控制
- ✅ 标准化日志系统
- ✅ 统一异常处理
- ✅ 数据库连接池
- ✅ 配置化管理

## 项目结构

```
admin-system/
├── backend/                 # FastAPI后端
│   ├── app/
│   │   ├── api/            # API路由
│   │   ├── models/         # 数据模型
│   │   ├── schemas/        # Pydantic模式
│   │   ├── services/       # 业务逻辑
│   │   ├── core/           # 核心配置
│   │   ├── utils/          # 工具函数
│   │   └── middleware/     # 中间件
│   ├── alembic/            # 数据库迁移
│   ├── requirements.txt    # Python依赖
│   └── main.py            # 应用入口
├── frontend/               # Vue前端
│   ├── src/
│   │   ├── views/         # 页面组件
│   │   ├── components/    # 可复用组件
│   │   ├── store/         # 状态管理
│   │   ├── utils/         # 工具函数
│   │   └── types/         # TypeScript类型
│   ├── package.json       # 项目配置
│   └── vite.config.js     # Vite配置
└── README.md              # 项目说明
```

## 快速开始

### 1. 环境准备

确保已安装：
- Python 3.12+
- Node.js 16+
- PostgreSQL

### 2. 数据库设置

```bash
# 创建数据库
createdb demo

# 或使用psql
psql -U frank -h localhost -d postgres -c "CREATE DATABASE demo;"
```

### 3. 后端启动

```bash
# 进入后端目录
cd admin-system/backend

# 安装Python依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑.env文件，修改数据库连接等信息

# 运行数据库迁移
alembic upgrade head

# 启动开发服务器
python main.py
```

后端服务将运行在 http://localhost:8000

### 4. 前端启动

```bash
# 进入前端目录
cd admin-system/frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务将运行在 http://localhost:3000

## 默认账号

- **用户名**: admin
- **密码**: secret

## API文档

启动后端服务后，访问 http://localhost:8000/docs 查看Swagger UI文档。

## 开发规范

### 后端规范
- 遵循PEP 8代码规范
- 使用Black进行代码格式化
- 使用类型提示和Pydantic进行数据验证
- 统一的错误码和异常处理

### 前端规范
- 使用TypeScript确保类型安全
- 遵循Vue 3组合式API最佳实践
- 使用ESLint + Prettier进行代码检查
- 组件化开发，关注可复用性

## 部署说明

### 生产环境部署

1. **后端部署**
   ```bash
   # 使用Gunicorn + Nginx
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

2. **前端部署**
   ```bash
   npm run build
   # 将dist目录部署到Nginx或CDN
   ```

### Docker部署

项目支持Docker容器化部署，具体配置参考Dockerfile和docker-compose.yml文件。

## 许可证

MIT License