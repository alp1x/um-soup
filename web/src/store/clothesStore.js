import { defineStore } from 'pinia';
import { fetchClothes } from '../utils/fetchData.js';

export const useClothesStore = defineStore('clothes', {
  state: () => ({
    myClothes: [],
    clothesJSON: [],
  }),
  getters: {
    resultsJson(state) {
      return state.clothesJSON;
    },
    resultsClothes(state) {
      return state.myClothes;
    },
  },
  actions: {
    setClothes(clothesData) {
        this.myClothes = clothesData;
      },
    async fetchAndSetJSONClothes() {
      const clothesData = await fetchClothes();
        this.clothesJSON = clothesData;
        console.log('Json Loaded')
    },
  },
});
