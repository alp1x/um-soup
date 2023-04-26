<template>
 <main v-if="soupState" v-draggable font-semibold bg-dark-900 w-200 rounded-1 h-185 text-white all:transition-400 font-mono antialiased>
    <div flex flex-col items-center justify-start h-full p5>
      <Header />
      <ResultList/>
      <Footer />
    </div>
  </main>
</template>

<script setup>
import { onMounted, onUnmounted, ref} from 'vue';
import { useClothesStore } from './store/clothesStore.js';
import { fetchNui } from './utils/fetchNui';
import { vDraggable } from '@neodrag/vue';
import Header from './components/Header.vue';
import ResultList from './components/ResultList.vue';
import Footer from './components/Footer.vue';

const soupState = ref(false);
const clothesStore = useClothesStore();


const handleMessage = (event) => {
  if (event.data.clothesData) {
    clothesStore.setClothes(event.data.clothesData);
    soupState.value = true;
  }
};

const handleKeyDown = (e) => {
    if (e.key !== 'Escape') return;
    soupState.value = false;
    fetchNui('close');
};

onMounted(async () => {
  await clothesStore.fetchAndSetJSONClothes();
  window.addEventListener('message', handleMessage);
  document.addEventListener('keydown', handleKeyDown);
});

onUnmounted(() => {
  window.removeEventListener('message', handleMessage);
  document.removeEventListener('keydown', handleKeyDown);
});

</script>


<style>
body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
  background-color: transparent;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

</style>