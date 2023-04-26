<template>
    <div @click="characterModelToggle" p2 rounded bg-pink color-black cursor-pointer>
    <button i-tabler-gender-bigender text-2xl></button>
     Model: {{ characterModel }}
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useLocalStorageStore } from '../store/localStorage.js';

const localStorageStore = useLocalStorageStore();
const emit = defineEmits(['character-model'])
const characterModel = ref('mp_m');

const emitCharacterModel = (model) => {
  emit('character-model', model);
};

const characterModelToggle = () => {
  if (characterModel.value === 'mp_m') {
    characterModel.value = 'mp_f';
  } else {
    characterModel.value = 'mp_m';
  }
  localStorageStore.setItem('characterModel', characterModel.value);
  emitCharacterModel(characterModel.value)
};

onMounted(() => {
    const savedCharacterModel = localStorageStore.getItem('characterModel');
    if (savedCharacterModel) characterModel.value = savedCharacterModel;
    emitCharacterModel(characterModel.value)
});
</script>