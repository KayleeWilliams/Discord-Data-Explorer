<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg h-fit">
      <h3 class="text-background font-bold mb-2"> Favourite Browsers </h3>
      <Doughnut :data="chartData" :options="options" />
    </div>
</template>

<script>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Doughnut } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  props: {
    data: Object,
  },

  name: 'DoughnutChart',
  components: { Doughnut },
  data() {
    return {
      chartData: {
        labels: Object.keys(this.data.browsers),
        datasets: [
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#F7B733','#F5A623', '#F39C12', '#F28C10', '#F27F1D', '#F26C1D', '#F25A1D', '#F24D1D', '#F23C1D', '#F22C1D', '#F21D1D'],
            data: Object.values(this.data.browsers)
          }
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
      }
    }
  },
}

</script>