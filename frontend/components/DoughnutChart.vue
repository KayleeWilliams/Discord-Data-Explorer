<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg h-fit flex flex-col">
      <h3 class="text-background font-bold mb-2"> {{ title }} </h3>
      <Doughnut :data="chartData" :options="options" class="h-full self-center"/>
    </div>
</template>

<script>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Doughnut } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)
let delayed = false;

export default {
  props: {
    title: String,
    data: Object,
  },

  name: 'DoughnutChart',
  components: { Doughnut },
  data() {
    return {
      chartData: {
        labels: Object.keys(this.data),
        datasets: [
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#F7B733','#F5A623', '#F39C12', '#F28C10', '#F27F1D', '#F26C1D', '#F25A1D', '#F24D1D', '#F23C1D', '#F22C1D', '#F21D1D'],
            data: Object.values(this.data)
          }
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
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