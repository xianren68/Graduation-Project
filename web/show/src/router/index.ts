import {createRouter,createWebHistory} from 'vue-router'
// 路由列表
const routes = [
    {
        name:'home',
        path:'/',
        component:()=>import('@/views/home.vue'),
        children:[
            {
                name:'main',
                path:'/',
                component:()=>import('@/views/main.vue')
                
            },
            {
                name:'boxtop',
                path:'/top100',
                component:()=>import('@/views/charts/BoxTop.vue')
            },
            {
                name:'wordcloud',
                path:'wordcloud',
                component:()=>import('@/views/charts/wordcloud.vue')
            },
            {
                name:'types',
                path:'types',
                component:()=>import('@/views/charts/types.vue')
            },
            {
                name:'calender',
                path:'calender',
                component:()=>import('@/views/charts/calendar.vue')
            },
            {
                name:'tandp',
                path:'tandp',
                component:()=>import('@/views/charts/TandP.vue')
            },
            {
                name:'tandg',
                path:'tandg',
                component:()=>import('@/views/charts/TandG.vue')
            },
            {
                name:'country',
                path:'country',
                component:()=>import('@/views/charts/country.vue')
            }
        ]

    },
    {
        name:'self',
        path:'/self',
        component:()=>import('@/views/self.vue')
    },
    {
        name:'login',
        path:'/login',
        component:()=>import('@/views/login.vue')
    },
    {
        name:'register',
        path:'/register',
        component:()=>import('@/views/register.vue')
    },
    {
        name:'set',
        path:'/set',
        component:()=>import('@/views/set.vue')
    }
]
const router = createRouter({
    routes,
    history:createWebHistory()
})
export default router