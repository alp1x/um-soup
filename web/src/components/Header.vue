<template>
      <div i-tabler-soup text-3xl font-semibold color-orange hover:op50 cursor-pointer></div>
      <small bg-orange p1 rounded-1 color-black font-mono>um-soup</small>
      <small bg-purple-3 p0.5 rounded-1 color-black mt2>beta</small>
      <SelectLang />
      <!-- <p text-m>
        {{ t('header') }}
      </p> -->
</template>


<script setup>
import SelectLang from './SelectLang.vue';
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>