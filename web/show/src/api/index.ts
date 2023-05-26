import req from './req'
import { user } from '../type/User'
// 用户注册
export const reqRegister = (data:FormData)=> req.post('/user/register/',data)
// 用户登录
export const reqLogin = (data:user) => req.get(`/user/login/?name=${data.name}&password=${data.password}`)
// 获取票房排行信息
export const reqBoxoffice = ()=> req.get('/show/boxoffice/')
// 返回词云图地址
export const reqCiyun = (name:string)=>req.get(`/show/ciyun/?name=${name}`)
// 返回类型占比
export const reqTypes = ()=>req.get('/show/types/')
// 返回推荐的电影
export const reqRecommend = ()=>req.get('/show/recommend/')
// 获取历年票房排行榜
export const reqCalendar = (year:number)=>req.get(`/show/yeartop/?year=${year}`)
// 首页接口
export const reqhome = ()=>req.get('/show/home/')
// 获取类型与盈利数据
export const reqTandP = ()=>req.get('/show/tandp/')
// 获取类型与评分数据
export const reqTandG = ()=>req.get('/show/tandg/')
// 国家数量
export const reqCountry = ()=>req.get('/show/cy/')
// 搜索电影
export const reqSearch = (name:string)=>req.get(`/show/search/?name=${name}`)
// 获取画廊')