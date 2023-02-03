<template>
    <div class="text-background text-center grid grid-cols-5 auto-rows-max gap-4 w-screen mb-8 ">
        <BarChart class="col-start-2 row-start-3 col-span-3" :data="data" v-show="showMessageChart" @messageToggle="messageToggle" />
        <BrowserChart class="col-start-2 row-start-4 col-span-2 h-full" :data="data" />

        <div class="col-start-4 col-span-1 row-start-4 flex flex-col gap-4">
          <single-container title="Total Messages" :value="data.total_messages"/>
          <single-container title="Money Spent" :value="moneySpent"/>
          <single-container title="Predicted Age" :value="data.predicted_age"/>
          <single-container title="Calls Started" :value="data.events['start_call']"/>
          <single-container title="Voice Channels Joined" :value="data.events['join_voice_channel']"/>

        </div>
        
        <list-container class="col-start-2 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Friends" :list="data.friends" :toggle="false" />
        <list-container class="col-start-3 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Servers" :list="data.servers" :toggle="false" />
        <list-container class="col-start-4 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Groups" :list="data.groups" :toggle="true" @messageToggle="messageToggle"/>

        <Analytics class="col-start-2 row-start-5 col-span-3" :data="data.events" />

    </div>
</template>

<script>
export default {
  props: {
    data: Object,
  },
  data() {
    return {
      showMessageChart: true,
    }
  },
  computed: {
    moneySpent() {
      return `$${this.data.payment_total / 100}`;
    }
  },
  methods: {
    messageToggle() {
      this.showMessageChart = !this.showMessageChart;
    }
  },
}
</script>