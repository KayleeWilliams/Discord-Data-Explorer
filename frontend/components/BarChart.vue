<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg">
      <div class="flex flex-row justify-between items-center">
        <div class="w-10 h-10"/>
        <h3 class="text-center font-bold mb-2"> Top Messages </h3>
        <button
          type="button"
          class="group relative inline-flex items-center px-2 py-2 bg-background focus:z-10 active:bg-accent hover:bg-accent transition ease-in-out duration-300 rounded-full float-right"
          @click="$emit('messageToggle')">
          <svg class="text-accent group-active:text-background group-hover:text-background w-6 h-6" viewBox="0 0 24 24"><path fill="currentColor" d="M4 9h4v11H4zm12 4h4v7h-4zm-6-9h4v16h-4z"></path></svg>  
        </button>
      </div>
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

  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: [...this.data.friends.slice(0, 5), ...this.data.servers.slice(0, 5), ...this.data.groups.slice(0, 5)].map((item) => item[1]['name']),
        datasets: [
          {
            label: 'Messages',
            data: [...this.data.friends.slice(0, 5).map((friend) => friend[1]['messages']), 
                   ...this.data.servers.slice(0, 5).map((server) => server[1]['messages']),
                   ...this.data.groups.slice(0, 5).map((group) => group[1]['messages'])],
            backgroundColor: [
            ...Array(5).fill('#4465F1'),
            ...Array(5).fill('#FF5B9F'),
            ...Array(5).fill('#FFC458'),
            ],

            borderRadius: 8,
            // borderColor: [
            // ...Array(5).fill('rgba(181, 15, 4, 1)'),
            // ...Array(5).fill('rgba(8, 6, 145, 1)'),
            // ...Array(5).fill('rgba(35, 145, 46, 1)'),
            // ],
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
            beginAtZero: true,
            ticks: { color: '#EBEBF7' }
          },
          y: { ticks: { color: '#EBEBF7' } },
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