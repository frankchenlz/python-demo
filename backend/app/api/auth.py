from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.database import get_db
from app.core.security import create_access_token, authenticate_user
from app.core.config import settings
from app.schemas.user import Token, LoginRequest
from app.utils.exceptions import InvalidCredentialsException
from app.utils.logger import logger

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """用户登录"""
    logger.info(f"用户登录尝试: {form_data.username}")
    
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        logger.warning(f"登录失败: {form_data.username}")
        raise InvalidCredentialsException()
    
    # 创建访问令牌
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    logger.info(f"用户登录成功: {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login-json", response_model=Token)
def login_json(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """用户登录（JSON格式）"""
    logger.info(f"用户登录尝试(JSON): {login_data.username}")
    
    user = authenticate_user(db, login_data.username, login_data.password)
    if not user:
        logger.warning(f"登录失败(JSON): {login_data.username}")
        raise InvalidCredentialsException()
    
    # 创建访问令牌
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    logger.info(f"用户登录成功(JSON): {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}