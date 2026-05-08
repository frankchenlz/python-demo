---
name: "web-project-generator"
description: "快速生成包含前后端的完整web项目模板，支持Python+FastAPI+PostgreSQL后端和多种现代前端框架。Invoke when user wants to create a new web project with full-stack architecture."
---

# Web项目生成器

这个skill帮助您快速创建包含前后端的完整web项目，提供现代化的技术栈选择和项目结构模板。

## 功能特性

### 后端技术栈
- **Python 3.8+** - 现代Python开发
- **FastAPI** - 高性能异步Web框架
- **PostgreSQL** - 强大的关系型数据库
- **SQLAlchemy** - ORM数据库操作
- **Pydantic** - 数据验证和序列化
- **Alembic** - 数据库迁移工具
- **JWT认证** - 安全的用户认证系统
- **CORS支持** - 跨域请求处理

### 前端框架推荐
1. **React + TypeScript** - 企业级应用首选
2. **Vue 3 + TypeScript** - 渐进式框架，易于上手
3. **Svelte + TypeScript** - 编译时框架，性能优秀
4. **Next.js** - React全栈框架，SEO友好
5. **Nuxt.js** - Vue全栈框架，开发效率高

## 项目结构

生成的完整项目包含：

### 后端结构
```
backend/
├── app/
│   ├── api/           # API路由
│   ├── core/          # 核心配置
│   ├── db/            # 数据库配置
│   ├── models/        # 数据模型
│   ├── schemas/       # Pydantic模式
│   └── services/      # 业务逻辑
├── alembic/           # 数据库迁移
├── tests/             # 测试文件
├── requirements.txt   # Python依赖
└── main.py            # 应用入口
```

### 前端结构（以React为例）
```
frontend/
├── public/            # 静态资源
├── src/
│   ├── components/    # 可复用组件
│   ├── pages/         # 页面组件
│   ├── services/      # API服务
│   ├── hooks/         # 自定义Hooks
│   ├── utils/         # 工具函数
│   └── types/         # TypeScript类型
├── package.json       # 项目配置
└── tsconfig.json     # TypeScript配置
```

## 使用流程

1. **选择前端框架** - 根据项目需求选择合适的前端技术栈
2. **配置项目名称** - 设置项目根目录名称
3. **数据库配置** - 设置PostgreSQL连接信息
4. **功能模块选择** - 选择需要包含的功能模块
5. **自动生成** - 一键生成完整项目结构

## 生成的功能模块

### 基础功能
- 用户注册/登录/认证
- CRUD操作模板
- 错误处理中间件
- 日志记录系统
- 环境配置管理

### 可选功能
- 文件上传服务
- 邮件发送功能
- 缓存系统（Redis）
- 任务队列（Celery）
- API文档自动生成
- Docker容器化配置

## 开发工具集成

- **代码格式化** - Black, Prettier
- **代码检查** - Flake8, ESLint
- **测试框架** - pytest, Jest
- **热重载** - 开发时自动重载
- **API文档** - Swagger UI自动生成

## 部署配置

- Dockerfile配置
- docker-compose.yml
- 生产环境配置
- Nginx反向代理
- SSL证书配置

## 最佳实践

1. **代码规范** - 遵循PEP 8和前端代码规范
2. **安全考虑** - 输入验证、SQL注入防护
3. **性能优化** - 数据库索引、缓存策略
4. **错误处理** - 统一的错误响应格式
5. **测试覆盖** - 单元测试、集成测试

这个skill将引导您完成从项目初始化到基础功能实现的完整流程，确保项目结构清晰、代码质量高、易于维护和扩展。