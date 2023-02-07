<template>
  <div class="flex flex-col bg-secondary rounded-xl drop-shadow-lg p-3">
    <p> {{ title }} </p>
    <p class="font-bold">{{ value }}</p>
  </div>
</template>

<script setup>
defineProps({
  'title': String,
  'value': [String, Number]
})
</script>