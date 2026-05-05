import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { User } from '@/types'

export const useUserStore = defineStore('user', () => {
  // 状态
  const token = ref<string>('')
  const userInfo = ref<User | null>(null)
  
  // 计算属性
  const isLoggedIn = computed(() => !!token.value)
  const isSuperuser = computed(() => userInfo.value?.is_superuser || false)
  
  // 动作
  const setToken = (newToken: string) => {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }
  
  const setUserInfo = (info: User) => {
    userInfo.value = info
    localStorage.setItem('userInfo', JSON.stringify(info))
  }
  
  const login = async (username: string, password: string) => {
    // 这里会在API服务中实现
    return true
  }
  
  const logout = () => {
    token.value = ''
    userInfo.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('userInfo')
  }
  
  const initFromStorage = () => {
    const storedToken = localStorage.getItem('token')
    const storedUserInfo = localStorage.getItem('userInfo')
    
    if (storedToken) {
      token.value = storedToken
    }
    
    if (storedUserInfo) {
      userInfo.value = JSON.parse(storedUserInfo)
    }
  }
  
  return {
    token,
    userInfo,
    isLoggedIn,
    isSuperuser,
    setToken,
    setUserInfo,
    login,
    logout,
    initFromStorage
  }
})