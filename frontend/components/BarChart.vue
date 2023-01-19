<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg">
      <h3 class="text-background text-center font-bold mb-2"> Top Messages </h3>
      <Bar :data="chartData" :options="options" />
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  props: {
    data: Object,
  },

  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: [...this.data.friends.slice(0, 5), ...this.data.servers.slice(0, 5), ...this.data.groups.slice(0, 5)].map((item) => item.name),
        datasets: [
          {
            label: 'Messages',
            data: [...this.data.friends.slice(0, 5).map((friend) => friend.messages), 
                   ...this.data.servers.slice(0, 5).map((server) => server.messages),
                   ...this.data.groups.slice(0, 5).map((group) => group.messages)],
            backgroundColor: [
            ...Array(5).fill('rgba(181, 15, 4, 0.2)'),
            ...Array(5).fill('rgba(8, 6, 145, 0.2)'),
            ...Array(5).fill('rgba(35, 145, 46, 0.2)'),
            ],
            borderColor: [
            ...Array(5).fill('rgba(181, 15, 4, 1)'),
            ...Array(5).fill('rgba(8, 6, 145, 1)'),
            ...Array(5).fill('rgba(35, 145, 46, 1)'),
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        scales: {
          y: {
            beginAtZero: true,
          },
        },
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          x: { ticks: { color: '#382D43' } },
          y: { ticks: { color: '#382D43' } },
        }
      }
    }
  },
}

</script>