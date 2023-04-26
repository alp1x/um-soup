import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { VueClipboard } from '@soerenmartius/vue3-clipboard'
import 'virtual:uno.css'
import i18n from './locale';
import App from './App.vue'

const pinia = createPinia()
const app = createApp(App)
app.use(pinia)
app.use(VueClipboard)
app.use(i18n)  
app.mount('#app')