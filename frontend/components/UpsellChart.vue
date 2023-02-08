<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg ">
      <h3 class="text-center font-bold mb-2"> Upsells Viewed </h3>
      <Bar :data="chartData" :options="options" class="w-full"/>
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
let delayed = false;

export default {
  props: {
    data: Object,
  },

  name: 'UpsellChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ["Server", "Gifts", "Nitro"],
        datasets: [
          {
            label: 'Messages',
            data: [this.data.premium_guild_upsell_viewed,this.data.premium_gift_upsell_viewed, this.data.premium_marketing_page_viewed],
            backgroundColor: ["#FF8B70", "#FFC458", "#F9F871"],
            borderRadius: 8,
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          x: { 
            beginAtZero: false,
            ticks: { color: '#EBEBF7' }
          },
          y: { 
            display: false,
            ticks: { color: '#EBEBF7' } },
        },
        animation: {
          onComplete: () => {
            delayed = true;
          },
          delay: (context) => {
            let delay = 0;
            if (context.type === 'data' && context.mode === 'default' && !delayed) {
              delay = context.dataIndex * 300 + context.datasetIndex * 100;
            }
            return delay;
          },
        }
      }
    }
  },
}

</script>