from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from app.utils.exceptions import UserNotFoundException, UserAlreadyExistsException
from app.utils.logger import logger


class UserService:
    """用户服务类"""
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """根据ID获取用户"""
        logger.info(f"查询用户ID: {user_id}")
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """根据用户名获取用户"""
        logger.info(f"查询用户名: {username}")
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_users(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        search: Optional[str] = None
    ) -> List[User]:
        """获取用户列表（支持搜索）"""
        logger.info(f"查询用户列表 - 跳过: {skip}, 限制: {limit}, 搜索: {search}")
        
        query = db.query(User)
        
        if search:
            query = query.filter(
                or_(
                    User.username.ilike(f"%{search}%"),
                    User.email.ilike(f"%{search}%"),
                    User.full_name.ilike(f"%{search}%")
                )
            )
        
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def get_users_count(db: Session, search: Optional[str] = None) -> int:
        """获取用户总数"""
        query = db.query(User)
        
        if search:
            query = query.filter(
                or_(
                    User.username.ilike(f"%{search}%"),
                    User.email.ilike(f"%{search}%"),
                    User.full_name.ilike(f"%{search}%")
                )
            )
        
        return query.count()
    
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        """创建用户"""
        logger.info(f"创建用户: {user_data.username}")
        
        # 检查用户名是否已存在
        existing_user = UserService.get_user_by_username(db, user_data.username)
        if existing_user:
            raise UserAlreadyExistsException(f"用户名 {user_data.username} 已存在")
        
        # 检查邮箱是否已存在
        existing_email = db.query(User).filter(User.email == user_data.email).first()
        if existing_email:
            raise UserAlreadyExistsException(f"邮箱 {user_data.email} 已存在")
        
        # 创建用户
        hashed_password = get_password_hash(user_data.password)
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            full_name=user_data.full_name,
            is_active=user_data.is_active,
            is_superuser=user_data.is_superuser
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        logger.info(f"用户创建成功: {db_user.username}")
        return db_user
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserUpdate) -> User:
        """更新用户信息"""
        logger.info(f"更新用户ID: {user_id}")
        
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            raise UserNotFoundException(f"用户ID {user_id} 不存在")
        
        # 更新字段
        update_data = user_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.commit()
        db.refresh(db_user)
        
        logger.info(f"用户更新成功: {db_user.username}")
        return db_user
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """删除用户（软删除）"""
        logger.info(f"删除用户ID: {user_id}")
        
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            raise UserNotFoundException(f"用户ID {user_id} 不存在")
        
        # 软删除：设置用户为不活跃状态
        db_user.is_active = False
        db.commit()
        
        logger.info(f"用户删除成功: {db_user.username}")
        return True
    
    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
        """用户认证"""
        logger.info(f"用户认证: {username}")
        
        user = UserService.get_user_by_username(db, username)
        if not user:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None
        
        if not user.is_active:
            return None
        
        logger.info(f"用户认证成功: {username}")
        return user