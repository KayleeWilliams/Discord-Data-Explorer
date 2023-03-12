<template>
  <div class="flex flex-col bg-secondary rounded-xl drop-shadow-lg p-3 h-full justify-center items-center">
    <p class="lg:text-sm xl:text-base"> {{ title }} </p>
    <p class="xl:text-base font-bold">{{ value }}</p>
  </div>
</template>

<script setup>
defineProps({
  'title': String,
  'value': [String, Number]
})
</script>