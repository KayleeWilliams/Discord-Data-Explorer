<template>
    <div class="text-background text-center grid grid-cols-5 auto-rows-max gap-4 w-screen mb-8 ">
        <BarChart class="col-start-2 row-start-3 col-span-3" :data="data" v-if="showMessageChart" @messageToggle="messageToggle" />
        <BrowserChart class="col-start-2 row-start-4 col-span-2 h-full" :data="data" />

        <div class="col-start-4 col-span-1 row-start-4 flex flex-col gap-4">
          <single-container title="Total Messages" :value="data.total_messages"/>
          <single-container title="Money Spent" :value="moneySpent"/>
          <single-container title="Predicted Age" :value="data.predicted_age"/>
          <single-container title="Calls Started" :value="data.events['start_call']"/>
          <single-container title="Voice Channels Joined" :value="data.events['join_voice_channel']"/>
          <single-container title="Average Words Sent" :value="averageWords"/>
          <single-container title="Friends DM Ratio" :value="friendDMRatio"/>

        </div>
        
        <list-container class="col-start-2 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Friends" :list="data.friends" :toggle="false" />
        <list-container class="col-start-3 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Servers" :list="data.servers" :toggle="false" />
        <list-container class="col-start-4 row-start-3 col-span-1" v-show="!showMessageChart" title="Top Groups" :list="data.groups" :toggle="true" @messageToggle="messageToggle"/>

        <ActivityChart class="col-start-2 row-start-5 col-span-2" :activity="data.activity_analytics" />
        <Analytics class="col-start-2 row-start-6 col-span-3" :data="data.events" />

        <!-- <p class="bg-white"> {{ data.events }}</p> -->

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
      return `${(this.data.message_analytics.total_words / this.data.total_messages).toFixed(2)}`;
    },
    friendDMRatio() {
      // return the ratio of messages_to_friends to messages_to_nonfriends
      return `${(this.data.message_analytics.messages_to_friends / this.data.message_analytics.messages_to_nonfriends).toFixed(2)}`;
    }
  },
  methods: {
    messageToggle() {
      this.showMessageChart = !this.showMessageChart;
    }
  },
}
</script>