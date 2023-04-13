// 排行榜条形图
import * as echarts from 'echarts/core';
import {
  TitleComponent,
  TitleComponentOption,
  TooltipComponent,
  TooltipComponentOption,
  GridComponent,
  GridComponentOption,
  LegendComponent,
  LegendComponentOption
} from 'echarts/components';
import { BarChart, BarSeriesOption } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
import { DataZoomComponent } from 'echarts/components';

echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
  BarChart,
  CanvasRenderer,
  DataZoomComponent
]);

type EChartsOption = echarts.ComposeOption<
  | TitleComponentOption
  | TooltipComponentOption
  | GridComponentOption
  | LegendComponentOption
  | BarSeriesOption
>;
let option: EChartsOption;
export const setBoxchart = (nameData:Array<string>,boxData:Array<number>):EChartsOption=>{
    return option = {
        title: {
          text: '世界票房前百',
          left:'center',
          top:'10'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
          boundaryGap: [0, 0.01],
          axisLabel: {
            formatter: '{value} $'
          }
        },
        yAxis: {
          type: 'category',
          data: boxData.reverse(),
        },
        series: [
          {
            name: '票房数据',
            type: 'bar',
            data: nameData.reverse(),
            
          }
        ],
        dataZoom:[
            {
            type: 'slider',
            maxValueSpan:10,//显示数据的条数(默认显示10个)
            show: true,
            yAxisIndex: [0],
            left: '100%', //滑动条位置
            start:0,//默认为0
            end: 70,//默认为100
            orient:"vertical",
            filterMode: 'empty',
            zoomLock:true,
            },
            {
            type: 'inside', //内置滑动，随鼠标滚轮展示
            yAxisIndex: [0],
            start: 1,//初始化时，滑动条宽度开始标度
            end: 100, //初始化时，滑动条宽度结束标度
            zoomOnMouseWheel:false, //如何触发缩放。可选值为：true：表示不按任何功能键，鼠标滚轮能触发缩放。false：表示鼠标滚轮不能触发缩放。'shift'：表示按住 shift 和鼠标滚轮能触发缩放。'ctrl'：表示按住 ctrl 和鼠标滚轮能触发缩放。'alt'：表示按住 alt 和鼠标滚轮能触发缩放。。
            moveOnMouseMove:true,
            moveOnMouseWheel:true,//鼠标滚轮实现移动
            }
            ],
      }
}
export const setPrecent = (name:Array<string>,favourable:Array<number>,differ:Array<number>):EChartsOption=>{
  return option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      orient: 'vertical',  //垂直显示
      left:'right',
      bottom:'center',
    },
    grid: {
      left: '3%',
      right: '10%',
      bottom: 'center',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      boundaryGap: [0, 0.01]
    },
    yAxis: {
      type: 'category',
      data: name,
    },
    series: [
      {
        name: '好评',
        type: 'bar',
        data: favourable,
      },
      {
        name: '差评',
        type: 'bar',
        data: differ,
      }
    ]
  }
}
export const calendarBar = (year:number,nameData:Array<string>,boxData:Array<number>):EChartsOption=>{
   return option = {
    title: {
      text: year+'年票房榜前十',
      left:'center',
      top:'10'
    },
    xAxis: {
      type: 'category',
      data: nameData,
      axisLabel:{
        interval:0,
        rotate:-20
      }
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: boxData,
        type: 'bar'
      }
    ]
  };
}
export const countryCount = (nameArr:Array<string>,dataArr:Array<number>,year:number):EChartsOption=>{
  option = {
    title: {
      text: `${year}~${year+10}各国家及地区高分电影数量`,
      left:'center',
      top:'10'
    },
    xAxis: {
      type: 'category',
      data: nameArr,
      axisLabel:{
        interval:0,
        rotate:-60
      }
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: dataArr,
        type: 'bar'
      }
    ]
  }
  return option
}