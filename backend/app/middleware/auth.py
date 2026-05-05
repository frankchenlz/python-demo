from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.exceptions import CustomException
from app.utils.logger import logger


class AuthMiddleware(BaseHTTPMiddleware):
    """认证中间件"""
    
    async def dispatch(self, request: Request, call_next):
        # 跳过认证的路径
        skip_paths = ["/auth/login", "/auth/login-json", "/docs", "/openapi.json"]
        if request.url.path in skip_paths:
            return await call_next(request)
        
        # 检查认证头
        authorization = request.headers.get("Authorization")
        if not authorization:
            return JSONResponse(
                status_code=401,
                content={
                    "error_code": 3001,
                    "detail": "缺少认证令牌",
                    "headers": {"WWW-Authenticate": "Bearer"}
                }
            )
        
        # 验证令牌格式
        if not authorization.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={
                    "error_code": 3003,
                    "detail": "令牌格式错误",
                    "headers": {"WWW-Authenticate": "Bearer"}
                }
            )
        
        # 继续处理请求
        response = await call_next(request)
        return response