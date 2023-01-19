<template>
    <div class="text-background text-center grid grid-cols-5 auto-rows-max gap-4 h-screen w-screen">
        <single-container class="col-start-2 row-start-5" title="Total Messages" :value="data.total_messages"/>
        <single-container class="col-start-3 row-start-5" title="Total Channels" :value="data.total_channels"/>

        <list-container class="col-start-2 row-start-6 col-span-1" title="Top Friends" :list="data.friends"/>
        <list-container class="col-start-3 row-start-6 col-span-1" title="Top Servers" :list="data.servers"/>
        <list-container class="col-start-4 row-start-6 col-span-1" title="Top Groups" :list="data.groups"/>

        <BarChart class="col-start-2 row-start-7 col-span-3" :data="data"/>

        <!-- <BarChart class="col-start-2 row-start-7 col-span-3" :data="data.friends"/> -->
    </div>
</template>

<script>
export default {
  props: {
    data: Object,
  }
}
</script>