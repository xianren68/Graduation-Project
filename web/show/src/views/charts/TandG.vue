<template>
    <div ref="chart" class="boxplot">
            
    </div>
</template>

<script setup lang="ts">
import {onMounted,ref} from 'vue'
import { reqTandG } from '../../api';
import {TandPInt} from '@/type/Show'
import {TandPEchart} from '@/chart/box'
import * as echarts from 'echarts/core'
// 需要挂载的地方
let chart = ref()
// 对数据进行处理的函数并挂载数据
const format = (data:TandPInt)=>{
    // 一个数组
    let arr:Array<Array<number>> = []
    // 另一个数组，用作标识
    let strArr:Array<string> = []
    for(let i in data){
        arr.push(data[i])
        strArr.push(i)
    }
    let option = TandPEchart(arr,strArr,'%','评分')
    let mychart = echarts.init(chart.value)
    option && mychart.setOption(option)
     
}
// 获取数据
const gettanp = async ()=>{
    let {data} =  await reqTandG()
    if (data.code == 200){
        format(data.data)
    }
}
onMounted(()=>{ 
    gettanp()
})
</script>

<style scoped lang="scss">
.boxplot {
    height:100%;
}
</style>