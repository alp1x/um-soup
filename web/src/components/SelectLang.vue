<template>
    <select v-model="selectLang" @change="changeLanguage" p1 bg-purple cursor-pointer hover:bg-gray i-tabler-language font-mono text-center m5 w25 text-l>
      <option :value="item" v-for="item in availableLocales" :key="item">
        {{ item.toUpperCase()}} 
      </option>
    </select>
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
  