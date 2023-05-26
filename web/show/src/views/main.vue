<template>
    <div class="recommend">
        <!-- 背景 -->
        <img :src="homeData.background" alt="" class="cover">
        <div class="search">
            <el-input v-model="input" placeholder="请输入电影名" >
                <template #prefix>
                    <i-ep-Search @click="search"></i-ep-Search>
                  </template>
            </el-input>
        </div>
        <div class="main">
            <div class="left">
                <img :src="homeData.cover" alt="">
            </div>
            <div class="right">
                <div class="title">{{homeData.title}}</div>
                <div class="info">{{`${homeData.release_date}  ${homeData.types}  ${homeData.runtime}`}}</div>
                <div class="grade">
                    用户评分
                    <el-progress :percentage="homeData.grade" color="#13CE66" />
                </div>
                <div class="line">
                    {{homeData.line }}
                </div>
                <div class="introduce">
                    {{homeData.introduction}}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import {reactive,ref,onMounted} from 'vue'
import { reqhome,reqSearch } from '../api';
// 推荐电影
const homeData:any = reactive({})
const main = ref()
const input = ref<string>('')
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
        localStorage.setItem('homeData',JSON.stringify({home:data.data,day:new Date().getDate()}))
    
    }
}
// 搜索电影
const search = async()=>{
    const {data} = await reqSearch(input.value)
    if(data.code == 200){
        Object.assign(homeData,data.data)
    }
}
onMounted(()=>{
    reqHome()
})
</script>

<style lang="scss" scoped>
    .recommend {
        position: relative;
        padding: 10px;
        color:#fff;
        .cover {
            width:100%;
            filter: blur(1rem);
            position: fixed;
            left: 0;
            top:0;
            z-index: -2;
        }
        .search {
            width: 400px;
            margin-left: 700px;
            margin-top: 100px;
        }
        .main {
            margin-top: 100px;
            display: flex;
            .left {
                padding: 20px;
                width:20%;
                img{
                    width:100%;
                }
            }
            .right {
                width:80%;
                padding-left: 40px;
                display: flex;
                flex-direction: column;
                .title {
                    font-size: 50px;
                }
                .info {
                    margin-top: 20px;
                    font-size: 14px;
                }
                .grade{
                    margin-top: 20px;
                    width: 400px;
                }
                .line {
                    margin-top: 20px;
                    font-size: 20px;
                    font-style: italic;
                    color:#2e2d2d;
                }
                .introduce {
                    margin-top:40px;
                    width: 800px;
                    
                }

            }
        }
    }
</style>