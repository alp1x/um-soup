<template>
  <div class="text-sm flex mt-10">
    <button
      v-for="item in translatedCategories"
      :key="item.icon"
      mr-2 hover:bg-gray scale cursor-pointer text-1xl bg-orange p2 font-semibold rounded border-none text-sm
      @click="handleClick(item.category)"
      :class="{ 'active': selectedCategory === item.category }"
    >{{item.name}}</button>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { ref,computed } from 'vue'

const { t } = useI18n()
const emit = defineEmits(['get-category'])
const selectedCategory = ref('')

const handleClick = (category) => {
  selectedCategory.value = category
  emit('get-category', category)
}

const categories = [
  { icon: 'scissors', category: 'HAIR', key: 'categories.hair' },
  { icon: 'scuba-mask', category: 'BERD', key: 'categories.mask' },
  { icon: 'hand-stop', category: 'UPPR', key: 'categories.hands' },
  { icon: 'shirt-sport', category: 'ACCS', key: 'categories.shirt' },
  { icon: 'tie', category: 'TEEF', key: 'categories.scarf' },
  { icon: 'jacket', category: 'JBIB', key: 'categories.jackets' },
  { icon: 'sock', category: 'FEET', key: 'categories.shoes' },
  { icon: 'paper-bag', category: 'HAND', key: 'categories.bags' },
  { icon: 'paper-bag', category: 'TASK', key: 'categories.armor' },
  { icon: 'paper-bag', category: 'LOWR', key: 'categories.legs' },
  // { icon: 'paper-bag', category: 'HEAD', key: 'categories.face' }
]

const translatedCategories = computed(() =>
  categories.map(item => ({
    ...item,
    name: t(item.key)
  }))
)
</script>


<style scoped>
.active {
  background-color: #9ca3af;
}
</style>