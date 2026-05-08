# 项目初始化器

## 概述

一个用于从头初始化全栈Web项目的综合技能。此技能帮助用户设置完整的项目结构，包括前端和后端组件，以及必要的配置、依赖项和基本功能。

## 何时使用

当以下情况时使用此技能：
- 用户想要从头创建一个新的全栈Web项目
- 用户需要帮助设置前端+后端的项目结构
- 用户请求关于初始化Web应用程序的指导
- 用户需要项目设置和配置的帮助
- 用户想要使用特定技术启动新的Web开发项目

## 核心功能

### 1. 项目结构创建

#### 前端结构
```
frontend/
├── src/
│   ├── assets/         # 静态资源
│   ├── components/     # Vue组件
│   ├── views/          # 页面视图
│   ├── router/         # Vue Router配置
│   ├── store/          # 状态管理（Pinia）
│   ├── utils/          # 工具函数
│   ├── services/       # API服务
│   ├── App.vue         # 根组件
│   └── main.js         # 入口点
├── public/             # 公共文件
├── index.html          # HTML模板
├── vite.config.js      # Vite配置
├── package.json        # NPM依赖
└── .env                # 环境变量
```

#### 后端结构
```
backend/
├── app/
│   ├── api/            # API路由
│   ├── models/         # 数据库模型
│   ├── schemas/        # Pydantic模式
│   ├── utils/          # 工具函数
│   ├── middleware/     # 中间件
│   └── database.py     # 数据库连接
├── main.py             # FastAPI应用
├── requirements.txt    # Python依赖
└── .env                # 环境变量
```

### 2. 技术栈配置

#### 前端选项
- **框架**：Vue 3, React, Angular
- **构建工具**：Vite, Webpack
- **UI库**：Element Plus, Ant Design, Bootstrap
- **状态管理**：Pinia, Redux, Vuex
- **HTTP客户端**：Axios, Fetch API

#### 后端选项
- **框架**：FastAPI, Django, Express
- **数据库**：PostgreSQL, MySQL, SQLite
- **认证**：JWT, OAuth2
- **API风格**：RESTful, GraphQL

### 3. 项目初始化工作流

1. **收集需求**
   - 项目名称和描述
   - 前端技术栈
   - 后端技术栈
   - 数据库选择
   - 认证需求
   - 其他功能

2. **生成项目结构**
   - 创建目录结构
   - 初始化包管理器（npm, pip）
   - 配置构建工具
   - 设置环境变量

3. **实现核心功能**
   - 用户认证（登录/注册）
   - 数据库模型
   - API端点
   - 基本前端视图
   - 错误处理
   - 日志记录

4. **配置和设置**
   - 数据库连接
   - CORS设置
   - 环境变量
   - 开发服务器配置

5. **测试和验证**
   - 运行开发服务器
   - 测试API端点
   - 验证前后端集成

### 4. 常见项目模板

#### 模板1：Vue 3 + FastAPI + PostgreSQL
- **前端**：Vue 3, Vite, Element Plus, Pinia, Axios
- **后端**：FastAPI, SQLAlchemy, PostgreSQL, JWT
- **功能**：用户认证，CRUD操作，错误处理

#### 模板2：React + Express + MongoDB
- **前端**：React, Vite, Ant Design, Redux, Axios
- **后端**：Express, Mongoose, MongoDB, JWT
- **功能**：用户认证，RESTful API，文件上传

#### 模板3：Vue 3 + Django + MySQL
- **前端**：Vue 3, Vite, Bootstrap, Pinia, Axios
- **后端**：Django, Django REST Framework, MySQL
- **功能**：用户认证，管理面板，ORM

### 5. 分步实现

#### 前端设置
1. **初始化项目**
   ```bash
   npm create vite@latest frontend -- --template vue
   cd frontend
   npm install
   ```

2. **安装依赖**
   ```bash
   npm install element-plus pinia vue-router axios
   ```

3. **配置Vite**
   - 设置API调用代理
   - 配置环境变量

4. **创建基本组件**
   - 登录/注册表单
   - 布局组件
   - 导航

#### 后端设置
1. **初始化项目**
   ```bash
   mkdir backend
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

2. **安装依赖**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib python-dotenv
   ```

3. **创建数据库模型**
   - 用户模型
   - 其他业务模型

4. **实现API端点**
   - 认证端点
   - CRUD操作
   - 错误处理

5. **配置CORS**
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

### 6. 最佳实践

- **安全性**
  - 在生产环境中使用HTTPS
  - 实现适当的认证和授权
  - 验证用户输入
  - 使用环境变量存储敏感信息

- **性能**
  - 实现缓存
  - 优化数据库查询
  - 使用适当的索引
  - 压缩和打包资源

- **可维护性**
  - 遵循一致的编码规范
  - 编写全面的文档
  - 实现自动化测试
  - 使用版本控制

### 7. 故障排除

#### 常见问题
- **CORS错误**：检查后端CORS配置
- **数据库连接问题**：验证连接字符串和凭据
- **认证失败**：检查JWT密钥和过期设置
- **构建错误**：确保正确安装所有依赖

#### 调试技巧
- 在开发中启用调试模式
- 使用日志进行错误跟踪
- 使用Postman等工具测试API端点
- 检查浏览器控制台的前端错误

## 示例用法

### 示例1：初始化Vue 3 + FastAPI项目

**输入：**
"我想创建一个使用Vue 3前端和FastAPI后端的新项目。我需要用户认证和简单的CRUD界面。"

**输出：**
```
# 项目初始化计划

## 1. 项目结构
- 前端：Vue 3 + Vite + Element Plus + Pinia + Vue Router + Axios
- 后端：FastAPI + SQLAlchemy + PostgreSQL + JWT

## 2. 设置步骤
1. 创建项目目录
2. 初始化前端项目
3. 安装前端依赖
4. 初始化后端虚拟环境
5. 安装后端依赖
6. 配置数据库连接
7. 实现用户认证
8. 创建基本CRUD端点
9. 设置前端视图
10. 测试集成

## 3. 执行命令
```bash
# 创建项目结构
mkdir -p project/{frontend,backend}

# 前端设置
cd project/frontend
npm create vite@latest . -- --template vue
npm install element-plus pinia vue-router axios

# 后端设置
cd ../backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib python-dotenv

# 运行开发服务器
# 前端：npm run dev
# 后端：python -m uvicorn main:app --reload
```

## 4. 关键文件创建
- frontend/src/views/Login.vue
- frontend/src/views/Register.vue
- frontend/src/store/user.js
- frontend/src/utils/request.js
- backend/app/api/user.py
- backend/app/models/user.py
- backend/app/schemas/user.py
- backend/app/utils/security.py
- backend/main.py
```

### 示例2：初始化React + Express项目

**输入：**
"我需要创建一个React前端，Express后端和MongoDB数据库。"

**输出：**
```
# 项目初始化计划

## 1. 项目结构
- 前端：React + Vite + Ant Design + Redux + Axios
- 后端：Express + Mongoose + MongoDB + JWT

## 2. 设置步骤
1. 创建项目目录
2. 初始化前端项目
3. 安装前端依赖
4. 初始化后端项目
5. 安装后端依赖
6. 配置MongoDB连接
7. 实现用户认证
8. 创建API端点
9. 设置前端视图
10. 测试集成

## 3. 执行命令
```bash
# 创建项目结构
mkdir -p project/{frontend,backend}

# 前端设置
cd project/frontend
npm create vite@latest . -- --template react
npm install antd @reduxjs/toolkit react-redux axios

# 后端设置
cd ../backend
npm init -y
npm install express mongoose jsonwebtoken bcrypt cors dotenv

# 运行开发服务器
# 前端：npm run dev
# 后端：node server.js
```

## 4. 关键文件创建
- frontend/src/components/Login.jsx
- frontend/src/components/Register.jsx
- frontend/src/redux/store.js
- frontend/src/redux/userSlice.js
- frontend/src/utils/api.js
- backend/models/User.js
- backend/routes/auth.js
- backend/routes/api.js
- backend/server.js
```
