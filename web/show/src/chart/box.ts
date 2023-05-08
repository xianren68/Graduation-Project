import * as echarts from 'echarts/core';
import {
  DatasetComponent,
  DatasetComponentOption,
  TitleComponent,
  TitleComponentOption,
  TooltipComponent,
  TooltipComponentOption,
  GridComponent,
  GridComponentOption,
  TransformComponent
} from 'echarts/components';
import {
  BoxplotChart,
  BoxplotSeriesOption,
  ScatterChart,
  ScatterSeriesOption
} from 'echarts/charts';
import { UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';
import { log } from 'console';

echarts.use([
  DatasetComponent,
  TitleComponent,
  TooltipComponent,
  GridComponent,
  TransformComponent,
  BoxplotChart,
  ScatterChart,
  CanvasRenderer,
  UniversalTransition
]);

type EChartsOption = echarts.ComposeOption<
  | DatasetComponentOption
  | TitleComponentOption
  | TooltipComponentOption
  | GridComponentOption
  | BoxplotSeriesOption
  | ScatterSeriesOption
>;
var option: EChartsOption;

export function TandPEchart(arr:Array<Array<number>>,strArr:Array<string>,show:string,type:string):EChartsOption{
    return option = {
        title: [
          {
            text: `${type}与类型`,
            left: 'center'
          },
          {
            text: 'upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
            borderColor: '#008c8c',
            borderWidth: 1,
            textStyle: {
              fontSize: 14
            },
            left: '10%',
            top: '90%'
          }
        ],
        dataset: [
          {
            // prettier-ignore
            source: arr
          },
          {
            transform: {
              type: 'boxplot',
              config: { itemNameFormatter:function(param:any):string{
                  return strArr[param.value]
              } }
            }
          },
          {
            fromDatasetIndex: 1,
            fromTransformResult: 1
          }
        ],
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '10%',
          right: '10%',
          bottom: '15%'
        },
        yAxis: {
          type: 'category',
          boundaryGap: true,
          nameGap: 30,
          splitArea: {
            show: false
          },
          splitLine: {
            show: false
          },
        },
        xAxis: {
          type: 'value',
          name: show,
          splitArea: {
            show: true
          },
          min: 'dataMin' // 最小值
        },
        series: [
          {
            name: 'boxplot',
            type: 'boxplot',
            datasetIndex: 1
          },
          {
            name: 'outlier',
            type: 'scatter',
            encode: { x: 1, y: 0 },
            datasetIndex: 2
          }
        ]
      };
}