<template>
    <div class="my">
        <div class="card">
            <div class="main">
                <div class="profile"><img src="@/assets/images.png" alt=""></div>
                <div class="edit">
                    <span>用户名：xianren</span>
                </div>
            </div>
            <div class="press">
                <div>权限：</div>
                <div>管理员</div>
            </div>
            <div class="quit">
                <el-button type="primary">编辑</el-button>
                 <el-button type="info" >退出</el-button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import {ref,reactive,onMounted} from 'vue'
import { reqRecommend } from '@/api';
import {useRouter} from 'vue-router'
const line = ref('')
const from = ref('')
const router = useRouter()
// 获取异步的数据
const getRec = async ()=>{
    let lines = localStorage.getItem('line')
    let res
    lines && (res=JSON.parse(lines))
    if(lines && res.time !== new Date().getDate()){
        line.value = res.line
        from.value = res.from
        return 
    }
    const {data} = await reqRecommend()
    if(data.code === 200){
        console.log(data)
        line.value = data.line.split('。')[0]
        from.value = data.line.split('。')[1]
        // 将数据保存
        localStorage.setItem('line',JSON.stringify({
            line:line.value,
            from:from.value,
            time:new Date().getDate
        }))

    }
}
// 生命周期钩子中获取数据
onMounted(() => {
    getRec()
})
</script>

<style lang="scss" scoped>
.my {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    .card {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 300px;
        height: 500px;
        border-radius: 5% 5% 0 0;
        box-shadow: 0 0 10px #000;

        .main {
            padding: 40px 20px 0 20px;
            text-align: center;
            margin-bottom: 40px;
            .profile {
                height: 150px;
                width: 150px;
                margin-bottom: 10px;
                border-radius: 50%;
                background: #ccc;
                overflow: hidden;
                img {
                    height: 100%;
                }
            }
            .edit {
                height: 20px;
                line-height: 20px;
                display: flex;
                justify-content: space-evenly;
                .icon {
                    width:10px;
                    height: 10px;
                }
            }
        }

       .press {
        display:  flex;
        justify-content: space-evenly;
       }
        .quit {
           margin-top: 100px;
        }

    } 
    
   
}

</style>
