<template>
    <div class="login">
        <div class="box-card">
                <div class="card-header">
                    <el-avatar :size="60" src="" >
                        <img src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png" />
                    </el-avatar>
                </div>
            <el-form label-position="left" label-width="60px" :rules="rules" :model="userInfo" ref="formRef">
                <el-form-item label="用户名" prop="name">
                    <el-input v-model="userInfo.name">
                        <template #prefix>
                            <i-ep-User></i-ep-User>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input type="password" v-model="userInfo.password">
                        <template #prefix>
                            <i-ep-Lock></i-ep-Lock>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary"  @click="submitForm">登录</el-button>
                </el-form-item>
            </el-form>
            <div class="bottom">
                <span>还未</span>
            <router-link to="/register">注册</router-link>
            <span>?</span>
            </div>
            </div>
    </div>
</template>

<script setup lang="ts">
import {checkName,checkPassword} from '@/utils/rules'
import {ElMessage} from 'element-plus'
import type { FormRules,FormInstance} from 'element-plus'
import {user} from '@/types/User'
import {ref,reactive} from 'vue'
import {reqLogin} from '@/api'
import { useRouter } from 'vue-router'
const router = useRouter()
// 表单对象
const formRef = ref<FormInstance>()
// 表单验证
const rules = reactive<FormRules>({
    name: [
        { validator: checkName, trigger: 'blur' }
    ],
    password: [
        { validator: checkPassword, trigger: 'blur' }
    ],
})
// 表单数据
const userInfo = reactive<user>({
    name:'',
    password:''
})
// 发送登录请求
const login = async ()=>{
    const {data} = await reqLogin(userInfo)
    if (data.code == 200 ){
        ElMessage.success("登录成功")
        router.push('/')
    }else {
        ElMessage.error(data.msg)
    }
}
// 提交
const submitForm = ()=>{
    if (! formRef.value) return
    formRef.value.validate((valid)=>{
        if (!valid){
            ElMessage({
                message:"输入不合法",
                type:'error'
            })
        }else {
            login()
            return false
        }
    })
}
</script>

<style lang="scss" scoped>
.login {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: linear-gradient(to right,#ead6ee,#a0f1ea);
    @media  screen and (min-width:960px) {
        .box-card {
            width: 250px;
        }
    }
    @media screen and (max-width:960px) {
        .box-card {
            width: 180px;
        }
    }
    .box-card {
        box-shadow: 0 0 60px #000 ;
        padding-top:30px;
        padding-bottom: 10px;
        padding-left: 50px;
        padding-right: 50px;

        .card-header {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 40px;
        }
        .bottom {
            height: 20px;
            margin-top: 20px;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
        }
    }
}
</style>