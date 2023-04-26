<template>
  <CharacterModel @character-model="characterModel" />
  <FindMode @find-mode="findMode"/>
  <Button @get-category="generateClothesFileNames" />
  <div mt10 color-black p10 rounded-1 all:transition-200 overflow-auto overscroll-revert v-if="resultState" style='max-height: 12rem;'
  :class="resultFiles.length === 1 ? 'bg-green' : (resultFiles.length > 1 && resultFiles.length <= 4 ? 'bg-orange' : 'bg-red')"
  >
    <div rounded p1 bg-purple>
      {{ resultCategory }}
    </div>
    <div mt3 t> 
      {{ resultFiles.length }} {{ t('results.found') }}
    </div>
    <div p2 m5 bg-orange-1 rounded-1 hover:op80 cursor-pointer v-for="(resultFile, index) in resultFiles" :key="index" v-clipboard="resultFile">
      {{ resultFile }}
      <button i-tabler-copy rounded hover:op80 cursor-pointer bg-black border-none p-1 font-mono v-clipboard="resultFile"></button>
    </div>
  </div>
  <div v-else mt30 flex items-center>
    <span bg-red p1 rounded color-black font-mono >{{ t('results.notFound') }}</span>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useClothesStore } from "../store/clothesStore";
import { formatClothesFileName } from "../utils/clothesUtils";
import { useI18n } from 'vue-i18n'
import Button from "./Button.vue";
import CharacterModel from "./CharacterModel.vue";
import FindMode from "./FindMode.vue";

const clothesStore = useClothesStore();
const resultState = ref(false);
const resultFiles = ref([]);
const resultCategory = ref('');
const defaultModel = ref('mp_m');
const findModeRef = ref(false);
const { t } = useI18n()

const characterModel = (model) => {
  defaultModel.value = model;
};

const findMode = (mode) => {
  findModeRef.value = mode;
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
    const { value: findModeRefValue } = findModeRef;

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
      const isChillMode = !findModeRefValue;
      const isMatchingRoot = isChillMode
        ? textures.length >= clothesObj.objTotalTxt
        : textures.length === clothesObj.objTotalTxt;

      if (isMatchingRoot) {
        matchingRoots.push(rootName);
      }
    }

    resolve(matchingRoots);
  });
};

</script>