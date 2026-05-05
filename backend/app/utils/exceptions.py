from fastapi import HTTPException, status
from typing import Any, Dict, Optional

from app.core.security import ErrorCode


class CustomException(HTTPException):
    """自定义异常基类"""
    
    def __init__(
        self,
        status_code: int,
        error_code: int,
        detail: str,
        headers: Optional[Dict[str, Any]] = None
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.error_code = error_code


class UserNotFoundException(CustomException):
    """用户不存在异常"""
    
    def __init__(self, detail: str = "用户不存在"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            error_code=ErrorCode.USER_NOT_FOUND,
            detail=detail
        )


class UserAlreadyExistsException(CustomException):
    """用户已存在异常"""
    
    def __init__(self, detail: str = "用户已存在"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code=ErrorCode.USER_ALREADY_EXISTS,
            detail=detail
        )


class InvalidCredentialsException(CustomException):
    """无效凭据异常"""
    
    def __init__(self, detail: str = "用户名或密码错误"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code=ErrorCode.INVALID_CREDENTIALS,
            detail=detail
        )


class TokenExpiredException(CustomException):
    """令牌过期异常"""
    
    def __init__(self, detail: str = "认证令牌已过期"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code=ErrorCode.TOKEN_EXPIRED,
            detail=detail
        )


class PermissionDeniedException(CustomException):
    """权限不足异常"""
    
    def __init__(self, detail: str = "权限不足"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            error_code=ErrorCode.PERMISSION_DENIED,
            detail=detail
        )