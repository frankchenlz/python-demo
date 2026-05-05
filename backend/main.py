from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import engine, Base
from app.api import user, auth
from app.middleware.auth import AuthMiddleware
from app.middleware.activity import ActivityMiddleware
from app.utils.exceptions import CustomException
from app.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时
    logger.info("应用启动中...")
    
    # 创建数据库表
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("数据库表创建完成")
    except Exception as e:
        logger.error(f"数据库表创建失败: {e}")
    
    yield
    
    # 关闭时
    logger.info("应用关闭中...")


# 创建FastAPI应用
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="基于Python 3.12+FastAPI+PostgreSQL的后台管理系统",
    lifespan=lifespan
)

# 添加中间件
app.add_middleware(AuthMiddleware)
app.add_middleware(ActivityMiddleware)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(user.router)
app.include_router(auth.router)


# 自定义异常处理器
@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc: CustomException):
    """自定义异常处理器"""
    logger.error(f"自定义异常: {exc.detail} (错误码: {exc.error_code})")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "detail": exc.detail,
            "success": False
        },
        headers=exc.headers
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """HTTP异常处理器"""
    logger.error(f"HTTP异常: {exc.detail} (状态码: {exc.status_code})")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": 1000 + exc.status_code,  # 系统错误码
            "detail": exc.detail,
            "success": False
        },
        headers=exc.headers
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    """通用异常处理器"""
    logger.error(f"未处理异常: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error_code": 1001,  # 系统错误
            "detail": "系统内部错误",
            "success": False
        }
    )


@app.get("/")
async def root():
    """根路径"""
    return {
        "message": f"欢迎使用{settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "success": True
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z",
        "success": True
    }


if __name__ == "__main__":
    import uvicorn
    
    logger.info("启动开发服务器...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )