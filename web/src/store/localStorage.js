import { defineStore } from 'pinia';

export const useLocalStorageStore = defineStore({
  id: 'localStorage',
  actions: {
    getItem(key) {
      return localStorage.getItem(key);
    },
    setItem(key, value) {
      localStorage.setItem(key, value);
    },
    removeItem(key) {
      localStorage.removeItem(key);
    },
  },
});
