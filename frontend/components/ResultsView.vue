<template>
  <div class="bg-background pb-8">
    <div class="text-primary text-center grid grid-cols-1 lg:grid-cols-5 auto-rows-max gap-4 w-screen mt-8 px-4 lg:px-0">
        <h1 class="text-primary text-3xl xl:text-4xl font-black text-center tracking-wide col-span-full row-start-2 lg:row-start-1"> Your Discord Data </h1>
        <Exports class="col-start-1 lg:col-start-4 row-start-1" :data="data" />
        <BarChart class="col-start-1 col-span-1 lg:col-start-2 lg:col-span-3" :data="data.message_analytics" v-if="showMessageChart" @messageToggle="messageToggle" />
        
        <ListContainer class="lg:col-start-2 lg:row-start-2 col-span-1" v-show="!showMessageChart" title="Top Friends" :list="data.message_analytics.friends" :toggle="false" />
        <ListContainer class="lg:col-start-3 lg:row-start-2 col-span-1" v-show="!showMessageChart" title="Top Servers" :list="data.message_analytics.servers" :toggle="false" />
        <ListContainer class="lg:col-start-4 lg:row-start-2 col-span-1" v-show="!showMessageChart" title="Top Groups" :list="data.message_analytics.groups" :toggle="true" @messageToggle="messageToggle"/>
        
        <div class="col-start-1 row-start-6 lg:row-start-3 lg:col-start-2 lg:col-span-3">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <DoughnutChart class="lg:col-span-1 lg:h-full" :data="data.message_analytics.total_messages_by" title="Total Messages By Channel" />
            
            <div class="grid col-span-1 grid-cols-1 gap-4">
              <SingleContainer title="Total Messages" :value="data.message_analytics.total_messages" />
              <SingleContainer title="Money Spent" :value="moneySpent"/>
              <SingleContainer title="Predicted Age" :value="data.predicted_age"/>

              <UpsellChart :data="data.events" class="" />
            </div>

          </div>
        </div>
        
        <ActivityChart class="col-span-1 col-start-1 lg:col-start-2 lg:col-span-2 lg:row-start-4" :activity="data.activity_analytics" />
        <DoughnutChart class="col-span-1 lg:col-start-4 lg:row-start-4 h-full" :data="data.message_analytics.messages_to" title="DMs To Friends VS Nonfriends"/>
        
        <Analytics class="col-span-1 col-start-1 lg:col-start-2 lg:col-span-3 lg:row-start-5" :data="data.events" />
        
        <div class="lg:row-start-6 lg:col-start-2 lg:col-span-3"> 
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <DoughnutChart class="col-span-1 h-full" :data="data.browsers" title="Top Browsers" />

            <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-1 gap-4 ">
              <SingleContainer title="Total Friends" :value="data.message_analytics.friends.length" />
              <SingleContainer title="Total Servers" :value="data.message_analytics.servers.length"/>
              <SingleContainer title="Total Groups" :value="data.message_analytics.groups.length"/>
              <SingleContainer title="Mentioned @everyone" :value="data.message_analytics.everyone_mentions"/>
              <SingleContainer title="Calls Started" :value="data.events['start_call']"/>
              <SingleContainer title="Voice Channels Joined" :value="data.events['join_voice_channel']"/>
              <SingleContainer title="Average Words Sent" :value="averageWords"/>
              <SingleContainer title="Average Characters" :value="averageLength"/>
            </div>
          </div>
        </div>
        
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
    },
  },
}
</script>