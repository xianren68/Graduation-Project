import * as echarts from 'echarts/core';
import {
  ToolboxComponent,
  ToolboxComponentOption,
  LegendComponent,
  LegendComponentOption
} from 'echarts/components';
import { PieChart, PieSeriesOption } from 'echarts/charts';
import { LabelLayout } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';
import { proportionInt } from '@/type/Show';

echarts.use([
  ToolboxComponent,
  LegendComponent,
  PieChart,
  CanvasRenderer,
  LabelLayout
]);

type EChartsOption = echarts.ComposeOption<
  ToolboxComponentOption | LegendComponentOption | PieSeriesOption
>;
export interface pieData { value: number, name: string }
// 返回echarts配置
export const setTyesPie = (data: Array<pieData>): EChartsOption => {
  let option: EChartsOption = {
    legend: {
      top: 'bottom',
      right: 'center'
    },
    series: [
      {
        name: 'Nightingale Chart',
        type: 'pie',
        radius: [50, 250],
        center: ['50%', '50%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 8
        },
        data: data
      }
    ]
  }
  return option
}
// 转化数据
export const formatPieData = (data: proportionInt): Array<pieData> => {
  let res: Array<pieData> = []
  for (let i of Object.keys(data)) {
    let o: pieData = {
      value: data[i],
      name: i
    }
    res.push(o)
  }
  return res
}
export const setCountry = (data: Array<pieData>, title: Array<string>,year:number): EChartsOption => {
  let option: EChartsOption = {
    title: {
      text: `${year}~${year+10}各国家及地区出品电影占比`,
      left: 'center',
      top:'10'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      type: 'scroll',            // 设置图例翻页
      icon: 'rect',
      itemWidth: 12,             // 图例图形宽度
      itemHeight: 10,

      orient: 'vertical',
      data: title,              // title是一个列表，存着图例的数据
      left: 20,				// 图例位置
      bottom: 8,
      textStyle: {
        color: '#000',
        fontSize: 12
      },
      pageIconColor: '#fff',
      pageTextStyle: {
        color: '#fff'
      },
      itemGap: 20
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: '50%',
        data: data,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  return option
}
