<template>
  <el-dialog
    v-model="visible"
    :title="dialogTitle"
    width="500px"
    :before-close="handleClose"
  >
    <el-form
      :model="form"
      :rules="rules"
      ref="formRef"
      label-width="80px"
    >
      <el-form-item label="用户名" prop="username">
        <el-input
          v-model="form.username"
          :disabled="!!user"
          placeholder="请输入用户名"
        />
      </el-form-item>
      
      <el-form-item label="邮箱" prop="email">
        <el-input
          v-model="form.email"
          placeholder="请输入邮箱"
        />
      </el-form-item>
      
      <el-form-item label="姓名" prop="full_name">
        <el-input
          v-model="form.full_name"
          placeholder="请输入姓名"
        />
      </el-form-item>
      
      <el-form-item label="密码" prop="password" v-if="!user">
        <el-input
          v-model="form.password"
          type="password"
          placeholder="请输入密码"
          show-password
        />
      </el-form-item>
      
      <el-form-item label="状态" prop="is_active">
        <el-switch
          v-model="form.is_active"
          active-text="启用"
          inactive-text="禁用"
        />
      </el-form-item>
      
      <el-form-item label="角色" prop="is_superuser">
        <el-switch
          v-model="form.is_superuser"
          active-text="管理员"
          inactive-text="普通用户"
        />
      </el-form-item>
    </el-form>
    
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleClose">取消</el-button>
        <el-button type="primary" @click="handleSubmit" :loading="loading">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref, reactive, computed, watch } from 'vue'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'
import { User, UserCreate, UserUpdate } from '@/types'

// Props
interface Props {
  modelValue: boolean
  user?: User | null
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: false,
  user: null
})

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: boolean]
  success: []
}>()

// 数据
const visible = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const formRef = ref<FormInstance>()
const loading = ref(false)

const form = reactive({
  username: '',
  email: '',
  full_name: '',
  password: '',
  is_active: true,
  is_superuser: false
})

// 计算属性
const dialogTitle = computed(() => 
  props.user ? '编辑用户' : '新增用户'
)

// 验证规则
const rules: FormRules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 50, message: '用户名长度在3-50个字符', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
  ],
  password: [
    { required: !props.user, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度至少6位', trigger: 'blur' }
  ]
}

// 监听器
watch(visible, (newVal) => {
  if (newVal) {
    resetForm()
    if (props.user) {
      Object.assign(form, {
        username: props.user.username,
        email: props.user.email,
        full_name: props.user.full_name || '',
        password: '',
        is_active: props.user.is_active,
        is_superuser: props.user.is_superuser
      })
    }
  }
})

// 方法
const resetForm = () => {
  Object.assign(form, {
    username: '',
    email: '',
    full_name: '',
    password: '',
    is_active: true,
    is_superuser: false
  })
  
  if (formRef.value) {
    formRef.value.clearValidate()
  }
}

const handleClose = () => {
  visible.value = false
}

const handleSubmit = async () => {
  if (!formRef.value) return
  
  const valid = await formRef.value.validate()
  if (!valid) return
  
  loading.value = true
  
  try {
    // 模拟API调用
    await new Promise(resolve => setTimeout(resolve, 500))
    
    ElMessage.success(props.user ? '用户更新成功' : '用户创建成功')
    emit('success')
    handleClose()
  } catch (error) {
    ElMessage.error(props.user ? '用户更新失败' : '用户创建失败')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>