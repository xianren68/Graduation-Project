<template>
    <div class="main">
        
        <div class="left">
            <div class="bar" ref="bar"></div>
            <div class="line" ref="line"></div>
        </div>
        <div class="right">
            <div class="pie" ref="pie"></div>
            <div class="bottom">
                <el-select v-model="country" class="m-2" placeholder="Select" size="small" >
                    <el-option
                      v-for="item in optionsC"
                      :key="item.value"
                      :label="item.value"
                      :value="item.value"
                    />
                  </el-select>
                <el-select v-model="year" class="m-2" placeholder="Select" size="small" >
                    <el-option
                      v-for="item in optionsY"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                    />
                  </el-select>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref,watch } from 'vue'
import { reqCountry } from '../../api'
import { CountryInt } from '../../type/Show'
import { countryCount } from '@/chart/bar'
import { setCountry, pieData } from '@/chart/pie'
import { setCountryLine } from '@/chart/line'
import * as echarts from 'echarts/core'

// 总数据
const totalData: CountryInt = reactive({})
// 挂载柱形图的区域
const bar = ref()
// 挂载饼图的区域
const pie = ref()
// 挂载折线图的地方
const line = ref()
// 选择器年份数据
const year = ref(2010)
// 选择年份配置数据
const optionsY = function(){
    let res = []
    for(let i = 1900;i<=2020;i+=10){
        let d:{value:number,label:string} = {value:i,label:`${i} ~ ${i+10}`}
        res.push(d)
    }
    return res
}()
// 监听年份变化
watch(year,()=>{
    barmount()
    piemount()
})
// 选择器国家数据
const country = ref('中国大陆')
// 选择国家配置数据
const optionsC = [
    {value:'中国大陆'},
    {value:'美国'},
    {value:'中国台湾'},
    {value:'中国香港'},
    {value:'英国'},
    {value:'日本'},
    {value:'印度'},
    {value:'法国'},
    {value:'德国'}
]
// 监听年份变化
watch(country,()=>{
    linemount()
})
// 格式化bar数据并挂载
const barmount = () => {
    let data = totalData[year.value]
    let nameArr = Object.keys(data)
    nameArr.sort((a: string, b: string): number =>
        data[a] - data[b]
    )
    let dataArr: Array<number> = []
    for (let i of nameArr) {
        dataArr.push(data[i])
    }

    let option = countryCount(nameArr, dataArr,year.value)
    let mychart = echarts.init(bar.value)
    option && mychart.setOption(option)

}
// 格式化pie数据并挂载
const piemount = () => {
    let data: Array<pieData> = []
    let range = totalData[year.value]
    for (let i in range) {
        let res: pieData = {}
        res.value = range[i]
        res.name = i
        data.push(res)
    }
    data.sort((a: pieData, b: pieData): number => a.value - b.value)
    let title = data.map(item => item.name)
    let option = setCountry(data, title,year.value)
    let mychart = echarts.init(pie.value)
    option && mychart.setOption(option)
}
// 格式化line数据并挂载
const linemount = () => {
    let nameArr = []
    let dataArr = []
    for(let i = 1900;i<=2020;i+=10){
        nameArr.push(`${i}~${i+10}`)
        if (totalData[i]) {
            if (totalData[i][country.value]){
                dataArr.push(totalData[i][country.value])
            }else {
                dataArr.push(0)
            }
        }else {
            dataArr.push(0)
        }
    }
    let option = setCountryLine(nameArr, dataArr,country.value)
    let mychart = echarts.init(line.value)
    option && mychart.setOption(option)
}
// 获取数据
const reqcountry = async () => {
    let { data } = await reqCountry()
    if (data.code == 200) {
        Object.assign(totalData, data.data)
        barmount()
        piemount()
        linemount()

    }
}

// 获取数据
onMounted(() => {
    reqcountry()
})
</script>

<style lang="scss" scoped>
.main {
    height: 100%;
    display: flex;

    .left {
        width: 60%;
        display: flex;
        flex-direction: column;
        .bar {
            height:60%;
            width:100%;
        }
        .line{
            height: 40%;
            width: 100%;
        }
    }
    .right{
        height:100%;
        width:40%;
        .pie {
            height: 90%;
        }
    }
}
</style>