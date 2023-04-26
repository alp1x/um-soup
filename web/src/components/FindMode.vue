<template>
    <div @click="emitFindMode">
    <div v-if="!findMode" p2 rounded bg-orange-3 color-black cursor-pointer mt5>
        <button i-tabler-coffee text-xl></button>
        {{t('mode.chill.title')}}
        <small text-xs> {{t('mode.chill.description')}}</small>
    </div>
    <div v-else p2 rounded bg-red color-black cursor-pointer mt5>
        <button i-tabler-mood-off text-xl></button>
        {{t('mode.aggressive.title')}}
        <small text-xs>{{t('mode.aggressive.description')}}</small>
    </div>
</div>
</template>


<script setup>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
const findMode = ref(false)
const emit = defineEmits(['find-mode'])
const emitFindMode = () => {
    findMode.value = !findMode.value
    emit('find-mode', findMode.value);
};
</script>