// 用户相关类型
export interface User {
  id: number
  username: string
  email: string
  full_name?: string
  is_active: boolean
  is_superuser: boolean
  created_at: string
  updated_at: string
}

export interface UserCreate {
  username: string
  email: string
  password: string
  full_name?: string
  is_active?: boolean
  is_superuser?: boolean
}

export interface UserUpdate {
  email?: string
  full_name?: string
  is_active?: boolean
  is_superuser?: boolean
}

// 认证相关类型
export interface LoginRequest {
  username: string
  password: string
}

export interface Token {
  access_token: string
  token_type: string
}

// 分页响应类型
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
  pages: number
}

// API响应类型
export interface ApiResponse<T = any> {
  success: boolean
  data?: T
  error_code?: number
  detail?: string
}

// 用户列表响应
export type UserListResponse = PaginatedResponse<User>

// 路由元信息
export interface RouteMeta {
  title: string
  requiresAuth?: boolean
  roles?: string[]
}