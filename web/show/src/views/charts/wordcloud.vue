<template>
    <div class="charts">
        <div class="search">
            <div class="input">
                <el-input  class="w-50 m-2" size="large" placeholder="请输入想知道的电影" 
                v-model="inValue" >
                    <template #suffix>
                        <i-ep-Search @click="getUrl"></i-ep-Search>
                    </template>
                </el-input>
            </div>
            <div class="img">
                <div ref="pre" class="pre">
                </div>
                <img :src="imgUrl" alt="">
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import {ref,reactive} from 'vue'
import {reqCiyun} from '@/api'
import {precentInt} from '@/type/show'
import {ElMessage} from 'element-plus'
import * as echarts from 'echarts/core';
import {setPrecent} from '@/chart/bar'
// 绑定输入数据
const inValue = ref('')
// 词云地址
const imgUrl = ref('')
// 电影的评论数据
const precent:precentInt = reactive({
    title:'',
    favourable:undefined,
    differ:undefined,
    general:undefined
})
const pre = ref()
// 获取词云地址
const getUrl = async ()=>{
    imgUrl.value = '/src/assets/加载.png'
    const {data} = await reqCiyun(inValue.value)
    if(data.code==200){
        imgUrl.value = "http://127.0.0.1:5000"+data.path
        Object.assign(precent,data.precent)
        let option = setPrecent([precent.title],[precent.favourable],[precent.differ])
        let mychart = echarts.init(pre.value)
        option && mychart.setOption(option)
        
    }else{
        ElMessage.error(data.msg)
    }
}


</script>

<style lang="scss" scoped>
.charts {
    height: 100%;
    .search {
        position: absolute;
        top: 20%;
        left:20%;
        right: 20%;
        .img {
            width: 100%;
            .pre {
                height: 100px;
                width: 100%;
                
            }
            img {
                width: 100%;
            }
        }
    }
}
</style>