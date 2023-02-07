<template>
  <div>
    <h1 class="text-primary text-3xl font-black text-center mt-8 tracking-wide"> Your Discord Data </h1>
    <div class="text-primary bg-background text-center grid grid-cols-5 auto-rows-max gap-4 w-screen mb-8 ">
        <BarChart class="col-start-2 row-start-3 col-span-3" :data="data.message_analytics" v-if="showMessageChart" @messageToggle="messageToggle" />
        <DoughnutChart class="col-start-2 row-start-4 col-span-2 h-full" :data="data.message_analytics.total_messages_by" title="Total Messages By Channel" />

        <div class="col-start-4 col-span-1 row-start-4 flex flex-col gap-4">
          <SingleContainer title="Total Messages" :value="data.message_analytics.total_messages"/>
          <SingleContainer title="Money Spent" :value="moneySpent"/>
          <SingleContainer title="Predicted Age" :value="data.predicted_age"/>
          <SingleContainer title="Total Friends" :value="data.message_analytics.friends.length" />
          <SingleContainer title="Total Servers" :value="data.message_analytics.servers.length"/>
          <SingleContainer title="Total Groups" :value="data.message_analytics.groups.length"/>
          <SingleContainer title="Calls Started" :value="data.events['start_call']"/>
        </div>
        
        <ListContainer class="col-start-2 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Friends" :list="data.message_analytics.friends" :toggle="false" />
        <ListContainer class="col-start-3 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Servers" :list="data.message_analytics.servers" :toggle="false" />
        <ListContainer class="col-start-4 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Groups" :list="data.message_analytics.groups" :toggle="true" @messageToggle="messageToggle"/>
        
        <ActivityChart class="col-start-2 row-start-5 col-span-2" :activity="data.activity_analytics" />
        <DoughnutChart class="col-start-4 row-start-5 col-span-1 h-full" :data="data.message_analytics.messages_to" title="DMs To Friends VS Nonfriends"/>
        <Analytics class="col-start-2 row-start-6 col-span-3" :data="data.events" />
        
        <DoughnutChart class="col-start-2 row-start-7 col-span-2 h-full" :data="data.browsers" title="Top Browsers" />
        <div class="col-start-4 col-span-1 row-start-7 flex flex-col gap-4">
          <UpsellChart :data="data.events" />
          <SingleContainer title="Voice Channels Joined" :value="data.events['join_voice_channel']"/>
          <SingleContainer title="Average Words Sent" :value="averageWords"/>
          <SingleContainer title="Times mentioned @everyone" :value="data.message_analytics.everyone_mentions"/>
          <SingleContainer title="Average Words Sent" :value="averageWords"/>
          <SingleContainer title="Average Characters" :value="averageLength"/>
        </div>
        
        <!-- <p class="bg-white"> {{ data.events }}</p> -->

    </div>
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
      return `$${(this.data.payment_total / 100).toFixed(2)}`;
    },
    averageWords() {
      return `${(this.data.message_analytics.total_words / this.data.message_analytics.total_messages).toFixed(2)}`;
    },    
    averageLength() {
      return `${(this.data.message_analytics.total_length / this.data.message_analytics.total_messages).toFixed(2)}`;
    },    
  },
  methods: {
    messageToggle() {
      this.showMessageChart = !this.showMessageChart;
    }
  },
}
</script>