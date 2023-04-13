import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import { resolve } from "path"
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(),
  // 自动导入element plus
  AutoImport({
    resolvers: [ElementPlusResolver()
    ,
  // Auto import icon components
  // 自动导入图标组件
  IconsResolver({
    prefix: 'Icon',
  }),
],
  }),
  Components({

    resolvers: [
      // Auto register icon components
      // 自动注册图标组件
      IconsResolver({
        enabledCollections: ['ep'],
      }), 
      ElementPlusResolver()],
  }),
  Icons({
    autoInstall: true,
  }),
],
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
    }
  },

})
