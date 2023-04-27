import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'
import VueI18nPlugin from '@intlify/unplugin-vue-i18n/vite'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    UnoCSS(),
    VueI18nPlugin({
      include: [path.resolve(__dirname, './src/locales/*.json')],
    }),
  ],
  base: './',
  build: {
    outDir: 'build',
  },
})
