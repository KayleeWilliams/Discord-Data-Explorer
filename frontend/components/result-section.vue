<template>
    <div class="text-background text-center grid grid-cols-5 auto-rows-max gap-8 h-screen w-screen">
        <single-container class="col-start-2 row-start-5" title="Total Messages" :value="data[0]"/>
        <single-container class="col-start-3 row-start-5" title="Total Channels" :value="data[4]"/>

        <list-container class="col-start-2 row-start-6 col-span-1" title="Top Friends" :list="data[1]"/>
        <list-container class="col-start-3 row-start-6 col-span-1" title="Top Servers" :list="data[2]"/>
        <list-container class="col-start-4 row-start-6 col-span-1" title="Top Groups" :list="data[3]"/>
    </div>
</template>

<script>
export default {
  props: {
    data: Array,
  }
}
</script>