from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import User

# 密码加密上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 错误码定义
class ErrorCode:
    # 系统错误 (1000-1999)
    SYSTEM_ERROR = 1001
    DATABASE_ERROR = 1002
    CONFIG_ERROR = 1003
    
    # 业务错误 (2000-2999)
    USER_NOT_FOUND = 2001
    USER_ALREADY_EXISTS = 2002
    INVALID_USER_DATA = 2003
    USER_INACTIVE = 2004
    
    # 认证错误 (3000-3999)
    INVALID_CREDENTIALS = 3001
    TOKEN_EXPIRED = 3002
    TOKEN_INVALID = 3003
    PERMISSION_DENIED = 3004


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """创建JWT令牌"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    """验证JWT令牌"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的认证令牌",
            headers={"WWW-Authenticate": "Bearer"},
        )


def authenticate_user(db: Session, username: str, password: str):
    """验证用户凭据"""
    # 根据用户名查找用户
    user = db.query(User).filter(User.username == username).first()
    
    # 如果用户不存在或密码不匹配
    if not user or not verify_password(password, user.hashed_password):
        return None
    
    # 如果用户被禁用
    if not user.is_active:
        return None
    
    return user