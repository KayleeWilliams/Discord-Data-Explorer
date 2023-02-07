<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg h-fit flex flex-col">
      <h3 class="font-bold mb-2"> {{ title }} </h3>
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
            backgroundColor: ['#4465F1', '#D953D2', '#FF5B9F', '#FF8B70', '#FFC458','#F9F871'],
            data: Object.values(this.data),
            borderWidth: 0
          }
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: {
            padding: 1,
            labels: {
              color: 'white',
              boxWidth: 4,
            }
          }
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