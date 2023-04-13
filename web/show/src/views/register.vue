<template>
    <div class="register">
        <div class="box-card">
            <el-form label-position="left" label-width="80px" :model="formInfo" :rules="rules"
            ref="formRef">
                <el-form-item label="用户名" prop="name">
                    <el-input v-model="formInfo.name">
                        <template #prefix>
                            <i-ep-User></i-ep-User>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input type="password" v-model="formInfo.password">
                        <template #prefix>
                            <i-ep-Lock></i-ep-Lock>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="repassword">
                    <el-input type="password" v-model="formInfo.repassword">
                        <template #prefix>
                            <i-ep-Lock></i-ep-Lock>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item label-width="0" size="default">
                    <div class="upload">
                            <input type="file" ref="prefile" id="file" size="1" @change="getPath">
                            <div class="myUp">
                                <button>上传头像</button> 
                            &nbsp;
                            <span>{{filepath}}</span>
                            </div>
                    </div>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm">注册</el-button>
                </el-form-item>
            </el-form>
            <div class="bottom">
                <span>已有账号</span>
                <router-link to="/login">登录</router-link>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { genFileId,ElMessage} from 'element-plus'
import type { FormRules,FormInstance} from 'element-plus'
import { checkName, checkPassword } from '@/utils/rules'
import { reqRegister } from '../api'
import {useRouter} from 'vue-router'
// 路由
const router = useRouter()
// form表单信息
const formInfo = reactive({
    name: '',
    password: '',
    repassword: ''
})
// 校验规则
const rules = reactive<FormRules>({
    name: [
        { validator: checkName, trigger: 'blur' }
    ],
    password: [
        { validator: checkPassword, trigger: 'blur' }
    ],
    repassword: [
        { validator: checkPassword, trigger: 'blur' }
    ]
})
// 表单对象
const formRef = ref<FormInstance>()
// 记录图片路径
const filepath = ref('')
const getPath = (e:any)=>{
    filepath.value = e.target.files[0].name   
}
// 提交对象
const prefile = ref()
// 提交验证
const submitForm = ()=>{
    if (! formRef.value) return
    formRef.value.validate((valid)=>{
        if (!valid){
            ElMessage({
                message:"输入不合法",
                type:'error'
            })
        }else if(formInfo.password !== formInfo.repassword) {
            ElMessage({
                message:"两次密码不一致",
                type:'error'
            })
        }else {
            submit()
            return false

        }
    })
}
// 提交注册请求
const submit = async ()=>{
    let Filedata = new FormData()
    Filedata.append('name',formInfo.name)
    Filedata.append('password',formInfo.password)
    Filedata.append('permissions','2')
    Filedata.append('file',prefile.value.files[0])
    const {data} = await reqRegister(Filedata)
    if (data.code == 200){
        ElMessage.success("注册成功")
        router.push('/login')
    }else {
        ElMessage.error(data.msg)
    }
    
    
}


</script>

<style lang="scss" scoped>
.register {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: linear-gradient(to right, #ead6ee, #a0f1ea);
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
        box-shadow: 0 0 60px #000;
        padding-top: 30px;
        padding-bottom: 10px;
        padding-left: 50px;
        padding-right: 50px;

        .bottom {
            height: 20px;
            margin-top: 20px;
            font-size: 14px;
            line-height: 20px;
            text-align: center;
        }

        .upload {
            position: relative;
            #file {    
                opacity: 0;
                z-index: 4;
            }
            input {
                position: absolute;
                top:3px;
                left: 0;
                z-index: 3;
            }
            .myUp {
                font-size: 12px;
            }
        }
    }
}</style>