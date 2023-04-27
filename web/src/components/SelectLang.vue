<template>
  <div absolute top-5 right-0 left-3 p1 bg-orange-2 cursor-pointer font-mono text-center m5 w25 rounded-1 color-black>
    <button i-tabler-language text-l cursor-pointer></button>
    <select v-model="selectLang" @change="changeLanguage" cursor-pointer bg-transparent border-none font-mono>
      <option :value="item" v-for="item in availableLocales" :key="item" color-black>
        {{ item.toUpperCase()}} 
      </option>
    </select>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { useLocalStorageStore } from '../store/localStorage.js';

const localStorageStore = useLocalStorageStore();
const { availableLocales, locale } = useI18n();
const selectLang = ref(locale.value);

const changeLanguage = () => {
  locale.value = selectLang.value;
  localStorageStore.setItem('language', selectLang.value);
};

onMounted(() => {
  const savedLanguage = localStorageStore.getItem('language');
  if (savedLanguage) {
    locale.value = savedLanguage;
    selectLang.value = savedLanguage;
  }
});
</script>
  