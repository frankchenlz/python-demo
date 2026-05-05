<template>
  <div class="user-list-container">
    <div class="header">
      <h2>用户管理</h2>
      <el-button type="primary" @click="handleCreate">
        <el-icon><Plus /></el-icon>
        新增用户
      </el-button>
    </div>
    
    <div class="toolbar">
      <el-input
        v-model="searchKeyword"
        placeholder="搜索用户名、邮箱或姓名"
        style="width: 300px"
        clearable
        @clear="handleSearch"
        @keyup.enter="handleSearch"
      >
        <template #append>
          <el-button @click="handleSearch">
            <el-icon><Search /></el-icon>
          </el-button>
        </template>
      </el-input>
      
      <el-button @click="handleRefresh">
        <el-icon><Refresh /></el-icon>
        刷新
      </el-button>
    </div>
    
    <el-table
      :data="userList"
      v-loading="loading"
      style="width: 100%"
      border
    >
      <el-table-column prop="id" label="ID" width="80" />
      <el-table-column prop="username" label="用户名" />
      <el-table-column prop="email" label="邮箱" />
      <el-table-column prop="full_name" label="姓名" />
      <el-table-column prop="is_active" label="状态" width="100">
        <template #default="{ row }">
          <el-tag :type="row.is_active ? 'success' : 'danger'">
            {{ row.is_active ? '启用' : '禁用' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="is_superuser" label="角色" width="100">
        <template #default="{ row }">
          <el-tag :type="row.is_superuser ? 'warning' : 'info'">
            {{ row.is_superuser ? '管理员' : '用户' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="created_at" label="创建时间" width="180">
        <template #default="{ row }">
          {{ formatDate(row.created_at) }}
        </template>
      </el-table-column>
      <el-table-column label="操作" width="200" fixed="right">
        <template #default="{ row }">
          <el-button size="small" @click="handleEdit(row)">编辑</el-button>
          <el-button 
            size="small" 
            type="danger" 
            @click="handleDelete(row)"
            :disabled="row.id === currentUser?.id"
          >
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    
    <div class="pagination">
      <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="pageSize"
        :page-sizes="[10, 20, 50, 100]"
        :total="total"
        layout="total, sizes, prev, pager, next, jumper"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>
    
    <!-- 用户编辑对话框 -->
    <user-edit-dialog
      v-model="editDialogVisible"
      :user="editingUser"
      @success="handleDialogSuccess"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useUserStore } from '@/store/user'
import { User } from '@/types'
import UserEditDialog from '@/components/UserEditDialog.vue'

const userStore = useUserStore()

// 数据
const userList = ref<User[]>([])
const loading = ref(false)
const searchKeyword = ref('')
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)

// 对话框
const editDialogVisible = ref(false)
const editingUser = ref<User | null>(null)

// 计算属性
const currentUser = computed(() => userStore.userInfo)

// 生命周期
onMounted(() => {
  loadUserList()
})

// 方法
const loadUserList = async () => {
  loading.value = true
  
  try {
    // 模拟API调用
    await new Promise(resolve => setTimeout(resolve, 500))
    
    // 模拟数据
    userList.value = [
      {
        id: 1,
        username: 'admin',
        email: 'admin@example.com',
        full_name: '系统管理员',
        is_active: true,
        is_superuser: true,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      },
      {
        id: 2,
        username: 'user1',
        email: 'user1@example.com',
        full_name: '普通用户',
        is_active: true,
        is_superuser: false,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      }
    ]
    
    total.value = userList.value.length
  } catch (error) {
    ElMessage.error('加载用户列表失败')
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  currentPage.value = 1
  loadUserList()
}

const handleRefresh = () => {
  loadUserList()
}

const handleCreate = () => {
  editingUser.value = null
  editDialogVisible.value = true
}

const handleEdit = (user: User) => {
  editingUser.value = { ...user }
  editDialogVisible.value = true
}

const handleDelete = async (user: User) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除用户 "${user.username}" 吗？此操作不可恢复。`,
      '确认删除',
      {
        type: 'warning',
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }
    )
    
    // 模拟删除操作
    await new Promise(resolve => setTimeout(resolve, 500))
    
    ElMessage.success('用户删除成功')
    loadUserList()
  } catch {
    // 用户取消删除
  }
}

const handleDialogSuccess = () => {
  editDialogVisible.value = false
  loadUserList()
}

const handleSizeChange = (size: number) => {
  pageSize.value = size
  currentPage.value = 1
  loadUserList()
}

const handleCurrentChange = (page: number) => {
  currentPage.value = page
  loadUserList()
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('zh-CN')
}
</script>

<style scoped>
.user-list-container {
  padding: 20px;
  background: white;
  border-radius: 8px;
  min-height: calc(100vh - 40px);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.toolbar {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>