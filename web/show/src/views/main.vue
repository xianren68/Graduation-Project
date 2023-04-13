<template>
    <div class="recommend">
        <div ref="main" class="main">
            <img :src="homeData[11]" alt="">
            <div class="content">
                <h2 class="title">{{homeData[1]}}</h2>
                <div class="type">{{homeData[2]}}·{{homeData[3]}}·{{homeData[7]}}</div>
                <div class="line">{{homeData[8]}}</div>
                <div class="desc">{{homeData[9]}}</div>
                <div></div>
            </div>
            <div class="aside">
                    <el-progress type="circle" :percentage="homeData[4]" status="success">
                    <template #default="{ percentage }">
                        <span class="percentage-value">{{ percentage }}%</span>
                        <br>
                        <span class="percentage-label">好评率</span>
                      </template>
                      </el-progress>
                <div>预算${{homeData[5]==0?homeData[5]:"-"}}</div>
                <div>票房${{homeData[6]==0?homeData[6]:"-"}}</div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import {reactive,ref,onMounted} from 'vue'
import { reqhome } from '../api';
// 推荐电影
const homeData = reactive([])
const main = ref()
// 获取本地存储数据
const getHomeData = ():boolean=>{
    let data = localStorage.getItem('homeData')
    if(data && new Date().getDate() == JSON.parse(data).day){
        Object.assign(homeData,JSON.parse(data).home)
        return true
    }
    return false
}
// 获取数据
const reqHome = async ()=>{
    // 已经有数据并且还未过一天
    if (getHomeData()){
        return
    }
    const {data} = await reqhome()
    if(data.code == 200){
        Object.assign(homeData,data.data)
        // 设置背景图片
        main.value.style.backgroundImage = "url("+ data.data[10] +")"
        localStorage.setItem('homeData',JSON.stringify({home:data.data,day:new Date().getDate()}))
    
    }
}
onMounted(()=>{
    reqHome()
})
</script>

<style lang="scss" scoped>
    .recommend{
        .main {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            height: 100%;
            background-size:cover;
            background-repeat:no-repeat;
            background-blend-mode: multiply;
            background-color: rgba(112, 103, 103, 0.6);
            background-attachment:fixed;
            color:#fff;
            padding: 20px;
            img {
                margin-top: 80px;
                height: 60%;
            }
            .content {
                padding: 40px;
                width:50%;
                .type {
                    margin:10px 0;
                }
                .line {
                    margin-top:60px;
                    height: 40px;
                    font-family: 楷体;
                }
                .desc {
                    height: 40%;
                    overflow:hidden;
                }
            }
            .aside {
                .score{
                    .demo-progress {
                        width: 200px;
                    }
                    line-height: 20px;
                }
                margin-top: 40px;
                width: 20%;
            }
        }
    }
</style>