const colorArray = [
    "#5470c6",
    "#91cc75",
    "#fac858",
    "#ee6666",
    "#73c0de",
    "#3ba272",
    "#fc8452",
    "#9a60b4",
    "#ea7ccc",
    "#008c8c"
]
// 随机返回颜色函数
export const Color = (n:number):string=>{
    return colorArray[n]
}