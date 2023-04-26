<template>
<footer absolute bottom-5 right-0 left-0 text-center op30 fw300 text-sm>
    <button i-tabler-brand-github text-1xl></button>
    {{t('feedback')}}
</footer>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>