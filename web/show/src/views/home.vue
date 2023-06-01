<template>
    <div class="home" ref="home">
        <div class="nav">
            <el-menu :mode="mode" :router="true">
                <el-menu-item index="/">
                    <el-icon><i-ep-menu/></el-icon>
                    <span>首页</span>    
                </el-menu-item>
                <el-menu-item index="/wordcloud">
                    <el-icon><i-ep-Search/></el-icon>
                    <span>词云</span>
                </el-menu-item>
                <el-sub-menu index="1">
                    <template #title>
                        <el-icon><i-ep-PieChart/></el-icon>
                        <span>类型</span>
                    </template>
                    <el-menu-item index="/types">
                        类型占比
                    </el-menu-item>
                    <el-menu-item index="/tandp" >
                        类型与盈利
                    </el-menu-item>  
                    <el-menu-item index="/tandg">类型与评分</el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon><i-ep-Film/></el-icon>  
                        <span>票房</span>
                    </template>
                    <el-menu-item index="/top100">票房前百</el-menu-item>
                    <el-menu-item index="/calender">历年票房</el-menu-item>
                      
                </el-sub-menu>
                <el-menu-item index="/country">
                    <el-icon><i-ep-Orange/></el-icon>  
                        <span>国家</span>
                </el-menu-item>
                <el-menu-item index="/self">
                    <el-icon><i-ep-Setting/></el-icon>
                    <span>个人设置</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="show" ref="show">
            <router-view></router-view>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount, watch, onMounted, reactive } from 'vue'
import { reqhome } from '../api';
import { Sunny, Moon } from '@element-plus/icons-vue'
import { objectExpression } from '@babel/types';
// 定义一个监听屏幕的属性
let ScreenWidth = ref()

// 监听尺寸变化
watch(ScreenWidth, (n, o) => {
    if (n > 960) {
        mode.value = 'vertical'
    } else {
        mode.value = 'horizontal'
    }
})
// 导航栏方向
let mode = ref('vertical')


// 生命周期钩子，添加页面宽度事件绑定
onBeforeMount(() => {
    window.onresize = () => {
        ScreenWidth.value = document.body.clientWidth
    }
})
</script>

<style lang="scss" scoped>
.home {
    height: 100%;
    display: flex;
    .nav {
        background-color: #fff;
    }
    

}

@media screen and (min-width:960px) {
    .home {
        flex-direction: row;

        .show {
            width: 90%;
        }

        .nav {
            width: 10%;
        }
    }
}

@media screen and (max-width:960px) {
    .home {
        flex-direction: column;

        .show {
            height: 90%;
        }

        .nav {
            height: 10%;
        }
    }
}
</style>