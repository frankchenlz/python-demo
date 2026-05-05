from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.core.security import verify_token
from app.schemas.user import UserCreate, UserUpdate, UserResponse, UserListResponse
from app.services.user import UserService
from app.utils.exceptions import UserNotFoundException, InvalidCredentialsException
from app.utils.logger import logger

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=UserListResponse)
def get_users(
    page: int = Query(1, ge=1, description="页码"),
    size: int = Query(10, ge=1, le=100, description="每页大小"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    db: Session = Depends(get_db),
    token_data: dict = Depends(verify_token)
):
    """获取用户列表"""
    logger.info(f"获取用户列表 - 页码: {page}, 大小: {size}, 搜索: {search}")
    
    skip = (page - 1) * size
    users = UserService.get_users(db, skip=skip, limit=size, search=search)
    total = UserService.get_users_count(db, search=search)
    pages = (total + size - 1) // size
    
    return UserListResponse(
        items=users,
        total=total,
        page=page,
        size=size,
        pages=pages
    )


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    token_data: dict = Depends(verify_token)
):
    """根据ID获取用户"""
    logger.info(f"获取用户ID: {user_id}")
    
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise UserNotFoundException()
    
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    token_data: dict = Depends(verify_token)
):
    """创建用户"""
    logger.info(f"创建用户: {user_data.username}")
    
    try:
        user = UserService.create_user(db, user_data)
        return user
    except Exception as e:
        logger.error(f"创建用户失败: {str(e)}")
        raise


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    token_data: dict = Depends(verify_token)
):
    """更新用户信息"""
    logger.info(f"更新用户ID: {user_id}")
    
    try:
        user = UserService.update_user(db, user_id, user_data)
        return user
    except Exception as e:
        logger.error(f"更新用户失败: {str(e)}")
        raise


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    token_data: dict = Depends(verify_token)
):
    """删除用户"""
    logger.info(f"删除用户ID: {user_id}")
    
    try:
        success = UserService.delete_user(db, user_id)
        return {"message": "用户删除成功"}
    except Exception as e:
        logger.error(f"删除用户失败: {str(e)}")
        raise