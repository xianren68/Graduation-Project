import * as echarts from 'echarts/core';
import { GridComponent, GridComponentOption } from 'echarts/components';
import { LineChart, LineSeriesOption } from 'echarts/charts';
import { UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';
import {proportionInt} from '../type/Show'

echarts.use([GridComponent, LineChart, CanvasRenderer, UniversalTransition]);

type EChartsOption = echarts.ComposeOption<
  GridComponentOption | LineSeriesOption
>;

export const setTypeline = (name:Array<string>,value:Array<number>):EChartsOption=>{
    let option:EChartsOption = {
        xAxis: {
          type: 'category',
          data: name,
          axisLabel:{
            interval:0,
            rotate:-40
          }
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name:"类型个数",
            data: value,
            type: 'line'
          }
        ]
      }
      return option
}
export const formatLine = (data:proportionInt):{name:Array<string>,value:Array<number>} =>{
    let res:{name:Array<string>,value:Array<number>} = {
      name:[],
      value:[]
    }
    res.name = [...Object.keys(data)]
    res.value = [...Object.values(data)]
    return res
   
}
export const setCountryLine = (name:Array<string>,data:Array<number>,country:string):EChartsOption=>{
  let option:EChartsOption = {
    title: {
      text: `${country}出品电影数量随年份变化图`,
      left: 'center',
      top:'10',
    },
    xAxis: {
      type: 'category',
      data: name,
      axisLabel:{
        interval:0,
        rotate:-38
      }
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: data,
        type: 'line'
      }
    ]
  }
  return option
}

