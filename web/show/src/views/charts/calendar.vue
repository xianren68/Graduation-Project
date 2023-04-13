<template>
    <div class="main">
        <div class="show">
            <div class="chart" ref="chart"></div>
            <div class="handoff">
                    <el-button type="default" :disabled="leftDis" @click="jump(0)">
                        <el-icon><i-ep-ArrowLeft /></el-icon>
                        Previous Year</el-button>
                   <div class="input">
                    <el-input v-model="InputYear" placeholder="输入年份" @keyup.enter="getYearTop(InputYear)"/>
                   </div>
                    <el-button type="default" :disabled="rightDis" @click="jump(1)">Next Year
                        <el-icon><i-ep-ArrowRight /></el-icon>
                    </el-button>
            </div>
        </div>
        <div class="total">
            <el-table :data="CalendarYear.data" border style="width: 100%" height="100%">
                <el-table-column prop="year" label="年份" width="100" />
                <el-table-column prop="name" label="电影名" width="200" />
                <el-table-column prop="boxOffice" label="票房(万)" />
            </el-table>
        </div>
    </div>
</template>

<script setup lang="ts">
import { reqCalendar, } from '@/api';
import { reactive, ref, onMounted,watch } from 'vue'
import { CalendarInt } from '@/type/Show'
import { calendarBar } from '@/chart/bar.ts'
import * as echarts from 'echarts/core';
import {ElMessage} from 'element-plus'
import { fa, tr } from 'element-plus/es/locale';
import { messageConfig } from 'element-plus';
// 排行榜
const CalendarYear: { data: Array<CalendarInt> } = reactive({
    data: []
})
// 要绑定图像的组件
const chart = ref()
// 输入的年份
const InputYear = ref(2023)
// 左右按钮是否被禁用
const leftDis = ref(false)
const rightDis = ref(false)
// 对年份进行侦听
watch(InputYear,(newValue,oldValue)=>{
    if (!newValue || newValue > 2023 || newValue < 1994){
        leftDis.value = true
        rightDis.value = true
    }else if(newValue == 1994){
        leftDis.value = true
        rightDis.value = false
    }else if(newValue == 2023){
        leftDis.value = false
        rightDis.value = true
    }else {
        leftDis.value = false
        rightDis.value = false
    }
},{
    immediate:true
})
// 用于切换年份的方法
const jump = (flag:number)=>{
    // 前一年
    if(flag===0){
        getYearTop(--InputYear.value)
    }else {
        getYearTop(++InputYear.value)
    }
}
// 处理数据的方法
// 定义返回值类型
type resData = {
    nameData: Array<string>,
    boxData: Array<number>
}
const transFormate = (data: Array<CalendarInt>): resData => {
    let res: resData = {
        nameData: [],
        boxData: []
    }
    // 取前十/总数
    let len = data.length >= 10 ? 10 : data.length
    for (let i = 0; i < len; i++) {
        res.nameData.push(data[i].name)
        res.boxData.push(data[i].boxOffice)
    }

    return res
}
// 获取历年排行榜数据并挂载
const getYearTop = async (year: number) => {
    let { data } = await reqCalendar(year)
    if (data.code == 200) {
        CalendarYear.data = data.data
        // 挂载到页面
        let res = transFormate(data.data)
        let option = calendarBar(year, res.nameData, res.boxData)
        let mychart = echarts.init(chart.value)
        option && mychart.setOption(option)
    }
    
}
// 生命周期中默认挂载2023年
onMounted(() => {
    getYearTop(2023)
})

</script>

<style scoped lang="scss">
.main {
    height: 100%;
    display: flex;

    .show {
        width: 70%;
        height: 100%;
        display: flex;
        flex-direction: column;

        .chart {
            height: 90%;
            width: 100%;
        }

        .handoff {
            display: flex;
            justify-content: center;
            align-items: center;
            .input {
                width: 10%;
            }
        }
    }

    .total {
        width: 30%;
    }
}</style>