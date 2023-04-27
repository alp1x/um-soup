import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { VueClipboard } from '@soerenmartius/vue3-clipboard'
import { createI18n } from 'vue-i18n'
import messages from '@intlify/unplugin-vue-i18n/messages'
import App from './App.vue'
import 'virtual:uno.css'

const i18n = createI18n({
    legacy: false, 
    locale: 'en',
    fallbackLocale: 'en',
    globalInjection: true,
    messages,
});

const pinia = createPinia()
const app = createApp(App)
app.use(pinia)
app.use(VueClipboard)
app.use(i18n)  
app.mount('#app')