// 票房排行榜数据
export interface boxTopInt {
    name: string
    date: number
    types: string
    direct: string
    boxoffice: string
}
// 好评率数据
export interface precentInt {
    title: string
	favourable: number
	differ: number
	general: number
}
// 定义占比数据的格式
export interface proportionInt {
    [propName:string]:number,
}
// 定义历年排行榜的类型
export interface CalendarInt {
    id:number,
    year:number,
    name:string,
    boxOffice:number
}
// 类型与盈利
export interface TandPInt {
    [propName:string]:Array<number>
}
// 国家数量类型
export interface CountryInt{
    [propName:string]:{[propName:string]:number}
}
