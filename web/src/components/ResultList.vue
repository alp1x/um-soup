<template>
  <CharacterModel @character-model="characterModel" />
  <FindMode/>
  <Button @get-category="generateClothesFileNames" />
  <div mt10 color-black p10 rounded-1 all:transition-200 overflow-auto overscroll-revert v-if="resultState" style='max-height: 12rem;'
  :class="resultFiles.length === 1 ? 'bg-green' : (resultFiles.length > 1 && resultFiles.length <= 4 ? 'bg-orange' : 'bg-red')"
  >
    <div rounded p1 bg-orange-1>
      <button i-tabler-category-2></button>
      {{ resultCategory }}
    </div>
    <div mt3 t> 
      {{ resultFiles.length }} {{ $t('results.found') }}
    </div>
    <div p2 m5 bg-orange-1 rounded-1 hover:op80 cursor-pointer v-for="(resultFile, index) in resultFiles" :key="index" v-clipboard="resultFile">
      {{ resultFile }}
      <button i-tabler-copy rounded hover:op80 cursor-pointer bg-black border-none p-1 font-mono v-clipboard="resultFile"></button>
    </div>
  </div>
  <div v-else mt30 flex items-center flex-col>
    <span bg-red p1 rounded color-black font-mono >{{ $t('results.notFound') }}</span>
    <small bg-blue-3 p1 rounded color-black font-mono mt3 p2>{{ $t('results.infoMeta') }}</small>
    <small bg-blue-3 p1 rounded color-black font-mono mt3 p2>{{ $t('results.infoDefault') }}</small>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useClothesStore } from "../store/clothesStore";
import { formatClothesFileName } from "../utils/clothesUtils";
import Button from "./Button.vue";
import CharacterModel from "./CharacterModel.vue";
import FindMode from "./FindMode.vue"

const clothesStore = useClothesStore();
const resultState = ref(false);
const resultFiles = ref([]);
const resultCategory = ref('');
const defaultModel = ref('mp_m');

const characterModel = (model) => {
  defaultModel.value = model;
};

const generateClothesFileNames = async (category) => {
  const matchingRoots = await findMatchingRoot(category, clothesStore);

  if (matchingRoots.length === 0) {
    resultState.value = false;
    return null;
  }

  const generatedFileNames = matchingRoots.map(rootName => formatClothesFileName(rootName, category, clothesStore.resultsClothes[category].objID));
  resultState.value = true;
  resultCategory.value = category;
  resultFiles.value = generatedFileNames;
};

const findMatchingRoot = (category) => {
  return new Promise((resolve) => {
    const matchingRoots = [];
    const { resultsJson, resultsClothes } = clothesStore;
    const { value: defaultModelValue } = defaultModel;

    const searchInMode = (mode) => {
      for (const rootName in resultsJson) {
        const root = resultsJson[rootName];

        if (!rootName.startsWith(defaultModelValue) || !root.hasOwnProperty(category)) {
          continue;
        }

        const categoryFilter = root[category];
        const clothesObj = resultsClothes[category];
        const object = categoryFilter[clothesObj.objID];

        if (!object || !object.textures.hasOwnProperty(clothesObj.txtID)) {
          continue;
        }

        const textures = object.textures;
        let isMatchingRoot = false;

        if (mode === 'aggressive' && textures.length === clothesObj.objTotalTxt) {
          isMatchingRoot = true;
        } else if (mode === 'chill' && textures.length >= clothesObj.objTotalTxt) {
          isMatchingRoot = true;
        } else if (mode === 'mix' && textures.length >= clothesObj.txtID) {
          isMatchingRoot = true;
        }

        if (isMatchingRoot) {
          matchingRoots.push(rootName);
        }
      }
    };

    searchInMode('aggressive');
    if (matchingRoots.length === 0) {
      searchInMode('chill');
    }
    if (matchingRoots.length === 0) {
      searchInMode('mix');
    }

    resolve(matchingRoots);
  });
};

</script>