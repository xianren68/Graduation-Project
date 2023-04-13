<template>
    <div ref="chart" class="chart">

    </div>
</template>

<script setup lang="ts">
import {reactive,ref,onMounted} from 'vue'
import {boxTopInt} from '@/type/Show'
import {setBoxchart} from '@/chart/bar'
import { Color } from '@/chart/pub'
import { reqBoxoffice } from '@/api';
// import {} from 'echarts/charts'
import * as echarts from 'echarts/core';
const boxTop:{
    list:Array<boxTopInt>
} = reactive({
    list :[]
})
// 展示的区域
const chart = ref()
// 接收后端返回的数据
// 获取数据的方法
const getboxTop = async ()=>{
    const {data} = await reqBoxoffice()
    if (data.code == 200){
        boxTop.list = data.list
        const {boxData,nameData} = formatData(boxTop.list)
        let option = setBoxchart(boxData,nameData)
        let mychart = echarts.init(chart.value)
        option && mychart.setOption(option)
    }
    
}
// 转换数据的方法
const formatData = (list :Array<boxTopInt>):{boxData:Array<any>,nameData:Array<string>}=>{
    // 横轴数据
    let boxData:Array<any> = []
    // 纵轴数据
    let nameData:Array<string> = []
    let j = 0
    for(let i of list){
        let name:string = i.name
        nameData.push(name)   
        let str:string = i.boxoffice
        str = str.replaceAll(',','')
        let value = Number(str)
        let box = {
            value,
            itemStyle:{
                color:Color(j%10)
            }

        }
        boxData.push(box)
        j++
    }   
    
    return {boxData:boxData,nameData:nameData}
}
// 获取数据
onMounted(() => {
    getboxTop()
})
</script>

<style lang="scss" scoped>
    .chart{
        height: 100%;
    }
</style>