<template>
    <div class="type">
        <div ref="pie" class="pie"></div>
        <div ref="line" class="line"></div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, reactive } from 'vue'
import * as echarts from 'echarts/core'
import { reqTypes } from '@/api'
import { proportionInt } from '@/type/Show.ts'
import { setTyesPie, formatPieData, pieData } from '@/chart/pie'
import { setTypeline, formatLine } from '@/chart/line'
// 后端返回的数据
const typePro: proportionInt = reactive({})
// 绑定占比的组件
const pie = ref()
// 绑定折线图的组件
const line = ref()
// 获取数据
const bindTypes = async () => {
    const { data } = await reqTypes()
    if (data.code == 200) {
        Object.assign(typePro, data.types)
        bindPie()
        bindLine()
    }
}
// 绑定饼图
const bindPie = () => {
    let opt = formatPieData(typePro)
    // 排序
    opt = opt.sort((a: pieData, b: pieData) => {
        return b.value - a.value
    })
    opt = opt.slice(0, 10)
    let option = setTyesPie(opt)
    let mychart = echarts.init(pie.value)
    option && mychart.setOption(option)
}
// 绑定折线图
const bindLine = () => {
    let o = formatLine(typePro)
    let option = setTypeline(o.name,o.value)
    let mychart = echarts.init(line.value)
    option && mychart.setOption(option)
}
// 声明周期钩子中获取数据
onMounted(() => {
    bindTypes()
})
</script>

<style lang="scss" scoped>
@media screen and (min-width:960px){
    .type {
        height: 100%;
        flex-direction: row;
        display: flex;
    
        .pie {
            width: 50%;
            height: 100%;
        }
        .line {
            width: 50%;
            height: 100%;
        }
}
}
@media screen and (max-width:960px){
    .type {
        height: 100%;
        flex-direction: column;
        display: flex;
    
        .pie {
            width: 100%;
            height: 50%;
        }
        .line {
            width: 100%;
            height: 50%;
        }
    }
}

</style>