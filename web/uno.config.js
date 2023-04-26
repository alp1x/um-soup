import {
  defineConfig,
  presetAttributify,
  presetUno,
  presetIcons,
} from 'unocss'

export default defineConfig({
    presets: [
        presetAttributify(),
        presetUno(),
        presetIcons({}),
      ],
})